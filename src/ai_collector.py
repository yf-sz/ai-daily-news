"""
使用 Claude API + web_search 工具自动收集每日 AI 资讯。

Claude 通过 web_search_20250305 内置工具实时搜索，结构化输出 JSON，
再解析为项目现有数据类（NewsItem / Paper / InfluencerUpdate / GithubProject）。
"""
from __future__ import annotations

import json
import logging
import os
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from typing import List, Tuple

import anthropic

from src.collectors.news_collector import NewsItem
from src.collectors.paper_collector import Paper
from src.collectors.influencer_collector import InfluencerUpdate, GithubProject

logger = logging.getLogger(__name__)

MODEL = "claude-sonnet-4-6"
SEARCH_TOOLS = [
    {
        "type": "web_search_20250305",
        "name": "web_search",
        "max_uses": 8,
    }
]


# ── 底层调用 ─────────────────────────────────────────────────────────────────

def _call(client: anthropic.Anthropic, prompt: str, max_tokens: int = 8000) -> str:
    """带 web_search 的单次 Claude 调用，返回最终文本。

    web_search_20250305 是服务端内置工具：API 在同一次请求内完成搜索，
    stop_reason="end_turn" 时响应已包含所有结果文本。若触发多轮工具调用
    （极少数场景），此函数也能正确处理。
    """
    messages: list = [{"role": "user", "content": prompt}]

    for _ in range(12):  # 防止无限循环
        resp = client.messages.create(
            model=MODEL,
            max_tokens=max_tokens,
            tools=SEARCH_TOOLS,
            messages=messages,
        )

        # 提取所有 text 块
        texts = [
            b.text
            for b in resp.content
            if getattr(b, "type", "") == "text" and getattr(b, "text", "")
        ]

        if resp.stop_reason == "end_turn":
            return "\n".join(texts)

        if resp.stop_reason != "tool_use":
            return "\n".join(texts)

        # 继续处理 tool_use（对 web_search 不需要手动提供结果，但需维持消息链）
        messages.append({"role": "assistant", "content": resp.content})
        tool_results = [
            {"type": "tool_result", "tool_use_id": b.id, "content": ""}
            for b in resp.content
            if getattr(b, "type", "") == "tool_use"
        ]
        if tool_results:
            messages.append({"role": "user", "content": tool_results})

    return ""


# ── JSON 提取 ────────────────────────────────────────────────────────────────

def _extract_json(text: str) -> dict:
    """从 Claude 回复中提取 JSON，兼容 markdown 代码块包裹。"""
    # 先尝试 ```json ... ``` 代码块
    m = re.search(r"```(?:json)?\s*(\{[\s\S]*?\})\s*```", text)
    if m:
        try:
            return json.loads(m.group(1))
        except json.JSONDecodeError:
            pass
    # 直接找最外层 {...}
    m = re.search(r"(\{[\s\S]*\})", text)
    if m:
        try:
            return json.loads(m.group(1))
        except json.JSONDecodeError:
            pass
    logger.debug("JSON 提取失败，原始文本：%s", text[:500])
    return {}


def _safe_date(s: str, fallback: str) -> datetime:
    """将日期字符串解析为带时区的 datetime，解析失败时回退到 fallback。"""
    for candidate in (s, fallback):
        try:
            dt = datetime.fromisoformat(candidate[:10])
            return dt.replace(tzinfo=timezone.utc)
        except Exception:
            continue
    return datetime.now(tz=timezone.utc)


# ── 各维度收集 ────────────────────────────────────────────────────────────────

