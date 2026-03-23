"""论文收集器 - 从 arXiv 和 Papers With Code 收集最新 AI 论文"""
from __future__ import annotations

import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone, timedelta
from typing import List, Optional

import requests

from src.config import settings, sources

logger = logging.getLogger(__name__)

ARXIV_API_URL = "http://export.arxiv.org/api/query"
PWC_API_URL = "https://paperswithcode.com/api/v1/papers/"


@dataclass
class Paper:
    title: str
    url: str
    arxiv_id: str
    authors: List[str]
    abstract: str
    categories: List[str]
    published: Optional[datetime]
    pdf_url: str = ""
    github_url: str = ""
    stars: int = 0


def _fetch_arxiv(category: str, max_results: int, days_back: int) -> List[Paper]:
    """通过 arXiv API 获取指定分类的最新论文"""
    papers: List[Paper] = []

    # 构建日期过滤查询
    cutoff = datetime.now(tz=timezone.utc) - timedelta(days=days_back)
    date_filter = cutoff.strftime("%Y%m%d") + "000000"

    params = {
        "search_query": f"cat:{category} AND submittedDate:[{date_filter} TO 99991231235959]",
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }

    try:
        resp = requests.get(ARXIV_API_URL, params=params, timeout=settings.request_timeout)
        resp.raise_for_status()
    except Exception as e:
        logger.warning(f"arXiv API 请求失败 [{category}]: {e}")
        return papers

    # 解析 Atom XML
    import xml.etree.ElementTree as ET
    ns = {
        "atom": "http://www.w3.org/2005/Atom",
        "arxiv": "http://arxiv.org/schemas/atom",
    }

    try:
        root = ET.fromstring(resp.content)
    except ET.ParseError as e:
        logger.warning(f"解析 arXiv 响应失败: {e}")
        return papers

    for entry in root.findall("atom:entry", ns):
        title_el = entry.find("atom:title", ns)
        title = title_el.text.strip().replace("\n", " ") if title_el is not None else ""

        abstract_el = entry.find("atom:summary", ns)
        abstract = abstract_el.text.strip().replace("\n", " ") if abstract_el is not None else ""
        abstract = abstract[:500] + ("..." if len(abstract) > 500 else "")

        published_el = entry.find("atom:published", ns)
        published = None
        if published_el is not None:
            try:
                published = datetime.fromisoformat(published_el.text.replace("Z", "+00:00"))
            except ValueError:
                pass

        # arxiv ID
        id_el = entry.find("atom:id", ns)
        arxiv_id = ""
        arxiv_url = ""
        if id_el is not None:
            arxiv_url = id_el.text.strip()
            arxiv_id = arxiv_url.split("/abs/")[-1]

        # PDF 链接
        pdf_url = ""
        for link in entry.findall("atom:link", ns):
            if link.get("title") == "pdf":
                pdf_url = link.get("href", "")
                break

        # 作者
        authors = [
            a.find("atom:name", ns).text.strip()
            for a in entry.findall("atom:author", ns)
            if a.find("atom:name", ns) is not None
        ]

        # 分类
        categories = [
            c.get("term", "")
            for c in entry.findall("atom:category", ns)
        ]

        papers.append(Paper(
            title=title,
            url=arxiv_url,
            arxiv_id=arxiv_id,
            authors=authors,
            abstract=abstract,
            categories=categories,
            published=published,
            pdf_url=pdf_url,
        ))

    return papers


def _fetch_papers_with_code(days_back: int, max_results: int = 20) -> List[Paper]:
    """从 Papers With Code 获取热门论文（附代码实现）"""
    papers: List[Paper] = []
    cutoff = (datetime.now(tz=timezone.utc) - timedelta(days=days_back)).strftime("%Y-%m-%d")

    try:
        resp = requests.get(
            PWC_API_URL,
            params={
                "ordering": "-published",
                "items_per_page": max_results,
                "published_after": cutoff,
            },
            timeout=settings.request_timeout,
            headers={"User-Agent": "AI-Daily-News-Bot/1.0"},
        )
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        logger.warning(f"Papers With Code API 请求失败: {e}")
        return papers

    for item in data.get("results", []):
        published = None
        if item.get("published"):
            try:
                published = datetime.fromisoformat(item["published"]).replace(tzinfo=timezone.utc)
            except ValueError:
                pass

        arxiv_id = item.get("arxiv_id", "") or ""
        papers.append(Paper(
            title=item.get("title", ""),
            url=item.get("url_abs", "") or f"https://arxiv.org/abs/{arxiv_id}",
            arxiv_id=arxiv_id,
            authors=item.get("authors", []) or [],
            abstract=item.get("abstract", "") or "",
            categories=[],
            published=published,
            pdf_url=item.get("url_pdf", "") or "",
            github_url=item.get("repository", {}).get("url", "") if item.get("repository") else "",
            stars=item.get("repository", {}).get("stars", 0) if item.get("repository") else 0,
        ))

    return papers


def collect_all_papers() -> List[Paper]:
    """收集所有来源的 AI 论文"""
    all_papers: List[Paper] = []
    seen_ids: set = set()

    # 1. 从 arXiv 各分类收集
    arxiv_cats = sources.get("arxiv_categories", [])
    per_cat = max(3, settings.max_items_per_source // len(arxiv_cats)) if arxiv_cats else 5

    for cat in arxiv_cats:
        logger.info(f"收集 arXiv 论文: {cat['id']} ({cat['name']})")
        papers = _fetch_arxiv(cat["id"], per_cat, settings.days_back)
        for p in papers:
            if p.arxiv_id not in seen_ids:
                seen_ids.add(p.arxiv_id)
                all_papers.append(p)
        logger.info(f"  → 获取 {len(papers)} 篇")

    # 2. 从 Papers With Code 补充热门论文（附代码）
    logger.info("收集 Papers With Code 热门论文...")
    pwc_papers = _fetch_papers_with_code(settings.days_back, max_results=10)
    added = 0
    for p in pwc_papers:
        if p.arxiv_id and p.arxiv_id in seen_ids:
            # 用 PWC 数据补充 GitHub 链接和 stars
            for existing in all_papers:
                if existing.arxiv_id == p.arxiv_id:
                    existing.github_url = p.github_url
                    existing.stars = p.stars
                    break
        elif p.arxiv_id not in seen_ids:
            seen_ids.add(p.arxiv_id)
            all_papers.append(p)
            added += 1
    logger.info(f"  → 新增 {added} 篇")

    # 按发布时间排序
    all_papers.sort(
        key=lambda x: x.published or datetime.min.replace(tzinfo=timezone.utc),
        reverse=True,
    )
    return all_papers
