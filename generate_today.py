"""
自动生成今日 AI 日报并可选发布到博客。

使用 Claude API + web_search 实时搜索 AI 资讯，输出 Jekyll 格式的 Markdown 文章。

用法：
  # 仅生成文章到 reports/ 目录
  python generate_today.py

  # 指定日期
  python generate_today.py --date 2026-05-24

  # 生成并发布到博客（需配置 BLOG_DEPLOY_TOKEN 和 BLOG_REPO_URL）
  python generate_today.py --publish

  # 串行收集（便于调试，避免并发日志交叉）
  python generate_today.py --no-parallel

所需环境变量：
  ANTHROPIC_API_KEY    Claude API 密钥
  BLOG_DEPLOY_TOKEN    GitHub PAT（发布时需要，需 contents:write 权限）
  BLOG_REPO_URL        博客仓库地址（可选，默认 https://github.com/yf-sz/coco.github.io.git）
"""
import argparse
import logging
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from rich.console import Console
from rich.logging import RichHandler
from rich.panel import Panel
from rich.text import Text

console = Console()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="自动生成今日 AI 日报（Claude API + web_search）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--date", default=None, help="目标日期 YYYY-MM-DD（默认：今天 UTC）")
    parser.add_argument("--publish", action="store_true", help="生成后发布到博客")
    parser.add_argument("--no-parallel", action="store_true", help="串行收集（便于调试）")
    parser.add_argument("--output", type=Path, default=Path(__file__).parent / "reports",
                        help="报告输出目录（默认：./reports）")
    parser.add_argument("--verbose", "-v", action="store_true", help="详细日志")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(message)s",
        handlers=[RichHandler(console=console, rich_tracebacks=True)],
    )

    date_str = args.date or datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")

    console.print(Panel(
        Text(f"🤖 AI 日报自动生成  ·  {date_str}", style="bold cyan", justify="center"),
        subtitle="Claude API + web_search · 四类资讯并发收集",
    ))

    # ── 1. 收集数据 ──────────────────────────────────────────────────────────
    from src.ai_collector import collect_all
    try:
        news, papers, influencers, github = collect_all(
            date_str=date_str,
            parallel=not args.no_parallel,
        )
    except ValueError as e:
        console.print(f"[red]配置错误：{e}[/red]")
        sys.exit(1)
    except Exception as e:
        console.print(f"[red]收集失败：{e}[/red]")
        if args.verbose:
            console.print_exception()
        sys.exit(1)

    console.print(
        f"\n✅ 收集完成：[bold]资讯 {len(news)} 条[/bold] · "
        f"[bold]论文 {len(papers)} 篇[/bold] · "
        f"[bold]大牛动态 {len(influencers)} 条[/bold] · "
        f"[bold]GitHub 项目 {len(github)} 个[/bold]"
    )

    # ── 2. 生成 Jekyll 文章 ───────────────────────────────────────────────────
    from src.blog_publisher import generate_jekyll_post
    filename, content = generate_jekyll_post(news, papers, influencers, github)

    args.output.mkdir(parents=True, exist_ok=True)
    out_path = args.output / filename
    out_path.write_text(content, encoding="utf-8")

    console.print(f"📄 Jekyll 文章：[cyan]{out_path}[/cyan]  ({len(content):,} 字符)")

    # ── 3. 发布到博客 ─────────────────────────────────────────────────────────
    if args.publish:
        console.print("\n📝 正在发布到博客…")
        from src.blog_publisher import publish_from_env
        try:
            success = publish_from_env(news, papers, influencers, github)
        except Exception as e:
            console.print(f"[red]发布出错：{e}[/red]")
            success = False

        if success:
            console.print("✅ [bold green]博客发布成功[/bold green]")
        else:
            console.print(
                "⚠️  [yellow]博客发布跳过（请检查 BLOG_DEPLOY_TOKEN 和 BLOG_REPO_URL）[/yellow]"
            )


if __name__ == "__main__":
    main()
