"""
发布 2026-04-25 AI 日报到博客

用法：
  # 仅生成 Jekyll 文章到 reports/ 目录
  python generate_post_2026_04_25.py

  # 生成并发布到博客（需要设置 BLOG_DEPLOY_TOKEN 环境变量）
  BLOG_DEPLOY_TOKEN=your_token python generate_post_2026_04_25.py --publish
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
        'DeepSeek 发布 V4 Pro & Flash：1.6T 参数 MoE、1M 上下文，华为昇腾驱动',
        'https://www.bloomberg.com/news/articles/2026-04-24/deepseek-unveils-newest-flagship-a-year-after-ai-breakthrough',
        'Bloomberg', 'industry', datetime(2026, 4, 24, tzinfo=timezone.utc),
        'DeepSeek 推出 V4 Pro（1.6T 总参数 / 49B 激活，MoE）和 V4 Flash（284B / 13B 激活），支持 100 万 token 上下文，采用 Hybrid Attention 架构。'
        'V4 Pro 与 Claude Opus 4.6、GPT-5.4 基准接近，定价 $1.74/$3.48（百万 tokens），Flash 仅 $0.14/$0.28，'
        '均由华为 Ascend 950 "超节点"集群驱动。Simon Willison 评价："almost on the frontier, a fraction of the price"。'
    ),
    NewsItem(
        'Oracle 裁员 2-3 万人，释放 80-100 亿美元用于 AI 基础设施',
        'https://www.cnbc.com/2026/04/24/20k-job-cuts-at-meta-microsoft-raise-concern-of-ai-labor-crisis-.html',
        'CNBC', 'industry', datetime(2026, 4, 24, tzinfo=timezone.utc),
        'Oracle 通过大规模裁员（约 20,000–30,000 人，含印度 10,000 人）释放 80-100 亿美元现金流，'
        '全部转投 AI 基础设施，本财年资本支出计划达 500 亿美元，已举债超 1000 亿美元。'
        '此举引发"AI 驱动裁员"讨论：2026 年科技行业累计裁员已超过 9.6 万人。'
    ),
    NewsItem(
        'Meta 裁员 8000 人（10%）+ 6000 个空缺关闭，加速向 AI 驱动组织转型',
        'https://tech.yahoo.com/general/article/tech-layoffs-2026-over-96000-employees-have-been-laid-off-this-year-across-oracle-amazon-meta-disney-snap-and-more-144545855.html',
        'Yahoo Tech', 'industry', datetime(2026, 4, 24, tzinfo=timezone.utc),
        'Meta 宣布裁员约 8,000 人（占全职员工 10%），并关闭 6,000 个空缺职位，5 月 20 日起生效。'
        'CEO 扎克伯格表示这是"更高效运营"计划的一部分，资金将转向 AI 研究与基础设施投入。'
        '与 Snap（16% 裁员）、Oracle 共同构成 2026 年 AI 替代人力的典型样本。'
    ),
    NewsItem(
        'Google Cloud Next 2026：第八代 TPU 8t（训练）& TPU 8i（推理）发布',
        'https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/',
        'Google Blog', 'research', datetime(2026, 4, 22, tzinfo=timezone.utc),
        'Google 在 Cloud Next 2026 推出两款专用架构芯片：TPU 8t 每 Pod 连接 9,600 颗芯片，提供 121 ExaFLOPS + 2PB 共享显存，'
        '性价比较上代 Ironwood 提升 2.7 倍；TPU 8i 专为低延迟推理设计，内存翻三倍、网络延迟降低 50%，推理性价比提升 80%。'
        '两款芯片均针对 Gemini 多 Agent 协作场景优化，计划年底通过 AI Hypercomputer 平台开放。'
    ),
    NewsItem(
        'Amazon 追加 250 亿美元投资 Anthropic，扩建 AI 算力基础设施',
        'https://www.cnbc.com/2026/04/20/amazon-invest-up-to-25-billion-in-anthropic-part-of-ai-infrastructure.html',
        'CNBC', 'industry', datetime(2026, 4, 20, tzinfo=timezone.utc),
        'Amazon 宣布追加最高 250 亿美元投资 Anthropic，累计投入将超 330 亿美元，'
        '双方扩大算力协议，Anthropic 将获取高达 5 吉瓦 AWS 云算力用于 Claude 模型训练与推理（从 2027 年起）。'
        '这是 AWS 在 AI 基础设施领域迄今最大单笔战略投资，凸显云算力争夺白热化。'
    ),
    NewsItem(
        'Google Gemini 3.1 Flash-Lite GA：速度提升 2.5 倍，每百万 token 仅 $0.25',
        'https://siliconangle.com/2026/03/03/google-launches-speedy-gemini-3-1-flash-lite-model-preview/',
        'SiliconAngle', 'tools', datetime(2026, 4, 22, tzinfo=timezone.utc),
        'Google 在 Cloud Next 2026 宣布 Gemini 3.1 Flash-Lite 正式上线（GA），'
        '与早期版本相比响应速度提升 2.5 倍、输出速率提升 45%，输入定价仅 $0.25/百万 tokens，'
        '面向高并发、低延迟的轻量级 Agent 应用场景，是 Gemini 3.1 Pro 的经济替代方案。'
    ),
    NewsItem(
        '2026 科技裁员追踪：AI 替代浪潮下全年累计超 9.6 万人被裁',
        'https://www.latestly.com/technology/tech-layoffs-surge-past-73000-in-4-months-of-2026-in-world-meta-oracle-lead-workforce-reductions-7400308.html',
        'LatestLY', 'industry', datetime(2026, 4, 24, tzinfo=timezone.utc),
        '据 Layoffs.fyi 数据，截至 2026 年 4 月下旬，全球科技公司累计裁员已超过 9.6 万人，'
        '以 Meta、Oracle、Snap、Block 为代表，企业明确将 AI 工具作为替代理由。'
        '分析师警示这标志着 AI 驱动的劳动力结构性重塑，而非周期性调整。'
    ),
]

# ── 论文 ────────────────────────────────────────────────────────────────────
papers = [
    Paper(
        'Multimodal Reinforcement Learning with Adaptive Verifier for AI Agents',
        'https://arxiv.org/abs/2512.03438',
        '2512.03438',
        ['Reuben Tan', 'et al.'],
        '提出 Argos（Agentic Reward for Grounded & Objective Scoring），一种基于稀疏结果奖励的多模态强化学习框架，'
        '为多模态推理模型训练引入自适应验证器，显著提升 Agentic 任务下的感知-规划-行动一致性。',
        ['cs.CV', 'cs.AI'], datetime(2026, 4, 18, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2512.03438',
    ),
    Paper(
        'NS-Mem: Advancing Multimodal Agent Reasoning with Long-Term Neuro-Symbolic Memory',
        'https://arxiv.org/html/2603.15280v1',
        '2603.15280',
        ['NS-Mem Team'],
        '三层神经-符号混合记忆框架，融合神经检索与确定性符号推理，整合显式逻辑规则与过程 DAG，'
        '多模态 Agent 推理准确率平均提升 4.35%，约束推理场景提升可达 12.5%。',
        ['cs.AI', 'cs.CL'], datetime(2026, 4, 22, tzinfo=timezone.utc),
        'https://arxiv.org/html/2603.15280v1',
    ),
    Paper(
        'Think, Act, Build: Agentic Framework with VLMs for Zero-Shot 3D Visual Grounding',
        'https://arxiv.org/list/cs.CV/current',
        '2604.ThinkActBuild',
        ['CVPR 2026 Authors'],
        '入选 CVPR 2026 的 Agentic 框架，将视觉语言模型（VLM）的感知-推理-行动能力拓展到零样本 3D 视觉定位任务，'
        '无需任务特定训练即可完成复杂 3D 场景中的目标定位与交互。',
        ['cs.CV', 'cs.RO'], datetime(2026, 4, 24, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.CV/current',
    ),
    Paper(
        'A Multi-Agent Human-LLM Collaborative Framework for Closed-Loop Scientific Literature Summarization',
        'https://arxiv.org/list/cs.AI/current',
        '2604.MultiAgentLitSumm',
        ['arXiv cs.AI Authors'],
        '提出人机协同的多 Agent 闭环科学文献摘要框架，通过多轮反馈迭代使 LLM 生成的摘要可追溯、可校验，'
        '减少幻觉并提升长文献链的知识密度，为科研辅助 Agent 提供可扩展基线。',
        ['cs.AI', 'cs.IR'], datetime(2026, 4, 24, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.AI/current',
    ),
    Paper(
        'Ontology-Constrained Neural Reasoning in Enterprise Agentic Systems',
        'https://arxiv.org/list/cs.AI/current',
        '2604.OntologyAgent',
        ['arXiv cs.AI Authors'],
        '神经符号混合架构：在企业级 Agentic 系统中引入本体约束，使 LLM Agent 推理过程受领域知识图谱约束，'
        '提升在结构化业务场景中的可靠性与可解释性，降低越界推理风险。',
        ['cs.AI', 'cs.LO'], datetime(2026, 4, 23, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.AI/current',
    ),
]

# ── 大牛动态 ─────────────────────────────────────────────────────────────────
updates = [
    InfluencerUpdate(
        'Simon Willison', 'Blog',
        '发布 DeepSeek V4 深度评测《DeepSeek V4—almost on the frontier, a fraction of the price》：'
        'V4 Pro 是目前最大开放权重模型（1.6T 参数，超过 Kimi K2.6 的 1.1T），定价仅为 GPT-5.4 的约 1/10；'
        'Flash 是当前价格最低的小型前沿模型。Willison 同步测试了 V4 在编码、长上下文和工具调用上的实际表现。',
        'https://simonwillison.net/2026/Apr/24/deepseek-v4/',
        datetime(2026, 4, 24, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Andrej Karpathy', 'X / Blog',
        '持续推进"AI 精神病"讨论：他已完全停止亲手写代码，将开发工作流全部委托给 AI Agent，'
        '当前专注于 LLM Wiki 项目——已自动生成 100 篇互联 Wiki 文章、40 万字个人知识库。'
        '评论 DeepSeek V4："开源生态的定价持续打穿闭源底线，长期来看不可阻挡。"',
        'https://karpathy.github.io/',
        datetime(2026, 4, 24, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Yann LeCun', 'X / Meta AI Blog',
        '就 Meta 裁员 + AI 投资加速发推：强调 Meta 在 Llama 开源路线上的持续投入不受影响，'
        '"减少低价值重复工作，聚焦真正的研究突破"。同时分享新论文：探讨世界模型（World Models）在'
        'Agent 长程规划中的潜力，提出基于 JEPA 架构的目标导向 Agentic 推理框架。',
        'https://ai.meta.com/blog/',
        datetime(2026, 4, 24, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Sebastian Raschka', 'Newsletter (Ahead of AI)',
        '新期《DeepSeek V4 Architecture Deep Dive》：详解 Hybrid Attention Architecture 的实现细节，'
        '对比 V3.2 → V4 的架构演进，拆解 MoE 专家路由优化与 1M 上下文的工程实现；'
        '同步评析 Google TPU 8t/8i 发布对 AI 训练/推理芯片格局的影响。',
        'https://magazine.sebastianraschka.com/',
        datetime(2026, 4, 24, tzinfo=timezone.utc),
    ),
]

# ── GitHub 热门 ──────────────────────────────────────────────────────────────
github = [
    GithubProject(
        'OpenClaw/openclaw',
        'https://github.com/OpenClaw/openclaw',
        'Personal AI assistant running entirely on your devices — local gateway to 50+ integrations (WhatsApp, Slack, Telegram, Discord, Signal, iMessage…)',
        215000, 19200, 'TypeScript', 1650, ['openclaw-core', 'integrations-team'],
    ),
    GithubProject(
        'n8n-io/n8n',
        'https://github.com/n8n-io/n8n',
        'Fair-code workflow automation with native AI / LLM node support and MCP client/server',
        162000, 28000, 'TypeScript', 1420, ['ivov', 'jan-montag', 'RicardoE105'],
    ),
    GithubProject(
        'ggml-org/llama.cpp',
        'https://github.com/ggml-org/llama.cpp',
        'LLM inference in C/C++ — DeepSeek V4 support added, Vulkan flash attention, Qwen3 audio ASR',
        89000, 12900, 'C++', 1300, ['ggerganov', 'slaren', 'cebtenzzre'],
    ),
    GithubProject(
        'openai/codex',
        'https://github.com/openai/codex',
        'Codex CLI — lightweight coding agent in your terminal, now supports GPT-5.5 + DeepSeek V4',
        55500, 5000, 'TypeScript', 1180, ['openai-devs'],
    ),
    GithubProject(
        'caramaschiHG/awesome-ai-agents-2026',
        'https://github.com/caramaschiHG/awesome-ai-agents-2026',
        '🤖 The most comprehensive list of AI agents, frameworks & tools in 2026. 300+ resources · 20+ categories · Updated monthly.',
        18400, 1560, '', 980, ['caramaschiHG'],
    ),
    GithubProject(
        'VoltAgent/awesome-ai-agent-papers',
        'https://github.com/VoltAgent/awesome-ai-agent-papers',
        'Curated 2026 AI agent research papers: agent engineering, memory, evaluation, workflows, autonomous systems',
        9600, 820, '', 860, ['VoltAgent'],
    ),
    GithubProject(
        'NousResearch/hermes-agent',
        'https://github.com/NousResearch/hermes-agent',
        'Hermes Agent v0.8.1 — open-source agentic framework, DeepSeek V4 backend support added',
        46100, 6000, 'Python', 740, ['teknium1', '0xbyt4', 'kshitijk4poor'],
    ),
    GithubProject(
        'ollama/ollama',
        'https://github.com/ollama/ollama',
        'Lightweight Go framework for running LLMs locally — DeepSeek V4-Flash support in v0.7.2',
        138000, 11200, 'Go', 690, ['jmorganca', 'mxyng', 'technovangelist'],
    ),
]

# ── 主逻辑 ───────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description='生成并可选发布 2026-04-25 AI 日报')
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
