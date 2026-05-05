"""
发布 2026-05-05 AI 日报到博客

用法：
  # 仅生成 Jekyll 文章到 reports/ 目录
  python generate_post_2026_05_05.py

  # 生成并发布到博客（需要设置 BLOG_DEPLOY_TOKEN 环境变量）
  BLOG_DEPLOY_TOKEN=your_token python generate_post_2026_05_05.py --publish
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
        'OpenAI 发布 Workspace Agents：企业版 Custom GPT 继任者，5 月 6 日起启动积分计费',
        'https://openai.com/index/introducing-workspace-agents-in-chatgpt/',
        'OpenAI', 'industry', datetime(2026, 5, 4, tzinfo=timezone.utc),
        'OpenAI 推出 Workspace Agents，基于 Codex 驱动，是 Custom GPT 的企业级进化版。'
        '团队可在 Slack、Salesforce 等平台中共建共用 Agent，支持长时间运行工作流；'
        '可执行报告生成、代码编写、消息处理等任务，并在云端持续运行无需人工守候。'
        '现已开放至 Business/Enterprise/Edu/Teachers 计划，免费期至 5 月 6 日，'
        '此后切换为积分计费（具体单价暂未公布）。',
    ),
    NewsItem(
        'Anthropic 联手 Blackstone、Goldman Sachs 成立 AI 原生企业服务公司，募资 15 亿美元',
        'https://fortune.com/2026/05/04/anthropic-claude-consulting-industry-joint-venture-blackstone-goldman-sachs/',
        'Fortune', 'industry', datetime(2026, 5, 4, tzinfo=timezone.utc),
        'Anthropic 宣布与黑石集团、Hellman & Friedman 及高盛联合成立 AI 原生企业服务公司，'
        '已承诺资本约 15 亿美元，目标是将 Anthropic 工程师与 Claude 模型直接嵌入中大型企业核心运营。'
        '此举被视为 Anthropic 进军企业咨询市场、挑战 Accenture 等传统 IT 服务商的关键行动，'
        '也标志着 AI 公司从"卖 API"转向"买断业务流程"的新商业模式。',
    ),
    NewsItem(
        'Google Cloud Next 2026：Gemini Enterprise Agent 平台、第 8 代 TPU 及 Agentic Data Cloud 发布',
        'https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/next-2026/',
        'Google Cloud Blog', 'industry', datetime(2026, 4, 24, tzinfo=timezone.utc),
        'Google Cloud Next 26 三大核心发布：'
        '①Gemini Enterprise Agent Platform——内置 Agent Designer、Inbox、长时 Agent、Skills 等，'
        '直接集成 Gemini 3.1 Pro、Flash Image 及 Lyria 3，并新增 Claude Opus 4.7 多模型选择；'
        '②第 8 代 TPU（TPU 8t 训练/TPU 8i 推理与强化学习）；'
        '③Agentic Data Cloud。目前 Google Cloud 模型每分钟处理超 160 亿 Token，'
        '较上季度的 100 亿提升 60%，75% 客户已用上 AI 产品。',
    ),
    NewsItem(
        'DeepSeek-V4 正式发布：1.6 万亿参数、MIT 许可、百万 Token 上下文，搭载华为昇腾 950',
        'https://techcrunch.com/2026/04/24/deepseek-previews-new-ai-model-that-closes-the-gap-with-frontier-models/',
        'TechCrunch', 'industry', datetime(2026, 4, 24, tzinfo=timezone.utc),
        'DeepSeek 发布 V4 系列：DeepSeek-V4-Pro（1.6 万亿参数）和 V4-Flash（2840 亿参数），'
        '均支持百万 Token 上下文，MIT 开源协议。V4 依赖华为"超节点"技术，'
        '将大规模昇腾 950 集群整合以满足算力需求，是国产 AI 芯片大规模训练落地的标志性案例。'
        'DeepSeek 技术报告坦承 V4 推理与 Agent 能力对标约半年前的 GPT-5.2/Gemini 3.0 Pro，'
        'API 缓存输入价格已降至 0.025 元/百万 Token（限时优惠）。',
    ),
    NewsItem(
        'Google I/O 2026 定档 5 月 19 日：Gemini 4.0、Android 17、神秘视频模型"Omni"抢先看',
        'https://developers.googleblog.com/get-ready-for-google-io-2026/',
        'Google Developers Blog', 'industry', datetime(2026, 5, 1, tzinfo=timezone.utc),
        'Google I/O 2026 将于 5 月 19–20 日在加州山景城 Shoreline Amphitheatre 举办。'
        '预期重磅：Gemini 4.0 多模态旗舰升级；Android 17 深度集成 Gemini 语音操控（含车载与文件生成）；'
        '以及代号"Omni"的新一代视频生成模型，可能替代或扩展基于 Veo-3.1 的现有 Gemini 视频流。'
        'Google Cloud Q1 收入同比增长 63% 至 200 亿美元，Gemini Enterprise 付费 MAU 季度环比增长 40%。',
    ),
    NewsItem(
        'Prime Intellect 提出递归语言模型（RLM）：模型主动管理上下文，瞄准数周至数月长程任务',
        'https://www.primeintellect.ai/blog/rlm',
        'Prime Intellect Blog', 'research', datetime(2026, 5, 1, tzinfo=timezone.utc),
        'Prime Intellect 发布《Recursive Language Models: the paradigm of 2026》，'
        '提出 RLM 范式——将完整输入加载为 Python REPL 中的字符串变量，'
        '根模型无需直接处理庞大上下文，而是主动将任务委托给子 LLM 和 Python 脚本，'
        '通过 llm_batch 并行扇出多路查询，并经由 RL 训练持续优化上下文折叠策略。'
        '与传统摘要法不同，RLM 不丢失信息，已在 Environments Hub 开放多个 RLM 环境。',
    ),
    NewsItem(
        'Anthropic Claude Code 5 月更新：模型选择器支持自定义网关、新增 project purge 命令',
        'https://releasebot.io/updates/anthropic/claude-code',
        'Releasebot / Anthropic', 'tools', datetime(2026, 5, 3, tzinfo=timezone.utc),
        'Claude Code 本周推出批量改进：/model 选择器现可列出自定义网关（ANTHROPIC_BASE_URL）'
        '的 /v1/models 端点模型；新增 claude project purge 命令可清除项目全部本地状态；'
        '还带来更强大的 OAuth 登录流程、Windows/PowerShell 兼容修复及稳定性提升。'
        '同期，Anthropic 已将 Sonnet 4.5/4 的百万 Token 上下文 Beta 迁移至'
        'Sonnet 4.6 和 Opus 4.6 正式版（标准定价），并为 Claude 新增'
        'Adobe、Blender、Ableton、Affinity、Autodesk Fusion 创意工具连接器。',
    ),
    NewsItem(
        '大厂 AI 资本开支 2026 年将破 7000 亿美元：Alphabet 上调全年至 1900 亿，云收入 Q1 暴增 63%',
        'https://fortune.com/2026/04/30/big-tech-hyperscalers-will-spend-700-billion-on-ai-infrastructure-this-year-with-no-clear-end-in-sight-eye-on-ai/',
        'Fortune', 'industry', datetime(2026, 4, 30, tzinfo=timezone.utc),
        '科技超大规模厂商 2026 年 AI 基础设施资本开支预计突破 7000 亿美元，"终点不在视野之内"。'
        'Alphabet 将全年 Capex 上限上调至 1900 亿美元；微软预计超 400 亿美元（含约 50 亿美元'
        '额外组件涨价）；Meta 全年 1150–1350 亿美元。分析师指出投资者仍担忧 ROI 兑现时间表，'
        '但各 CEO 一致认为"不投更危险"。',
    ),
]

# ── 论文 ────────────────────────────────────────────────────────────────────
papers = [
    Paper(
        'Agentic Reasoning for Large Language Models',
        'https://arxiv.org/abs/2601.12538',
        '2601.12538',
        ['arXiv Authors'],
        '系统梳理 LLM 的"Agent 推理"能力框架，涵盖规划、工具调用、多步反馈循环与自我校正。'
        '论文区分"静态推理"（单次前向）与"动态 Agent 推理"（迭代 + 工具），'
        '分析当前主流方法（ReAct、Reflexion、Tree-of-Thought）的能力边界，'
        '并提出评估 Agent ROI 的量化指标，指出可靠性工程是 LLM Agent 可用性的真正壁垒。',
        ['cs.AI', 'cs.LG'], datetime(2026, 1, 21, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2601.12538',
        None,
    ),
    Paper(
        'A Comprehensive Evaluation of LLM Reasoning: From Single-Model to Multi-Agent Paradigms',
        'https://arxiv.org/abs/2601.13243',
        '2601.13243',
        ['arXiv Authors'],
        '对比单模型推理与多 Agent 协作两类范式的推理能力，覆盖数学、代码、科学、常识等 8 类任务。'
        '研究发现：多 Agent 协作在复杂任务上平均提升 12–18%，但通信开销和错误传播是主要瓶颈；'
        '提出"推理一致性"新评估维度，量化模型在语义等价但表述不同的问题上的稳定性。',
        ['cs.AI', 'cs.CL'], datetime(2026, 1, 22, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2601.13243',
        None,
    ),
    Paper(
        'Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering',
        'https://arxiv.org/html/2604.08224v1',
        '2604.08224',
        ['arXiv Authors'],
        '从"外化"视角统一综述 LLM Agent 工程：将 Agent 能力分解为记忆外化（短期/长期/知识库）、'
        '技能外化（工具、代码、API）、协议外化（MCP、A2A）和框架外化（上下文管理、权限控制）四层。'
        '横跨 2022–2026 年的演进路径显示：Agent 架构从 Weights → Context → Harness 三层递进，'
        '当前行业重心已转移至 Harness 层（即编排与安全基础设施）的工程化建设。',
        ['cs.AI', 'cs.SE'], datetime(2026, 4, 10, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2604.08224',
        None,
    ),
    Paper(
        'ICLR 2026 精选：12 篇关于 AI 系统可靠性、效率与安全性的论文综述',
        'https://lambda.ai/blog/iclr-2026-12-papers',
        '2026.ICLR.Lambda',
        ['Lambda Labs Blog'],
        'Lambda Labs 梳理 ICLR 2026 最值得关注的 12 篇论文，主题集中在：'
        '①高效推理（稀疏激活、投机解码新变体）；'
        '②模型可靠性（幻觉检测、不确定性校准）；'
        '③安全对齐（越狱攻击防御、视觉语言模型安全基准）；'
        '④跨模态推理（文本-图像交错思维链在机器人长程操控中的应用）。',
        ['cs.LG', 'cs.AI'], datetime(2026, 5, 2, tzinfo=timezone.utc),
        None,
        None,
    ),
    Paper(
        'Position: The Real Barrier to LLM Agent Usability is Agentic ROI',
        'https://arxiv.org/html/2505.17767',
        '2505.17767',
        ['arXiv Authors'],
        '立场论文，主张 LLM Agent 大规模落地的核心障碍不是模型能力，而是"Agent ROI"——'
        '即每次 Agent 执行的成本/收益可量化性。提出 Agent ROI 框架，包含任务完成率、'
        '人工干预率、端到端延迟和成本四个维度，并分析当前主流 Agent 框架在 ROI 可观测性上的缺失，'
        '呼吁社区建立标准化 Agent 基准测试套件。',
        ['cs.AI', 'cs.HC'], datetime(2026, 5, 1, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2505.17767',
        None,
    ),
]

# ── 大牛动态 ─────────────────────────────────────────────────────────────────
updates = [
    InfluencerUpdate(
        'Simon Willison', 'Blog',
        '5 月 4 日发布《April 2026 Newsletter》，梳理个人过去一个月的研究与工具使用心得：'
        '① 深入剖析"Agent"定义之争——认为该词汇终于具备了足够共识可作为工程术语使用，'
        '核心要素：能自主规划多步行动、可调用外部工具、能在错误中恢复；'
        '② 记录与 Claude Code、Gemini 2.5 Pro 的实测对比：'
        'Claude Code 在代码重构任务上一致性更强，Gemini 在超长文档摘要上有优势；'
        '③ 持续关注 Prompt Injection 安全议题，整理了最新绕过案例并呼吁业界建立"AI 内核/用户层"隔离标准。',
        'https://simonwillison.net/2026/May/4/april-newsletter/',
        datetime(2026, 5, 4, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Sebastian Raschka', 'Blog (sebastianraschka.com)',
        '近期两篇重磅博文：'
        '① 《My Workflow for Understanding LLM Architectures》（4 月 18 日）：'
        '分享逐层阅读模型代码、手绘注意力图、对比消融实验的"三步理解法"，'
        '附带 Muse Spark 与 Gemini 3 架构拆解对比；'
        '② 《Components of A Coding Agent》（4 月 4 日）：'
        '将编码 Agent 拆解为 6 个组件（规划器、工具路由器、执行沙箱、测试验证器、错误解析器、上下文管理器），'
        '每个组件给出设计决策矩阵，是工程实践的高价值参考。'
        '同期 YouTube 发布《LLM Architecture in 2026》视频课，已超 30 万次播放。',
        'https://sebastianraschka.com/blog/',
        datetime(2026, 4, 18, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Chip Huyen', 'Blog (huyenchip.com)',
        '持续更新《AI Engineering》系列：近期重点关注 AI Agent 的工程实现层面，'
        '探讨工具调用的幂等性设计、状态管理与错误恢复机制；'
        '分析 Anthropic + Blackstone/Goldman 企业服务合资公司案例，'
        '认为"AI 公司直接参与业务流程重构"是 2026 年最重要的商业模式创新，'
        '将比单纯卖 API 产生更深远的行业影响。'
        '同时呼吁 AI 工程师关注"可观测性"——在 Agent 系统中，'
        '监控 Token 使用、工具调用链和中间状态至少与监控推理结果同等重要。',
        'https://huyenchip.com/blog/',
        datetime(2026, 5, 3, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Andrej Karpathy', 'Blog / X',
        '在 Sequoia Ascent 演讲后的持续传播中，本周重点转向"LLM 能力锯齿状特征"的深入讨论：'
        '①在 X 上发布线程，举例说明同类任务在 RL 训练分布边界内外的性能断崖，'
        '并建议工程师用"小型探测测试"预先检测任务是否在模型分布内；'
        '②转发 Prime Intellect 的 RLM 博文，评论："这是正确方向——'
        '让模型自己管理上下文，而不是让框架帮它管"；'
        '③在采访中透露正在与团队研究"ambient programming"原型，'
        '目标是让 AI 在后台持续监控代码库并主动提出优化建议，无需开发者主动触发。',
        'https://karpathy.bearblog.dev/sequoia-ascent-2026/',
        datetime(2026, 5, 4, tzinfo=timezone.utc),
    ),
]

# ── GitHub 热门 ──────────────────────────────────────────────────────────────
github = [
    GithubProject(
        'TauricResearch/TradingAgents',
        'https://github.com/TauricResearch/TradingAgents',
        'Multi-agent LLM financial trading framework — fund managers, analysts, risk managers and traders collaborate autonomously to execute strategies',
        65300, 5800, 'Python', 2100, ['TauricResearch'],
    ),
    GithubProject(
        'ruvnet/ruflo',
        'https://github.com/ruvnet/ruflo',
        'Agent orchestration platform for Claude — deploy intelligent multi-agent swarms, coordinate autonomous workflows with RAG integration and native Claude Code/Codex support',
        39800, 3100, 'Python', 1850, ['ruvnet'],
    ),
    GithubProject(
        'Vinci/Scrapling',
        'https://github.com/scrapling/scrapling',
        'Adaptive web scraping framework — automatically adjusts to website changes, undetectable by anti-bot systems, built for AI data pipelines',
        43000, 3400, 'Python', 1420, ['scrapling'],
    ),
    GithubProject(
        'OpenClaw/openclaw',
        'https://github.com/OpenClaw/openclaw',
        'Personal AI assistant running entirely on your devices — local gateway to 50+ integrations (WhatsApp, Slack, Telegram, Signal, iMessage)',
        219000, 19800, 'TypeScript', 1280, ['openclaw-core'],
    ),
    GithubProject(
        'nexu-io/open-design',
        'https://github.com/nexu-io/open-design',
        'Local-first, open-source alternative to Anthropic Claude Design — generate and edit visual assets with any LLM backend, no cloud required',
        19800, 1600, 'TypeScript', 980, ['nexu-io'],
    ),
    GithubProject(
        'alexzhang13/rlm',
        'https://github.com/alexzhang13/rlm',
        'General plug-and-play inference library for Recursive Language Models (RLMs) — enables models to actively manage their own context via Python REPL and sub-LLM delegation',
        8200, 620, 'Python', 870, ['alexzhang13'],
    ),
    GithubProject(
        'n8n-io/n8n',
        'https://github.com/n8n-io/n8n',
        'Fair-code workflow automation platform with native AI capabilities — visual agent pipelines, LLM chains, vector DB queries, 400+ integrations',
        187000, 23100, 'TypeScript', 760, ['janober', 'ivov'],
    ),
    GithubProject(
        'VoltAgent/awesome-ai-agent-papers',
        'https://github.com/VoltAgent/awesome-ai-agent-papers',
        'Curated collection of 2026 AI agent research papers — covers agent engineering, memory, evaluation, workflows, and autonomous systems',
        6400, 480, 'Markdown', 650, ['VoltAgent'],
    ),
]


# ── 主逻辑 ───────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description='生成并可选发布 2026-05-05 AI 日报')
    parser.add_argument('--publish', action='store_true', help='发布到博客（需 BLOG_DEPLOY_TOKEN）')
    args = parser.parse_args()

    filename, content = generate_jekyll_post(news, papers, updates, github)

    filename = '2026-05-05-ai-daily-news.md'
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