def _collect_news(client: anthropic.Anthropic, date_str: str) -> List[NewsItem]:
    """搜索 AI 行业资讯（6-8 条）。"""
    prompt = f"""今天是 {date_str}。请使用 web_search 搜索最近 2 天内最重要的 AI 行业新闻（6-8 条）。

重点关注：
- OpenAI、Google、Anthropic、Meta、Microsoft、Apple 等主要 AI 公司的重大发布和公告
- 重要的 AI 产品发布、模型更新
- AI 政策监管新动态
- 重大 AI 融资与并购事件

搜索完成后，**仅输出**以下 JSON（不要包含任何说明文字）：
{{
  "news": [
    {{
      "title": "资讯标题（中文翻译）",
      "url": "原文链接（必须是真实存在的 URL）",
      "source": "来源媒体名称，如 TechCrunch",
      "category": "industry 或 research 或 tools 或 newsletter",
      "published": "YYYY-MM-DD",
      "summary": "150-200 字中文摘要，包含具体数据和细节"
    }}
  ]
}}"""
    text = _call(client, prompt)
    data = _extract_json(text)
    items: List[NewsItem] = []
    for n in data.get("news", []):
        try:
            items.append(NewsItem(
                title=n["title"],
                url=n["url"],
                source=n.get("source", ""),
                category=n.get("category", "industry"),
                published=_safe_date(n.get("published", ""), date_str),
                summary=n.get("summary", ""),
            ))
        except Exception as e:
            logger.debug("跳过资讯条目: %s", e)
    logger.info("资讯收集完成：%d 条", len(items))
    return items


def _collect_papers(client: anthropic.Anthropic, date_str: str) -> List[Paper]:
    """搜索最新 arXiv AI/ML 论文（4-6 篇）。"""
    prompt = f"""今天是 {date_str}。请使用 web_search 搜索最近 3 天内 arXiv 发布的重要 AI/ML 论文（4-6 篇）。
重点关注 cs.AI、cs.LG、cs.CL 分类，优先选择有实际应用价值或引发广泛关注的工作。

搜索完成后，**仅输出**以下 JSON：
{{
  "papers": [
    {{
      "title": "论文英文原标题",
      "url": "https://arxiv.org/abs/XXXX.XXXXX",
      "arxiv_id": "XXXX.XXXXX",
      "authors": ["作者1", "作者2", "作者3"],
      "abstract": "100-200 字中文摘要，说明核心贡献和主要结论",
      "categories": ["cs.AI", "cs.LG"],
      "published": "YYYY-MM-DD",
      "pdf_url": "https://arxiv.org/pdf/XXXX.XXXXX"
    }}
  ]
}}"""
    text = _call(client, prompt)
    data = _extract_json(text)
    papers: List[Paper] = []
    for p in data.get("papers", []):
        try:
            papers.append(Paper(
                title=p["title"],
                url=p["url"],
                arxiv_id=p.get("arxiv_id", ""),
                authors=p.get("authors", []),
                abstract=p.get("abstract", ""),
                categories=p.get("categories", []),
                published=_safe_date(p.get("published", ""), date_str),
                pdf_url=p.get("pdf_url", ""),
            ))
        except Exception as e:
            logger.debug("跳过论文条目: %s", e)
    logger.info("论文收集完成：%d 篇", len(papers))
    return papers


def _collect_influencers(client: anthropic.Anthropic, date_str: str) -> List[InfluencerUpdate]:
    """搜索 AI 领域知名人物近期动态（3-5 条）。"""
    prompt = f"""今天是 {date_str}。请使用 web_search 搜索以下 AI 领域知名人物最近 3 天的博客/社交媒体动态：
Andrej Karpathy、Simon Willison、Sebastian Raschka、Yann LeCun、Sam Altman、Demis Hassabis、Geoffrey Hinton

搜索完成后，**仅输出**以下 JSON：
{{
  "updates": [
    {{
      "author": "人名（英文）",
      "platform": "Twitter/X 或 Blog 或 Newsletter",
      "content": "120-200 字中文摘要，描述其分享的核心观点或内容",
      "url": "原文链接",
      "published": "YYYY-MM-DD",
      "likes": 0,
      "reposts": 0
    }}
  ]
}}
如果找不到某位人物的近期动态，可以跳过，不要捏造。"""
    text = _call(client, prompt)
    data = _extract_json(text)
    updates: List[InfluencerUpdate] = []
    for u in data.get("updates", []):
        try:
            updates.append(InfluencerUpdate(
                author=u["author"],
                platform=u.get("platform", "Blog"),
                content=u.get("content", ""),
                url=u["url"],
                published=_safe_date(u.get("published", ""), date_str),
                likes=int(u.get("likes", 0)),
                reposts=int(u.get("reposts", 0)),
            ))
        except Exception as e:
            logger.debug("跳过大牛动态条目: %s", e)
    logger.info("大牛动态收集完成：%d 条", len(updates))
    return updates


