"""生成今日 Jekyll 博客文章 - 2026-11-28"""
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
        'Anthropic 用 Claude Agent 将 Messages API 从 Python 迁移至 Rust',
        'https://www.anthropic.com/news',
        'Anthropic Blog',
        'tools',
        datetime(2026, 11, 27, tzinfo=timezone.utc),
        'Anthropic 发布了 Messages API Python→Rust 迁移事后报告，整个迁移工作由内部 Claude Agent 主导完成。迁移后服务 CPU 和内存使用率显著下降，响应延迟降低，高并发下的稳定性大幅提升。这是 Anthropic 迄今最大规模的由 AI Agent 驱动的基础设施变更。',
    ),
    NewsItem(
        'OpenAI 修复 GPT-6.2 用量统计漏洞，用户实际消耗比显示值更高',
        'https://techcrunch.com/category/artificial-intelligence/',
        'OpenAI / TechCrunch',
        'industry',
        datetime(2026, 11, 27, tzinfo=timezone.utc),
        'OpenAI 确认修复了 GPT-6.2 中存在的用量计数 Bug，该漏洞导致前端显示的 Token 消耗低于实际用量，部分用户因此比预期更早触达速率限制。受影响用户可申请补偿额度，OpenAI 表示已在所有区域完成修复。',
    ),
    NewsItem(
        'Google Cogentic：多 Agent 框架在 5 个开放数学问题上取得全新结果',
        'https://deeplearn.org/arxiv/836084/cogentic:-multi-agent-orchestration-for-automated-proof-discovery',
        'Google Research / DeepMind',
        'research',
        datetime(2026, 11, 25, tzinfo=timezone.utc),
        'Google Research 发布 Cogentic，一个基于 Gemini 的多代理证明发现框架，在在线学习、拍卖理论和机制设计领域的 5 个长期悬而未决的开放问题上给出了新结果，并由领域专家独立验证。系统通过证明者、对抗验证者、文献综述者和论文写作者等角色分工协作，大多数问题在约 100 次 Gemini 调用内完成。',
    ),
    NewsItem(
        'Scott Aaronson：关于 AI 破解 RSA 加密的传言无法证实',
        'https://scottaaronson.blog/',
        'Scott Aaronson / Blog',
        'research',
        datetime(2026, 11, 24, tzinfo=timezone.utc),
        'Scott Aaronson 在其博客撰文，就近期网络上流传的"OpenAI 或 Anthropic 已实现大整数分解突破"的传言进行辟谣。他表示尚未见到任何技术证据，并解释了即使 AI 能辅助数学证明，克服量子优势所需的技术壁垒依然极高。传言引发了社区对密码学安全的广泛关注。',
    ),
    NewsItem(
        'Anthropic 发布 Claude Ship Beta：三款 GitHub 专属代理正式上线',
        'https://www.anthropic.com/news',
        'Anthropic',
        'tools',
        datetime(2026, 11, 23, tzinfo=timezone.utc),
        'Anthropic 推出 Claude Ship，包含三个面向 GitHub Team 和 Enterprise 客户的 Beta 代理：PR Review Agent（自动审查 PR）、Issue Triage Agent（自动分类 Issue）和 Docs Sync Agent（同步代码注释与文档）。所有代理均通过 MCP 接口运行，支持自定义规则配置。',
    ),
    NewsItem(
        '英国央行发布金融稳定报告：AI 企业 4 万亿美元敞口加剧系统性风险',
        'https://business-standard.com/technology/artificial-intelligence/ai-firms-4-trillion-exposure-amplifies-global-market-risks-boe-126112601042_1.html',
        'Bank of England / Business Standard',
        'industry',
        datetime(2026, 11, 26, tzinfo=timezone.utc),
        '英国央行在最新金融稳定报告中警示，超大规模云和 AI 企业的 AI 相关金融敞口已超过 4 万亿美元，复杂融资安排正在加深 AI 行业与金融市场的关联，可能引发系统性风险。报告建议将 AI 基础设施纳入系统重要性机构的监管框架。',
    ),
]

