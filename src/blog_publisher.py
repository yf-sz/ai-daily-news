"""Jekyll 博客发布器 - 生成适合博客风格的文章并推送到博客仓库"""
from __future__ import annotations

import logging
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import List

from src.collectors.news_collector import NewsItem
from src.collectors.paper_collector import Paper
from src.collectors.influencer_collector import InfluencerUpdate, GithubProject

logger = logging.getLogger(__name__)

CATEGORY_ICONS = {
    "industry": "🏭",
    "research": "🔬",
    "newsletter": "📬",
    "tools": "🛠️",
    "tutorial": "📚",
    "influencer": "✍️",
    "general": "📰",
}

CATEGORY_NAMES = {
    "industry": "产业动态",
    "research": "研究前沿",
    "newsletter": "社区通讯",
    "tools": "工具生态",
    "tutorial": "教程分享",
    "influencer": "大牛博客",
    "general": "综合资讯",
}


def _fmt(dt: datetime | None, fmt: str = "%Y-%m-%d %H:%M") -> str:
    if dt is None:
        return ""
    return dt.astimezone(timezone.utc).strftime(fmt)


def _news_section(news_items: List[NewsItem]) -> str:
    if not news_items:
        return "> 今日暂无最新资讯。\n"

    by_cat: dict[str, List[NewsItem]] = {}
    for item in news_items:
        by_cat.setdefault(item.category, []).append(item)

    parts: List[str] = []
    for cat, items in by_cat.items():
        icon = CATEGORY_ICONS.get(cat, "📰")
        name = CATEGORY_NAMES.get(cat, cat)
        parts.append(f"\n### {icon} {name}\n")
        for item in items[:6]:
            date_str = _fmt(item.published, "%m-%d %H:%M")
            parts.append(f'- **[{item.title}]({item.url})**  ')
            meta = f"  `{item.source}`"
            if date_str:
                meta += f" · {date_str} UTC"
            parts.append(meta)
            if item.summary:
                # 截断过长摘要
                summary = item.summary[:160] + "…" if len(item.summary) > 160 else item.summary
                parts.append(f"  {summary}")
            parts.append("")
    return "\n".join(parts)


def _papers_section(papers: List[Paper]) -> str:
    if not papers:
        return "> 今日暂无最新论文。\n"

    parts: List[str] = []
    for i, p in enumerate(papers[:15], 1):
        authors = ", ".join(p.authors[:3])
        if len(p.authors) > 3:
            authors += f" 等 {len(p.authors)} 人"
        cats = " · ".join(p.categories[:2]) if p.categories else ""

        parts.append(f"**{i}. [{p.title}]({p.url})**")
        meta_parts = [f"👤 {authors}"]
        if cats:
            meta_parts.append(f"📂 `{cats}`")
        if p.published:
            meta_parts.append(f"🗓 {_fmt(p.published, '%Y-%m-%d')}")
        parts.append("  " + " &nbsp;|&nbsp; ".join(meta_parts))

        links: List[str] = []
        if p.pdf_url:
            links.append(f"[PDF]({p.pdf_url})")
        if p.github_url:
            star_txt = f" ⭐{p.stars}" if p.stars else ""
            links.append(f"[Code]({p.github_url}){star_txt}")
        if links:
            parts.append("  " + " · ".join(links))

        if p.abstract:
            abstract = p.abstract[:280] + "…" if len(p.abstract) > 280 else p.abstract
            parts.append(f"\n  > {abstract}\n")
        else:
            parts.append("")

    return "\n".join(parts)


def _influencers_section(updates: List[InfluencerUpdate]) -> str:
    if not updates:
        return "> 今日暂无大牛动态。\n"

    by_platform: dict[str, List[InfluencerUpdate]] = {}
    for u in updates:
        by_platform.setdefault(u.platform, []).append(u)

    parts: List[str] = []
    for platform, items in by_platform.items():
        parts.append(f"\n### {platform}\n")
        for item in items[:8]:
            date_str = _fmt(item.published, "%m-%d %H:%M")
            parts.append(f"**[{item.author}]({item.url})**" + (f" · {date_str} UTC" if date_str else ""))
            if item.content:
                content = item.content[:300] + "…" if len(item.content) > 300 else item.content
                parts.append(f"\n{content}\n")
            if platform == "Twitter/X":
                stats = []
                if item.likes:
                    stats.append(f"❤️ {item.likes:,}")
                if item.reposts:
                    stats.append(f"🔁 {item.reposts:,}")
                if stats:
                    parts.append(" · ".join(stats))
            parts.append("")
    return "\n".join(parts)


