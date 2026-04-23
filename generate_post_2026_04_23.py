"""
发布 2026-04-23 AI 日报到博客

用法：
  # 仅生成 Jekyll 文章到 reports/ 目录
  python generate_post_2026_04_23.py

  # 生成并发布到博客（需要设置 BLOG_DEPLOY_TOKEN 环境变量）
  BLOG_DEPLOY_TOKEN=your_token python generate_post_2026_04_23.py --publish
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
        'Google Cloud Next 2026：A2A 协议 v1.2 进入 Linux 基金会，Gemini Enterprise Agent 平台正式发布',
        'https://thenextweb.com/news/google-cloud-next-ai-agents-agentic-era',
        'The Next Web', 'industry', datetime(2026, 4, 23, tzinfo=timezone.utc),
        'Google Cloud Next 大会宣布 Agent2Agent（A2A）协议已有 150 家机构在生产环境部署，协议治理移交 Linux 基金会 Agentic AI Foundation；'
        'Vertex AI 更名为 Gemini Enterprise Agent Platform；发布无代码 Workspace Studio，支持跨 Gmail/Docs/Sheets 构建 Agent；'
        '开发者平台整合超 200 个模型（含 Anthropic Claude）；Project Mariner 浏览器 Agent 在 WebVoyager 基准得分 83.5%，支持 10 任务并发。'
    ),
    NewsItem(
        'Google 发布第七代 TPU Ironwood：单芯片 4.6 PetaFLOPS，9216 芯片超级 Pod 达 42.5 ExaFLOPS',
        'https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/',
        'Google Blog', 'industry', datetime(2026, 4, 22, tzinfo=timezone.utc),
        'Ironwood 是谷歌首款专为推理时代设计的 TPU，单芯片 192 GB HBM3E / 7.37 TB/s 带宽，性能较 TPU v5p 提升 10 倍；'
        '9216 芯片 Pod 总算力 42.5 ExaFLOPS，内存 1.77 PB；同步预告第八代 TPU 将分拆为训练版和推理版，采用台积电 2nm 制程。'
    ),
    NewsItem(
        'Mira Murati 的 Thinking Machines Lab 与 Google Cloud 签署数十亿美元合作协议',
        'https://techcrunch.com/2026/04/22/exclusive-google-deepens-thinking-machines-lab-ties-with-new-multi-billion-dollar-deal/',
        'TechCrunch', 'industry', datetime(2026, 4, 22, tzinfo=timezone.utc),
        '前 OpenAI CTO Mira Murati 创立的 Thinking Machines Lab（成立 14 个月）在 Cloud Next 期间宣布与 Google Cloud 扩大合作，'
        '协议价值数十亿美元，获取 Nvidia GB300 芯片及 Google 最新 AI 基础设施；该公司已完成 120 亿美元估值 20 亿美元种子轮，'
        '其产品 Tinker 可自动化创建定制前沿 AI 模型，此次合作非排他性。'
    ),
    NewsItem(
        'Anthropic Claude Opus 4.7 正式发布：高分辨率视觉、任务预算、xhigh 推理档位',
        'https://www.anthropic.com/news/claude-opus-4-7',
        'Anthropic', 'industry', datetime(2026, 4, 16, tzinfo=timezone.utc),
        'Claude Opus 4.7（4 月 16 日 GA）是 Anthropic 迄今最强 GA 模型，在高阶软件工程和长周期 Agentic 任务上大幅领先 Opus 4.6；'
        '首次支持高分辨率图像（最大 2576px / 3.75MP）；新增任务预算（Task Budget）机制控制 Agent 循环 token 消耗；'
        '引入 xhigh 推理档位；同步推出 Claude Design（视觉原型创作工具）；定价不变（$5/$25 per MTok）。'
    ),
    NewsItem(
        'Claude Code 大更新：Opus 4.7 xhigh 模式、Auto mode、/ultrareview 斜杠命令',
        'https://releasebot.io/updates/anthropic/claude-code',
        'Releasebot / Anthropic', 'tools', datetime(2026, 4, 22, tzinfo=timezone.utc),
        'Claude Code 随 Opus 4.7 同步升级：新增 /effort xhigh 命令、Max 订阅用户可用 Auto 模式自动切换推理档位；'
        '/ultrareview 支持多 Agent 云端代码审查；新增终端配色主题、大幅减少权限提示弹窗、改善 Windows 支持。'
    ),
    NewsItem(
        'Simon Willison：Claude Code 定价混乱深度解析，"$100/月"不太可能成真',
        'https://simonwillison.net/2026/Apr/22/claude-code-confusion/',
        'Simon Willison', 'tools', datetime(2026, 4, 22, tzinfo=timezone.utc),
        '针对近期网络盛传的 Claude Code 可能涨价到 $100/月 传言，Willison 详细梳理 Max 订阅、API 按量计费与 Claude Code 的关系，'
        '认为对大多数用户而言实际成本远低于预期，并强调 Anthropic 当前的定价沟通存在明确改进空间。'
    ),
    NewsItem(
        'Google Cloud Next 安全专场：新一代 Security Operations AI Agents + Wiz 深度集成',
        'https://siliconangle.com/2026/04/22/google-cloud-next-new-security-operations-agents-wiz-integrations-agent-governance-tools/',
        'SiliconAngle', 'industry', datetime(2026, 4, 22, tzinfo=timezone.utc),
        'Google Cloud 在 Next 发布新一批安全运营 AI Agent，自动化威胁检测、调查与响应；'
        '收购 Wiz 后深度集成云安全能力；新增 Agent Governance 工具，提供跨 Agent 的权限审计和行为监控框架。'
    ),
    NewsItem(
        'Anthropic 宣布：2027 年起将使用谷歌下一代 TPU 数吉瓦算力',
        'https://www.fool.com/investing/2026/04/22/anthropic-just-announced-huge-news-for-alphabet-an/',
        'Motley Fool', 'industry', datetime(2026, 4, 22, tzinfo=timezone.utc),
        'Anthropic 宣布从 2027 年起将使用谷歌下一代 TPU 提供数吉瓦级计算资源，这也标志着 Anthropic 与 Google 的战略绑定持续深化；'
        '对 Alphabet 和 Broadcom 均构成重大利好信号。'
    ),
    NewsItem(
        'PwC 2026 AI 绩效研究：AI 经济收益的 3/4 被 20% 顶尖企业垄断',
        'https://www.pwc.com/gx/en/news-room/press-releases/2026/pwc-2026-ai-performance-study.html',
        'PwC', 'research', datetime(2026, 4, 22, tzinfo=timezone.utc),
        'PwC 2026 年度 AI 绩效研究显示：AI 经济收益 3/4 集中于 20% 头部企业；领先企业将 AI 用于增长而非仅提效；'
        '2026 年 Q1 VC 投资额达 2672 亿美元，打破历史季度纪录（超上季度双倍）。'
    ),
]

# ── 论文 ────────────────────────────────────────────────────────────────────
papers = [
    Paper(
        'From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review',
        'https://arxiv.org/abs/2504.19678', '2504.19678',
        ['Comprehensive Review Team'],
        '系统梳理 LLM 推理到自主 Agent 演进路径，统一框架横向对比 2019-2025 年 25000+ Agent 运行评测基准，'
        '覆盖多域任务下的规划、工具调用与记忆机制。',
        ['cs.AI', 'cs.LG'], datetime(2026, 4, 20, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2504.19678v1',
    ),
    Paper(
        'Agentic Reasoning for Large Language Models',
        'https://arxiv.org/abs/2601.12538', '2601.12538',
        ['weitianxin et al.'],
        '将推理嵌入 LLM-Agent 的完整调查：涵盖规划、搜索、工具使用、记忆、反馈驱动适应与多 Agent 协调；'
        '配套 GitHub awesome 列表持续维护。',
        ['cs.AI', 'cs.CL'], datetime(2026, 4, 18, tzinfo=timezone.utc),
        'https://arxiv.org/abs/2601.12538',
        'https://github.com/weitianxin/Awesome-Agentic-Reasoning',
    ),
    Paper(
        'Uni-SafeBench: A Safety Benchmark for Unified Multimodal Large Models',
        'https://arxiv.org/list/cs.AI/current', '2604.UniSafe',
        ['Safety Research Group'],
        '针对统一多模态大模型的综合安全评测框架，覆盖图文融合场景下越狱攻击、对抗注入与幻觉检测，'
        '填补多模态 LLM 安全基准空白。',
        ['cs.CV', 'cs.CL'], datetime(2026, 4, 22, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.AI/current',
    ),
    Paper(
        'BloClaw: An Omniscient Multi-Modal Agentic Workspace for Next-Gen Scientific Discovery',
        'https://arxiv.org/list/cs.AI/current', '2604.BloClaw',
        ['BloClaw Team'],
        '多模态 Agentic 科学发现工作台，整合文献检索、实验设计、数据分析与论文撰写全流程，'
        '在跨模态科学推理基准上超越现有 Agentic 系统。',
        ['cs.AI', 'cs.LG'], datetime(2026, 4, 22, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.AI/current',
    ),
    Paper(
        'MOON3.0: Reasoning-Aware Multimodal Representation for E-commerce Product Understanding',
        'https://arxiv.org/list/cs.CV/current', '2604.MOON3',
        ['E-commerce AI Team'],
        '将推理能力注入多模态表征学习，在电商产品图文理解、属性提取与跨模态检索上刷新 SOTA，'
        '兼顾商业落地中的低延迟要求。',
        ['cs.CV', 'cs.IR'], datetime(2026, 4, 21, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.CV/current',
    ),
]

# ── 大牛动态 ─────────────────────────────────────────────────────────────────
updates = [
    InfluencerUpdate(
        'Andrej Karpathy', 'Blog / X',
        '在 X 上分享新方向：停止用 AI 生成代码，转而用 LLM 构建"第二大脑"——将研究素材丢入文件夹后，'
        '让 AI 自动生成互联 Wiki（含反向链接、分类体系），即 LLM Wiki 项目，已获大量关注和跟进实现。',
        'https://karpathy.github.io/', datetime(2026, 4, 20, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Simon Willison', 'Blog',
        '发布《Claude Code 定价混乱深度解析》，澄清 $100/月 传言；同时跟进 Google Cloud Next 核心发布，'
        '评测 Gemini 3.1 Pro SVG 动画能力（价格为 Opus 4.6 一半），综合覆盖本周 AI 生态大事件。',
        'https://simonwillison.net/2026/Apr/22/claude-code-confusion/', datetime(2026, 4, 22, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Sebastian Raschka', 'Newsletter (Ahead of AI)',
        '新一期深度文章：现代 LLM 中注意力变体可视化指南，从标准 MHA 到 GQA、混合注意力架构逐一拆解；'
        '结合 Opus 4.7 发布评述 Anthropic 2026 技术路线对开源社区的影响。',
        'https://magazine.sebastianraschka.com/', datetime(2026, 4, 22, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Chip Huyen', 'Blog',
        '深度分析 Google Cloud Next 发布的 Agent2Agent 协议正式进入 Linux 基金会后的治理意义，'
        '以及对企业 Agent 编排标准化的影响；探讨 Task Budget 机制在控制 Agentic 系统成本上的实用价值。',
        'https://huyenchip.com/', datetime(2026, 4, 22, tzinfo=timezone.utc),
    ),
]

# ── GitHub 热门 ──────────────────────────────────────────────────────────────
github = [
    GithubProject(
        'OpenClaw/openclaw',
        'https://github.com/OpenClaw/openclaw',
        'Personal AI assistant running entirely on your devices — local gateway to 50+ integrations (WhatsApp, Slack, Telegram, Discord…)',
        210000, 18400, 'TypeScript', 3200, ['openclaw-core', 'integrations-team'],
    ),
    GithubProject(
        'google/adk-python',
        'https://github.com/google/adk-python',
        'Google Agent Development Kit — modular framework for building multi-agent systems on Gemini & Vertex AI',
        12800, 1100, 'Python', 2800, ['google-devs'],
    ),
    GithubProject(
        'n8n-io/n8n',
        'https://github.com/n8n-io/n8n',
        'Fair-code workflow automation with native AI / LLM node support',
        98000, 26000, 'TypeScript', 1900, ['ivov', 'jan-montag', 'RicardoE105'],
    ),
    GithubProject(
        'mastra-ai/mastra',
        'https://github.com/mastra-ai/mastra',
        'TypeScript-first agent framework with workflow-driven development and built-in observability',
        19400, 1600, 'TypeScript', 1700, ['abhinav-mastra', 'DennisKainga'],
    ),
    GithubProject(
        'meta-llama/llama-stack',
        'https://github.com/meta-llama/llama-stack',
        'Standardized APIs for building Llama-powered agentic applications',
        14200, 1900, 'Python', 1400, ['ashwinb', 'yanxi0830'],
    ),
    GithubProject(
        'Shubhamsaboo/awesome-llm-apps',
        'https://github.com/Shubhamsaboo/awesome-llm-apps',
        '100+ AI Agent & RAG apps you can actually run — clone, customize, ship',
        42000, 5100, 'Python', 1200, ['Shubhamsaboo'],
    ),
    GithubProject(
        'ollama/ollama',
        'https://github.com/ollama/ollama',
        'Lightweight Go framework for running LLMs locally, now supports Llama 4 & Gemma 4',
        136000, 10800, 'Go', 1050, ['jmorganca', 'mxyng', 'technovangelist'],
    ),
    GithubProject(
        'caramaschiHG/awesome-ai-agents-2026',
        'https://github.com/caramaschiHG/awesome-ai-agents-2026',
        '🤖 The most comprehensive list of AI agents, frameworks & tools in 2026 — 300+ resources, 20+ categories',
        8700, 870, '', 980, ['caramaschiHG'],
    ),
]

# ── 主逻辑 ───────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description='生成并可选发布 2026-04-23 AI 日报')
    parser.add_argument('--publish', action='store_true', help='发布到博客（需 BLOG_DEPLOY_TOKEN）')
    args = parser.parse_args()

    filename, content = generate_jekyll_post(news, papers, updates, github)
    out_path = f'/home/user/ai-daily-news/reports/{filename}'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Jekyll 文章已生成：{filename}')
    print(f'路径：{out_path}')
    print(f'字符数：{len(content)}')

    if args.publish:
        success = publish_from_env(news, papers, updates, github)
        if success:
            print('✅ 已发布到博客')
        else:
            print('⚠️  发布失败，请检查 BLOG_DEPLOY_TOKEN 环境变量')


if __name__ == '__main__':
    main()
