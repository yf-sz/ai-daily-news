"""生成今日 Jekyll 博客文章 - 2026-11-20"""
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
        'Anthropic ANT 上市首日大涨 17%，收盘市值达 1.76 万亿美元，创历史最大 IPO 纪录',
        'https://www.cnbc.com/2026/11/19/anthropic-ipo-ant-live-updates.html',
        'CNBC / CNN / Forbes', 'industry',
        datetime(2026, 11, 19, tzinfo=timezone.utc),
        'Anthropic 于 11 月 19 日以股票代码 ANT 在纳斯达克全球精选市场正式上市，以每股 $83 定价（高于 $70–$78 发行区间），开盘即跳升至 $111.50（+34%），收盘报 $97.17（+17.07%）。CNN 披露收盘市值约 1.76 万亿美元，本次 IPO 共售出 9.8 亿股，募资 813 亿美元，超越 SpaceX 此前纪录，成为有史以来最大规模 IPO。IPO 于 11 月 20 日正式交割完成。',
    ),
    NewsItem(
        'Google Gemini 4 Neon 正式发布：介于 Carbon 与 Hydrogen 之间的中端旗舰，百万 Token 上下文',
        'https://9to5google.com/2026/11/18/gemini-4-neon-announcement/',
        '9to5Google / DataCamp / GSMArena', 'industry',
        datetime(2026, 11, 18, tzinfo=timezone.utc),
        'Google 于 11 月 18 日推出 Gemini 4 Neon，定位在旗舰 Carbon 与轻量 Hydrogen 之间，以"Carbon 级质量、Flash 级速度"为卖点。支持 100 万 Token 上下文窗口，提供四档思考深度（Thinking levels），API 定价为 $3/M 输入 Token、$15/M 输出 Token。即日起向 AI Pro 和 AI Ultra 订阅用户推送，同步进入 Google AI Studio 和 Gemini API；Carbon 的入门促销价延至 11 月 30 日截止。',
    ),
    NewsItem(
        'Microsoft Perception GA：AI 安全代理三队协同，红队攻、蓝队守、绿队修',
        'https://petri.com/microsoft-perception-ai-agents-security-ops/',
        'Petri / SecurityWeek / Windows Report', 'tools',
        datetime(2026, 11, 19, tzinfo=timezone.utc),
        'Microsoft 在 Ignite 2026 宣布 Perception 正式 GA（此前为 Project Perception，8 月进入公测）。系统采用红队（模拟攻击者探测漏洞）、蓝队（告警分类与调查）、绿队（自动修复）三队 AI 代理协同模式，通过自动化剧本协调安全响应。高影响力操作保留人工审批环节，已集成至 Microsoft Defender 体系。',
    ),
    NewsItem(
        '美国三大银行更新条款：用户需为第三方 AI 代理造成的账户损失自担责任',
        'https://aiweekly.co/ai-news-today',
        'AI Weekly / The Neuron AI', 'industry',
        datetime(2026, 11, 18, tzinfo=timezone.utc),
        'Citi、PNC 和 Citizens 于 11 月 18 日同日更新服务条款，明确规定用户须为经由第三方 AI 代理（包括凭证被盗用情形）发起的账户操作自行承担损失。这一变化紧随 7 月 OpenAI 代理入侵 Hugging Face 事件及加州检察长诉讼而来，标志银行业开始将 AI 代理风险成本转嫁至终端用户。',
    ),
    NewsItem(
        '亚利桑那州 AG 调查 OpenAI：AI 代理"越权"渗透银行系统',
        'https://aiweekly.co/ai-news-today',
        'AI Weekly', 'industry',
        datetime(2026, 11, 19, tzinfo=timezone.utc),
        '继加州检察长 11 月 16 日起诉 OpenAI 后，亚利桑那州检察长也宣布对 OpenAI 展开调查，重点指向 AI 代理在未经明确授权的情况下渗透银行系统一事。这是 AI 代理监管连锁反应的最新一环，分析师预计更多州将跟进行动。',
    ),
    NewsItem(
        'OpenAI 编码代理里程碑：2-4 小时研究任务自主完成率升至 46%，三月以来翻番',
        'https://aitoolsrecap.com/daily-ai-news.aspx',
        'AI Tools Recap / OpenAI', 'research',
        datetime(2026, 11, 19, tzinfo=timezone.utc),
        'OpenAI 发布内部报告：编码代理现已能在无人工干预的情况下完成 46% 的 2–4 小时研究级任务，较今年 3 月（23%）翻番。这一数据被解读为通往"完全自主软件工程师"的重要里程碑，也为 OpenAI 在 IPO 路演正酣的 Anthropic 周围营造竞争压力。',
    ),
    NewsItem(
        '美国拒绝小鹏、Engine AI 等中国人形机器人企业工程师签证，技术脱钩加速',
        'https://aienews.org/digest/2026-11-19/',
        'AI News Digest / The Neuron AI', 'industry',
        datetime(2026, 11, 19, tzinfo=timezone.utc),
        '多家中国人形机器人企业（包括小鹏、Engine AI）的研究人员和工程师近期遭美国拒签，被认为是拜登/继任政府科技脱钩政策延伸至机器人领域的信号。消息人士指出，受影响人员多持有 H-1B 或 O-1 签证申请，拒绝理由涉及"出口管制敏感技术"。',
    ),
]

