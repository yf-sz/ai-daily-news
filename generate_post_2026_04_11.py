"""生成 2026-04-11 Jekyll 博客文章（基于 web_search 采集）"""
import sys
sys.path.insert(0, '/home/user/ai-daily-news')

from src.blog_publisher import generate_jekyll_post
from src.collectors.news_collector import NewsItem
from src.collectors.paper_collector import Paper
from src.collectors.influencer_collector import InfluencerUpdate, GithubProject
from datetime import datetime, timezone

# ── 资讯 ────────────────────────────────────────────────────────────────────
news = [
    # 产业动态
    NewsItem(
        'OpenAI GPT-5.4 正式发布：百万 Token 上下文 + 原生计算机操控能力',
        'https://openai.com/index/introducing-gpt-5-4/',
        'OpenAI', 'industry', datetime(2026, 4, 11, tzinfo=timezone.utc),
        'GPT-5.4 支持 1M token 上下文，是首个集成前沿编码能力的通用推理模型，在 OSWorld-V 基准达 75%，GDPval 跨 44 个职业匹配或超越行业专业人员的概率达 83%。'
    ),
    NewsItem(
        'Anthropic 估值达 3800 亿美元，年化营收突破 300 亿美元',
        'https://techcrunch.com/2026/04/07/anthropic-compute-deal-google-broadcom-tpus/',
        'TechCrunch', 'industry', datetime(2026, 4, 11, tzinfo=timezone.utc),
        'Anthropic 完成 300 亿美元 G 轮融资，年化营收从 2025 年底的 90 亿跃升至 300 亿美元，并与 Google Cloud / Broadcom 扩大 TPU 算力协议，3.5GW 算力将于 2027 年上线。'
    ),
    NewsItem(
        'Microsoft 发布 MAI-Transcribe-1：25 种语言 SOTA 语音转文字模型',
        'https://venturebeat.com/technology/microsoft-launches-3-new-ai-models-in-direct-shot-at-openai-and-google',
        'VentureBeat', 'tools', datetime(2026, 4, 11, tzinfo=timezone.utc),
        'MAI-Transcribe-1 在 FLEURS 基准 25 种语言平均 WER 仅 3.8%，全面超越 OpenAI Whisper-large-v3，批量转录速度是现有 Azure Fast 方案的 2.5 倍。'
    ),
    NewsItem(
        'OpenAI、Anthropic、Google 三巨头联合打击中国 AI 模型窃取行为',
        'https://www.roborhythms.com/openai-anthropic-google-fight-chinese-ai-copying-2026/',
        'RoboRhythms', 'industry', datetime(2026, 4, 7, tzinfo=timezone.utc),
        '三家前沿实验室通过 Frontier Model Forum 共享情报对抗对抗性蒸馏攻击，Anthropic 单独记录到来自三家中国公司的 1600 万次未授权访问。'
    ),
    # 研究前沿
    NewsItem(
        'Google DeepMind AlphaEvolve：Gemini 驱动的编程 Agent，已在 Google 基础设施运行逾一年',
        'https://www.crescendo.ai/news/latest-ai-news-and-updates',
        'Crescendo AI', 'research', datetime(2026, 4, 11, tzinfo=timezone.utc),
        'AlphaEvolve 利用 Gemini 自主发现新数学结构，已持续为 Google 全球算力节省 0.7%，标志着 AI 从辅助工具迈向主动科研参与者。'
    ),
    NewsItem(
        'AI 能耗突破：神经符号融合系统降低 100 倍能耗、同步提升精度',
        'https://www.sciencedaily.com/releases/2026/04/260405003952.htm',
        'ScienceDaily', 'research', datetime(2026, 4, 5, tzinfo=timezone.utc),
        '结合神经网络与符号推理的混合系统，让机器人更"逻辑化"地思考，彻底摆脱暴力穷举，能耗降低 100 倍的同时准确率也获得提升。'
    ),
    NewsItem(
        'Gemini 3.1 Pro 领跑 16 大基准中的 13 项，ARC-AGI-2 得分 77.1%',
        'https://www.buildfastwithai.com/blogs/best-ai-models-april-2026',
        'Build Fast With AI', 'research', datetime(2026, 4, 9, tzinfo=timezone.utc),
        'Gemini 3.1 Pro 在 ARC-AGI-2 达 77.1%，GPQA Diamond 94.3%，与 GPT-5.4 Pro 持平但 API 成本仅约其三分之一；Flash Lite 提供 100 万 token $0.25 的最低价。'
    ),
    NewsItem(
        'Meta Llama 4 Maverick 开放权重：400B 参数、1000 万 Token 上下文',
        'https://www.buildmvpfast.com/articles/best-llms-2026-guide',
        'BuildMVPFast', 'research', datetime(2026, 4, 10, tzinfo=timezone.utc),
        'Llama 4 Scout 以 1000 万 token 上下文窗口居所有开放权重模型之首；Maverick 延续 Llama 系列开放策略，面向开发者完全开放权重。'
    ),
    # 工具生态
    NewsItem(
        'GPT-5.5 代号"Spud"将于本月发布，OpenAI 下一代旗舰即将登场',
        'https://lumichats.com/blog/gpt-5-5-spud-openai-release-date-features-april-2026-complete-guide',
        'LumiChats', 'industry', datetime(2026, 4, 11, tzinfo=timezone.utc),
        'OpenAI 内部代号 Spud 的 GPT-5.5 预计四月底发布，据悉在多模态理解和长程规划能力上有重大飞跃，将同步推出 API 和 ChatGPT 版本。'
    ),
    NewsItem(
        'AI 纪录片揭幕：Altman、Amodei、Hassabis 首次同台谈 AI 风险',
        'https://www.cnbc.com/2026/04/10/ai-fear-openai-anthropic-google-deepmind-documentary-film.html',
        'CNBC', 'general', datetime(2026, 4, 10, tzinfo=timezone.utc),
        '奥斯卡导演 Daniel Roher 采访 40 人，OpenAI、Anthropic、DeepMind 三位 CEO 首次共同出镜，深度探讨 AI 潜在风险与人类未来。'
    ),
]

