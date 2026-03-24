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


def collect_github_trending() -> List[GithubProject]:
    """收集 GitHub AI 相关趋势项目"""
    projects: List[GithubProject] = []

    try:
        # 使用非官方 trending API
        resp = requests.get(
            "https://github-trending-api.walidvb.com/repositories",
            params={"language": "", "since": "daily", "spoken_language_code": ""},
            timeout=settings.request_timeout,
            headers={"User-Agent": "AI-Daily-News-Bot/1.0"},
        )
        resp.raise_for_status()
        data = resp.json()
    except Exception:
        # 备用：抓取 GitHub trending 页面
        try:
            resp = requests.get(
                "https://api.github.com/search/repositories",
                params={
                    "q": "topic:machine-learning+topic:deep-learning stars:>100",
                    "sort": "updated",
                    "order": "desc",
                    "per_page": 10,
                },
                timeout=settings.request_timeout,
                headers={
                    "User-Agent": "AI-Daily-News-Bot/1.0",
                    "Accept": "application/vnd.github.v3+json",
                },
            )
            resp.raise_for_status()
            items = resp.json().get("items", [])
            for item in items:
                projects.append(GithubProject(
                    name=item.get("full_name", ""),
                    url=item.get("html_url", ""),
                    description=item.get("description", "") or "",
                    stars=item.get("stargazers_count", 0),
                    forks=item.get("forks_count", 0),
                    language=item.get("language", "") or "",
                ))
            return projects[:10]
        except Exception as e:
            logger.warning(f"GitHub Trending 获取失败: {e}")
            return projects

    ai_keywords = {"ai", "llm", "ml", "deep", "neural", "gpt", "bert", "diffus", "transformer"}

    for repo in data[:30]:
        desc = (repo.get("description") or "").lower()
        name = repo.get("name", "").lower()
        if any(kw in desc or kw in name for kw in ai_keywords):
            projects.append(GithubProject(
                name=repo.get("author", "") + "/" + repo.get("name", ""),
                url=repo.get("url", ""),
                description=repo.get("description", "") or "",
                stars=repo.get("stars", 0),
                forks=repo.get("forks", 0),
                language=repo.get("language", "") or "",
                today_stars=repo.get("currentPeriodStars", 0),
                contributors=[c.get("username", "") for c in repo.get("builtBy", [])],
            ))

    return projects[:10]


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