# --- 论文 ---
papers = [
    Paper(
        'Potential Emergence in LLM Agents: A Statistical Physics Perspective',
        'https://arxiv.org/abs/2611.27618',
        '2611.27618',
        ['arXiv Authors'],
        '从统计物理视角研究 LLM 代理网络中的涌现行为，将代理集体决策过程类比为自旋玻璃模型中的相变现象。通过建立量化涌现强度的指标，发现当代理数量超过临界阈值时，系统会出现宏观行为的突变。为多代理系统设计提供了预测涌现的理论工具。',
        ['cs.AI', 'cs.MA'],
        datetime(2026, 11, 20, tzinfo=timezone.utc),
        None,
    ),
    Paper(
        'Cogentic: Multi-Agent Orchestration for Automated Proof Discovery',
        'https://arxiv.org/abs/2609.40324',
        '2609.40324',
        ['Yang Cai', 'Vineet Gupta', 'Yanchen Jiang', 'Christopher Liaw', 'Aranyak Mehta', 'Grigoris Velegkas', 'Di Wang'],
        'Google Research 提出 Cogentic，一套基于 Gemini 的多代理数学证明发现框架。系统将证明过程分解为证明者、对抗验证者、策略协调者、文献综述者和论文写作者五种角色，通过持久化验证账本保存中间结果。在在线学习、拍卖理论等领域解决了 5 个开放问题，每个问题平均约 100 次大模型调用。',
        ['cs.LG', 'cs.AI'],
        datetime(2026, 9, 30, tzinfo=timezone.utc),
        None,
    ),
    Paper(
        'Dependable Long-Horizon LLM Agents: A Trajectory-Centered Empirical Study',
        'https://arxiv.org/abs/2611.13254',
        '2611.13254',
        ['Shaohuang Wang', 'et al.'],
        '在 500 条以上的完整任务轨迹上标注错误发生时刻，发现超过 60% 的失败源于中期推理偏移而非初始规划错误。在已失败的轨迹中，88% 的案例轨迹中早已出现了对错误判断的反驳证据，但代理未能利用。对比了 8 种主动/被动控制手段的拦截效果，为构建可靠长时 Agent 提供了实证路线图。',
        ['cs.AI', 'cs.LG'],
        datetime(2026, 11, 9, tzinfo=timezone.utc),
        None,
    ),
    Paper(
        'Phantom Consensus: Measuring Social Reasoning in Multi-Agent LLM Decision-Making',
        'https://arxiv.org/list/cs.MA/current',
        '2611.phantom',
        ['NeurIPS 2026 Authors'],
        '被 NeurIPS 2026 收录。研究多代理 LLM 系统中的"幽灵共识"现象：即使实际分歧明显，代理之间会形成虚假的一致性表象。通过构建社会推理基准测试，发现主流 LLM 代理在社会推理任务上的准确率比人类低约 30%，并提出了基于异议激励的改进方案。',
        ['cs.MA', 'cs.AI'],
        datetime(2026, 11, 15, tzinfo=timezone.utc),
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
]

# --- 大牛动态 ---
updates = [
    InfluencerUpdate(
        'Scott Aaronson', 'Blog',
        '在个人博客详细分析了近期网络流传的"AI 破解 RSA"传言，从理论计算复杂性角度阐明：即使 LLM 能辅助生成数学证明，其对整数分解问题的帮助仍受制于已知的量子优势门槛。文章梳理了 Shor 算法与当前 AI 推理能力之间的本质差异，呼吁公众理性看待 AI 能力边界。',
        'https://scottaaronson.blog/',
        datetime(2026, 11, 24, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Sabafish38 (gifted_snail5503)', 'Blog',
        '在 Note.com 发布每日 AI 要闻梳理，重点解析 Google Cogentic 框架与 OpenAI/Anthropic 在数学证明领域的最新进展，并分析了美中 AI 新监管措施对反蒸馏条款的影响。同时关注了 27B 参数 5.9GB 模型的发布对本地部署生态的意义。',
        'https://note.com/gifted_snail5503/n/nc7287a0edefc',
        datetime(2026, 11, 27, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Simon Willison', 'Blog',
        '撰文分析 Anthropic 将 Messages API 从 Python 迁移到 Rust 的事后报告，聚焦"AI Agent 主导基础设施变更"的工程实践意义。认为这代表了 AI 辅助软件工程的新里程碑，同时指出此类迁移需要的测试覆盖密度和人类监督机制仍是工程挑战的核心。',
        'https://simonwillison.net/',
        datetime(2026, 11, 28, tzinfo=timezone.utc),
    ),
]

# --- GitHub 热门 ---
github = [
    GithubProject(
        'obra/superpowers',
        'https://github.com/obra/superpowers',
        'Agentic skills framework for Claude Code and other AI coding assistants. Consistently in the top-5 trending repos since its viral spike last week.',
        328000, 28500, 'Perl', 180, [],
    ),
    GithubProject(
        'patchy631/ai-engineering-hub',
        'https://github.com/patchy631/ai-engineering-hub',
        '93+ hands-on AI engineering tutorials covering RAG, agents, multimodal pipelines and production deployment. One of the fastest-growing educational AI repositories this month.',
        40466, 5200, 'Jupyter Notebook', 95, [],
    ),
    GithubProject(
        'debpalash/VoiceStudio',
        'https://github.com/debpalash/VoiceStudio',
        'Real-time voice AI platform for speech synthesis, voice cloning, and streaming TTS. Leads the AI Voice category with the highest star growth this month.',
        118400, 9800, 'Python', 599, [],
    ),
    GithubProject(
        'elementalsouls/Claude-BugHunter',
        'https://github.com/elementalsouls/Claude-BugHunter',
        'Automated bug hunting skill for Claude Code. Runs static analysis, fuzzing and AI-powered code review in one workflow. #1 fastest-growing AI skills repo in November 2026.',
        20800, 1900, 'TypeScript', 290, [],
    ),
    GithubProject(
        'thedotmack/claude-mem',
        'https://github.com/thedotmack/claude-mem',
        'Persistent memory layer for Claude Code agents. Captures session activity, compresses with AI, and injects relevant context into future sessions automatically.',
        12300, 980, 'TypeScript', 210, [],
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
print(f'输出路径：{out_path}')
