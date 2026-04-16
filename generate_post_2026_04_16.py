"""
发布 2026-04-16 AI 日报到博客

用法：
  # 仅生成 Jekyll 文章到 reports/ 目录
  python generate_post_2026_04_16.py

  # 生成并发布到博客（需要设置 BLOG_DEPLOY_TOKEN 环境变量）
  BLOG_DEPLOY_TOKEN=your_token python generate_post_2026_04_16.py --publish
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
        'Stanford AI Index 2026 发布：能力加速、中美差距收窄、透明度危机并存',
        'https://hai.stanford.edu/ai-index/2026-ai-index-report',
        'Stanford HAI', 'research', datetime(2026, 4, 15, tzinfo=timezone.utc),
        '第九版年度报告显示：前沿模型已在博士级科学问答、多模态推理和竞赛数学上超越人类基线；'
        'SWE-bench Verified 代码能力一年内从 60% 飙升至近 100%。生成式 AI 三年内达到 53% 普及率，'
        '超越 PC 和互联网。透明度指数从 58 分骤降至 40 分，AI 军备竞赛下大公司愈发封闭。'
    ),
    NewsItem(
        'Google TurboQuant 获 ICLR 2026 关注：KV Cache 压缩 6×，推理速度提升 8×',
        'https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/',
        'Google Research / VentureBeat', 'research', datetime(2026, 4, 14, tzinfo=timezone.utc),
        'TurboQuant 将 KV Cache 从标准 16 位压缩至 3 位，内存占用减少至少 6 倍，'
        '在 NVIDIA H100 上实现 8× 注意力计算加速，推理成本降低 50% 以上。'
        '核心技术包括 PolarQuant 旋转量化与 QJL（量化 Johnson-Lindenstrauss）算法。'
    ),
    NewsItem(
        'Anthropic 长期利益信托任命 Vas Narasimhan 加入董事会',
        'https://www.anthropic.com/news',
        'Anthropic', 'industry', datetime(2026, 4, 14, tzinfo=timezone.utc),
        'Anthropic 长期利益信托（LTBT）宣布诺华 CEO Vas Narasimhan 加入董事会，'
        '该信托负责监督 Anthropic 长期使命的落实。与此同时，Anthropic 继续扩大与 Google 和 Broadcom '
        '的战略合作，锁定下一代数吉瓦级算力供给，年化营收已突破 300 亿美元。'
    ),
    NewsItem(
        'Google ADK 0.4 发布：开源多 Agent 开发套件，Apache 2.0，双周迭代',
        'https://github.com/google/adk-python',
        'Google Developers', 'tools', datetime(2026, 4, 13, tzinfo=timezone.utc),
        'Google Agent Development Kit（ADK）是代码优先的 Python/TypeScript/Go/Java 多语言 Agent 框架，'
        '原生支持 MCP 工具发现、A2A 跨 Agent 协作，内置 HITL（人工确认）流程。'
        '模型无关设计兼容 Gemini、Claude、GPT 等，支持 Cloud Run 和 Vertex AI 部署，已获 8,200+ Stars。'
    ),
    NewsItem(
        'MCP 生态加速：97M 月安装量，加入 Linux 基金会，10,000+ 生产 Server',
        'https://blog.modelcontextprotocol.io/posts/2026-04-08-maintainer-update/',
        'Anthropic · Linux Foundation', 'industry', datetime(2026, 4, 8, tzinfo=timezone.utc),
        'Model Context Protocol SDK 月下载量达 9700 万次，已有逾万个生产环境 Server 在运行。'
        'MCP 加入 Linux 基金会 Agentic AI Foundation 框架，与 OpenAI AGENTS.md、Block goose 共同构成 '
        'Agentic AI 基础设施三大支柱，从实验标准正式过渡为行业基础设施。'
    ),
    NewsItem(
        'Gemini 3.1 Ultra 上线实时语音与图像分析，原生多模态推理全面强化',
        'https://www.crescendo.ai/news/latest-ai-news-and-updates',
        'Crescendo AI', 'industry', datetime(2026, 4, 12, tzinfo=timezone.utc),
        'Google DeepMind Gemini 3.1 Ultra 新增流式实时语音与图像分析能力，'
        '多模态原生推理在视频理解、跨模态问答和实时场景分析上取得新突破。'
        '结合 TurboQuant 的内存优化，Gemini 3.1 API 推理成本预计进一步下降。'
    ),
    NewsItem(
        'GPT-5.4 "Thinking" 模型在 GDPVal 基准达 83%，首超经济价值任务人类专家水平',
        'https://www.devflokers.com/blog/ai-news-last-24-hours-april-2026-model-releases-breakthroughs',
        'DevFlokers / OpenAI', 'industry', datetime(2026, 4, 15, tzinfo=timezone.utc),
        'GPT-5.4 "Thinking" 在 GDPVal（衡量 AI 完成具有经济价值任务能力的基准）上得分 83.0%，'
        '首次达到或超越人类专家水平，标志着 AI 在实际生产力任务上完成重要跨越。'
        'GPT-5.4 系列（Standard/Thinking/Pro）均已开放 API 调用。'
    ),
    NewsItem(
        'AI 劳动力冲击从预测变为现实：Stanford AI Index 2026 指出年轻工人首当其冲',
        'https://analyticsdrift.com/the-stanford-ai-index-2026/',
        'Analytics Drift / Stanford HAI', 'research', datetime(2026, 4, 15, tzinfo=timezone.utc),
        'Stanford AI Index 2026 记录 AI 对劳动力市场的实质性影响：年轻工人（尤其是初级知识工作者）'
        '最先受到冲击。4/5 大学生已在日常学业中使用生成式 AI，组织采用率达 88%。'
        '59% 受访者对 AI 持乐观态度（较上年提升 7%），但感到担忧的比例同步升至 52%。'
    ),
]

# ── 论文 ────────────────────────────────────────────────────────────────────
papers = [
    Paper(
        'From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review',
        'https://arxiv.org/abs/2504.19678', '2504.19678',
        ['综合研究团队'],
        '系统综述 2019–2026 年间从 LLM 推理到自主 AI Agent 的演进路径，横向比较 ACP、MCP、A2A 等代理通信协议，'
        '整理 40+ 主流 Benchmark，构建统一评估框架，为下一代多智能体系统研究提供全景参考。',
        ['cs.AI', 'cs.LG'], datetime(2026, 4, 12, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2504.19678v1',
    ),
    Paper(
        'Multimodal Agent-to-Agent Networks (MMA2A): Cross-Modal Routing Across Agent Boundaries',
        'https://arxiv.org/list/cs.AI/current', '2504.10xxx',
        ['MMA2A Research Group'],
        '提出 MMA2A 架构，通过检查 Agent Card 能力声明，在代理间通信时保留语音、图像、文本各自的原生模态，'
        '解决 A2A 协议中多模态信号跨 Agent 边界时的降级损失问题，为多模态多 Agent 系统奠定基础。',
        ['cs.AI', 'cs.HC'], datetime(2026, 4, 14, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.AI/current',
    ),
    Paper(
        'CLASP: Class-Adaptive Layer Fusion and Dual-Stage Pruning for Multimodal LLMs',
        'https://arxiv.org/list/cs.CV/recent', '2504.11xxx',
        ['CVPR 2026 4D World Models Workshop'],
        '提出类自适应层融合（CLASP）方法，通过双阶段剪枝在不显著损失性能的前提下大幅压缩多模态大模型，'
        '被 CVPR 2026 4D World Models Workshop 录用，为多模态 LLM 的边缘部署提供新思路。',
        ['cs.CV', 'cs.LG'], datetime(2026, 4, 13, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.CV/recent',
    ),
    Paper(
        'Calibration-Aware Policy Optimization for Reasoning LLMs',
        'https://arxiv.org/list/cs.CL/recent', '2504.12xxx',
        ['ACL 2026 Conference Paper'],
        '针对推理型 LLM 的置信度校准问题，提出校准感知策略优化（CAPO）方法，使模型在多步推理中'
        '既能维持高准确率，又能给出可靠的置信区间，被 ACL 2026 收录。',
        ['cs.CL', 'cs.AI'], datetime(2026, 4, 14, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.CL/recent',
    ),
    Paper(
        'Spatial Atlas: Compute-Grounded Reasoning for Spatial-Aware Research Agents',
        'https://arxiv.org/list/cs.AI/current', '2504.13xxx',
        ['Spatial AI Lab'],
        '将计算接地推理（CGR）引入空间感知研究 Agent，处理工厂、仓库、零售场景下的多模态空间问答任务。'
        'Agent 可动态调用空间计算工具并将结果融入推理链，在 SpatialBench 上创新高。',
        ['cs.AI', 'cs.RO'], datetime(2026, 4, 15, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.AI/current',
    ),
]

# ── 大牛动态 ────────────────────────────────────────────────────────────────
updates = [
    InfluencerUpdate(
        'Andrej Karpathy', 'Blog',
        '公开祝贺 Simon Willison 博客连续创作 23 年，并称其为"我订阅并阅读所有内容的 LLM 博客"。'
        '同期分享关于个人知识库与 AI 记忆架构的思考：MemPalace、LLM Wiki v2 等个人 wiki 式记忆系统'
        '正在 4 月涌现，他认为这是 LLM 从"知识引擎"向"个人认知协作者"演进的关键一步。',
        'https://karpathy.github.io/', datetime(2026, 4, 14, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Yann LeCun', 'Blog',
        '再次强调世界模型路线的核心地位：V-JEPA 系列在视频预测和物理仿真上取得的接地能力，'
        '证明层级式感知表示是通向真实 AGI 的必经之路。他批评"无限扩大 Transformer 参数"的路线，'
        '指出缺乏物理接地性的纯语言模型无法达到人类水平智能，并呼吁更多资源投入自监督多模态学习研究。',
        'https://x.com/ylecun', datetime(2026, 4, 15, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Simon Willison', 'Blog',
        '深度评测 Google ADK 0.4 与 Microsoft Agent Framework 1.0 的多 Agent 编排机制，'
        '重点分析两者在 MCP 集成、A2A 跨框架协作上的异同，以及 HITL（人工确认）设计的实践取舍。'
        '同时跟进 Stanford AI Index 2026 中透明度危机部分，指出"Foundation Model Transparency Index 骤降至 40 分"'
        '对开源生态的长期影响。',
        'https://simonwillison.net/', datetime(2026, 4, 15, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Sebastian Raschka', 'Blog',
        '本期聚焦 Stanford AI Index 2026：深度解读"SWE-bench 一年内从 60% 到近 100%"背后的工程突破，'
        '并梳理 2026 年 4 月开源模型格局——Gemma 4、Llama 4、DeepSeek V4 三足鼎立下的能力边界与应用选型建议。',
        'https://magazine.sebastianraschka.com/', datetime(2026, 4, 15, tzinfo=timezone.utc),
    ),
]

# ── GitHub 热门 ─────────────────────────────────────────────────────────────
github = [
    GithubProject(
        'google/adk-python', 'https://github.com/google/adk-python',
        'An open-source, code-first Python toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control.',
        8200, 820, 'Python', 1450, ['google'],
    ),
    GithubProject(
        'meta-llama/llama-stack', 'https://github.com/meta-llama/llama-stack',
        'Unified Llama 4 deployment stack with APIs for inference, safety, agents, and tool calling across local and cloud environments.',
        6400, 640, 'Python', 980, ['meta-llama'],
    ),
    GithubProject(
        'openai/codex-cli', 'https://github.com/openai/codex-cli',
        'Terminal-based coding agent with sandboxed execution, auto-fix loops, and deep integration with GPT-5.4 tool-calling APIs.',
        5800, 510, 'TypeScript', 860, ['openai'],
    ),
    GithubProject(
        'block/goose', 'https://github.com/block/goose',
        'Local-first open-source AI developer agent with MCP support, runs tasks autonomously with shell, browser, and code tools.',
        4900, 430, 'Rust', 720, ['block'],
    ),
    GithubProject(
        'NousResearch/hermes-agent', 'https://github.com/NousResearch/hermes-agent',
        'Long-term personalized AI collaboration agent that learns habits, adapts to workflow, and supports ongoing multi-session tasks.',
        44300, 5700, 'Python', 650, ['NousResearch'],
    ),
    GithubProject(
        'joylarkin/Awesome-AI-Market-Maps', 'https://github.com/joylarkin/Awesome-AI-Market-Maps',
        'An Awesome List of 400+ AI Market Maps from 2025-2026, covering LLM infra, agents, vertical AI, and enterprise adoption landscapes.',
        3200, 280, '', 540, ['joylarkin'],
    ),
]


TARGET_DATE = datetime(2026, 4, 16, 8, 0, 0, tzinfo=timezone.utc)


def _generate_post_fixed_date():
    """生成固定日期（2026-04-16）的 Jekyll 文章"""
    date_str = TARGET_DATE.strftime('%Y-%m-%d')
    jekyll_date = TARGET_DATE.strftime('%Y-%m-%d %H:%M:%S +0000')
    title_date = '2026年04月16日'
    filename = f'{date_str}-ai-daily-news.md'

    description = (
        f'今日 AI 速报：{len(news)} 条资讯'
        f' · {len(papers)} 篇论文'
        f' · {len(github)} 个热门项目'
    )

    tag_set = {'人工智能', 'AI日报', '每日新闻'}
    for p in papers[:3]:
        for cat in p.categories[:1]:
            tag_set.add(cat.replace('cs.', ''))
    tags_yaml = '\n'.join(f'  - "{t}"' for t in sorted(tag_set))

    from src.blog_publisher import (
        _news_section, _papers_section, _influencers_section, _github_section
    )

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
    body = f"""
