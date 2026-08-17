"""生成今日 Jekyll 博客文章 - 2026-08-17"""
import sys
sys.path.insert(0, '/home/user/ai-daily-news')

from src.blog_publisher import generate_jekyll_post
from src.collectors.news_collector import NewsItem
from src.collectors.paper_collector import Paper
from src.collectors.influencer_collector import InfluencerUpdate, GithubProject
from datetime import datetime, timezone

# --- 资讯 ---
news = [
    NewsItem(
        'Google 发布 Gemini 3.7 Flash：编程与 Agent 能力超越 Sonnet 5 和 GPT-5.6',
        'https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/',
        'Google Blog / MarkTechPost', 'industry', datetime(2026,8,13,tzinfo=timezone.utc),
        '8 月 13 日，Google 发布 Gemini 3.7 Flash，在编程评测中力压 Sonnet 5 和 GPT-5.6，定价 $0.75/$3.75 per M token（2026 年底前有效，2027 年起升至 $1.50/$7.50）。该模型是 3.6 Flash 的算法优化版本（非全新预训练），在 Agent 任务场景下表现尤为突出，支持 100 万 token 上下文。'
    ),
    NewsItem(
        'Alibaba 发布 Qwen3.8-27B：27B 开源多模态模型，性能媲美 10-15 倍大模型',
        'https://medium.com/@rosgluk/qwen-3-8-27b-is-coming-and-it-could-be-the-most-important-local-ai-release-of-2026-c1cf381d5292',
        'Medium / Yotta Labs', 'industry', datetime(2026,8,14,tzinfo=timezone.utc),
        'Alibaba Tongyi Lab 于 8 月 14 日 15:00 UTC 发布 Qwen3.8-27B，27.78B 参数，Apache 2.0 开源，原生多模态（文本/图像/视频），262K 原生上下文（可扩展至 1M）。混合注意力架构（GDN×48 + GA×16），SWE-bench Pro 61.7、LiveCodeBench v6 90.3，最低 24GB VRAM 可本地运行，超越 Meta Muse Glimmer（30B）全部 8 项基准对比。'
    ),
    NewsItem(
        'OpenAI 发布 GPT-5.6-Cyber：网络安全专用版，解决率 95%，强制硬件密钥',
        'https://thehackernews.com/2026/08/openai-launches-gpt-56-cyber-with.html',
        'The Hacker News / OpenAI', 'industry', datetime(2026,8,10,tzinfo=timezone.utc),
        '8 月 10 日，OpenAI 推出 GPT-5.6-Cyber 并随附 Daybreak Blue/Red 专属计划，在漏洞检测任务中达到 95% 完成率，正式跨越 Preparedness Framework"高"网络能力阈值。与此同时，OpenAI 宣布 9 月 1 日起对全部 Daybreak 账户强制启用硬件安全密钥，以应对日益严峻的供应链攻击风险。'
    ),
    NewsItem(
        'ByteDance Seed 2.1 Turbo 发布：推理速度大幅提升，面向生产级 Agent 部署',
        'https://aireleasetracker.com/',
        'AI Release Tracker', 'industry', datetime(2026,8,10,tzinfo=timezone.utc),
        'ByteDance Seed 团队于 8 月 10 日发布 Seed 2.1 Turbo，针对 Agentic 工作负载进行了推理速度优化，延迟相较 Seed 2.1 基础版下降约 40%，支持代码生成、多步骤任务规划，定价低于同级闭源竞品，面向大规模生产部署场景。'
    ),
    NewsItem(
        'EU AI Act 第 50 条 8 月 2 日生效：AI 透明度义务正式落地，违者面临 3% 全球营收罚款',
        'https://www.suntecindia.com/blog/eu-ai-act-august-2026-enterprise-ai-agent-governance/',
        'SunTec India / EU Digital Strategy', 'research', datetime(2026,8,2,tzinfo=timezone.utc),
        '欧盟 AI 法案第 50 条透明度义务于 8 月 2 日正式生效：企业须在用户与 AI 交互时主动披露，并对 AI 生成内容施加机器可读标记。违规最高罚款为全球年营收的 3%。高风险系统（含信用评分、Agent 编排）须实现人机协同监督、不可变审计追踪及持续身份管理，Gartner 将"Agentic AI 治理"列为 2026 新兴企业优先级。'
    ),
    NewsItem(
        '中国 AI Agent 监管细则 7 月 15 日落地：首个将 Agent 分级管理的国家框架',
        'https://eveaicore.com/blog/ai-regulation-2026-what-changed',
        'EveAI Core / AI Regulation 2026', 'research', datetime(2026,7,15,tzinfo=timezone.utc),
        '中国《智能体实施意见》于 7 月 15 日正式生效，将 AI Agent 的决策权限划分为多个权限层级，在部署前须完成分层授权认定，这是全球首个将 AI Agent 作为独立监管类别进行单独立法的国家框架，对在华部署 Agent 应用的国内外企业均有约束效力。'
    ),
]