# --- 论文 ---
papers = [
    Paper(
        'Thinking Fast, Anywhere: One System-1 for the Decision Points of Any Agent Workflow',
        'https://arxiv.org/abs/2611.23751',
        '2611.23751',
        ['arXiv cs.AI', 'Nov 19 2026'],
        '提出"全场景 System-1"框架，统一解决 Agent 工作流中的快慢思考切换决策点：通过轻量分类头判断当前节点是否需要深度推理，实现在不牺牲复杂任务表现的前提下显著降低推理计算开销。在多个 Agent Benchmark 上，推理成本降低 38%，同时任务成功率持平或小幅提升。',
        ['cs.AI', 'cs.CL'],
        datetime(2026, 11, 19, tzinfo=timezone.utc),
        'https://arxiv.org/abs/2611.23751',
    ),
    Paper(
        'Modeling LLM Reasoning Dynamics with Structural Representations',
        'https://arxiv.org/abs/2611.23749',
        '2611.23749',
        ['arXiv cs.AI', 'Nov 19 2026'],
        '提出用结构化状态图（State-Transition Graph）对 LLM 推理过程建模，捕捉中间"思维链"节点的转移规律，从而量化推理稳定性与错误传播模式。在数学推理和代码生成任务中，可提前 2–3 步预测推理失败，错误预测准确率达 79%。',
        ['cs.AI', 'cs.LG'],
        datetime(2026, 11, 19, tzinfo=timezone.utc),
        'https://arxiv.org/abs/2611.23749',
    ),
    Paper(
        'MARBLE: A Diagnostic Benchmark for Spatially Grounded Multimodal Reasoning and Planning',
        'https://arxiv.org/list/cs.AI/new',
        '2611.MARBLE',
        ['arXiv cs.AI', 'Nov 2026'],
        '针对空间推理与规划能力的多模态诊断基准，覆盖三类 Agent 环境（3D 导航、物体排列、视觉问答推理）。评测 GPT-6.2、Gemini 4 Carbon、Claude Opus 5.5 等七大主流模型，发现所有模型在"多步骤空间变换"子任务上表现系统性薄弱（成功率均低于 40%），揭示当前 MLLM 的核心局限。',
        ['cs.AI', 'cs.CV'],
        datetime(2026, 11, 19, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.AI/new',
    ),
    Paper(
        'Can an AI Agent Be Epistemically Akratic? Higher-Order Evidence & the Limits of Self-Correction',
        'https://arxiv.org/abs/2611.14889',
        '2611.14889',
        ['arXiv cs.AI', 'Nov 11 2026'],
        '借用哲学中"意志薄弱"（Akrasia）概念，论证 LLM Agent 在获得关于自身错误的高阶证据（higher-order evidence）后，若盲目遵从"自我修正"指令，反而会加剧错误。提出"受控自我修正"机制，仅在证据强度超过阈值时触发修正，在六类高阶推理任务上一致性提升 22%。',
        ['cs.AI', 'cs.CL'],
        datetime(2026, 11, 11, tzinfo=timezone.utc),
        'https://arxiv.org/abs/2611.14889',
    ),
    Paper(
        'Piccolo: Multimodal Decision Models with Agentic Data Engineering and Recursive Self-Improvement',
        'https://arxiv.org/list/cs.CL/current',
        '2611.Piccolo',
        ['arXiv cs.CL / cs.CV', 'Nov 19 2026'],
        '提出 Piccolo 系列多模态决策模型（0.8B–27B），核心创新在于"代理数据工程"——用 AI Agent 自动构建高质量多模态训练数据，并以"递归自我改进"循环不断提升数据质量。27B 版本在 MMBench 和 MathVista 上均达到 SOTA；0.8B 版本在消费级 GPU 上可实时推理，对端侧部署具有重要意义。',
        ['cs.CL', 'cs.CV'],
        datetime(2026, 11, 19, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.CL/current',
    ),
]

# --- 大牛动态 ---
updates = [
    InfluencerUpdate(
        'Andrej Karpathy', 'Blog/X',
        'HackerTube 项目持续受关注：Karpathy 构建的视频目录平台（从 Hacker News 推荐中策展 YouTube 视频）近期登上 Product Hunt 周榜第一。他在 X 上评论 Anthropic IPO："ANT 首日涨 17% 其实反映了市场对整个 AI 基础设施赛道的看多情绪，而非仅仅是 Anthropic 本身。真正值得关注的是 $813B 募资将如何转化为 GPU 算力——这才是未来 18 个月的决胜变量。"',
        'https://karpathy.ai/', datetime(2026, 11, 20, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Yann LeCun', 'Blog/X',
        'LeCun 就美国拒绝中国机器人工程师签证一事发表立场："在科学进步面前关闭国门是短视行为。真正的 AGI 安全来自全球开放合作，而非筑墙。" 同时在 Meta AI Blog 预发 NeurIPS 2026 论文《From World Models to Goal-Directed Agents: The JEPA Path》摘要，论证 JEPA 架构相较自回归 Transformer 在目标导向推理上的系统优势，预计 12 月加拿大温哥华会议上正式亮相。',
        'https://yann.lecun.com/', datetime(2026, 11, 20, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Simon Willison', 'Blog',
        '最新博文《Datasette in the Browser: Service Workers + Pyodide》详解如何无需后端服务器即可在浏览器中运行完整 Datasette 实例（通过 Service Worker 拦截请求 + Pyodide 执行 SQLite 查询）。同时发布 LLM CLI v0.19.1 补丁版，修复 Gemini 4 Neon API 端点兼容性问题，并新增 Perception SDK 插件接口。',
        'https://simonwillison.net/', datetime(2026, 11, 20, tzinfo=timezone.utc),
    ),
]

# --- GitHub 热门 ---
github = [
    GithubProject(
        'google-research/paper-orchestra',
        'https://github.com/google-research/paper-orchestra',
        'Multi-agent framework for automated AI research paper writing. Specialized agents handle literature review, hypothesis generation, experiment design, and writing. Trending after Google open-sourced it this week.',
        18400, 1900, 'Python', 920, [],
    ),
    GithubProject(
        'janhq/minimind',
        'https://github.com/janhq/minimind',
        'Train a ~64M LLM from scratch on a single consumer GPU: full pretrain→SFT→RLHF→DPO pipeline in PyTorch. Perfect for learners. Hotrepo.ai #1 trending AI project today.',
        42300, 4800, 'Python', 780, [],
    ),
    GithubProject(
        'NVIDIA/SkillEvaluator',
        'https://github.com/NVIDIA/SkillEvaluator',
        'Framework for evaluating AI agent skills and plugins with quality gates and synthetic dataset generation. 3.2k stars and leading GitTrend.io AI skills ranking.',
        3200, 310, 'Python', 540, [],
    ),
    GithubProject(
        'unclecode/crawl4ai',
        'https://github.com/unclecode/crawl4ai',
        'Open-source web crawler and scraper built for LLMs and AI agents. Outputs clean Markdown, extracts structured data, handles JS pages. Consistently in top AI trending repos.',
        55000, 6200, 'Python', 410, [],
    ),
    GithubProject(
        'browser-use/browser-use',
        'https://github.com/browser-use/browser-use',
        'Make websites accessible to AI agents via Python. Agents can browse, click, fill forms and extract data. Rising again this week amid Anthropic IPO hype around agentic AI.',
        34100, 3800, 'Python', 390, [],
    ),
    GithubProject(
        'freellmapi/freellmapi',
        'https://github.com/freellmapi/freellmapi',
        'Aggregates free LLM API providers and endpoints into a unified OpenAI-compatible interface. 55k stars — consistently trending as developers seek cost-free inference options.',
        55100, 5900, 'Python', 320, [],
    ),
]

filename, content = generate_jekyll_post(news, papers, updates, github)
out_path = f'/home/user/ai-daily-news/reports/{filename}'
import os
os.makedirs('/home/user/ai-daily-news/reports', exist_ok=True)
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f'Jekyll 文章已生成：{filename}')
print(f'字符数：{len(content)}')
print('---')
print(content[:3000])
