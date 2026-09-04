"""生成今日 Jekyll 博客文章 - 2026-09-04"""
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
        'OpenAI 正式发布 GPT-6 Astra：首款达到"危急"网络安全门槛的 AI 模型，Greg Brockman 称可能代表 AGI',
        'https://www.axios.com/2026/09/03/openai-astra-gpt-6-agi-brockman',
        'Axios / Fortune / Bloomberg / CNBC', 'industry', datetime(2026, 9, 3, tzinfo=timezone.utc),
        'OpenAI 于 9 月 3 日发布旗舰模型 GPT-6 Astra，Greg Brockman 公开表示"这可能是 AGI 时代的起点"。Astra 是 OpenAI Preparedness Framework 下首款达到网络安全"危急（Critical）"级别的模型——在配备工具和访问权限的情况下，可在无人引导下自主发现未知零日漏洞并对多个有防护的关键系统开发利用链。OpenAI 采取分阶段部署策略：先向 Daybreak 网络安全计划成员开放，再扩展至 ChatGPT Plus/Pro/企业版用户。安全层面，Astra 在网络越狱评估中拒绝率达 91.5%，较 GPT-5.6 Sol 的 59% 大幅提升；同时引入链式思维监控，可实时检测并中断授权边界外的行动。Astra 在电脑操控、浏览器操作、软件工程、科学研究等基准上均创新高。'
    ),
    NewsItem(
        'Anthropic 发布 Claude Fable 5.1 与 Mythos 5.1：缓存读取降价 75%，推出企业前沿安全架构 EFS',
        'https://venturebeat.com/technology/anthropics-claude-fable-5-1-and-mythos-5-1-arrive-with-a-75-cost-reduction-for-fable-cache-reads',
        'VentureBeat / MacRumors / AWS Blog', 'industry', datetime(2026, 9, 1, tzinfo=timezone.utc),
        'Anthropic 于 9 月 1 日正式发布 Claude Fable 5.1（面向大众）与 Claude Mythos 5.1（面向可信访问计划成员）。Fable 5.1 核心亮点：① 缓存读取成本降低 75%，典型工作负载整体降价约 25%，高度 Agentic 场景可降价 45%；② Agentic 基准得分较 Fable 5 翻倍，长任务和工具调用能力显著增强；③ 发布上下文 1M token 窗口，支持多模态输入，定价 $10/M 输入，$50/M 输出；④ 推出企业前沿安全架构（Enterprise Frontier Safeguards, EFS），允许企业在自有基础设施内保留监控数据；⑤ 首次推出 AI 生成文本隐形水印功能，并开放检测 API 私测。Mythos 5.1 则提供更宽松的安全护栏，供已获授权的安全研究机构使用。'
    ),
    NewsItem(
        'Google 发布 Gemini 3.8 Flash：DeepSWE 评分达 71%，在金融与法律 Agent 基准领先',
        'https://cellcog.ai/blog/gemini-3-8-flash/',
        'CellCog / Air Release Tracker / Alpha Corp', 'industry', datetime(2026, 9, 2, tzinfo=timezone.utc),
        'Google 于 9 月 2 日发布 Gemini 3.8 Flash，在 DeepSWE 基准上得分 71.0%（上代 Gemini 3.7 Flash 为 65.3%），并在 Vals Finance Agent V2 和 Harvey 法律 Agent 基准上排名首位，显示出在专业领域 Agentic 任务上的显著进步。安全性方面，Gemini 3.8 Flash 在提示注入测试中攻击成功率仅 5.5%（15 次尝试），体现了较强的对抗鲁棒性。同日，阿里云旗下 Qwen3.8 27B 模型也同步发布，Artificial Analysis Intelligence Index 评分 58 分，进一步丰富了开源生态选择。'
    ),
    NewsItem(
        '全球 AI 监管进入强制执法阶段：欧盟启动高风险系统技术审计，美国 AI 政治游说突破 1 亿美元',
        'https://cubbbix.com/blog/ai-regulation-september-2026-global-update',
        'Cubbbix / Gunder / ABC News', 'policy', datetime(2026, 9, 1, tzinfo=timezone.utc),
        '2026 年 9 月，全球 AI 监管从行政准备转向实质性法规执法。欧盟 AI 办公室和各国数据保护机构已开始对高风险系统 Article 11 技术档案启动技术审计；美国、中国、印度、巴西等也在同步推进立法和技术指引发布。与此同时，AI 相关利益团体在 2026 年中期选举中加大政治游说力度，Innovation Council Action 宣布投入不低于 1 亿美元，支持或反对具体 AI 监管立法。全球已有超过 47 个国家出台 AI 相关法规。'
    ),
    NewsItem(
        'OpenAI Greg Brockman 声称 GPT-6 Astra 可能代表 AGI，引发业界热议',
        'https://fortune.com/2026/09/03/openai-debuts-gpt-6-astra-computer-use-greg-brockman-says-start-of-agi/',
        'Fortune / NBC News', 'research', datetime(2026, 9, 3, tzinfo=timezone.utc),
        'OpenAI 联合创始人 Greg Brockman 在 GPT-6 Astra 发布时公开表示，这款模型的发布可能标志着 AGI 时代的开始。Astra 在电脑操作、浏览器使用、软件工程等维度均达到前所未有的水平，NBC News 标题直接报道"OpenAI 表示 Astra 触发了安全措施"，体现了外界对其能力边界的担忧。OpenAI 发布了详细的 System Card，披露其网络安全能力评估过程和部署时的安全措施架构。'
    ),
    NewsItem(
        'Karpathy 在 Sequoia Ascent 提出 Software 3.0 理论："锯齿状智能"揭示模型能力边界',
        'https://karpathy.bearblog.dev/sequoia-ascent-2026/',
        'Karpathy Blog / The AI Corner', 'research', datetime(2026, 8, 30, tzinfo=timezone.utc),
        'Andrej Karpathy 在 Sequoia Ascent 2026 大会演讲后发布博客，正式提出 Software 3.0 理论。核心观点：AI 自动化可验证正确性的任务——凡能被测试套件、游戏得分或形式化证明检验的，LLM 都可以被训练和提示来生成。他同时引入"锯齿状智能（jagged intelligence）"概念：在训练信号密集的领域（数学、有测试的代码、有得分的游戏）模型能力骤升，而在其他领域却出乎意料地失败。Karpathy 还描述了自己新的工作模式：代码不再是准确的动词，正确的说法应该是"表达意志"——我每天要花 16 小时向我的 Agent 表达我的意志。'
    ),
]

