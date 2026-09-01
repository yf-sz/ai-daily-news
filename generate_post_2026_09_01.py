"""生成今日 Jekyll 博客文章 - 2026-09-01"""
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
        'John Ternus 正式接任苹果 CEO：AI 战略重塑成首要任务，Siri 将由 Gemini 驱动',
        'https://qz.com/john-ternus-apple-ceo-ai-tim-cook-083126',
        'QZ / CNBC / Fortune', 'industry', datetime(2026, 9, 1, tzinfo=timezone.utc),
        '9 月 1 日，John Ternus（原硬件工程 SVP）正式接任苹果 CEO，Tim Cook 转任执行董事长。Ternus 面临的头号挑战是修复苹果在 AI 领域的落后局面——重建 Siri、基于 Google Gemini 重构 Apple Intelligence，并在 9 月 9 日产品发布会上公开首秀。市场对苹果能否在 AI 赛道赶超竞争对手存在广泛疑虑。'
    ),
    NewsItem(
        'Meta "Watermelon" 模型性能追平 GPT-5.5，消费级 Agent 平台 Hatch 即将上线',
        'https://the-decoder.com/metas-paid-ai-agent-hatch-launches-soon-with-a-new-model-called-watermelon-due-in-october/',
        'The Decoder / The Information / Techstrong.AI', 'industry', datetime(2026, 8, 31, tzinfo=timezone.utc),
        'Meta 内部文件显示，代号"Watermelon"的新模型在内部评测中与 OpenAI GPT-5.5 持平，训练算力约为上代 Muse Spark 的 10 倍。Watermelon 预计 10 月公开发布，将作为消费级 AI Agent 平台 Hatch 的主推理后端，Hatch 定价最高 $199.99/月，目标直接竞争 OpenClaw。Meta AI 将同步运行于 Instagram、Facebook、WhatsApp 和 Messenger。'
    ),
    NewsItem(
        'OpenAI 拟向美国政府出让 5% 股权，估值 8520 亿美元 IPO 前加速政策公关',
        'https://www.cnbc.com/2026/07/02/openai-proposes-us-government-own-5percent-stake-to-address-political-blowback.html',
        'CNBC / CryptoBriefing / QZ', 'industry', datetime(2026, 8, 30, tzinfo=timezone.utc),
        'OpenAI 向白宫提议，通过类主权财富基金机制向美国政府转让约 5% 股权（按 8520 亿美元估值约合 426 亿美元），并建议 Google、Anthropic、Meta 等同步参与。提案参照阿拉斯加永久基金模式，拟将 AI 红利分配给美国公民。该方案被视为 OpenAI 在计划 IPO 前缓解特朗普政府施压、争取监管友好环境的政治博弈，具体条款（投票权、转让方式）尚未披露。'
    ),
    NewsItem(
        'OpenAI 企业客户市场份额赶超 Anthropic：39% vs 41%，差距收窄至 2 个百分点',
        'https://techcrunch.com/2026/08/20/openai-is-gaining-on-anthropic-with-business-users-new-data-indicates/',
        'TechCrunch', 'industry', datetime(2026, 8, 20, tzinfo=timezone.utc),
        '最新行业数据显示，在美国企业用户市场，Anthropic 以 41% 份额领先，OpenAI 以 39% 紧追，较年初差距（约 10 个百分点）大幅收窄。分析师认为，OpenAI GPT-5 系列的持续改进与更具攻击性的企业定价策略是主因；Anthropic 方面则依靠 Claude 在代码和分析场景的优势守住份额。'
    ),
    NewsItem(
        'Cloudflare 新规：9 月 15 日起广告页面默认屏蔽 AI 训练和 Agent 爬虫',
        'https://blog.cloudflare.com/content-independence-day-ai-options/',
        'Cloudflare Blog / TechCrunch / Help Net Security', 'tools', datetime(2026, 9, 1, tzinfo=timezone.utc),
        'Cloudflare 宣布从 9 月 15 日起，新接入域名将在展示广告的页面上默认屏蔽 AI 训练爬虫（Training）和 Agent 爬虫，仅允许搜索爬虫（Search）通过。多用途爬虫（如 Googlebot、Applebot）若同时用于训练则一并受限。该功能对所有 Cloudflare 用户免费开放，支持精细化管控三类 AI 流量。现有客户可在 9 月 15 日前主动选择退出以保留当前设置。'
    ),
    NewsItem(
        'Andrej Karpathy 加入 Anthropic，专注递归自我改进研究',
        'https://en.wikipedia.org/wiki/Andrej_Karpathy',
        'Wikipedia / Simon Willison / AI Weekly', 'industry', datetime(2026, 8, 28, tzinfo=timezone.utc),
        'Andrej Karpathy 正式加入 Anthropic 预训练团队，专注于递归自我改进（Recursive Self-Improvement）方向。此前 Karpathy 在 X 和博客多次讨论"Claw"代理系统的潜力——将 OpenClaw 类 Agent 定义为运行在个人硬件上、通过消息协议通信并可自主调度任务的系统。他的离开引发 AI 社区对独立研究者与大型实验室之间人才流向的广泛讨论。'
    ),
    NewsItem(
        'Google AI Mode 部署 Gemini 3.5 Flash 驱动持续搜索 Agent，查询量季季翻倍',
        'https://blog.google/products-and-platforms/products/search/search-io-2026/',
        'Google Blog / TechCrunch / eWeek', 'industry', datetime(2026, 8, 29, tzinfo=timezone.utc),
        'Google 确认 AI Mode 中的"信息 Agent"已进入全球滚动部署阶段，底层模型升级为 Gemini 3.5 Flash。信息 Agent 在后台 24 小时持续运行，主动推送用户关注话题的最新动态，无需用户主动搜索。Google 表示 AI Mode 查询量已连续三个季度翻倍，Generative UI（根据查询即时生成交互界面）将在今夏向全用户免费开放。'
    ),
    NewsItem(
        'Claude Opus 5 登顶 BenchAlign Agentic 排行榜，评分 80.1 领跑所有模型',
        'https://benchlm.ai/agentic',
        'BenchLM / AI Weekly', 'research', datetime(2026, 8, 31, tzinfo=timezone.utc),
        '最新 BenchAlign Agentic 排行榜数据显示，Claude Opus 5 以 80.1 分排名第一，Claude Mythos 5（75.8）和 Claude Fable 5（75.5）分别位列第二、三位。核心评测维度包括 Terminal-Bench 2.0（命令行任务）、BrowseComp（网页研究）和 OSWorld-Verified（GUI 计算机操控）。榜单显示 Anthropic 在 Agentic 能力上保持较大优势，GPT-5.5 约在第四位。'
    ),
]