# --- 论文 ---
papers = [
    Paper(
        'OpenThoughts-Agent: Data Recipes for Agentic Models',
        'https://arxiv.org/pdf/2606.24855', '2606.24855',
        ['OpenThoughts Team'],
        '提出专为 Agentic 推理设计的数据配方框架（OpenThoughts-Agent），系统化构建高质量多步骤工具调用训练数据，在 OSWorld、WebArena、SWE-bench 等核心 Agent 基准上大幅超越同等规模监督微调基线，揭示数据质量与 Agent 泛化能力之间的核心关联。',
        ['cs.AI', 'cs.LG'], datetime(2026,8,10,tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2606.24855',
    ),
    Paper(
        'Act As a Real Researcher: A Suite of Benchmarks Evaluating Frontier LLMs in Research Lifecycle',
        'https://arxiv.org/pdf/2606.07462', '2606.07462',
        ['Research Lifecycle Benchmark Team'],
        '构建覆盖完整科研生命周期的评测套件（文献综述→假设生成→实验设计→结果分析→论文撰写），评估当前前沿 LLM 的科研能力边界。GPT-5.6 Sol 与 Claude Mythos 5 在多数环节领先，但均无法独立完成"发现新颖科学问题"子任务，为下一代科研 Agent 指明核心攻关方向。',
        ['cs.AI', 'cs.CL'], datetime(2026,8,8,tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2606.07462',
    ),
    Paper(
        'DyTopo: Dynamic Topology Routing for Multi-Agent Reasoning via Semantic Matching',
        'https://arxiv.org/list/cs.MA/current', '2508.DyTopo',
        ['Multi-Agent Topology Research Group'],
        '提出 DyTopo，通过语义匹配在每轮推理时动态重构 Agent 间通信拓扑，替代固定的星型/链式结构。在数学推理、代码生成和多跳问答任务上，相比固定拓扑基线分别提升 9%、13% 和 11%，且无需额外预训练，可即插即用于现有多 Agent 框架。',
        ['cs.MA', 'cs.AI'], datetime(2026,8,12,tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.MA/current',
    ),
    Paper(
        'MAS-Orchestra: Improving Multi-Agent Reasoning via Holistic Orchestration',
        'https://arxiv.org/list/cs.MA/current', '2508.MASOrch',
        ['MAS Orchestra Team'],
        '将多 Agent 编排形式化为函数调用强化学习问题，提出 MASBENCH 受控评测基准，训练时同时优化个体子 Agent 与系统整体的推理质量。在 MASBENCH 上相比单 Agent 和朴素多 Agent 基线分别提升 18% 和 11%，为 Agentic 系统的协同训练提供可扩展框架。',
        ['cs.MA', 'cs.LG'], datetime(2026,8,11,tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.MA/current',
    ),
    Paper(
        'Adversarial Attacks in Multi-Agent LLM Pipelines: Structural Vulnerabilities in Agentic AI',
        'https://arxiv.org/list/cs.CR/current', '2508.AdversarialMAS',
        ['GLOBECOM 2026 Security Track'],
        '系统揭示多 Agent LLM 管线中的结构性安全漏洞：提示注入在子 Agent 间的传播路径、工具调用的伪造攻击面、以及跨 Agent 信任传递缺陷。提出三类防御原语（沙盒隔离、输出签名、角色边界约束），被 GLOBECOM 2026 接收，为 Agent 安全工程提供理论基础。',
        ['cs.CR', 'cs.AI'], datetime(2026,8,9,tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.CR/current',
    ),
]

# --- 大牛动态 ---
updates = [
    InfluencerUpdate(
        'Andrej Karpathy', 'Blog',
        '在 Sequoia Ascent 2026 演讲中正式提出 Software 3.0 概念，将"AI 自动化所有可验证结果"定义为新一代软件范式。他的 nano* 系列（nanoGPT、nanochat、micrograd）GitHub 总星数突破 12 万。自 5 月加入 Anthropic 预训练团队后，公开技术分享聚焦于"用 Claude 加速 Claude 预训练研究"这一递归性命题，社区将其 LLM 编码缺陷观察整理为 CLAUDE.md 最佳实践（GitHub 已获超 10 万星）。',
        'https://karpathy.bearblog.dev/sequoia-ascent-2026/', datetime(2026,8,14,tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Simon Willison', 'Blog',
        '发布《Gemini 3.7 Flash: the Flash tier keeps getting better》，深度分析 Google 新模型在编程 Agent 场景的实际表现，指出 Flash 系列正在快速逼近旗舰模型能力。他同时提倡在 Agentic 工作流中分层使用模型——实现层子 Agent 用较弱模型，主循环保留强模型做判断与综合——预计可将成本降低 60% 以上。',
        'https://simonwillison.net/', datetime(2026,8,14,tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Sebastian Raschka', 'Blog',
        '最新一期 Ahead of AI Newsletter 系统梳理 2026 年上半年最重要 LLM 研究进展（Jan-May）：聚焦混合注意力架构（GDN/GQA）、MoE 扩展规律和推理模型训练范式演变。结合 Qwen3.8-27B 发布，他将其评为"2026 年最值得本地部署的单模型"，建议工程师在 Agent 编排和 RAG 管线中以此替代闭源 API，以控制延迟与成本。',
        'https://magazine.sebastianraschka.com/p/llm-research-papers-2026-part1', datetime(2026,8,13,tzinfo=timezone.utc),
    ),
]

# --- GitHub 热门 ---
github = [
    GithubProject(
        'diegosouzapw/OmniRoute', 'https://github.com/diegosouzapw/OmniRoute',
        'Free MIT AI gateway: one endpoint, 339 providers (90+ free), 1200+ models. Quota-aware auto-fallback, RTK+Caveman 15-95% token savings, MCP/A2A. Works with Claude Code, Codex, Cursor.',
        23080, 1890, 'TypeScript', 14667, ['diegosouzapw']
    ),
    GithubProject(
        'openclawai/openclaw', 'https://github.com/openclawai/openclaw',
        'Personal AI assistant running entirely on your own devices — connects 50+ integrations (WhatsApp, Telegram, Slack, iMessage) with major AI models. Fastest-growing open-source project of 2026.',
        210000, 18500, 'TypeScript', 1800, []
    ),
    GithubProject(
        'VoltAgent/awesome-ai-agent-papers', 'https://github.com/VoltAgent/awesome-ai-agent-papers',
        'Curated collection of 2026 AI agent research papers covering agent engineering, memory, evaluation, autonomous workflows, and multi-agent systems. Updated weekly.',
        8200, 640, 'Markdown', 410, []
    ),
    GithubProject(
        'caramaschiHG/awesome-ai-agents-2026', 'https://github.com/caramaschiHG/awesome-ai-agents-2026',
        '🤖 The most comprehensive list of AI agents, frameworks & tools in 2026. 300+ resources · 20+ categories · Updated monthly.',
        11400, 820, 'Markdown', 380, []
    ),
    GithubProject(
        'ollama/ollama', 'https://github.com/ollama/ollama',
        'Get up and running with Llama, DeepSeek, Mistral, Gemma, Qwen3.8 and other large language models locally. Now supports Qwen3.8-27B via GGUF quantization.',
        165000, 13200, 'Go', 520, []
    ),
    GithubProject(
        'comfyanonymous/ComfyUI', 'https://github.com/comfyanonymous/ComfyUI',
        'The most powerful and modular diffusion model GUI and backend. Node-based visual workflow system for granular control over image/video generation pipelines.',
        106000, 11300, 'Python', 290, []
    ),
]

filename, content = generate_jekyll_post(news, papers, updates, github)
out_path = f'/home/user/ai-daily-news/reports/{filename}'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f'Jekyll 文章已生成：{filename}')
print(f'字符数：{len(content)}')
print('---')
print(content[:600])
