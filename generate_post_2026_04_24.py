"""
发布 2026-04-24 AI 日报到博客

用法：
  # 仅生成 Jekyll 文章到 reports/ 目录
  python generate_post_2026_04_24.py

  # 生成并发布到博客（需要设置 BLOG_DEPLOY_TOKEN 环境变量）
  BLOG_DEPLOY_TOKEN=your_token python generate_post_2026_04_24.py --publish
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
        'OpenAI 正式发布 GPT-5.5：首款完全重训 Agentic 模型，Terminal-Bench 2.0 得分 82.7%',
        'https://techcrunch.com/2026/04/23/openai-chatgpt-gpt-5-5-ai-model-superapp/',
        'TechCrunch', 'industry', datetime(2026, 4, 23, tzinfo=timezone.utc),
        'GPT-5.5 是 OpenAI 自 GPT-4.5 以来首个完全重训的基础模型，专为 Agentic 计算机使用场景设计：自主写代码、调试、浏览网页、填写表格并完成多步骤任务，无需人工监督每一步。'
        'Terminal-Bench 2.0 达到 82.7%，GDPval 84.9%，均刷新 SOTA。'
        'Greg Brockman 称其为"新一类智能"。即日起向 Plus、Pro、Business、Enterprise 用户开放，5.5 Pro 版向 Pro 及以上用户开放。'
    ),
    NewsItem(
        'Anthropic 二级市场估值突破 1 万亿美元，超越 OpenAI（8800 亿）',
        'https://thenextweb.com/news/anthropic-1-trillion-valuation-secondary-market',
        'The Next Web', 'industry', datetime(2026, 4, 23, tzinfo=timezone.utc),
        '在私人股权交易平台 Forge Global，Anthropic 隐含估值已攀升至约 1 万亿美元，超过 OpenAI（8800 亿）。'
        '距上一轮主融资（GIC/Coatue 领投，估值 3800 亿）不足三个月，差距悬殊。'
        '年化收入从去年底 90 亿美元飙升至 2026 年 3 月 300 亿美元，增长主要由 Claude Code 在开发者群体的爆发式采用驱动。'
        '分析师提示：二级市场价格反映的是对非流动性少数股的出价，与一级融资估值性质不同。'
    ),
    NewsItem(
        'Google TurboQuant：KV Cache 6 倍压缩，3.5-bit 量化无需重训、近零精度损失',
        'https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/',
        'Google Research', 'research', datetime(2026, 4, 22, tzinfo=timezone.utc),
        'Google Research 发布 TurboQuant，对 LLM KV Cache 实现 6 倍压缩，无需校准数据或模型重训，在所有基准上保持完整精度，同时降低推理延迟。'
        '核心技术：PolarQuant（向量旋转） + QJL（量化 Johnson-Lindenstrauss 投影），3.5-bit 量化即可保全质量。'
        '将发表于 ICLR 2026；vLLM PR #39890（4 月 15 日）已加入官方 3-bit / 4-bit 支持，Google 官方实现预计 Q2 2026 正式发布。'
        '技术社区将其比作"Pied Piper"，导致内存芯片股当日下跌。'
    ),
    NewsItem(
        'Snap 裁员 1000 人：AI 已生成 65% 新代码，节省 5 亿美元年化成本',
        'https://techcrunch.com/2026/04/15/snap-is-cutting-1000-jobs-16-of-its-workforce/',
        'TechCrunch', 'industry', datetime(2026, 4, 15, tzinfo=timezone.utc),
        'Snap 裁员约 1000 人（占全职员工 16%），CEO Evan Spiegel 指出 AI 带来"全新工作方式"。'
        'AI Agent 已生成超过 65% 新代码并每月响应超百万次查询，转向更小规模高度专注团队。'
        '年化成本降低逾 5 亿美元（H2 2026 生效）。此案成为 2026 年科技裁员潮代表性案例，行业内已有超 7.3 万人在 95 家公司被裁。'
    ),
    NewsItem(
        'Anthropic 与亚马逊签署新协议：2027 年起使用数吉瓦 AWS 算力训练和部署 Claude',
        'https://www.marktechpost.com/2026/04/23/openai-releases-gpt-5-5-a-fully-retrained-agentic-model-that-scores-82-7-on-terminal-bench-2-0-and-84-9-on-gdpval/',
        'MarkTechPost', 'industry', datetime(2026, 4, 23, tzinfo=timezone.utc),
        'Anthropic 与亚马逊达成新扩容协议，将获取高达 5 吉瓦的 AWS 云算力，用于 Claude 系列模型的训练与推理部署，计划从 2027 年起执行。'
        '这是继此前 Google Cloud 数十亿美元协议之后，Anthropic 同时深化与 AWS 战略合作的信号，凸显其在两大云平台的双轨扩张路线。'
    ),
    NewsItem(
        'Meta MTIA 芯片大规模部署，降低对英伟达依赖',
        'https://www.devflokers.com/blog/ai-news-last-24-hours-april-2026-model-releases-breakthroughs',
        'devFlokers', 'industry', datetime(2026, 4, 23, tzinfo=timezone.utc),
        'Meta 宣布在旗下数据中心大规模部署 MTIA（Meta Training and Inference Accelerator）自研芯片，'
        '以减少对英伟达 GPU 的依赖。这是 Meta 推进硬件垂直整合战略的关键一步，'
        '与 Google TPU Ironwood 和 Amazon Trainium 构成云大厂自研 AI 芯片三足鼎立格局。'
    ),
    NewsItem(
        'Karpathy 提出"AI 精神病"：已停止亲手写代码，成为 Agentic 系统的指挥者',
        'https://thenewstack.io/karpathy-says-developers-have-ai-psychosis-everyone-else-is-next/',
        'The New Stack', 'tools', datetime(2026, 4, 22, tzinfo=timezone.utc),
        'Andrej Karpathy 在 No Priors 播客（3 月 20 日）提出"AI 精神病"——一种强迫性超度投入、极短反馈循环与无界可能感叠加形成的近乎躁狂工作节奏。'
        '自 2025 年 12 月他已停止亲手写代码，工作流从"八成自写代码"翻转为"百分之百委托给 AI Agent"，'
        '每天向 Agent 群发指令 16 小时，自称"Agentic 系统导演"。YC 总裁 Garry Tan 称同现象为"网络精神病"。'
    ),
]

# ── 论文 ────────────────────────────────────────────────────────────────────
papers = [
    Paper(
        'PAPO: Perception-Aware Policy Optimization for Multimodal Reasoning',
        'https://arxiv.org/abs/2507.06448',
        '2507.06448',
        ['PAPO Research Team'],
        '将隐式感知损失融入 GRPO 目标函数以提升多模态推理，不依赖外部数据或模型。'
        '在多模态基准上整体提升 4.4%，视觉依赖度高的任务提升接近 8.0%。',
        ['cs.CV', 'cs.AI'], datetime(2026, 4, 23, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2507.06448v1',
    ),
    Paper(
        'NS-Mem: Advancing Multimodal Agent Reasoning with Long-Term Neuro-Symbolic Memory',
        'https://arxiv.org/html/2603.15280v1',
        '2603.15280',
        ['NS-Mem Team'],
        '提出三层神经-符号混合记忆框架，融合直觉神经检索与确定性符号推理，整合显式逻辑规则与过程 DAG。'
        '多模态 Agent 推理准确率平均提升 4.35%，约束推理查询上提升可达 12.5%。',
        ['cs.AI', 'cs.CL'], datetime(2026, 4, 22, tzinfo=timezone.utc),
        'https://arxiv.org/html/2603.15280v1',
    ),
    Paper(
        'AltTrain: Altering Reasoning Structure of LRMs via Supervised Finetuning with 1K Examples',
        'https://arxiv.org/list/cs.AI/new',
        '2604.AltTrain',
        ['AltTrain Authors'],
        '后训练方法，仅使用 1000 个训练样本通过监督微调改变大型推理模型（LRM）的推理结构，'
        '以极低数据成本实现推理路径的结构化对齐与安全控制。',
        ['cs.CL', 'cs.LG'], datetime(2026, 4, 23, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.AI/new',
    ),
    Paper(
        'DW-Bench: Evaluating LLMs on Graph-Topology Reasoning over Data Warehouse Schemas',
        'https://arxiv.org/list/cs.CL/recent',
        '2604.DWBench',
        ['DW-Bench Team'],
        '针对数据仓库 Schema 图拓扑推理的新基准，含 1046 道自动生成题目，评估 LLM 对结构化数据库知识的深度理解与多跳推理能力。',
        ['cs.CL', 'cs.DB'], datetime(2026, 4, 22, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.CL/recent',
    ),
    Paper(
        'Large Language Model Agent: A Survey on Methodology, Applications and Challenges',
        'https://arxiv.org/abs/2503.21460',
        '2503.21460',
        ['LLM Agent Survey Team'],
        '系统综述 LLM Agent 方法论、应用与挑战，涵盖感知-规划-行动-反思四大模块及工具调用、多 Agent 协作范式，'
        '同步跟踪 2026 年最新进展，是 Agent 领域入门和速查必读文献。',
        ['cs.AI', 'cs.LG'], datetime(2026, 4, 20, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2503.21460',
    ),
]

# ── 大牛动态 ─────────────────────────────────────────────────────────────────
updates = [
    InfluencerUpdate(
        'Andrej Karpathy', 'Blog / X',
        '延续"AI 精神病"话题引发大规模讨论：他自 2025 年 12 月起彻底停止亲自写代码，'
        '每天向 AI Agent 群发指令 16 小时，称自己是"Agentic 系统导演"而非程序员。'
        '其 LLM Wiki 项目（将研究素材自动生成互联 Wiki）已成长为 100 篇文章、40 万字的个人知识库，获大量开发者跟进实现。',
        'https://thenewstack.io/karpathy-says-developers-have-ai-psychosis-everyone-else-is-next/',
        datetime(2026, 4, 22, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Simon Willison', 'Blog',
        '发布 GPT-5.5 深度评测：首款完全重训 Agentic 模型，Terminal-Bench 2.0 82.7% 达 SOTA；'
        '同步评析 Anthropic 二级市场万亿估值事件，指出二级市场价格结构与一级融资的本质差异，'
        '并横向比较 GPT-5.5 vs Gemini 3.1 Pro vs Claude Opus 4.7 在实际开发任务中的表现。',
        'https://simonwillison.net/',
        datetime(2026, 4, 23, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Sebastian Raschka', 'Newsletter (Ahead of AI)',
        '新一期：《现代 LLM 注意力变体可视化指南》——从标准 MHA 到 GQA、MLA、混合注意力架构逐一拆解，'
        '配合 TurboQuant KV Cache 压缩原理阐述注意力内存瓶颈；同时评述 GPT-5.5 发布对开源社区路线图的潜在影响。',
        'https://magazine.sebastianraschka.com/',
        datetime(2026, 4, 23, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Chip Huyen', 'Blog',
        '深度分析 Snap 裁员事件中的"AI 代码生成 65%"数据背后的真实含义：区分代码行数占比与工程价值占比，'
        '探讨 Agentic 编程规模化后企业软件组织架构如何重塑；并评析 GPT-5.5 Agentic 定位对工具链生态的冲击。',
        'https://huyenchip.com/',
        datetime(2026, 4, 23, tzinfo=timezone.utc),
    ),
]

# ── GitHub 热门 ──────────────────────────────────────────────────────────────
github = [
    GithubProject(
        'OpenClaw/openclaw',
        'https://github.com/OpenClaw/openclaw',
        'Personal AI assistant running entirely on your devices — local gateway to 50+ integrations (WhatsApp, Slack, Telegram, Discord, Signal, iMessage…)',
        212000, 18700, 'TypeScript', 1800, ['openclaw-core', 'integrations-team'],
    ),
    GithubProject(
        'ggml-org/llama.cpp',
        'https://github.com/ggml-org/llama.cpp',
        'LLM inference in C/C++ — now ships Vulkan flash attention + Qwen3 audio (ASR) support',
        88000, 12600, 'C++', 1420, ['ggerganov', 'slaren', 'cebtenzzre'],
    ),
    GithubProject(
        'openai/codex',
        'https://github.com/openai/codex',
        'Codex CLI — lightweight coding agent in your terminal, v0.121 alpha with GPT-5.5 support',
        54000, 4800, 'TypeScript', 1350, ['openai-devs'],
    ),
    GithubProject(
        'VoltAgent/awesome-ai-agent-papers',
        'https://github.com/VoltAgent/awesome-ai-agent-papers',
        'Curated 2026 AI agent research papers: agent engineering, memory, evaluation, workflows, autonomous systems',
        9200, 780, '', 1100, ['VoltAgent'],
    ),
    GithubProject(
        'n8n-io/n8n',
        'https://github.com/n8n-io/n8n',
        'Fair-code workflow automation with native AI / LLM node support',
        99000, 26500, 'TypeScript', 950, ['ivov', 'jan-montag', 'RicardoE105'],
    ),
    GithubProject(
        'NousResearch/hermes-agent',
        'https://github.com/NousResearch/hermes-agent',
        'Hermes Agent v0.8.0 — open-source agentic framework, the agent that grows with you',
        45600, 5900, 'Python', 820, ['teknium1', '0xbyt4', 'kshitijk4poor'],
    ),
    GithubProject(
        'alvinreal/awesome-opensource-ai',
        'https://github.com/alvinreal/awesome-opensource-ai',
        'Curated list of the best truly open-source AI projects, models, tools, and infrastructure',
        7400, 520, '', 760, ['alvinreal'],
    ),
    GithubProject(
        'ollama/ollama',
        'https://github.com/ollama/ollama',
        'Lightweight Go framework for running LLMs locally, now supports Llama 4 & Gemma 4',
        137000, 11000, 'Go', 680, ['jmorganca', 'mxyng', 'technovangelist'],
    ),
]

# ── 主逻辑 ───────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description='生成并可选发布 2026-04-24 AI 日报')
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
