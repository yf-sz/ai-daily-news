"""报告生成器 - 将收集到的数据生成 Markdown 报告"""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import List

from src.collectors.news_collector import NewsItem
from src.collectors.paper_collector import Paper
from src.collectors.influencer_collector import InfluencerUpdate, GithubProject
from src.config import settings

# 分类中文名映射
CATEGORY_NAMES = {
    "industry": "产业动态",
    "research": "研究前沿",
    "newsletter": "社区通讯",
    "tools": "工具生态",
    "tutorial": "教程分享",
    "influencer": "大牛博客",
    "general": "综合资讯",
}


def _format_date(dt: datetime | None) -> str:
    if dt is None:
        return "未知"
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def _build_news_section(news_items: List[NewsItem]) -> str:
    if not news_items:
        return "_今日暂无最新资讯_\n"

    # 按分类分组
    by_category: dict[str, List[NewsItem]] = {}
    for item in news_items:
        by_category.setdefault(item.category, []).append(item)

    lines: List[str] = []
    for cat, items in by_category.items():
        cat_name = CATEGORY_NAMES.get(cat, cat)
        lines.append(f"\n### {cat_name}\n")
        for item in items[:8]:  # 每分类最多 8 条
            date_str = _format_date(item.published)
            lines.append(f"- **[{item.title}]({item.url})**")
            lines.append(f"  - 来源：{item.source} | 时间：{date_str}")
            if item.summary:
                lines.append(f"  - {item.summary}")
            lines.append("")

    return "\n".join(lines)


def _build_papers_section(papers: List[Paper]) -> str:
    if not papers:
        return "_今日暂无最新论文_\n"

    lines: List[str] = []
    for i, paper in enumerate(papers[:20], 1):
        date_str = _format_date(paper.published)
        authors_str = ", ".join(paper.authors[:3])
        if len(paper.authors) > 3:
            authors_str += f" 等 {len(paper.authors)} 人"

        cats_str = " / ".join(paper.categories[:3]) if paper.categories else ""

        lines.append(f"#### {i}. [{paper.title}]({paper.url})")
        lines.append(f"**作者：** {authors_str}")
        if cats_str:
            lines.append(f"**分类：** `{cats_str}`")
        lines.append(f"**发布：** {date_str}")

        links: List[str] = []
        if paper.pdf_url:
            links.append(f"[📄 PDF]({paper.pdf_url})")
        if paper.github_url:
            stars_badge = f" ⭐{paper.stars}" if paper.stars else ""
            links.append(f"[💻 代码]({paper.github_url}){stars_badge}")
        if links:
            lines.append(" | ".join(links))

        if paper.abstract:
            lines.append(f"\n> {paper.abstract}")

        lines.append("")

    return "\n".join(lines)


def _build_influencer_section(updates: List[InfluencerUpdate]) -> str:
    if not updates:
        return "_今日暂无大牛动态_\n"

    # 按平台分组
    by_platform: dict[str, List[InfluencerUpdate]] = {}
    for update in updates:
        by_platform.setdefault(update.platform, []).append(update)

    lines: List[str] = []
    for platform, items in by_platform.items():
        lines.append(f"\n### {platform}\n")
        for item in items[:10]:
            date_str = _format_date(item.published)
            lines.append(f"#### [{item.author}]({item.url})")
            lines.append(f"_{date_str}_")
            if platform == "Twitter/X":
                lines.append(f"\n{item.content}")
                stats = []
                if item.likes:
                    stats.append(f"❤️ {item.likes}")
                if item.reposts:
                    stats.append(f"🔁 {item.reposts}")
                if stats:
                    lines.append(" | ".join(stats))
            else:
                lines.append(f"\n{item.content}")
            lines.append("")

    return "\n".join(lines)


def _build_github_section(projects: List[GithubProject]) -> str:
    if not projects:
        return "_今日暂无热门项目_\n"

    lines: List[str] = []
    for i, proj in enumerate(projects[:10], 1):
        lang_badge = f"`{proj.language}`" if proj.language else ""
        today_badge = f"（今日 +{proj.today_stars}⭐）" if proj.today_stars else ""

        lines.append(f"#### {i}. [{proj.name}]({proj.url})")
        lines.append(f"⭐ {proj.stars:,} | 🍴 {proj.forks:,} | {lang_badge}{today_badge}")
        if proj.description:
            lines.append(f"\n{proj.description}")
        if proj.contributors:
            contribs = ", ".join(f"@{c}" for c in proj.contributors[:5])
            lines.append(f"\n贡献者：{contribs}")
        lines.append("")

    return "\n".join(lines)


def generate_report(
    news_items: List[NewsItem],
    papers: List[Paper],
    influencer_updates: List[InfluencerUpdate],
    github_projects: List[GithubProject],
) -> str:
    """生成完整的 Markdown 报告"""
    today = datetime.now(tz=timezone.utc).strftime("%Y年%m月%d日")
    generated_at = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    report = f"""# 🤖 AI 日报 - {today}

> 生成时间：{generated_at}
> 数据来源：RSS Feed / arXiv / Papers With Code / Twitter/X / GitHub

---

## 📰 AI 资讯

{_build_news_section(news_items)}

---

## 📄 最新论文

{_build_papers_section(papers)}

---

## 🧑‍🔬 大牛动态

{_build_influencer_section(influencer_updates)}

---

## 🔥 GitHub 热门 AI 项目

{_build_github_section(github_projects)}

---

*本报告由 AI Daily News 自动生成 | [项目地址](https://github.com/yf-sz/ai-daily-news)*
"""
    return report


def save_report(content: str, output_dir: Path | None = None) -> Path:
    """将报告保存为 Markdown 文件"""
    out_dir = output_dir or settings.output_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    date_str = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")
    file_path = out_dir / f"ai-daily-{date_str}.md"

    file_path.write_text(content, encoding="utf-8")
    return file_path
