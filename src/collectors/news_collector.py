"""新闻收集器 - 通过 RSS/Atom Feed 收集 AI 相关新闻（原生 xml.etree 解析，无需 feedparser）"""
from __future__ import annotations

import logging
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime
from typing import List, Optional

import requests

from src.config import settings, sources

logger = logging.getLogger(__name__)

# XML 命名空间
_NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "dc": "http://purl.org/dc/elements/1.1/",
    "content": "http://purl.org/rss/1.0/modules/content/",
    "media": "http://search.yahoo.com/mrss/",
}


@dataclass
class NewsItem:
    title: str
    url: str
    source: str
    category: str
    published: Optional[datetime]
    summary: str = ""
    tags: List[str] = field(default_factory=list)


def _strip_html(text: str) -> str:
    """去除 HTML 标签"""
    try:
        from bs4 import BeautifulSoup
        return BeautifulSoup(text, "lxml").get_text(separator=" ", strip=True)
    except Exception:
        return re.sub(r"<[^>]+>", " ", text).strip()


def _parse_date(date_str: str) -> Optional[datetime]:
    """解析多种日期格式，统一返回 UTC datetime"""
    if not date_str:
        return None
    date_str = date_str.strip()
    # RFC 2822 (RSS 2.0)
    try:
        dt = parsedate_to_datetime(date_str)
        return dt.astimezone(timezone.utc)
    except Exception:
        pass
    # ISO 8601 / Atom
    for fmt in (
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%d %H:%M:%S%z",
        "%Y-%m-%d",
    ):
        try:
            s = date_str[:len(fmt) + 6]
            dt = datetime.strptime(s, fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt.astimezone(timezone.utc)
        except ValueError:
            continue
    return None


def _is_recent(dt: Optional[datetime], days: int) -> bool:
    if dt is None:
        return True
    cutoff = datetime.now(tz=timezone.utc) - timedelta(days=days)
    return dt >= cutoff


def _text(el: ET.Element | None, *paths, ns=None) -> str:
    """从元素中提取文本，支持多路径回退"""
    if el is None:
        return ""
    for path in paths:
        try:
            found = el.find(path, ns or _NS)
            if found is not None and found.text:
                return found.text.strip()
        except Exception:
            pass
    return ""


def _parse_rss2(root: ET.Element, name: str, category: str) -> List[NewsItem]:
    """解析 RSS 2.0 格式"""
    items: List[NewsItem] = []
    channel = root.find("channel")
    if channel is None:
        channel = root

    for item in channel.findall("item")[: settings.max_items_per_source]:
        title = _text(item, "title")
        link = _text(item, "link")
        if not link:
            # link 有时作为 CDATA 文本节点而不是子元素
            link_el = item.find("link")
            if link_el is not None:
                link = (link_el.text or "").strip()

        # 日期
        date_str = _text(item, "pubDate") or _text(item, "dc:date", ns=_NS)
        published = _parse_date(date_str)
        if not _is_recent(published, settings.days_back):
            continue

        # 摘要
        summary_raw = (
            _text(item, "description")
            or _text(item, "content:encoded", ns=_NS)
            or ""
        )
        summary = _strip_html(summary_raw)[:300]
        if len(summary_raw) > 300:
            summary += "..."

        # 标签
        tags = [c.get("term", c.text or "") for c in item.findall("category")]

        if title and link:
            items.append(NewsItem(
                title=title,
                url=link,
                source=name,
                category=category,
                published=published,
                summary=summary,
                tags=tags,
            ))
    return items


def _parse_atom(root: ET.Element, name: str, category: str) -> List[NewsItem]:
    """解析 Atom 1.0 格式"""
    items: List[NewsItem] = []
    # root 就是 <feed>
    entries = root.findall("atom:entry", _NS) or root.findall("entry")
    for entry in entries[: settings.max_items_per_source]:
        title = _text(entry, "atom:title", "title")

        # link: 优先 rel=alternate
        link = ""
        for link_el in (entry.findall("atom:link", _NS) or entry.findall("link")):
            rel = link_el.get("rel", "alternate")
            href = link_el.get("href", "")
            if href and rel in ("alternate", ""):
                link = href
                break
        if not link:
            for link_el in (entry.findall("atom:link", _NS) or entry.findall("link")):
                href = link_el.get("href", "")
                if href:
                    link = href
                    break

        # 日期
        date_str = (
            _text(entry, "atom:published", "atom:updated", "published", "updated")
        )
        published = _parse_date(date_str)
        if not _is_recent(published, settings.days_back):
            continue

        # 摘要
        summary_raw = _text(entry, "atom:summary", "atom:content", "summary", "content")
        summary = _strip_html(summary_raw)[:300]
        if len(summary_raw) > 300:
            summary += "..."

        # 标签
        tags = [
            c.get("term", "")
            for c in (entry.findall("atom:category", _NS) or entry.findall("category"))
        ]

        if title and link:
            items.append(NewsItem(
                title=title,
                url=link,
                source=name,
                category=category,
                published=published,
                summary=summary,
                tags=tags,
            ))
    return items


def collect_from_rss(feed_config: dict) -> List[NewsItem]:
    """从单个 RSS/Atom Feed 收集新闻"""
    url = feed_config["url"]
    name = feed_config["name"]
    category = feed_config.get("category", "general")

    try:
        resp = requests.get(url, timeout=settings.request_timeout, headers={
            "User-Agent": "AI-Daily-News-Bot/1.0",
            "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml",
        })
        resp.raise_for_status()
        content = resp.content
    except Exception as e:
        logger.warning(f"无法获取 RSS [{name}]: {e}")
        return []

    try:
        # 去除 BOM 和非法 XML 字符
        if content.startswith(b"\xef\xbb\xbf"):
            content = content[3:]
        root = ET.fromstring(content)
    except ET.ParseError as e:
        logger.debug(f"XML 解析失败 [{name}]: {e}")
        return []

    tag = root.tag.lower()
    if "feed" in tag or "atom" in tag:
        return _parse_atom(root, name, category)
    else:
        return _parse_rss2(root, name, category)


def collect_all_news() -> List[NewsItem]:
    """并发收集所有配置来源的新闻（失败的源静默跳过）"""
    from concurrent.futures import ThreadPoolExecutor, as_completed

    all_items: List[NewsItem] = []
    feeds = sources.get("news_feeds", [])

    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_feed = {
            executor.submit(collect_from_rss, feed_config): feed_config
            for feed_config in feeds
        }
        for future in as_completed(future_to_feed):
            feed_config = future_to_feed[future]
            try:
                items = future.result()
                if items:
                    logger.info(f"  ✓ {feed_config['name']}: {len(items)} 条")
                all_items.extend(items)
            except Exception as e:
                logger.debug(f"  ✗ {feed_config['name']}: {e}")

    all_items.sort(
        key=lambda x: x.published or datetime.min.replace(tzinfo=timezone.utc),
        reverse=True,
    )
    return all_items