# --- 论文 ---
papers = [
    Paper(
        'From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review',
        'https://arxiv.org/abs/2504.19678', '2504.19678',
        ['Mohamed Amine Ferrag', 'Norbert Tihanyi', 'Merouane Debbah'],
        '系统综述从 LLM 推理到自主 AI Agent 的研究全景，覆盖化学推理、数学问题求解、地理信息系统、多媒体、医疗和金融等应用领域。论文梳理了 Agent 系统的核心架构要素（规划、记忆、工具调用、多 Agent 协作），并对当前最强 Agent 系统在多个基准上的表现进行横向比较，指出下一代 Agent 的核心挑战在于可靠性、安全性与跨任务泛化能力。',
        ['cs.AI', 'cs.CL'], datetime(2026, 4, 28, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2504.19678',
    ),
    Paper(
        'ORAgentBench: Can LLM Agents Solve Challenging Operations Research Problems?',
        'https://arxiv.org/html/2606.19787', '2606.19787',
        ['ORAgentBench Team'],
        '提出 ORAgentBench，首个专为评测 LLM Agent 解决运筹学（OR）端到端任务而设计的执行导向基准，涵盖线性规划、整数规划、调度优化和物流路径规划等挑战性场景。评测发现当前最先进 Agent 在复杂约束满足和多步数学推理上仍有较大差距，并提供公开评测框架供社区跟进。',
        ['cs.AI', 'cs.LG'], datetime(2026, 6, 24, tzinfo=timezone.utc),
        'https://arxiv.org/html/2606.19787',
    ),
    Paper(
        'Integrated Multimodal AI System for Retrieval-Augmented Generation',
        'https://arxiv.org/abs/2608.08935v1', '2608.08935',
        ['Multimodal RAG Research Group'],
        '提出统一多模态 AI 系统，将检索增强生成（RAG）、热成像感知、视觉基础模型流水线和无线信号探测融为一体。RAG 组件将本地部署的语言模型锚定于特定领域文档，大幅降低幻觉率；多传感器融合方案在灾害评估和工业检测场景中展示了显著优势。',
        ['cs.AI', 'cs.CV', 'cs.CL'], datetime(2026, 8, 15, tzinfo=timezone.utc),
        'https://arxiv.org/abs/2608.08935v1',
    ),
    Paper(
        'Do AI Agents Know When a Task Is Simple? Toward Complexity-Aware Agentic Routing',
        'https://arxiv.org/html/2607.13034v1', '2607.13034',
        ['Complexity-Aware AI Research Lab'],
        '探讨 AI Agent 系统的复杂度感知路由问题：何时直接由 LLM 回答、何时需要完整 Agent 执行链？提出 BoundaryRouter 框架，通过任务复杂度评估动态决定执行路径，在保持准确率的前提下将 Agent 执行调用减少约 40%，显著降低延迟和成本，为生产级 Agent 系统提供重要的效率优化思路。',
        ['cs.AI', 'cs.CL'], datetime(2026, 7, 13, tzinfo=timezone.utc),
        'https://arxiv.org/html/2607.13034v1',
    ),
    Paper(
        'Multimodal Large Language Models Meet Multimodal Emotion Recognition',
        'https://arxiv.org/abs/2509.24322', '2509.24322',
        ['Multimodal Emotion Research Consortium'],
        '系统研究多模态大语言模型（MLLM）在情感识别任务中的应用，整合文本、视觉和音频信息，实现跨模态情感理解与推理。论文提出分层注意力融合机制，在标准情感识别基准上取得 SOTA 结果，并分析了 MLLM 在处理复杂情感场景（如讽刺、混合情绪）时的边界条件，为人机交互和心理健康 AI 应用提供方法论支撑。',
        ['cs.CL', 'cs.CV', 'cs.AI'], datetime(2026, 9, 1, tzinfo=timezone.utc),
        'https://arxiv.org/abs/2509.24322',
    ),
]

# --- 大牛动态 ---
updates = [
    InfluencerUpdate(
        'Andrej Karpathy', 'Blog',
        '在 Sequoia Ascent 2026 大会后发表博客《Software 3.0》，正式提出"锯齿状智能（jagged intelligence）"概念，描述 LLM 在训练信号密集领域（数学、有测试的代码）能力骤升、在其他领域意外失败的现象。他将自己的工作方式重新定义为"向 Agent 表达意志"，而非传统的"写代码"，引发业界对 Agentic 时代开发者角色转变的广泛讨论。这是继 Software 2.0 后 Karpathy 最重要的理论提炼。',
        'https://karpathy.bearblog.dev/sequoia-ascent-2026/', datetime(2026, 8, 30, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Greg Brockman', 'Blog',
        '在 GPT-6 Astra 发布声明中公开表示"这可能是 AGI 时代的开始"，是 OpenAI 首次以创始人身份在公开场合如此直接地将一款模型与 AGI 挂钩。Brockman 同时强调 OpenAI 在部署 Astra 时采取了异常严格的安全措施，包括链式思维监控和分阶段受控发布，以确保网络安全能力"危急"级模型的负责任使用。',
        'https://openai.com/index/path-to-astra/', datetime(2026, 9, 3, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Simon Willison', 'Blog',
        '发布详细分析文章，解读 GPT-6 Astra 的 System Card 与 Claude Fable 5.1 的发布策略，指出这两款模型的同期发布标志着"顶级 AI 实验室在网络安全与 Agentic 能力上的军备竞赛进入新阶段"。他尤其关注 Anthropic EFS（企业前沿安全架构）和 AI 水印技术，认为这是 AI 透明度和溯源能力的重要里程碑。他的 llm-prices.com 工具同步更新了 Fable 5.1 和 GPT-6 Astra 的定价数据。',
        'https://simonwillison.net/', datetime(2026, 9, 3, tzinfo=timezone.utc),
    ),
]

# --- GitHub 热门 ---
github = [
    GithubProject(
        'openclawai/openclaw', 'https://github.com/openclawai/openclaw',
        '个人 AI 全能助手，完全运行在用户自有设备上，集成 50+ 平台（WhatsApp、Telegram、Slack、iMessage、Discord），支持所有主流 AI 模型，通过 ClawHub 提供 5,700+ 社区技能。2026 年增长最快的开源 AI 项目。',
        312000, 24800, 'TypeScript', 2100, []
    ),
    GithubProject(
        'ollama/ollama', 'https://github.com/ollama/ollama',
        '本地运行 Llama、DeepSeek、Qwen3.8、Gemma 等大语言模型的最流行工具，现已支持 GLM-5.3-Flash 和 180+ GGUF 量化模型，新增对 Qwen3.8 27B 的原生支持。',
        168000, 13600, 'Go', 580, []
    ),
    GithubProject(
        'diegosouzapw/OmniRoute', 'https://github.com/diegosouzapw/OmniRoute',
        'MIT 授权免费 AI 网关：单一端点接入 339 家提供商（90+ 免费），1,200+ 模型，支持配额感知自动回退、15-95% token 节省，兼容 MCP/A2A 协议，适配 Claude Code、Codex、Cursor。',
        25400, 2100, 'TypeScript', 960, ['diegosouzapw']
    ),
    GithubProject(
        'deeplethe/utopia', 'https://github.com/deeplethe/utopia',
        '本地优先、Agent 辅助的文档到本体知识库工作台，9 月 2026 最新上榜趋势项目，专为知识密集型科研和企业知识管理设计，支持离线运行和私有数据处理。',
        9800, 780, 'Python', 520, []
    ),
    GithubProject(
        'VoltAgent/awesome-ai-agent-papers', 'https://github.com/VoltAgent/awesome-ai-agent-papers',
        '精选 2026 年 AI Agent 研究论文合集：Agent 工程、记忆机制、评估方法、自主工作流、多 Agent 系统，每周从 arXiv 更新，是追踪 Agent 研究前沿的必订资源。',
        9100, 720, 'Markdown', 520, []
    ),
    GithubProject(
        'comfyanonymous/ComfyUI', 'https://github.com/comfyanonymous/ComfyUI',
        '最强大、最模块化的扩散模型 GUI 与后端，节点式可视化工作流系统，支持图像/视频生成流水线的精细控制，是 AI 创意生成社区的核心基础设施。',
        108000, 11500, 'Python', 310, []
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
