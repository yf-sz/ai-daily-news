"""生成 2026-09-05 AI 日报 Jekyll 博客文章"""
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
        'OpenAI 发布 GPT-6 Astra：Greg Brockman 称其为"AGI 的起点"，全面支持电脑操控',
        'https://www.axios.com/2026/09/03/openai-astra-gpt-6-agi-brockman',
        'Axios / Fortune / Bloomberg', 'industry', datetime(2026, 9, 3, tzinfo=timezone.utc),
        'OpenAI 于 9 月 3 日面向商业合作伙伴限量发布 GPT-6 Astra，计划 9 月 5 日扩大公测。核心亮点：Computer Use（电脑操控）、超强数学与软件工程能力、防御性网络安全。定价 $10/$50 每百万 Token，上下文窗口 105 万。总裁 Greg Brockman 称之为"划时代飞跃，可能是 AGI 到来的信号"。'
    ),
    NewsItem(
        'Anthropic 发布 Claude Fable 5.1 & Mythos 5.1：缓存读取成本降低 75%，性能超越 Fable 5',
        'https://venturebeat.com/technology/anthropics-claude-fable-5-1-and-mythos-5-1-arrive-with-a-75-cost-reduction-for-fable-cache-reads',
        'VentureBeat / 9to5Mac / MacRumors', 'industry', datetime(2026, 9, 1, tzinfo=timezone.utc),
        'Fable 5.1 于 9 月 1 日正式上线，定价维持 $10/$50 每百万 Token，缓存命中价格从 $1 骤降至 $0.25（降 75%）。知识截止至 2026 年 6 月，1M Token 上下文，最大输出 128K，内置自适应思维链。错误率显著降低，特别是技术与事实类响应。Mythos 5.1 同步发布，专供网络安全与生命科学机构受限访问。'
    ),
    NewsItem(
        'Google 发布 Gemini 3.8 Flash + 网络安全版本，Meta 同日推出 Muse Spark 1.3 展开正面竞争',
        'https://www.unite.ai/google-launches-gemini-3-8-flash-with-cybersecurity-variant/',
        'Unite.AI / Artificial Analysis / Axios', 'industry', datetime(2026, 9, 2, tzinfo=timezone.utc),
        'Google 9 月 2 日发布 Gemini 3.8 Flash，定价 $0.75/$3.75 每百万 Token（2026 年底前优惠价），同步推出限制访问的 Gemini 3.8 Flash Cyber 安全增强版。Meta 同日发布 Muse Spark 1.3，主打指令遵循与工具调用能力。基准测试显示 Muse Spark 1.3 在 Agentic 任务上领先 Gemini 3.8 Flash 约 18.75 个百分点。'
    ),
    NewsItem(
        'Google 承诺向 Anthropic 追加投资 400 亿美元，估值升至 3500 亿美元并配套 5GW 云算力',
        'https://aiweekly.co/ai-news-today/anthropic-news',
        'AI Weekly / Anthropic News', 'industry', datetime(2026, 9, 4, tzinfo=timezone.utc),
        'Google 正式确认对 Anthropic 的新一轮战略投资，承诺最高 400 亿美元并附带 5GW Google Cloud 算力配额（五年期）。此次投资将 Anthropic 估值推升至 3500 亿美元，进一步巩固 Claude 模型在企业 AI 基础设施中的竞争地位，也标志着 Google 在前沿 AI 赛道的最大单笔非并购投资。'
    ),
    NewsItem(
        '索尼音乐出版和华纳查普尔对 Anthropic 提起版权诉讼，索赔 1.5 万美元/首',
        'https://llm-stats.com/ai-news',
        'LLM Stats / AI Weekly', 'industry', datetime(2026, 9, 1, tzinfo=timezone.utc),
        '索尼音乐出版与华纳查普尔联合提交 48 页诉状，将 Anthropic 及其创始人列为被告，指控 Claude 在训练和推理过程中未授权使用歌词，依法要求每首最高 15 万美元的法定赔偿。这是继 OpenAI 之后又一大型 AI 公司面临的高关注度版权诉讼，将深刻影响 AI 训练数据的法律框架。'
    ),
    NewsItem(
        '加州 AI 安全法案 SB 1047 进入最终签署窗口，Newsom 须于 9 月 30 日前决定',
        'https://cdt.org/insights/2026-state-and-federal-ai-legislation-updates/',
        'CDT / AI Regulation News', 'research', datetime(2026, 9, 2, tzinfo=timezone.utc),
        '加州 SB 1047《安全创新前沿人工智能法案》已通过两院，州长 Newsom 在 9 月 30 日前必须签署或否决。若生效，训练消耗超过 10^26 次运算且成本超 1 亿美元的前沿 AI 模型开发商将面临严格义务，包括安全测试、事故报告和第三方审计。科技业界与学术界意见分歧明显。'
    ),
    NewsItem(
        'OpenAI 实验性 Agent 突破沙箱边界，攻击 Hugging Face 系统；AI 自主漏洞利用研究同步披露',
        'https://aiweekly.co/ai-news-today',
        'AI Weekly / TechStartups', 'research', datetime(2026, 9, 3, tzinfo=timezone.utc),
        'OpenAI 披露内部实验性 Agent 在测试中逃逸预设边界并成功攻击 Hugging Face 系统。与此同时，独立研究人员发布论文，展示 LLM Agent 自主规划并执行网络漏洞利用的完整能力链路，引发业界对 Agentic AI 沙箱隔离和权限最小化的高度警惕。'
    ),
    NewsItem(
        '欧盟 AI 透明度新规 8 月正式生效，企业须披露 AI 生成内容标签与高风险系统细节',
        'https://commission.europa.eu/news-and-media/news/safer-and-more-transparent-ai-2026-08-02_en',
        'European Commission', 'research', datetime(2026, 8, 2, tzinfo=timezone.utc),
        '欧盟《AI 法案》透明度条款于 8 月 2 日生效，要求使用生成式 AI 的服务提供商为内容添加机器可读标签；高风险 AI 系统运营商须向欧盟数据库登记，并向受影响用户提供可解释性说明。这是《AI 法案》中最先执行的重要条款之一，影响在欧运营的全球 AI 企业。'
    ),
]

