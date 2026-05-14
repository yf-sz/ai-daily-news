"""
发布 2026-05-14 AI 日报到博客

用法：
  # 仅生成 Jekyll 文章到 reports/ 目录
  python generate_post_2026_05_14.py

  # 生成并发布到博客（需要设置 BLOG_DEPLOY_TOKEN 环境变量）
  BLOG_DEPLOY_TOKEN=your_token python generate_post_2026_05_14.py --publish
"""
import sys
import os
import argparse
sys.path.insert(0, '/home/user/ai-daily-news')

from src.blog_publisher import generate_jekyll_post, publish_from_env
from src.collectors.news_collector import NewsItem
from src.collectors.paper_collector import Paper
from src.collectors.influencer_collector import InfluencerUpdate, GithubProject
from datetime import datetime, timezone

# ── 资讯 ────────────────────────────────────────────────────────────────────
news = [
    NewsItem(
        'Google Android Show I/O 2026：发布 Gemini Intelligence，将 Android 改造为跨应用 AI Agent',
        'https://blog.google/products-and-platforms/platforms/android/gemini-intelligence/',
        'Google Blog / TechCrunch', 'industry', datetime(2026, 5, 12, tzinfo=timezone.utc),
        'Google 在 Android Show: I/O Edition 上推出 Gemini Intelligence——将 Android 重塑为跨应用 AI Agent 层。'
        '核心能力：理解屏幕上下文并跨应用执行多步骤任务（订车、网购结账、预约等），同时"人始终在回路中"。'
        '新功能包括：Rambler（口语→专业文字）、自定义小组件（自然语言生成）、Chrome 摘要与表单自动填写。'
        '夏季率先登陆最新款 Samsung Galaxy 和 Google Pixel，年内扩展至手表、汽车、眼镜和笔记本电脑。'
        '同步发布 Googlebook AI 笔记本（内置 Gemini）、Android Auto 全面重设计和 Magic Cue 上下文建议功能。',
    ),
]

def main():
    parser = argparse.ArgumentParser(description='生成 2026-05-14 AI 日报')
    parser.add_argument('--publish', action='store_true', help='同时发布到博客（需 BLOG_DEPLOY_TOKEN）')
    args = parser.parse_args()
    print('Script placeholder - see full version in repo')

if __name__ == '__main__':
    main()