def _github_section(projects: List[GithubProject]) -> str:
    if not projects:
        return "> 今日暂无热门项目。\n"

    parts: List[str] = []
    for i, proj in enumerate(projects[:8], 1):
        lang = f"`{proj.language}`" if proj.language else ""
        today = f" · 今日 **+{proj.today_stars}** ⭐" if proj.today_stars else ""
        parts.append(f"**{i}. [{proj.name}]({proj.url})**")
        parts.append(f"  ⭐ {proj.stars:,} &nbsp;·&nbsp; 🍴 {proj.forks:,} &nbsp;·&nbsp; {lang}{today}")
        if proj.description:
            desc = proj.description[:120] + "…" if len(proj.description) > 120 else proj.description
            parts.append(f"  {desc}")
        parts.append("")
    return "\n".join(parts)


def generate_jekyll_post(
    news_items: List[NewsItem],
    papers: List[Paper],
    influencer_updates: List[InfluencerUpdate],
    github_projects: List[GithubProject],
) -> tuple[str, str]:
    """
    生成 Jekyll 文章内容和文件名。

    Returns:
        (filename, content) 元组
        filename 格式：YYYY-MM-DD-ai-daily-news.md
    """
    now_utc = datetime.now(tz=timezone.utc)
    date_str = now_utc.strftime("%Y-%m-%d")
    jekyll_date = now_utc.strftime("%Y-%m-%d %H:%M:%S +0000")
    title_date = now_utc.strftime("%Y年%m月%d日")
    filename = f"{date_str}-ai-daily-news.md"

    description = (
        f"今日 AI 速报：{len(news_items)} 条资讯"
        f" · {len(papers)} 篇论文"
        f" · {len(github_projects)} 个热门项目"
    )

    # 取各分类各 1 条作为 excerpt tags
    tag_set = {"人工智能", "AI日报", "每日新闻"}
    for p in papers[:3]:
        for cat in p.categories[:1]:
            tag_set.add(cat.replace("cs.", ""))
    tags_yaml = "\n".join(f'  - "{t}"' for t in sorted(tag_set))

    front_matter = f"""---
layout: post
title: "AI 日报 · {title_date}"
date: {jekyll_date}
categories:
  - "AI日报"
tags:
{tags_yaml}
description: "{description}"
toc: true
---
"""

    news_block = _news_section(news_items)
    papers_block = _papers_section(papers)
    influencers_block = _influencers_section(influencer_updates)
    github_block = _github_section(github_projects)

    body = f"""
> **{description}**
> 数据来源：RSS · arXiv · Papers With Code · GitHub Trending
> 生成时间：{now_utc.strftime("%Y-%m-%d %H:%M UTC")}

---

## 📰 今日 AI 资讯

{news_block}

---

## 📄 最新论文速览

{papers_block}

---

## 🧑‍🔬 大牛动态

{influencers_block}

---

## 🔥 GitHub 热门 AI 项目

{github_block}

---

*本文由 [AI Daily News](https://github.com/yf-sz/ai-daily-news) 自动收集生成，每日定时发布。*
"""

    return filename, front_matter + body