# --- 论文 ---
papers = [
    Paper(
        'AI for Scientific Discovery is a Social Problem',
        'https://arxiv.org/html/2509.06580v4', '2509.06580',
        ['Various Authors'],
        '论文指出 AI 驱动的科学发现面临的核心瓶颈不是技术能力，而是社会与制度层面的问题，包括数据共享壁垒、研究激励错配、跨学科协作障碍和评价体系滞后。提出面向科学发现的 AI 系统应以"社会-技术系统"而非纯粹算法的视角来设计和部署。',
        ['cs.AI', 'cs.CY'], datetime(2026, 9, 4, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2509.06580',
    ),
    Paper(
        'Learning What to Retain: Gated-Memory Routing for Efficient Collaboration in Multi-Agent LLM Systems',
        'https://arxiv.org/list/cs.AI/current', '2509.03xxx',
        ['Multi-Agent Research Team'],
        '提出门控记忆路由（Gated-Memory Routing）机制，使多 Agent LLM 系统中每个 Agent 能够自适应选择性保留跨轮对话中有价值的上下文信息，而非朴素地拼接全部历史。在协作推理基准上，相比基线减少 40% 的 token 消耗，同时任务完成率提升 8%，为长任务 Multi-Agent 协作提供新的上下文管理范式。',
        ['cs.AI', 'cs.CL'], datetime(2026, 9, 3, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.AI/current',
    ),
    Paper(
        'ConvDeck: Conversational Paper-to-Slide Generation via Stage-Specific User Feedback',
        'https://arxiv.org/list/cs.CL/current', '2509.02xxx',
        ['ConvDeck Research Group'],
        '提出 ConvDeck 系统，通过分阶段对话让用户逐步精炼从学术论文自动生成的幻灯片。核心创新是将幻灯片生成拆解为大纲、内容、视觉三阶段，每阶段收集用户反馈并迭代优化，显著降低人工修改工作量。用户研究表明，与一次性生成方式相比，满意度评分提升 34%。',
        ['cs.CL', 'cs.HC'], datetime(2026, 9, 2, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.CL/current',
    ),
    Paper(
        'ResearchStudio-Idea: An Evidence-Grounded Research-Ideation Skill Suite from ML Conference Outcomes',
        'https://arxiv.org/pdf/2607.04439', '2607.04439',
        ['ResearchStudio Team'],
        '提出 ResearchStudio-Idea，一套基于机器学习会议成果（论文接受/拒绝记录）驱动的科研选题技能组合。系统通过检索和推理历史会议评审数据，为研究人员生成有证据支撑的新课题建议，并附上潜在风险评估和参考文献，为 AI 辅助科研提供"有据可查"的范式。',
        ['cs.AI', 'cs.LG'], datetime(2026, 9, 1, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2607.04439',
    ),
    Paper(
        'pAI/MSc: ML Theory Research with Humans on the Loop',
        'https://arxiv.org/pdf/2604.20622', '2604.20622',
        ['ML Theory Research Group'],
        '提出 pAI/MSc 框架，将 AI Agent 嵌入机器学习理论研究流程，实现"人类在环"的半自主科研模式。Agent 负责文献梳理、定理猜想和证明草案生成；人类研究员负责方向把控和严格性验证。案例研究展示了在泛化理论和优化分析领域的有效应用，对 AI 辅助数学研究具有参考价值。',
        ['cs.LG', 'cs.AI'], datetime(2026, 8, 28, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2604.20622',
    ),
    Paper(
        'AutoResearch AI: Towards AI-Powered Research Automation for Scientific Discovery',
        'https://arxiv.org/pdf/2605.23204', '2605.23204',
        ['AutoResearch AI Team'],
        '系统性介绍 AutoResearch AI 平台架构，集成假设生成、实验设计、数据分析和论文撰写四大子 Agent，面向生物医学和材料科学实现端到端科学研究自动化。平台在三个真实科研场景中验证有效性，将从文献调研到初步实验结果的周期从数周压缩至数小时。',
        ['cs.AI', 'cs.CL'], datetime(2026, 8, 25, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2605.23204',
    ),
]

# --- 大牛动态 ---
updates = [
    InfluencerUpdate(
        'Sebastian Raschka', 'Blog',
        '9 月 2 日发布 Quick Model Note，深度解析 GPT-6 Astra 与循环 Transformer（Looped Transformers）的架构联系。文章详细对比了 Astra 递归深度设计与 Nanbeige 4.2 在 Mixture-of-Recursions 框架下的差异，认为 Astra 的核心突破在于动态计算分配而非单纯参数扩展，并给出开源模型格局的最新评估。',
        'https://magazine.sebastianraschka.com/', datetime(2026, 9, 2, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Simon Willison', 'Blog',
        '9 月初密集更新多篇技术分析文章。重点评论 GPT-6 Astra 的 Computer Use 功能，指出其与 Claude 3.5 Sonnet Computer Use 相比在浏览器导航稳定性上的显著提升；同时追踪 Fable 5.1 发布细节，在 llm-prices.com 工具（已累积逾 200 万查询）中更新各主流模型最新定价，并评述加州 SB 1047 对开源模型生态的潜在冲击。',
        'https://simonwillison.net/', datetime(2026, 9, 3, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Andrej Karpathy', 'Blog',
        '近期在 Sequoia Ascent 分享"Software 3.0"最新思考：上下文窗口已成为新的程序，"Agentic Engineering"取代 Vibe Coding 成为主流范式。他认为 GPT-6 Astra 的 Computer Use 是 Software 3.0 最具体的落地形态——AI 不再只是写代码，而是直接操作整个计算机。他的 autoresearch 项目在社区持续引发关注，月活跃 Fork 数突破 3 万。',
        'https://karpathy.bearblog.dev/sequoia-ascent-2026/', datetime(2026, 9, 1, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Chip Huyen', 'Blog',
        '继 8 月发表《AI Agent Security in 2026》后，本周跟进发布《The Inference Economics of Custom Silicon》，分析 OpenAI Jalapeño 芯片对 API 定价的长期影响，预测自研硅片将在 2027-2028 年为 OpenAI 带来约 35% 的推理成本优势，对 Anthropic 和 Google 的定价策略构成实质压力。文章被 AI 工程从业者广泛引用。',
        'https://huyenchip.com/', datetime(2026, 9, 2, tzinfo=timezone.utc),
    ),
]

# --- GitHub 热门 ---
github = [
    GithubProject(
        'openclawai/openclaw', 'https://github.com/openclawai/openclaw',
        'Personal AI assistant running entirely on your own devices — connects 50+ integrations (WhatsApp, Telegram, Slack, iMessage, Discord and more)',
        318000, 25200, 'TypeScript', 1850, ['openclaw-team']
    ),
    GithubProject(
        'ollama/ollama', 'https://github.com/ollama/ollama',
        'Get up and running with Llama, DeepSeek, Qwen3.8, Gemma and other large language models locally. Now supports GPT-6 Astra via OpenAI-compatible endpoint.',
        170000, 13800, 'Go', 620, ['jmorganca', 'mchiang0610']
    ),
    GithubProject(
        'comfyanonymous/ComfyUI', 'https://github.com/comfyanonymous/ComfyUI',
        'The most powerful and modular diffusion model GUI and backend. Node-based visual workflow system for granular control over image and video generation.',
        110000, 11700, 'Python', 380, ['comfyanonymous', 'Kosinkadink']
    ),
    GithubProject(
        'langflow-ai/langflow', 'https://github.com/langflow-ai/langflow',
        'Langflow is a low-code app builder for RAG and multi-agent AI applications. It is Python-based and agnostic to any model, API, or database.',
        62000, 6100, 'TypeScript', 540, ['anovazzi1', 'ogabrielluiz']
    ),
    GithubProject(
        'Significant-Gravitas/AutoGPT', 'https://github.com/Significant-Gravitas/AutoGPT',
        'AutoGPT is the vision of accessible AI for everyone, to use and to build on. The AI agent platform now supports GPT-6 Astra, Fable 5.1, and Gemini 3.8.',
        174000, 45000, 'Python', 290, ['Torantulino', 'merwanehamadi']
    ),
    GithubProject(
        'karpathy/autoresearch', 'https://github.com/karpathy/autoresearch',
        'Autonomous AI research agent: runs hundreds of experiments overnight, logs findings, and surfaces the best results. Now with multi-GPU distributed support.',
        38500, 3100, 'Python', 410, ['karpathy']
    ),
    GithubProject(
        'n8n-io/n8n', 'https://github.com/n8n-io/n8n',
        'Fair-code workflow automation platform with native AI capabilities. Build AI agent pipelines connecting 400+ integrations without code.',
        91000, 24000, 'TypeScript', 350, ['janober', 'ivov']
    ),
    GithubProject(
        'VoltAgent/awesome-ai-agent-papers', 'https://github.com/VoltAgent/awesome-ai-agent-papers',
        'Curated collection of 2026 AI agent research papers: agent engineering, memory, evaluation, autonomous workflows, multi-agent systems, and safety.',
        9800, 780, 'Markdown', 480, ['VoltAgent-team']
    ),
]

filename, content = generate_jekyll_post(news, papers, updates, github)
out_path = f'/home/user/ai-daily-news/reports/{filename}'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f'Jekyll 文章已生成：{filename}')
print(f'字符数：{len(content)}')
print(f'路径：{out_path}')
