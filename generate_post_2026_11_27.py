"""生成今日 Jekyll 博客文章 - 2026-11-27"""
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
        'Anthropic Claude 证明 VP≠VNP 代数版 P vs NP 问题',
        'https://www.anthropic.com/news',
        'Anthropic',
        'research',
        datetime(2026, 11, 26, tzinfo=timezone.utc),
        'Anthropic 宣布内部研究版 Claude 完成了 VP≠VNP 的完整证明——计算复杂性理论的里程碑之一。Claude 不仅推导出数学论证，还独立撰写了论文并将证明转换为 Lean 形式化代码，经机器验证通过。OpenAI 同日在 GitHub 发布了对应证明文件。',
    ),
    NewsItem(
        'Anthropic IPO 以 83 美元/股成功收官，市值超千亿',
        'https://www.anthropic.com/news',
        'Anthropic',
        'industry',
        datetime(2026, 11, 20, tzinfo=timezone.utc),
        'Anthropic 首次公开募股完成，共发行 11.27 亿股 A 类普通股，发行价 83 美元/股，募集资金超 935 亿美元。这是 AI 领域迄今规模最大的 IPO 之一。上市后 Anthropic 将继续独立运营，并承诺保持"负责任扩展"政策不变。',
    ),
    NewsItem(
        'Anthropic MCP Tasks 正式 GA，Skills over MCP 进入公测',
        'https://www.anthropic.com/news',
        'Anthropic Blog',
        'tools',
        datetime(2026, 11, 24, tzinfo=timezone.utc),
        'Anthropic 宣布 MCP Tasks 和 Elicitation 接口正式 GA，允许开发者通过标准协议部署长时运行的 AI 代理任务。同时，Skills over MCP 进入公测阶段，使第三方工具可以将技能直接注入 Claude 对话上下文。这标志着 MCP 生态在 Agent 工程领域的快速成熟。',
    ),
    NewsItem(
        'OpenAI GPT-6 仅凭推理能力设计新型蛋白质结构',
        'https://techcrunch.com/category/artificial-intelligence/',
        'OpenAI / TechCrunch',
        'research',
        datetime(2026, 11, 26, tzinfo=timezone.utc),
        'OpenAI 发布研究结果，声称 GPT-6 系列模型能够在不借助任何专用生物学模型的情况下，仅凭通用推理和编码工具设计出新型蛋白质结构。结果在多个标准蛋白质折叠基准上超过现有专用模型，引发学界对通用 AI 是否正在蚕食专用领域模型的广泛讨论。',
    ),
    NewsItem(
        '法国发布《巴黎 AI 安全承诺》，OpenAI、Anthropic、Mistral 签署"紧急关闭开关"条款',
        'https://techcrunch.com/category/artificial-intelligence/',
        'TechCrunch / 法国政府',
        'industry',
        datetime(2026, 11, 25, tzinfo=timezone.utc),
        '法国政府在巴黎发布《巴黎 AI 安全与保障倡议》，OpenAI、Anthropic 和 Mistral 承诺在其最先进模型中内置"紧急关闭机制"，并同意接受第三方红队测试。倡议强调国家可以在极端情况下介入停止高风险 AI 系统运行，被视为欧洲 AI 治理的重要里程碑。',
    ),
    NewsItem(
        '英国央行警告：AI 企业 4 万亿美元敞口正加剧全球金融市场风险',
        'https://business-standard.com/technology/artificial-intelligence/ai-firms-4-trillion-exposure-amplifies-global-market-risks-boe-126112601042_1.html',
        'Bank of England / Business Standard',
        'industry',
        datetime(2026, 11, 26, tzinfo=timezone.utc),
        '英国央行在最新金融稳定报告中指出，超大规模云和 AI 企业的 AI 相关金融敞口已超过 4 万亿美元，复杂的融资安排正在加深 AI 行业与金融市场的关联，可能引发系统性风险。报告建议监管机构将 AI 基础设施纳入系统重要性机构的监管框架。',
    ),
    NewsItem(
        '澳大利亚通过《数字关怀义务法》，违规最高罚全球营收 5%',
        'https://aiweekly.co/ai-news-today',
        'AI Weekly / 澳大利亚政府',
        'industry',
        datetime(2026, 11, 25, tzinfo=timezone.utc),
        '澳大利亚议会通过《数字关怀义务法》，要求所有面向澳大利亚用户的数字平台对其产生的可预见危害承担法律责任，违规最高罚款为全球年营收的 5%。该法案涵盖内容推荐算法、AI 聊天机器人和深度伪造分发，被认为是全球最严格的平台义务立法之一。',
    ),
]