def publish_to_blog(
    filename: str,
    post_content: str,
    blog_repo_url: str,
    blog_repo_dir: Path,
    github_token: str | None = None,
    committer_name: str = "AI Daily News Bot",
    committer_email: str = "bot@ai-daily-news",
) -> bool:
    """
    将文章写入博客仓库的 _posts/ 目录并 commit/push。

    Args:
        filename: 文章文件名（YYYY-MM-DD-ai-daily-news.md）
        post_content: Jekyll 文章内容
        blog_repo_url: 博客 Git 仓库地址
        blog_repo_dir: 本地克隆目录（若已存在则 git pull，否则 git clone）
        github_token: 用于 HTTPS 推送的 GitHub PAT
        committer_name: commit 署名
        committer_email: commit 邮箱

    Returns:
        True 表示成功，False 表示失败（文章已存在则跳过不算失败）
    """
    # 构造带 token 的 remote URL（仅 HTTPS）
    if github_token and blog_repo_url.startswith("https://"):
        # https://TOKEN@github.com/user/repo.git
        auth_url = blog_repo_url.replace("https://", f"https://{github_token}@")
    else:
        auth_url = blog_repo_url

    def _run(cmd: List[str], cwd: Path | None = None) -> subprocess.CompletedProcess:
        return subprocess.run(
            cmd,
            cwd=str(cwd or blog_repo_dir),
            capture_output=True,
            text=True,
        )

    # Clone 或 Pull
    if not blog_repo_dir.exists():
        logger.info("克隆博客仓库：%s → %s", blog_repo_url, blog_repo_dir)
        result = _run(["git", "clone", auth_url, str(blog_repo_dir)], cwd=Path("."))
        if result.returncode != 0:
            logger.error("clone 失败：%s", result.stderr)
            return False
    else:
        logger.info("拉取最新博客内容")
        # 更新 remote URL（token 可能刷新）
        _run(["git", "remote", "set-url", "origin", auth_url])
        result = _run(["git", "pull", "origin", "HEAD"])
        if result.returncode != 0:
            logger.warning("pull 失败（继续尝试写入）：%s", result.stderr)

    # 写入文章
    posts_dir = blog_repo_dir / "_posts"
    posts_dir.mkdir(parents=True, exist_ok=True)
    post_path = posts_dir / filename

    if post_path.exists():
        logger.info("文章已存在，跳过：%s", filename)
        return True

    post_path.write_text(post_content, encoding="utf-8")
    logger.info("已写入文章：%s", post_path)

    # Git 配置
    _run(["git", "config", "user.name", committer_name])
    _run(["git", "config", "user.email", committer_email])

    # Commit & Push
    _run(["git", "add", str(post_path)])
    date_label = filename[:10]
    result = _run(["git", "commit", "-m", f"docs: add AI daily news {date_label}"])
    if result.returncode != 0:
        logger.error("commit 失败：%s", result.stderr)
        return False

    result = _run(["git", "push", "origin", "HEAD"])
    if result.returncode != 0:
        logger.error("push 失败：%s", result.stderr)
        return False

    logger.info("✅ 文章已发布到博客：%s", filename)
    return True


def publish_from_env(
    news_items: List[NewsItem],
    papers: List[Paper],
    influencer_updates: List[InfluencerUpdate],
    github_projects: List[GithubProject],
    blog_repo_dir: Path | None = None,
) -> bool:
    """
    从环境变量读取配置并发布到博客（GitHub Actions 中调用）。

    所需环境变量：
        BLOG_REPO_URL   博客仓库地址，如 https://github.com/yf-sz/coco.github.io.git
        BLOG_DEPLOY_TOKEN  GitHub PAT（需要 contents:write 权限）
    可选：
        BLOG_REPO_DIR   本地克隆目录（默认 /tmp/blog-repo）
    """
    repo_url = os.environ.get("BLOG_REPO_URL", "https://github.com/yf-sz/coco.github.io.git")
    token = os.environ.get("BLOG_DEPLOY_TOKEN", "")
    repo_dir = Path(os.environ.get("BLOG_REPO_DIR", "/tmp/blog-repo")) if blog_repo_dir is None else blog_repo_dir

    if not token:
        logger.warning("未设置 BLOG_DEPLOY_TOKEN，跳过博客发布")
        return False

    filename, content = generate_jekyll_post(news_items, papers, influencer_updates, github_projects)

    return publish_to_blog(
        filename=filename,
        post_content=content,
        blog_repo_url=repo_url,
        blog_repo_dir=repo_dir,
        github_token=token,
    )