def _collect_github(client: anthropic.Anthropic, date_str: str) -> List[GithubProject]:
    """搜索 GitHub Trending 热门 AI 项目（5-7 个）。"""
    prompt = f"""今天是 {date_str}。请使用 web_search 搜索 GitHub Trending 本周最热门的 AI/ML 相关开源项目（5-7 个）。
可以搜索 https://github.com/trending 或相关报道。

搜索完成后，**仅输出**以下 JSON：
{{
  "projects": [
    {{
      "name": "owner/repo",
      "url": "https://github.com/owner/repo",
      "description": "项目英文描述（原文）",
      "stars": 12345,
      "forks": 678,
      "language": "Python",
      "today_stars": 234
    }}
  ]
}}"""
    text = _call(client, prompt)
    data = _extract_json(text)
    projects: List[GithubProject] = []
    for p in data.get("projects", []):
        try:
            projects.append(GithubProject(
                name=p["name"],
                url=p["url"],
                description=p.get("description", ""),
                stars=int(p.get("stars", 0)),
                forks=int(p.get("forks", 0)),
                language=p.get("language", ""),
                today_stars=int(p.get("today_stars", 0)),
            ))
        except Exception as e:
            logger.debug("跳过 GitHub 项目条目: %s", e)
    logger.info("GitHub 项目收集完成：%d 个", len(projects))
    return projects


# ── 主入口 ───────────────────────────────────────────────────────────────────

def collect_all(
    date_str: str | None = None,
    parallel: bool = True,
) -> Tuple[List[NewsItem], List[Paper], List[InfluencerUpdate], List[GithubProject]]:
    """
    使用 Claude API + web_search 并发收集四类 AI 资讯。

    Args:
        date_str: 目标日期 (YYYY-MM-DD)，默认今天 UTC。
        parallel:  是否并发执行四类搜索（默认 True，约节省 3/4 时间）。

    Returns:
        (news_items, papers, influencer_updates, github_projects)

    Raises:
        ValueError: 未设置 ANTHROPIC_API_KEY 环境变量。
    """
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        raise ValueError("请设置 ANTHROPIC_API_KEY 环境变量")

    if date_str is None:
        date_str = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")

    client = anthropic.Anthropic(api_key=api_key)
    logger.info("开始收集 %s 的 AI 资讯（model=%s）…", date_str, MODEL)

    if not parallel:
        return (
            _collect_news(client, date_str),
            _collect_papers(client, date_str),
            _collect_influencers(client, date_str),
            _collect_github(client, date_str),
        )

    # 并发执行四个搜索任务
    tasks = {
        "news": lambda: _collect_news(client, date_str),
        "papers": lambda: _collect_papers(client, date_str),
        "influencers": lambda: _collect_influencers(client, date_str),
        "github": lambda: _collect_github(client, date_str),
    }
    results: dict = {}
    with ThreadPoolExecutor(max_workers=4) as executor:
        future_map = {executor.submit(fn): key for key, fn in tasks.items()}
        for future in as_completed(future_map):
            key = future_map[future]
            try:
                results[key] = future.result()
            except Exception as e:
                logger.warning("收集 %s 时出错（返回空列表）: %s", key, e)
                results[key] = []

    return (
        results.get("news", []),
        results.get("papers", []),
        results.get("influencers", []),
        results.get("github", []),
    )