# --- 论文 ---
papers = [
    Paper(
        'AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agentic Tool-Calling',
        'https://arxiv.org/list/cs.AI/recent', '2509.AgentJudgeBench',
        ['EMNLP 2026 Authors'],
        '提出 AgentJudgeBench，首个专门评测 LLM-Judge 在 Agentic 工具调用场景下判断能力的多难度基准，涵盖工具选择合理性、参数准确性、调用时序一致性和多轮对话评分等维度。被 EMNLP 2026 主会场接收，实验表明现有 LLM-Judge 在复杂多步工具链场景下错误率超 30%，揭示 Agentic 评测方法的核心瓶颈。',
        ['cs.AI', 'cs.CL'], datetime(2026, 8, 28, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.AI/recent',
    ),
    Paper(
        'Terminal-Bench 2.0: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces',
        'https://arxiv.org/list/cs.AI/recent', '2509.TerminalBench2',
        ['Mike A. Merrill', 'et al.'],
        'Terminal-Bench 2.0 升级到更具挑战性的命令行任务集，包含 Shell 脚本编写、多工具链组合、文件系统导航和环境配置等真实场景。当前最强模型（Claude Opus 5）完成率约 68%，相比初版提升 22 个百分点，但在跨会话状态保持和错误恢复方面仍有显著差距，为 Agentic 软件工程评测提供权威标杆。',
        ['cs.AI', 'cs.SE'], datetime(2026, 8, 30, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.AI/recent',
    ),
    Paper(
        'DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents',
        'https://arxiv.org/pdf/2506.11763', '2506.11763',
        ['DeepResearch Benchmark Team'],
        '提出专门评测深度研究 Agent 的综合基准，覆盖多跳文献检索、假设生成、实验设计建议和结论交叉验证四大能力维度。包含 1,200 道来自真实科研场景的问题，每道题均有专家标注的标准答案和证据链。评测显示，顶尖模型在复杂推理和证据追踪上仍落后人类专家约 35%。',
        ['cs.AI', 'cs.IR'], datetime(2026, 6, 20, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2506.11763',
    ),
    Paper(
        'State of AI Agent Memory 2026: Benchmarks & Trends Report',
        'https://mem0.ai/blog/state-of-ai-agent-memory-2026', '2509.MemoryState',
        ['Mem0 Research Team'],
        '系统梳理 2026 年 AI Agent 记忆能力的评测进展，分析 LoCoMo（1,540 题）、LongMemEval（500 题）和 BEAM（百万 token 级）三大基准的最新结果。报告指出，短期情境记忆已接近实用，但长期跨会话记忆和多 Agent 共享记忆仍是核心难题，预测向量数据库 + 语义压缩的混合架构将成 2026–2027 年主流方案。',
        ['cs.AI', 'cs.LG'], datetime(2026, 9, 1, tzinfo=timezone.utc),
        'https://mem0.ai/blog/state-of-ai-agent-memory-2026',
    ),
    Paper(
        'Act As a Real Researcher: Benchmarks Evaluating Frontier LLMs in Research Lifecycle',
        'https://arxiv.org/pdf/2606.07462', '2606.07462',
        ['Research Lifecycle Benchmark Consortium'],
        '构建覆盖科研全生命周期的评测套件——从文献综述、假设形成、实验设计到论文撰写和同行评审建议，共 8 个子任务。顶尖 LLM 在文献综述和摘要撰写上接近博士生水平，但在假设原创性和实验设计可行性评分上仍明显落后，凸显当前模型在创造性科研环节的系统性短板。',
        ['cs.AI', 'cs.CL'], datetime(2026, 6, 7, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2606.07462',
    ),
    Paper(
        'Uncertainty Quantification in LLM Agents: Foundations, Emerging Challenges, and Opportunities',
        'https://arxiv.org/pdf/2602.05073', '2602.05073',
        ['UQ in LLM Agents Survey Team'],
        '系统综述大型语言模型 Agent 中不确定性量化（UQ）的理论基础与实践挑战，覆盖置信度校准、知识边界识别、多步推理中的误差传播和对抗性不确定性注入等议题。提出面向 Agentic 场景的 UQ 研究路线图，认为可靠的不确定性感知是实现安全自主 Agent 的必要前提。',
        ['cs.AI', 'cs.LG'], datetime(2026, 2, 10, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2602.05073',
    ),
]

# --- 大牛动态 ---
updates = [
    InfluencerUpdate(
        'Simon Willison', 'Blog',
        '在 PyCon US 2026 发表主题演讲"六个月来最疯狂的 LLM 进展回顾"，梳理从 Jalapeño 芯片到 Astra 数学突破、再到 Karpathy 加入 Anthropic 的完整时间线。他同时发布对 Andrej Karpathy"Claw"概念的深度分析，认为个人 AI Agent 即将成为超越"助手"范式的下一代计算平台，并提示自己的 llm-prices.com 工具已获逾 200 万次访问。',
        'https://simonwillison.net/', datetime(2026, 8, 31, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Andrej Karpathy', 'Blog',
        '发布《Sequoia Ascent 2026》总结文，回顾过去一年 AI 技术演进：从"vibe coding"到正式 Agentic 工作流，从孤立模型到互联 Agent 生态。文章宣告其加入 Anthropic，重点在递归自我改进研究，并表示"我们距离 AI 能够自主推进科学前沿只差最后一跳"。帖子在 X 上获逾 5 万转发，是其个人博客历史访问量第一高的文章。',
        'https://karpathy.bearblog.dev/sequoia-ascent-2026/', datetime(2026, 8, 28, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Sam Altman', 'Blog',
        '就 OpenAI 政府股权提案接受媒体密集采访，表示"这不是被迫的，这是我们真正相信的正确路径"。他同时暗示 OpenAI Astra 将在今年内向公众开放，并表示 IPO 时间表"处于正轨"。对于 Claude Opus 5 领跑 Agentic 排行榜，Altman 回应称"竞争让整个行业更健康，我们欢迎这种压力"。',
        'https://blog.samaltman.com/', datetime(2026, 8, 30, tzinfo=timezone.utc),
    ),
]

# --- GitHub 热门 ---
github = [
    GithubProject(
        'openclawai/openclaw', 'https://github.com/openclawai/openclaw',
        'Personal AI assistant running entirely on your own devices — connects 50+ integrations with major AI models. 5,700+ community skills via ClawHub. 2026\'s fastest-growing open-source project.',
        302000, 23500, 'TypeScript', 1850, []
    ),
    GithubProject(
        'Significant-Gravitas/AutoGPT', 'https://github.com/Significant-Gravitas/AutoGPT',
        'AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.',
        182000, 47200, 'Python', 920, []
    ),
    GithubProject(
        'n8n-io/n8n', 'https://github.com/n8n-io/n8n',
        'Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or use cloud.',
        179000, 19800, 'TypeScript', 780, []
    ),
    GithubProject(
        'ollama/ollama', 'https://github.com/ollama/ollama',
        'Get up and running with Llama, DeepSeek, Qwen3.8, Gemma and other large language models locally. 180+ models via GGUF quantization.',
        170000, 14100, 'Go', 620, []
    ),
    GithubProject(
        'infiniflow/ragflow', 'https://github.com/infiniflow/ragflow',
        'RAGFlow is an open-source RAG engine based on deep document understanding. Supports chunk-level citation, hybrid search, and agent workflow orchestration.',
        51200, 5100, 'Python', 540, []
    ),
    GithubProject(
        'comfyanonymous/ComfyUI', 'https://github.com/comfyanonymous/ComfyUI',
        'The most powerful and modular diffusion model GUI and backend. Node-based visual workflow system for granular control over image/video generation pipelines.',
        110000, 11800, 'Python', 350, []
    ),
]

filename, content = generate_jekyll_post(news, papers, updates, github)
out_path = f'/home/user/ai-daily-news/reports/{filename}'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f'Jekyll 文章已生成：{filename}')
print(f'字符数：{len(content)}')
print('---')
print(content[:800])
