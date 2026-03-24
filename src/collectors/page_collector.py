"""页面抓取器 - 对无 RSS 的站点直接解析 HTML 文章列表"""
from __future__ import annotations

import logging
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import List, Optional
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

from src.config import settings, sources
from src.collectors.news_collector import NewsItem

logger = logging.getLogger(__name__)

# 看起来像文章 URL 的路径特征
_ARTICLE_PATH_RE = re.compile(
    r"/(blog|post|posts|news|article|articles|research|paper|update|"
    r"insight|story|read|entry|entries|press)/",
    re.IGNORECASE,
)
# 排除导航/资源链接
_SKIP_RE = re.compile(
    r"\.(css|js|png|jpg|jpeg|gif|svg|ico|pdf|zip)$|"
    r"/(tag|category|author|page|feed|rss|atom|login|signup|subscribe|"
    r"privacy|terms|about|contact)(/|$)",
    re.IGNORECASE,
)


def _looks_like_article(href: str, base_url: str) -> bool:
    """判断链接是否像一篇文章"""
    full = urljoin(base_url, href)
    parsed = urlparse(full)
    # 必须是同域名
    if urlparse(base_url).netloc not in parsed.netloc:
        return False
    path = parsed.path
    if _SKIP_RE.search(path):
        return False
    # 路径里有文章关键词，或路径层级 >= 2（排除首页 /）
    if _ARTICLE_PATH_RE.search(path):
        return True
    parts = [p for p in path.split("/") if p]
    return len(parts) >= 2


def _extract_date(el) -> Optional[datetime]:
    """从元素中提取日期（time 标签或 datetime 属性）"""
    time_el = el.find("time") if el else None
    if time_el:
        dt_str = time_el.get("datetime", "") or time_el.get_text(strip=True)
        for fmt in ("%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%SZ",
                    "%Y-%m-%d", "%B %d, %Y", "%b %d, %Y"):
            try:
                dt = datetime.strptime(dt_str[:len(fmt) + 5].strip(), fmt)
                return dt.replace(tzinfo=timezone.utc) if dt.tzinfo is None else dt
            except ValueError:
                continue
    return None


def scrape_page(page_config: dict) -> List[NewsItem]:
    """
    从单个 HTML 页面中提取文章列表。

    page_config 字段：
        name            来源名称
        url             页面 URL
        category        分类
        base_url        可选，链接补全用的基础 URL（默认同 url）
        link_selector   可选，BeautifulSoup CSS selector（默认自动检测）
    """
    items: List[NewsItem] = []
    name = page_config["name"]
    url = page_config["url"]
    category = page_config.get("category", "general")
    base_url = page_config.get("base_url", url)
    link_selector = page_config.get("link_selector", "a[href]")

    try:
        resp = requests.get(
            url,
            timeout=settings.request_timeout,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (compatible; AI-Daily-News-Bot/1.0; "
                    "+https://github.com/yf-sz/ai-daily-news)"
                ),
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            },
        )
        resp.raise_for_status()
    except Exception as e:
        logger.debug("页面抓取跳过 [%s]: %s", name, e)
        return items

    soup = BeautifulSoup(resp.text, "lxml")

    seen: set[str] = set()
    for a in soup.select(link_selector):
        href = a.get("href", "").strip()
        if not href or href.startswith(("#", "javascript:")):
            continue

        full_url = urljoin(base_url, href)
        if full_url in seen:
            continue
        if not _looks_like_article(href, base_url):
            continue
        seen.add(full_url)

        # 标题：优先取 <a> 内 h1/h2/h3，次取 <a> 文本，再取 title 属性
        title = ""
        for tag in ("h1", "h2", "h3", "h4"):
            h = a.find(tag)
            if h:
                title = h.get_text(strip=True)
                break
        if not title:
            title = a.get_text(strip=True) or a.get("title", "")
        title = re.sub(r"\s+", " ", title).strip()
        if not title or len(title) < 5:
            continue

        # 日期：从 <a> 父容器中找 <time>
        published = _extract_date(a.parent)

        # 摘要：从紧邻 <p> 取文字
        summary = ""
        p = a.find_next_sibling("p") or (a.parent and a.parent.find("p"))
        if p:
            summary = p.get_text(separator=" ", strip=True)[:200]

        items.append(NewsItem(
            title=title,
            url=full_url,
            source=name,
            category=category,
            published=published,
            summary=summary,
        ))

    # 去重（同标题保留第一条）
    seen_titles: set[str] = set()
    deduped: List[NewsItem] = []
    for item in items:
        key = item.title.lower()
        if key not in seen_titles:
            seen_titles.add(key)
            deduped.append(item)

    logger.info("  ✓ %s（页面抓取）: %d 条", name, len(deduped))
    return deduped[:settings.max_items_per_source]


def collect_all_pages() -> List[NewsItem]:
    """并发抓取所有 web_pages 配置的页面"""
    pages = sources.get("web_pages", [])
    if not pages:
        return []

    all_items: List[NewsItem] = []
    with ThreadPoolExecutor(max_workers=6) as executor:
        futures = {executor.submit(scrape_page, p): p for p in pages}
        for future in as_completed(futures):
            try:
                all_items.extend(future.result())
            except Exception as e:
                logger.debug("页面收集异常: %s", e)

    all_items.sort(
        key=lambda x: x.published or datetime.min.replace(tzinfo=timezone.utc),
        reverse=True,
    )
    return all_items