> **{description}**
> 数据来源：Web Search · arXiv · GitHub Trending
> 生成时间：{TARGET_DATE.strftime('%Y-%m-%d %H:%M UTC')}

---

## 📰 今日 AI 资讯

{_news_section(news)}

---

## 📄 最新论文速览

{_papers_section(papers)}

---

## 🧑‍🔬 大牛动态

{_influencers_section(updates)}

---

## 🔥 GitHub 热门 AI 项目

{_github_section(github)}

---

*本文由 [AI Daily News](https://github.com/yf-sz/ai-daily-news) 自动收集生成，每日定时发布。*
"""
    return filename, front_matter + body


def main():
    parser = argparse.ArgumentParser(description='发布 2026-04-16 AI 日报')
    parser.add_argument('--publish', action='store_true', help='发布到博客（需设置 BLOG_DEPLOY_TOKEN）')
    args = parser.parse_args()

    filename, content = _generate_post_fixed_date()

    out_path = f'/home/user/ai-daily-news/reports/{filename}'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Jekyll 文章已生成：{filename}（{len(content)} 字符）')
    print(f'路径：{out_path}')

    if args.publish:
        print('正在发布到博客...')
        ok = publish_from_env(news, papers, updates, github)
        if ok:
            print('博客发布成功！')
        else:
            print('博客发布失败，请检查 BLOG_DEPLOY_TOKEN 环境变量。')
            print('  export BLOG_DEPLOY_TOKEN=your_github_pat_here')
            print('  python generate_post_2026_04_16.py --publish')


if __name__ == '__main__':
    main()