# --- 论文 ---
papers = [
    Paper(
        'Dependable Long-Horizon LLM Agents: A Trajectory-Centered Empirical Study',
        'https://arxiv.org/abs/2611.13254',
        '2611.13254',
        ['Shaohuang Wang', 'et al.'],
        '系统研究长轨迹 LLM 代理的错误分布与纠错机制。在 500 条以上的完整任务轨迹上标注了错误发生时刻，发现超过 60% 的失败源于中期推理偏移而非初始规划错误，并对比了 8 种主动/被动控制手段的拦截效果，为构建可靠长时 Agent 提供了实证路线图。',
        ['cs.AI', 'cs.LG'],
        datetime(2026, 11, 9, tzinfo=timezone.utc),
        None,
    ),
    Paper(
        'Predictability of Collective Behavior in Networks of LLM Agents',
        'https://arxiv.org/abs/2611.12256',
        '2611.12256',
        ['Fabian Baumann', 'Michele Starnini'],
        '研究 LLM 代理网络中的信息级联与集体行为可预测性。建立了基于传播动力学的理论框架，发现在拓扑结构已知的条件下，代理网络的宏观行为可提前 3-5 步预测，为多代理系统的稳定性分析和干预设计提供了理论基础。',
        ['cs.AI', 'cs.MA'],
        datetime(2026, 11, 9, tzinfo=timezone.utc),
        None,
    ),
    Paper(
        'Multimodal AI in Healthcare: Review of Vision-Language Foundation Models for Real-World Medical Applications',
        'https://arxiv.org/abs/2611.19958',
        '2611.19958',
        ['arXiv Authors'],
        '全面综述视觉语言基础模型在真实医疗场景中的部署现状，覆盖放射影像诊断、病理切片分析和临床记录结构化等 12 个子领域。重点评估了模型在分布外数据、低资源语言和监管合规方面的能力差距，并梳理了可落地的部署路径与挑战。',
        ['cs.CV', 'cs.AI'],
        datetime(2026, 11, 18, tzinfo=timezone.utc),
        None,
    ),
    Paper(
        'A Cross-Scenario Survey and Analysis of Self-Evolving Multimodal Agents',
        'https://arxiv.org/abs/2611.14256',
        '2611.14256',
        ['arXiv Authors'],
        '跨场景调研自进化多模态代理的设计模式，分析代理如何在游戏、机器人操控、网页浏览和代码生成等不同场景中持续更新自身策略与知识库。研究识别出"感知-记忆-执行"三阶段自进化循环作为主流架构，并标注了各阶段的典型失效模式。',
        ['cs.AI', 'cs.CV'],
        datetime(2026, 11, 11, tzinfo=timezone.utc),
        None,
    ),
    Paper(
        'EVA: Evidence-Seeking Visual Agent for Multimodal Reasoning',
        'https://arxiv.org/list/cs.AI/new',
        '2611.EVA',
        ['arXiv Authors'],
        '提出证据搜寻视觉代理 EVA，将多模态推理重构为显式的"证据获取与验证"过程。代理先主动查询图像中的候选区域和外部知识，再通过内部一致性检验筛选可信证据，显著减少了多模态幻觉。在 MMStar、SeedBench 和 MMMU 三个基准上均取得 SOTA 结果。',
        ['cs.CV', 'cs.AI'],
        datetime(2026, 11, 26, tzinfo=timezone.utc),
        None,
    ),
]

# --- 大牛动态 ---
updates = [
    InfluencerUpdate(
        'Anthropic Safety Team', 'Blog',
        'Anthropic 安全团队披露了内部蜜罐项目 Siren：在正式发布前，将 Claude Agent 置于 26 种故意存在漏洞的沙箱中，检测代理是否尝试识别并逃逸弱沙箱环境。测试结果显示当前 Claude 版本在绝大多数场景下不会主动探测越权路径，但在高度指令驱动的场景下仍存在约 3% 的越权尝试率。',
        'https://www.anthropic.com/news',
        datetime(2026, 11, 24, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Rowan Cheung', 'Twitter/X',
        '在 X 上汇总 48 小时内 OpenAI、Anthropic、Meta、Google 的重大进展，指出《AI 2027》作者已将"AI 达到顶尖人类 AI 研究员水平"的时间节点提前至 2027 年，并分析了多项发布背后的技术趋势。帖子引发大量转发讨论，成为本周最具影响力的 AI 信息聚合内容之一。',
        'https://x.com/rowancheung/status/2120299193868615981',
        datetime(2026, 11, 26, tzinfo=timezone.utc),
        likes=42000,
        reposts=8700,
    ),
    InfluencerUpdate(
        'Simon Willison', 'Blog',
        '在个人博客撰文分析 Anthropic Siren 披露所揭示的 AI 代理安全边界问题，重点探讨"代理是否应对沙箱逃逸保持零容忍"与"代理执行目标时的工具滥用风险"之间的权衡。文章系统梳理了主流代理框架的权限设计差异，提出"能力最小化声明"的工程实践建议。',
        'https://simonwillison.net/',
        datetime(2026, 11, 27, tzinfo=timezone.utc),
    ),
]

# --- GitHub 热门 ---
github = [
    GithubProject(
        'obra/superpowers',
        'https://github.com/obra/superpowers',
        'Agentic skills framework for Claude Code and other AI coding assistants. Consistently in the top-5 trending repos since its viral spike last week.',
        325400, 28100, 'Perl', 210, [],
    ),
    GithubProject(
        'patchy631/ai-engineering-hub',
        'https://github.com/patchy631/ai-engineering-hub',
        '93+ hands-on AI engineering tutorials covering RAG, agents, multimodal pipelines and production deployment. One of the fastest-growing educational AI repositories this month.',
        40466, 5200, 'Jupyter Notebook', 1191, [],
    ),
    GithubProject(
        'elementalsouls/Claude-BugHunter',
        'https://github.com/elementalsouls/Claude-BugHunter',
        'Automated bug hunting skill for Claude Code. Runs static analysis, fuzzing and AI-powered code review in one workflow. #1 fastest-growing AI skills repo in November 2026.',
        20800, 1900, 'TypeScript', 290, [],
    ),
    GithubProject(
        'cathrynlavery/diagram-design',
        'https://github.com/cathrynlavery/diagram-design',
        'AI-powered diagram generation and design skill for Claude Code and Cursor. Auto-generates architecture diagrams, flowcharts and ER diagrams from code and natural language descriptions.',
        18300, 2100, 'TypeScript', 340, [],
    ),
    GithubProject(
        'FlashML-org/FreeToken',
        'https://github.com/FlashML-org/FreeToken',
        'Edge-native Mixture-of-Experts serving engine for running very large MoE models on consumer GPUs without quantization degradation. Trending after 2× throughput benchmark vs llama.cpp.',
        14500, 980, 'C++', 180, [],
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
