"""新闻收集器 - 通过 RSS Feed 收集 AI 相关新闻"""
from __future__ import annotations

import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone, timedelta
from typing import List, Optional

import feedparser
import requests

from src.config import settings, sources

logger = logging.getLogger(__name__)


@dataclass
class NewsItem:
    title: str
    url: str
    source: str
    category: str
    published: Optional[datetime]
    summary: str = ""
    tags: List[str] = field(default_factory=list)


def _parse_published(entry) -> Optional[datetime]:
    """解析发布时间，统一转为 UTC datetime"""
    for attr in ("published_parsed", "updated_parsed"):
        t = getattr(entry, attr, None)
        if t:
            try:
                import time
                ts = time.mktime(t)
                return datetime.fromtimestamp(ts, tz=timezone.utc)
            except Exception:
                pass
    return None


def _is_recent(dt: Optional[datetime], days: int) -> bool:
    if dt is None:
        return True  # 无时间信息时默认包含
    cutoff = datetime.now(tz=timezone.utc) - timedelta(days=days)
    return dt >= cutoff


def collect_from_rss(feed_config: dict) -> List[NewsItem]:
    """从单个 RSS Feed 收集新闻"""
    items: List[NewsItem] = []
    url = feed_config["url"]
    name = feed_config["name"]
    category = feed_config.get("category", "general")

    try:
        # feedparser 本身处理 HTTP，设置 timeout 需要用 requests 预取
        resp = requests.get(url, timeout=settings.request_timeout, headers={
            "User-Agent": "AI-Daily-News-Bot/1.0"
        })
        resp.raise_for_status()
        feed = feedparser.parse(resp.content)
    except Exception as e:
        logger.warning(f"无法获取 RSS [{name}]: {e}")
        return items

    for entry in feed.entries[: settings.max_items_per_source]:
        published = _parse_published(entry)
        if not _is_recent(published, settings.days_back):
            continue

        summary = getattr(entry, "summary", "") or ""
        # 去除 HTML 标签
        try:
            from bs4 import BeautifulSoup
            summary = BeautifulSoup(summary, "lxml").get_text(separator=" ", strip=True)
        except Exception:
            pass
        summary = summary[:300] + ("..." if len(summary) > 300 else "")

        tags = [t.get("term", "") for t in getattr(entry, "tags", [])]

        items.append(NewsItem(
            title=entry.get("title", "无标题"),
            url=entry.get("link", ""),
            source=name,
            category=category,
            published=published,
            summary=summary,
            tags=tags,
        ))

    return items


def collect_all_news() -> List[NewsItem]:
    """收集所有配置来源的新闻"""
    all_items: List[NewsItem] = []
    feeds = sources.get("news_feeds", [])

    for feed_config in feeds:
        logger.info(f"收集新闻: {feed_config['name']}")
        items = collect_from_rss(feed_config)
        all_items.extend(items)
        logger.info(f"  → 获取 {len(items)} 条")

    # 按发布时间倒序排列
    all_items.sort(
        key=lambda x: x.published or datetime.min.replace(tzinfo=timezone.utc),
        reverse=True,
    )
    return all_items
