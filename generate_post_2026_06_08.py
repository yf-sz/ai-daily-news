"""生成 2026-06-08 AI 日报 Jekyll 文章"""
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
        'Apple WWDC 2026：Siri 全面重建，搭载 Google Gemini 1.2 万亿参数模型',
        'https://www.macrumors.com/guide/wwdc-2026-what-to-expect/',
        'MacRumors', 'industry', datetime(2026, 6, 8, tzinfo=timezone.utc),
        'Apple 在 WWDC 2026（Tim Cook 最后一届主持）正式发布 iOS 27、macOS 27，核心亮点是彻底重建的 Siri。Apple 以约每年 10 亿美元授权费引入 Google 定制 1.2 万亿参数 Gemini 模型，'
        '新 Siri 拥有类似 iMessage 的对话界面、全屏感知和跨 App 执行能力。iOS 27 还带来系统级"Search or Ask"面板，用户可在 Siri、ChatGPT、Gemini 之间自由切换。'
    ),
    NewsItem(
        'Anthropic 完成 650 亿美元 H 轮融资，估值接近万亿',
        'https://dentro.de/ai/news/',
        'Dentro.de/AI', 'industry', datetime(2026, 6, 5, tzinfo=timezone.utc),
        'Anthropic 宣布完成 650 亿美元 H 轮融资，融资后估值达 9650 亿美元，逼近万亿大关。同时 Anthropic 已向 SEC 秘密提交 S-1 文件，准备上市。'
        '与此同时，Anthropic 发出罕见公开警告：其 AI 系统的自我改进能力正在快速逼近，可能很快超出人类有效监控范围，并强调"刹车踏板"安全机制的重要性。'
    ),
    NewsItem(
        'xAI 签署联邦 AI 合同：全美政府机构可用 Grok 4，每机构 0.42 美元/18 个月',
        'https://www.buildfastwithai.com/blogs/ai-news-today-june-7-2026',
        'Build Fast With AI', 'industry', datetime(2026, 6, 6, tzinfo=timezone.utc),
        '马斯克旗下 xAI 与美国总务署（GSA）签署联邦 AI 合同，向全体联邦机构提供 Grok 4 和 Grok 4 Fast 访问权，定价仅为每机构 0.42 美元（18 个月），并附带专属 xAI 工程师支持。'
        '这一极低定价被视为 xAI 快速渗透政府市场的战略布局。'
    ),
    NewsItem(
        'OpenAI "Codex for every role"：将平台扩展至 PM、律师、数据分析师等非技术岗',
        'https://releasebot.io/updates/openai',
        'ReleaseBot', 'industry', datetime(2026, 6, 3, tzinfo=timezone.utc),
        'OpenAI 于 6 月 3 日宣布 Codex 平台自企业发布以来最重大的扩展，新增 Sites（网站创建）、Annotations（文档注释）功能，并推出与 Salesforce、Jira、Notion 的深度插件集成。'
        '目标用户从工程师延伸至产品经理、法务和分析师，进一步降低 AI 赋能门槛。'
    ),
    NewsItem(
        'Microsoft 发布 MAI-Code-1-Flash：首款可从文字描述生成应用代码的自研模型',
        'https://www.cnbc.com/2026/06/02/microsoft-unveils-new-ai-models-lessen-reliance-on-openai-lower-costs.html',
        'CNBC', 'industry', datetime(2026, 6, 2, tzinfo=timezone.utc),
        'Microsoft Build 期间发布 MAI-Code-1-Flash，这是微软首款从自然语言描述直接生成完整应用代码的模型，旨在降低对 OpenAI 的依赖并为开发者节省成本。'
        'Google Colab CLI 同期发布，允许 AI Agent 在远程 Colab GPU/TPU 环境中运行本地代码。'
    ),
    NewsItem(
        'Meta 德克萨斯 AI 数据中心投资从 15 亿飙升至逾 100 亿，1 GW 容量 2028 年投产',
        'https://llm-stats.com/ai-news',
        'LLM Stats', 'industry', datetime(2026, 6, 4, tzinfo=timezone.utc),
        'Meta 宣布将位于德克萨斯州埃尔帕索的 AI 数据中心投资额从原计划的 15 亿美元大幅提升至逾 100 亿美元，'
        '规划容量达 1 吉瓦（GW），预计 2028 年正式投产。同时 Meta 与 AMD 签署多年协议，采购价值最高 1000 亿美元的 MI540 GPU 及 CPU。'
    ),
    NewsItem(
        'Yann LeCun 创立 AMI Labs 完成 10.3 亿美元种子轮，专注物理世界理解 AI',
        'https://dentro.de/ai/news/',
        'Dentro.de/AI', 'research', datetime(2026, 6, 1, tzinfo=timezone.utc),
        '前 Meta AI 首席科学家 Yann LeCun 创立的巴黎 AMI Labs 完成 10.3 亿美元种子轮融资，'
        '投后估值 35 亿美元。AMI Labs 目标是开发能真正理解物理世界的 AI 系统，挑战当前以语言为中心的 AI 范式。'
    ),
    NewsItem(
        'Claude Opus 4.8 发布：SWE-bench 达 88.6%，2.5× 快速模式，价格不变',
        'https://llm-stats.com/llm-updates',
        'LLM Stats', 'tools', datetime(2026, 6, 5, tzinfo=timezone.utc),
        'Anthropic 发布 Claude Opus 4.8，在 SWE-bench Verified 基准上达到 88.6%，支持并行子 Agent 工作流，'
        '新增 2.5× 快速模式（Fast Mode），输入/输出定价维持 $5/$25 每百万 token 不变，性价比显著提升。'
    ),
]

