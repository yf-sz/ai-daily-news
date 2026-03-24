"""AI 大牛动态收集器 - 收集知名 AI 研究者的最新动态"""
from __future__ import annotations

import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone, timedelta
from typing import List, Optional

import requests

from src.config import settings, sources

logger = logging.getLogger(__name__)


@dataclass
class InfluencerUpdate:
    author: str
    platform: str
    content: str
    url: str
    published: Optional[datetime]
    likes: int = 0
    reposts: int = 0
    tags: List[str] = field(default_factory=list)


# ─── Twitter/X ────────────────────────────────────────────────────────────────

def _collect_twitter_updates() -> List[InfluencerUpdate]:
    """通过 Twitter API v2 收集 AI 大牛推文"""
    updates: List[InfluencerUpdate] = []
    token = settings.twitter_bearer_token
    if not token:
        logger.info("未配置 TWITTER_BEARER_TOKEN，跳过 Twitter 收集")
        return updates

    accounts = sources.get("twitter_accounts", [])
    headers = {"Authorization": f"Bearer {token}"}
    cutoff = datetime.now(tz=timezone.utc) - timedelta(days=settings.days_back)
    start_time = cutoff.strftime("%Y-%m-%dT%H:%M:%SZ")

    for account in accounts:
        username = account["username"]
        name = account["name"]

        # 获取用户 ID
        try:
            resp = requests.get(
                f"https://api.twitter.com/2/users/by/username/{username}",
                headers=headers,
                timeout=settings.request_timeout,
            )
            resp.raise_for_status()
            user_id = resp.json()["data"]["id"]
        except Exception as e:
            logger.warning(f"获取 Twitter 用户 [{username}] 失败: {e}")
            continue

        # 获取最新推文
        try:
            resp = requests.get(
                f"https://api.twitter.com/2/users/{user_id}/tweets",
                headers=headers,
                timeout=settings.request_timeout,
                params={
                    "start_time": start_time,
                    "max_results": min(settings.max_items_per_source, 100),
                    "tweet.fields": "created_at,public_metrics,entities",
                    "exclude": "retweets,replies",
                },
            )
            resp.raise_for_status()
            tweets = resp.json().get("data", [])
        except Exception as e:
            logger.warning(f"获取 [{username}] 推文失败: {e}")
            continue

        for tweet in tweets:
            created_at = None
            if tweet.get("created_at"):
                try:
                    created_at = datetime.fromisoformat(
                        tweet["created_at"].replace("Z", "+00:00")
                    )
                except ValueError:
                    pass

            metrics = tweet.get("public_metrics", {})
            tweet_id = tweet["id"]

            updates.append(InfluencerUpdate(
                author=name,
                platform="Twitter/X",
                content=tweet["text"],
                url=f"https://twitter.com/{username}/status/{tweet_id}",
                published=created_at,
                likes=metrics.get("like_count", 0),
                reposts=metrics.get("retweet_count", 0),
            ))

        logger.info(f"  [{username}] 获取 {len(tweets)} 条推文")

    updates.sort(
        key=lambda x: x.published or datetime.min.replace(tzinfo=timezone.utc),
        reverse=True,
    )
    return updates


# ─── 博客 RSS（从新闻收集器中筛选 influencer 分类）─────────────────────────────

def _collect_blog_updates() -> List[InfluencerUpdate]:
    """从 RSS Feed 中收集 AI 研究者博客更新"""
    from src.collectors.news_collector import collect_from_rss

    updates: List[InfluencerUpdate] = []
    feeds = [f for f in sources.get("news_feeds", []) if f.get("category") == "influencer"]

    for feed_config in feeds:
        logger.info(f"收集博客更新: {feed_config['name']}")
        items = collect_from_rss(feed_config)
        for item in items:
            updates.append(InfluencerUpdate(
                author=feed_config["name"],
                platform="Blog",
                content=item.summary,
                url=item.url,
                published=item.published,
                tags=item.tags,
            ))
        logger.info(f"  → 获取 {len(items)} 篇")

    return updates


# ─── GitHub Trending（AI 相关热门项目）────────────────────────────────────────

@dataclass
class GithubProject:
    name: str
    url: str
    description: str
    stars: int
    forks: int
    language: str
    today_stars: int = 0
    contributors: List[str] = field(default_factory=list)


