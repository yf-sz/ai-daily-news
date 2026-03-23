"""AI Daily News - 主入口"""
from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

from rich.console import Console
from rich.logging import RichHandler
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.text import Text

console = Console()


def setup_logging(verbose: bool = False) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(message)s",
        handlers=[RichHandler(console=console, rich_tracebacks=True)],
    )


def run(
    output_dir: Path | None = None,
    days_back: int | None = None,
    skip_news: bool = False,
    skip_papers: bool = False,
    skip_influencers: bool = False,
    skip_github: bool = False,
    publish_blog: bool = False,
    verbose: bool = False,
) -> Path:
    """运行资讯收集并生成报告"""
    from src.config import settings

    if days_back is not None:
        settings.days_back = days_back

    setup_logging(verbose)
    logger = logging.getLogger(__name__)

    console.print(Panel(
        Text("🤖 AI Daily News Collector", style="bold cyan", justify="center"),
        subtitle=f"收集最近 {settings.days_back} 天的 AI 资讯",
    ))

    news_items = []
    papers = []
    influencer_updates = []
    github_projects = []

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
        transient=True,
    ) as progress:
        if not skip_news:
            task = progress.add_task("📰 收集 AI 资讯...", total=None)
            from src.collectors.news_collector import collect_all_news
            news_items = collect_all_news()
            progress.update(task, description=f"✅ 资讯：{len(news_items)} 条")
            progress.stop_task(task)

        if not skip_papers:
            task = progress.add_task("📄 收集最新论文...", total=None)
            from src.collectors.paper_collector import collect_all_papers
            papers = collect_all_papers()
            progress.update(task, description=f"✅ 论文：{len(papers)} 篇")
            progress.stop_task(task)

        if not skip_influencers:
            task = progress.add_task("🧑‍🔬 收集大牛动态...", total=None)
            from src.collectors.influencer_collector import collect_all_influencer_updates
            influencer_updates = collect_all_influencer_updates()
            progress.update(task, description=f"✅ 动态：{len(influencer_updates)} 条")
            progress.stop_task(task)

        if not skip_github:
            task = progress.add_task("🔥 收集 GitHub 热门项目...", total=None)
            from src.collectors.influencer_collector import collect_github_trending
            github_projects = collect_github_trending()
            progress.update(task, description=f"✅ 项目：{len(github_projects)} 个")
            progress.stop_task(task)

    # 生成 Markdown 报告（本地存档）
    from src.report_generator import generate_report, save_report
    report_content = generate_report(news_items, papers, influencer_updates, github_projects)
    report_path = save_report(report_content, output_dir)

    console.print(f"\n✅ [bold green]报告已生成：[/bold green][cyan]{report_path}[/cyan]")
    console.print(f"   📰 资讯：{len(news_items)} 条 | 📄 论文：{len(papers)} 篇 | "
                  f"🧑‍🔬 动态：{len(influencer_updates)} 条 | 🔥 项目：{len(github_projects)} 个")

    # 发布到 Jekyll 博客
    if publish_blog:
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
            transient=True,
        ) as progress:
            task = progress.add_task("📝 发布到博客...", total=None)
            from src.blog_publisher import publish_from_env
            success = publish_from_env(news_items, papers, influencer_updates, github_projects)
            if success:
                progress.update(task, description="✅ 博客发布成功")
            else:
                progress.update(task, description="⚠️  博客发布跳过（未配置 BLOG_DEPLOY_TOKEN）")
            progress.stop_task(task)

        if success:
            console.print("   📝 [bold green]已自动发布到博客[/bold green]")
        else:
            console.print("   ⚠️  [yellow]博客发布跳过，请检查 BLOG_DEPLOY_TOKEN 环境变量[/yellow]")

    return report_path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="AI Daily News - 收集每日最新 AI 资讯、论文和大牛动态",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例：
  python -m src.main                          # 收集今日资讯
  python -m src.main --days 3                 # 收集过去 3 天
  python -m src.main --skip-news              # 跳过新闻，只收集论文和动态
  python -m src.main --output ./my-reports    # 指定输出目录
  python -m src.main --verbose                # 详细日志
        """,
    )
    parser.add_argument("--days", type=int, default=None, help="收集过去几天的内容（默认：1）")
    parser.add_argument("--output", type=Path, default=None, help="报告输出目录")
    parser.add_argument("--skip-news", action="store_true", help="跳过资讯收集")
    parser.add_argument("--skip-papers", action="store_true", help="跳过论文收集")
    parser.add_argument("--skip-influencers", action="store_true", help="跳过大牛动态收集")
    parser.add_argument("--skip-github", action="store_true", help="跳过 GitHub 热门项目")
    parser.add_argument("--publish-blog", action="store_true",
                        help="生成报告后自动发布到 Jekyll 博客（需配置 BLOG_DEPLOY_TOKEN）")
    parser.add_argument("--verbose", "-v", action="store_true", help="输出详细日志")

    args = parser.parse_args()

    try:
        run(
            output_dir=args.output,
            days_back=args.days,
            skip_news=args.skip_news,
            skip_papers=args.skip_papers,
            skip_influencers=args.skip_influencers,
            skip_github=args.skip_github,
            publish_blog=args.publish_blog,
            verbose=args.verbose,
        )
    except KeyboardInterrupt:
        console.print("\n[yellow]已中断[/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"\n[red]错误：{e}[/red]")
        if args.verbose:
            console.print_exception()
        sys.exit(1)


if __name__ == "__main__":
    main()