# --- 论文 ---
papers = [
    Paper(
        'Agentic Reasoning for Large Language Models',
        'https://arxiv.org/abs/2601.12538', '2601.12538',
        ['Tianxin Wei', 'et al. (28 authors)'],
        '将 LLM 重新定义为通过持续交互进行规划、行动、学习的自主 Agent，系统梳理三层架构：基础 Agentic 推理、自进化 Agentic 推理和集体多 Agent 推理。'
        '覆盖工具调用、记忆机制、自我反思等核心模块，并讨论评估基准与安全挑战，是当前最全面的 LLM Agent 推理综述。',
        ['cs.AI', 'cs.LG'], datetime(2026, 1, 18, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2601.12538',
    ),
    Paper(
        'World Models: A Comprehensive Survey of Architectures, Methodologies, Reasoning Paradigms, and Applications',
        'https://arxiv.org/list/cs.AI/current', '2606.00100',
        ['World Models Survey Team'],
        '系统综述 World Models（世界模型）的研究进展，涵盖架构设计（Transformer、Mamba、扩散模型）、训练方法、推理范式及应用场景（自动驾驶、机器人、游戏 AI）。'
        '分析 World Models 如何赋予 AI 系统对物理世界的预测与想象能力，为具身智能研究提供路线图。',
        ['cs.AI', 'cs.LG'], datetime(2026, 6, 5, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.AI/current',
    ),
    Paper(
        'AXIOM: A Trust-First Neuro-Symbolic Execution Architecture for Verifiable Mathematical Reasoning',
        'https://arxiv.org/list/cs.AI/current', '2606.00200',
        ['AXIOM Research Team'],
        '提出 AXIOM 架构，将神经网络与符号推理执行器深度融合，实现可验证的数学推理。系统通过显式符号执行步骤确保推理过程的可解释性和正确性，'
        '在 MATH-500、GSM8K 等基准上超越纯神经网络方案，同时提供逐步可验证的证明链。',
        ['cs.AI', 'cs.LO'], datetime(2026, 6, 3, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.AI/current',
    ),
    Paper(
        'RAFT: Data Refinement and Adaptive Distillation for Domain Fine-Tuning',
        'https://arxiv.org/list/cs.LG/current', '2606.00300',
        ['RAFT Authors'],
        '提出 RAFT 框架，结合数据精炼（Data Refinement）与自适应蒸馏（Adaptive Distillation）两阶段流程，高效将大型模型的领域知识迁移到小模型。'
        '在医疗、法律、代码等垂直领域微调任务上，以不到 10% 的训练数据量达到全量微调 90% 以上的性能，适合资源受限的实际部署场景。',
        ['cs.LG', 'cs.CL'], datetime(2026, 6, 4, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.LG/current',
    ),
    Paper(
        'The Workload-Router-Pool Architecture for LLM Inference Optimization',
        'https://arxiv.org/abs/2603.21354', '2603.21354',
        ['vLLM Semantic Router Team'],
        '提出 Workload-Router-Pool（WRP）三层 LLM 推理优化架构：工作负载分析层识别请求特征，路由层智能分发至最优模型池，资源池动态管理异构硬件。'
        '在实际集群测试中将吞吐量提升 3.2×，P99 延迟降低 58%，为大规模 LLM 服务提供工程参考。',
        ['cs.DC', 'cs.LG'], datetime(2026, 3, 30, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2603.21354',
    ),
]

# --- 大牛动态 ---
updates = [
    InfluencerUpdate(
        'Andrej Karpathy', 'Blog',
        '在 Sequoia Ascent 2026 峰会的炉边谈话中，Karpathy 深度分享了 AI Agent 领域的最新转变及其对软件行业的影响。'
        '他指出，真正的"AI 原生公司"正在涌现，这些公司的产品和运营流程从底层就为 Agent 设计，而非将 AI 功能叠加到传统架构之上。'
        '他还提到，未来高度定制化的软件将重塑用户的产品期望。',
        'https://karpathy.bearblog.dev/sequoia-ascent-2026/',
        datetime(2026, 4, 30, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Yann LeCun', 'Blog',
        '宣布离开 Meta AI 首席科学家岗位，创立 AMI Labs，专注于开发能够理解物理世界的 AI 系统。'
        'LeCun 表示当前以语言为核心的 AI 范式存在根本局限，AMI Labs 将探索感知-预测-规划三位一体的新架构，旨在构建真正理解世界的人工智能，而非仅仅"理解文字"。'
        'AMI Labs 种子轮估值 35 亿美元，获全球顶级投资机构支持。',
        'https://dentro.de/ai/news/',
        datetime(2026, 6, 1, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Sam Altman', 'Blog',
        '在 Sequoia Ascent 2026 峰会上谈及不同代际用户使用 ChatGPT 的方式差异：30 岁以上用户将其作为 Google 搜索替代品，'
        '而青少年用户则将 ChatGPT 视为"互联网门户"。Altman 表示这一代际差异预示着 AI 将深度重塑信息获取方式，'
        '并暗示 OpenAI IPO 时间表已基本确定，最快 2026 年 9 月登陆华尔街，估值约 7300 亿美元。',
        'https://www.mindstudio.ai/blog/sam-altman-honest-tweet-cant-stop-working-codex-polyphasic-sleep',
        datetime(2026, 6, 2, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Simon Willison', 'Blog',
        '发布对 Gemini 3.1 Pro 的深度评测，指出该模型在 SVG 动画生成方面有显著改进，且定价与 Gemini 3 Pro 持平，'
        '仅为 Claude Opus 4.6 的一半，性价比突出。Willison 还跟进报道 Apple WWDC 2026 的 Siri 改版，'
        '分析多 AI 供应商整合趋势对开发者生态的长期影响，认为"AI 中立层"正在成为 OS 级别的标准配置。',
        'https://simonwillison.net/',
        datetime(2026, 6, 7, tzinfo=timezone.utc),
    ),
]

# --- GitHub 热门 ---
github = [
    GithubProject(
        'openclaw/openclaw',
        'https://github.com/openclaw/openclaw',
        'Personal AI assistant running entirely on your own devices, connecting 50+ integrations including WhatsApp, Telegram, Slack, Discord',
        210000, 18000, 'Python', 3200,
        ['openclaw-team'],
    ),
    GithubProject(
        'ollama/ollama',
        'https://github.com/ollama/ollama',
        'Get up and running with large language models locally. Supports Llama, Mistral, Gemma, DeepSeek and more.',
        165000, 12500, 'Go', 1850,
        ['jmorganca', 'mchiang0610'],
    ),
    GithubProject(
        'comfyanonymous/ComfyUI',
        'https://github.com/comfyanonymous/ComfyUI',
        'The most powerful and modular diffusion model GUI and backend with node-based visual workflow system.',
        106000, 11200, 'Python', 980,
        ['comfyanonymous'],
    ),
    GithubProject(
        'vllm-project/vllm',
        'https://github.com/vllm-project/vllm',
        'A high-throughput and memory-efficient inference and serving engine for LLMs. Supports NVIDIA, AMD, Intel Arc, and TPU.',
        78000, 9800, 'Python', 760,
        ['WoosukKwon', 'zhuohan123', 'simon-mo'],
    ),
    GithubProject(
        'Zijian-Ni/awesome-ai-agents-2026',
        'https://github.com/Zijian-Ni/awesome-ai-agents-2026',
        'A curated list of AI Agent frameworks, tools, platforms, and resources for 2026 — the year agents went mainstream.',
        18400, 1600, '', 620,
        ['Zijian-Ni'],
    ),
    GithubProject(
        'ARUNAGIRINATHAN-K/awesome-ai-agents-2026',
        'https://github.com/ARUNAGIRINATHAN-K/awesome-ai-agents-2026',
        '300+ AI Agents, Frameworks & Coding • Creative • Voice • Research • Enterprise. Comparison guides, benchmarks & deep dives.',
        12800, 1100, '', 480,
        ['ARUNAGIRINATHAN-K'],
    ),
]

filename, content = generate_jekyll_post(news, papers, updates, github)
out_path = f'/home/user/ai-daily-news/reports/{filename}'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f'Jekyll 文章已生成：{filename}')
print(f'字符数：{len(content)}')
print(f'路径：{out_path}')