def _scrape_github_trending() -> List[GithubProject]:
    """直接抓取 GitHub Trending 官方页面（无需 API，最稳定）"""
    import os
    from bs4 import BeautifulSoup

    projects: List[GithubProject] = []
    try:
        resp = requests.get(
            "https://github.com/trending",
            params={"since": "daily"},
            timeout=settings.request_timeout,
            headers={"User-Agent": "Mozilla/5.0 (compatible; AI-Daily-News-Bot/1.0)"},
        )
        resp.raise_for_status()
    except Exception as e:
        logger.warning(f"抓取 GitHub Trending 页面失败: {e}")
        return projects

    soup = BeautifulSoup(resp.text, "lxml")
    for article in soup.select("article.Box-row")[:30]:
        try:
            # 仓库名
            repo_link = article.select_one("h2 a")
            if not repo_link:
                continue
            full_name = repo_link.get("href", "").strip("/")
            url = f"https://github.com/{full_name}"

            # 描述
            desc_el = article.select_one("p")
            description = desc_el.get_text(strip=True) if desc_el else ""

            # Stars / Forks
            def _parse_int(el) -> int:
                if el is None:
                    return 0
                txt = el.get_text(strip=True).replace(",", "").replace("k", "00")
                try:
                    return int(txt)
                except ValueError:
                    return 0

            stars = _parse_int(article.select_one("a[href$='/stargazers']"))
            forks = _parse_int(article.select_one("a[href$='/forks']"))

            # 今日新增 Stars
            today_el = article.select_one("span.d-inline-block.float-sm-right")
            today_stars = 0
            if today_el:
                txt = today_el.get_text(strip=True).replace(",", "")
                nums = [c for c in txt.split() if c.isdigit()]
                today_stars = int(nums[0]) if nums else 0

            # 语言
            lang_el = article.select_one("[itemprop='programmingLanguage']")
            language = lang_el.get_text(strip=True) if lang_el else ""

            # 贡献者
            contributors = [
                a.get("href", "").strip("/")
                for a in article.select("a[data-hovercard-type='user']")
            ]

            # 只保留 AI 相关
            ai_keywords = {
                "ai", "llm", "ml", "deep", "neural", "gpt", "bert",
                "diffus", "transformer", "model", "inference", "agent",
            }
            text = (full_name + " " + description).lower()
            if not any(kw in text for kw in ai_keywords):
                continue

            projects.append(GithubProject(
                name=full_name,
                url=url,
                description=description,
                stars=stars,
                forks=forks,
                language=language,
                today_stars=today_stars,
                contributors=contributors[:5],
            ))
        except Exception:
            continue

    return projects[:10]


def _search_github_api(token: str | None = None) -> List[GithubProject]:
    """使用 GitHub Search API 搜索热门 AI 项目（需 token 避免限速）"""
    import os
    projects: List[GithubProject] = []
    headers = {
        "User-Agent": "AI-Daily-News-Bot/1.0",
        "Accept": "application/vnd.github.v3+json",
    }
    # 优先使用传入 token，其次读环境变量（GitHub Actions 自动提供 GITHUB_TOKEN）
    auth_token = token or os.environ.get("GITHUB_TOKEN", "")
    if auth_token:
        headers["Authorization"] = f"Bearer {auth_token}"

    try:
        resp = requests.get(
            "https://api.github.com/search/repositories",
            params={
                "q": "topic:llm OR topic:deep-learning OR topic:machine-learning stars:>500",
                "sort": "stars",
                "order": "desc",
                "per_page": 15,
            },
            headers=headers,
            timeout=settings.request_timeout,
        )
        resp.raise_for_status()
        for item in resp.json().get("items", []):
            projects.append(GithubProject(
                name=item.get("full_name", ""),
                url=item.get("html_url", ""),
                description=item.get("description", "") or "",
                stars=item.get("stargazers_count", 0),
                forks=item.get("forks_count", 0),
                language=item.get("language", "") or "",
            ))
    except Exception as e:
        logger.warning(f"GitHub API 搜索失败: {e}")

    return projects[:10]


def collect_github_trending() -> List[GithubProject]:
    """收集 GitHub AI 相关趋势项目（官方页面抓取 → API 兜底）"""
    # 1. 优先抓取官方 Trending 页面（无需认证，结果最准确）
    projects = _scrape_github_trending()
    if projects:
        return projects

    # 2. 兜底：GitHub Search API（使用 GITHUB_TOKEN 避免限速）
    logger.info("Trending 页面抓取为空，使用 GitHub API 搜索兜底")
    return _search_github_api()


# ─── 主入口 ───────────────────────────────────────────────────────────────────

def collect_all_influencer_updates() -> List[InfluencerUpdate]:
    """收集所有 AI 大牛动态"""
    all_updates: List[InfluencerUpdate] = []

    # Twitter/X 动态
    twitter_updates = _collect_twitter_updates()
    all_updates.extend(twitter_updates)

    # 博客更新
    blog_updates = _collect_blog_updates()
    all_updates.extend(blog_updates)

    all_updates.sort(
        key=lambda x: x.published or datetime.min.replace(tzinfo=timezone.utc),
        reverse=True,
    )
    return all_updates