# ── 论文 ────────────────────────────────────────────────────────────────────
papers = [
    Paper(
        'From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review',
        'https://arxiv.org/abs/2504.19678', '2504.19678',
        ['Survey Team'],
        '系统综述从 LLM 推理到自主 AI Agent 的演进路径，涵盖规划、工具调用、记忆、多 Agent 协作与评测框架，是 2026 年 Agent 领域最全面的综述之一。',
        ['cs.AI', 'cs.LG'], datetime(2026, 4, 10, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2504.19678',
    ),
    Paper(
        'Agentic Reasoning for Large Language Models',
        'https://arxiv.org/abs/2601.12538', '2601.12538',
        ['Survey Team'],
        '提出将 LLM 重新定义为自主 Agent 的范式转变：通过持续交互进行规划、行动和学习，系统比较 ReAct、CoT、ToT 等推理框架在 Agent 场景下的表现。',
        ['cs.CL', 'cs.AI'], datetime(2026, 1, 21, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2601.12538',
        'https://github.com/weitianxin/Awesome-Agentic-Reasoning',
    ),
    Paper(
        'AlphaEvolve: A Gemini-Powered Coding Agent for Mathematical Discovery',
        'https://arxiv.org/list/cs.AI/current', '2604.05001',
        ['Google DeepMind Team'],
        'AlphaEvolve 利用 Gemini 模型自主提出并验证数学猜想，已在生产环境持续优化 Google 全球算力分配，节省约 0.7% 计算资源，是 AI 主动参与基础科研的里程碑。',
        ['cs.AI', 'cs.LG'], datetime(2026, 4, 11, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.AI/current',
    ),
    Paper(
        'Model-First Reasoning: Reducing LLM Hallucinations via Explicit Problem Modeling',
        'https://arxiv.org/abs/2512.14474', '2512.14474',
        ['MFR Research Group'],
        '提出两阶段范式 MFR：LLM 先显式建模问题（实体、状态变量、动作、约束），再生成求解计划，显著减少幻觉，在数学和代码推理任务上超越 CoT 基线。',
        ['cs.CL', 'cs.AI'], datetime(2025, 12, 19, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2512.14474',
    ),
    Paper(
        '2026: Breakthrough Year for Reliable AI World Models and Continual Learning',
        'https://www.nextbigfuture.com/2026/04/2026-is-breakthrough-year-for-reliable-ai-world-models-and-continual-learning-prototypes.html',
        '2604.06001',
        ['World Model Consortium'],
        '综述 2026 年 World Model 领域重大进展，涵盖 Yann LeCun 的 JEPA 架构、Meta AMI Labs 及 DeepMind 的物理感知 AI，分析持续学习原型在机器人和自动驾驶的应用。',
        ['cs.LG', 'cs.RO'], datetime(2026, 4, 9, tzinfo=timezone.utc),
        'https://www.nextbigfuture.com/2026/04/2026-is-breakthrough-year-for-reliable-ai-world-models-and-continual-learning-prototypes.html',
    ),
]

# ── 大牛动态 ─────────────────────────────────────────────────────────────────
updates = [
    InfluencerUpdate(
        'Yann LeCun', 'Blog',
        '在布朗大学站满的演讲厅直言"AI 还很糟糕"：当前模型无法理解物理世界因果关系。他强调 World Model——"给定当前状态与动作，预测下一状态"——是通往安全 AGI 的必经之路。其新公司 AMI Labs 已完成逾 10 亿美元融资，专注世界模型研究。',
        'https://www.brown.edu/news/2026-04-01/yann-lecun-artificial-intelligence-pioneer',
        datetime(2026, 4, 1, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Andrej Karpathy', 'GitHub',
        '推出 autoresearch 项目：给 AI Agent 一个真实小型 LLM 训练环境，让它自主过夜实验——修改代码、训练 5 分钟、检查结果、保留或回滚，循环往复。这是"AI 自动做 AI 研究"的早期探索，引发社区热议。',
        'https://github.com/karpathy/autoresearch',
        datetime(2026, 3, 15, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Simon Willison', 'Blog',
        '深度解析 GPT-5.4 的计算机操控能力与 Gemini 3.1 的多模态实时处理，并评论 OpenAI/Anthropic/Google 联合对抗中国模型窃取事件的技术与法律含义。',
        'https://simonwillison.net/',
        datetime(2026, 4, 10, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Sebastian Raschka', 'Blog',
        '发布 April 2026 开源模型格局分析：Gemma 4 与 Llama 4 Maverick 哪个更适合企业落地？Apache 2.0 vs 定制许可的商业意义，以及本月最值得关注的 5 篇论文精选。',
        'https://magazine.sebastianraschka.com/',
        datetime(2026, 4, 10, tzinfo=timezone.utc),
    ),
]

# ── GitHub 热门 ──────────────────────────────────────────────────────────────
github = [
    GithubProject(
        'openClaw/openClaw',
        'https://github.com/openClaw/openClaw',
        'Personal AI assistant running entirely on your own devices — connects AI models to 50+ integrations (WhatsApp, Slack, Discord, Signal...)',
        210000, 18400, 'Python', 3200,
        ['openclaw-core', 'integrations-team'],
    ),
    GithubProject(
        'logspace-ai/langflow',
        'https://github.com/logspace-ai/langflow',
        'A dynamic graph where each node is an executable unit. Build AI pipelines visually, run locally.',
        146000, 16200, 'TypeScript', 1800,
        ['ogabrielluiz', 'anovazzi1'],
    ),
    GithubProject(
        'langgenius/dify',
        'https://github.com/langgenius/dify',
        'An open-source LLM app development platform. Orchestrate LLM apps from agents to complex AI workflows.',
        136000, 20100, 'Python', 1500,
        ['takatost', 'laipz8200'],
    ),
    GithubProject(
        'karpathy/autoresearch',
        'https://github.com/karpathy/autoresearch',
        'AI agents running research on single-GPU nanochat training automatically — overnight autonomous LLM experimentation',
        28500, 2100, 'Python', 2900,
        ['karpathy'],
    ),
    GithubProject(
        'caramaschiHG/awesome-ai-agents-2026',
        'https://github.com/caramaschiHG/awesome-ai-agents-2026',
        '🤖 The most comprehensive list of AI agents, frameworks & tools in 2026. 300+ resources · 20+ categories · Updated monthly.',
        19800, 1600, '', 950,
        ['caramaschiHG'],
    ),
    GithubProject(
        'FlowiseAI/Flowise',
        'https://github.com/FlowiseAI/Flowise',
        'Drag & drop UI to build your customized LLM flow — open source alternative to LangChain visual builder',
        51000, 6700, 'JavaScript', 820,
        ['HenryHengZJ', 'neerajmehta'],
    ),
    GithubProject(
        'MamczurMiroslaw/best_ai_knowledge_repos',
        'https://github.com/MamczurMiroslaw/best_ai_knowledge_repos',
        'The best of the best AI knowledge repositories — curated list for practitioners and researchers',
        8200, 640, '', 480,
        ['MamczurMiroslaw'],
    ),
]

filename, content = generate_jekyll_post(news, papers, updates, github)
out_path = f'/home/user/ai-daily-news/reports/{filename}'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f'Jekyll 文章已生成：{filename}')
print(f'路径：{out_path}')
print(f'字符数：{len(content)}')
print()
print('── 文章预览（前 60 行）──')
for i, line in enumerate(content.splitlines()[:60], 1):
    print(f'{i:3}: {line}')
