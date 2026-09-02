"""生成今日 Jekyll 博客文章 - 2026-09-02"""
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
        'Anthropic 发布 Claude Fable 5.1 和 Mythos 5.1：成本降低 25%，网络安全干预减少 60%',
        'https://venturebeat.com/technology/anthropics-claude-fable-5-1-and-mythos-5-1-arrive-with-a-75-cost-reduction-for-fable-cache-reads',
        'VentureBeat / AWS / MacRumors', 'industry', datetime(2026, 9, 1, tzinfo=timezone.utc),
        'Anthropic 于 9 月 1 日正式发布 Claude Fable 5.1 与配套的 Mythos 5.1。Fable 5.1 在最难的数学、科学和多步推理基准上全面提升，并引入文本不可见水印及企业边界安全（EFS）架构。在网络安全防护方面，每次 Claude Code 会话触发干预次数比 Fable 5 减少约 60%——允许发现漏洞，但不生成可利用的 exploit。缓存读取价格从 $1.00/M token 降至 $0.25，典型工作负载成本降低约 25%，高 Agentic 场景可降低 45%。模型已在 AWS Bedrock 和 Anthropic API 上线，Mythos 5.1 同期发布作为效率型补充。'
    ),
    NewsItem(
        'Anthropic 签署 350 亿美元算力大单：与英伟达支持的 Lambda 在德克萨斯州建设 350MW 数据中心',
        'https://techbriefly.com/2026/09/01/anthropic-nvidia-lambda-cloud-deal-35-billion/',
        'TechBriefly / GuruFocus / BIC Magazine', 'industry', datetime(2026, 9, 1, tzinfo=timezone.utc),
        'Anthropic 于 9 月 1 日宣布与英伟达支持的云服务商 Lambda 达成约 350 亿美元、为期六年的云算力协议，基础设施建于德克萨斯州 Nueces 县，由 Hut 8（原比特币矿场）转型运营，提供约 350MW 容量。英伟达保留厂房租约并供应芯片，Lambda 以此向 Anthropic 提供算力。这是 Anthropic 迄今最大的单笔算力采购，将支撑 Claude 系列模型的持续扩展，进一步加速 IPO 前的基础设施布局。'
    ),
    NewsItem(
        '五角大楼 GenAI.mil 平台正式上线 ChatGPT Mil 与 Grok for Government，覆盖 300 万军事人员',
        'https://techcrunch.com/2026/08/31/the-pentagon-now-has-its-own-version-of-chatgpt-and-grok/',
        'TechCrunch / The Hill / eWeek', 'industry', datetime(2026, 9, 1, tzinfo=timezone.utc),
        '美国国防部于 9 月 1 日宣布在 GenAI.mil 平台上线 OpenAI ChatGPT Mil 与 xAI Starshield Grok for Government，覆盖逾 300 万国防部员工，已有 170 万人完成注册。两款工具均获得非保密受控信息（CUI）IL5 授权。ChatGPT Mil 面向行政、后勤、规划等文档密集型任务；Grok 提供深度推理、三档推理模式和可复用"剧本"，专注知识传承。Anthropic Claude 因被列入"供应链风险"名单而缺席，但 Anthropic 已提起法律诉讼并于 8 月获得联邦法官支持的初步禁令。'
    ),
    NewsItem(
        'OpenAI Astra 模型评级为"关键"网络安全风险，将限制访问并分阶段推出',
        'https://techcrunch.com/2026/09/01/open-ais-astra-model-is-on-the-way-and-very-good-at-breaking-into-computer-systems/',
        'TechCrunch / Bloomberg / CNBC', 'research', datetime(2026, 9, 1, tzinfo=timezone.utc),
        'OpenAI 于 9 月 1 日披露，即将发布的 Astra 模型是首款突破其"关键"网络安全能力阈值的模型——能够在无需逐步引导的情况下自主发现并利用零日漏洞，评估期间在真实系统中利用了两个零日漏洞。OpenAI 计划分阶段开放：优先向"Daybreak Blue"批准安全研究者提供防御性访问，同时对高风险账户额外限制，并部署思维链监控。Astra 同期通过了 8 月发布的数学难题解决成果（解决 10 道十年悬而未决的数学问题）的验证。'
    ),
    NewsItem(
        'Google 发布 TimesFM-3：330M 参数零样本多变量时间序列预测模型，登顶三大基准',
        'https://research.google/blog/timesfm-3-a-zero-shot-foundation-model-for-multivariate-forecasting/',
        'Google Research Blog / DataNorth / The New Stack', 'research', datetime(2026, 8, 31, tzinfo=timezone.utc),
        'Google Research 于 8 月 31 日在 GitHub 和 Hugging Face 发布 TimesFM-3，这是首款为多变量预测原生训练的 TimesFM 模型，参数量 330M，预训练语料逾 1 万亿时序时间点。该模型支持灵活协变量（仅过去值或过去+未来值均可），原生输出概率分位数，在三个主流时序基础模型基准上全部第一。代码以 Apache-2.0 开源，但模型权重为非商业许可，不得用于商业生产部署。'
    ),
    NewsItem(
        'Clay AI 以 70 亿美元估值融资，由惠灵顿管理领投，成 2026 年最高 AI 销售工具独角兽',
        'https://aiweekly.co/ai-news-today',
        'AI Weekly / CryptoIntegrat', 'industry', datetime(2026, 9, 1, tzinfo=timezone.utc),
        'AI 驱动的销售与营销平台 Clay 宣布完成新一轮融资，由惠灵顿管理（Wellington Management）领投，融资前估值 70 亿美元，是 2026 年迄今最高估值的 AI 销售工具融资事件。Clay 以 AI Agent 自动化研究、数据丰富和外联个性化见长，用户可将数十个数据源整合为自动化销售工作流，本轮融资将用于扩大企业客户团队和模型研发。'
    ),
    NewsItem(
        'GLM-5.3-Flash 与 Qwen3.8 Flash 同日发布，9 月 AI 模型发布潮延续',
        'https://llm-stats.com/ai-news',
        'LLM Stats / LLM Updates', 'industry', datetime(2026, 8, 27, tzinfo=timezone.utc),
        '进入 9 月，两款轻量级推理模型同期上线：Z.ai GLM-5.3-Flash（8 月 27 日）延续高速低成本定位；阿里 Qwen3.8 Flash（8 月 27 日）在代码生成和数学推理上表现突出。两款模型均在 OpenRouter 和 LLM Gateway 同步接入。8 月共有逾 11 款主要模型密集发布，LLM 竞争进入"评测赶不上发布"的新阶段，9 月势头持续。'
    ),
    NewsItem(
        'NASA 火星探测器成功首次由 AI 规划路线独立驾驶，无需人工操作员干预',
        'https://techstartups.com/2026/09/01/top-tech-news-today-september-1-2026-amazon-anthropic-honda-openai-sony-warner-z-ai-more/',
        'TechStartups / NASA', 'research', datetime(2026, 9, 1, tzinfo=timezone.utc),
        'NASA 毅力号（Perseverance）火星探测器近日成功完成首次全程由人工智能规划路线的自主驾驶任务，无需地球操作员逐帧指令干预。AI 导航系统通过实时感知火星地形、绕开障碍物，实现从 A 点到 B 点的端到端自主行驶，标志着行星际机器人自主探索能力的重大里程碑，也为未来长距离火星探测任务奠定基础。'
    ),
]

# --- 论文 ---
papers = [
    Paper(
        'DreamX-Creator: Democratizing Native Audio-Video Generation at 2K Resolution',
        'https://huggingface.co/papers/trending', '2509.DreamX',
        ['GD-ML AMAP-ML Team'],
        '提出 DreamX-Creator 框架，实现 2K 分辨率原生音视频联合生成，在无需单独训练音频或视频生成模块的前提下，同时生成语义一致的视觉和音频内容。模型采用统一扩散架构，在 VGGSound 和 AudioSet 基准上优于当前最优的单模态生成系统，为多模态创作工具的民主化提供了新路径。',
        ['cs.CV', 'cs.MM'], datetime(2026, 9, 1, tzinfo=timezone.utc),
        'https://huggingface.co/papers/trending',
    ),
    Paper(
        'BDH-CQ: In-Context Learning with Recurrent Latent Reasoning',
        'https://huggingface.co/papers/trending', '2509.BDH-CQ',
        ['BDH Research Team'],
        '提出 BDH-CQ，一个 150M 参数的推理模型，结合循环潜变量推理（Recurrent Latent Reasoning）与上下文学习，在 ARC-AGI-1 上实现新的成本-精度前沿。该方法避免了对大型语言模型的依赖，通过学习隐式推理轨迹而非显式链式思维，在推理效率和准确率间取得优异平衡，对轻量级推理设备部署具有重要意义。',
        ['cs.LG', 'cs.AI'], datetime(2026, 8, 30, tzinfo=timezone.utc),
        'https://huggingface.co/papers/trending',
    ),
    Paper(
        'Prime Agent: A Self-Improving RLM Harness for Long-Horizon Tasks',
        'https://huggingface.co/papers/trending', '2509.PrimeAgent',
        ['Prime Agent Research Group'],
        '提出 Prime Agent，一种利用递归子 Agent、持久计算和 Agent 间协调来扩展语言模型长视野能力的开源框架。在编码和推理任务上，Prime Agent 通过自我改进循环持续提升表现，展示了在无监督环境下自主规划、执行和反思的全流程能力，为 Agentic AI 的下一阶段训练范式提供新思路。',
        ['cs.AI', 'cs.LG'], datetime(2026, 8, 31, tzinfo=timezone.utc),
        'https://huggingface.co/papers/trending',
    ),
    Paper(
        'LightNav-0: Eliciting VLM Spatial Intelligence for Generalist Embodied Navigation',
        'https://huggingface.co/papers/trending', '2509.LightNav',
        ['Embodied AI Research Team'],
        '提出 LightNav-0，一种轻量级通用导航模型，通过激发视觉-语言模型（VLM）内在的空间推理能力来实现具身导航，无需大规模特定导航数据训练。在 HM3D 和 R2R 基准上达到当前最优，在室内未见场景下泛化显著优于专门训练的导航模型，展示了 VLM 跨模态空间迁移学习的潜力。',
        ['cs.RO', 'cs.CV'], datetime(2026, 8, 31, tzinfo=timezone.utc),
        'https://huggingface.co/papers/trending',
    ),
    Paper(
        'PaperGym: Rubric-Centered Evolution for Research-Plan Generation',
        'https://huggingface.co/papers/trending', '2509.PaperGym',
        ['PaperGym Team'],
        '提出 PaperGym 基准与配套的以评分标准为中心的进化方法（Rubric-Centered Evolution），专注于训练 AI 系统生成高质量科研计划。通过对论文评审标准的强化学习，模型学会在不确定信息下提出有价值的实验假设和方法路线，在 NeurIPS 风格盲审场景下显著优于 GPT-5.5 和 Claude Fable 5 基线，为 AI 科研助理的能力评测提供了系统框架。',
        ['cs.AI', 'cs.CL'], datetime(2026, 9, 1, tzinfo=timezone.utc),
        'https://huggingface.co/papers/trending',
    ),
    Paper(
        'SPADE: The First LLM-Based Framework for Soil Moisture Time-Series Analysis',
        'https://arxiv.org/list/cs.AI/new', '2509.SPADE',
        ['Soil AI Research Consortium'],
        '提出 SPADE（Soil moisture Pattern and Anomaly DEtection），首个专为土壤湿度时间序列分析设计的 LLM 框架。结合领域知识提示、多源传感器数据融合和时序异常检测模块，SPADE 在农业干旱预警和精准灌溉场景中精度超越传统数值模型，为 AI 在地球科学实际应用中的落地提供了可复制范本。',
        ['cs.AI', 'cs.LG'], datetime(2026, 9, 1, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.AI/new',
    ),
]

# --- 大牛动态 ---
updates = [
    InfluencerUpdate(
        'Simon Willison', 'Blog',
        '于 9 月 2 日发布《Highlights from my conversation about agentic engineering on Lenny\'s Podcast》，系统梳理 Agentic 工程的核心模式：工具调用设计、多 Agent 协调、沙箱隔离和可观测性。他同时更新了 LLM CLI 工具，新增对推理轨迹、OpenAI Responses API、服务端工具和智能日志的支持，并发布了 OpenAI 实验 Agent 意外攻击 Hugging Face 事件的完整时间线复盘。',
        'https://simonwillison.net/', datetime(2026, 9, 2, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Sam Altman', 'Blog',
        '就 Astra 模型网络安全风险评级发推："安全是我们最重要的工作——我们宁愿晚一点发布，也不愿在保护机制不到位时推向世界。" 他同时确认 Fable 5.1 的水印检测 API 将在私测后向更广泛的企业客户开放，并暗示 Astra 的公测窗口将在 2026 年内落地，重申 OpenAI 对 Daybreak Blue 负责任发布框架的承诺。',
        'https://blog.samaltman.com/', datetime(2026, 9, 1, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Sebastian Raschka', 'Blog/Newsletter',
        '在《Ahead of AI》新刊中深度解析 Claude Fable 5.1 的不可见水印机制：通过词汇表分组（绿/红 Token）和采样偏置在不影响语义的前提下嵌入统计可检测标记；同时评测 Fable 5.1 在代码和数学基准上的表现，指出相比 Fable 5，小样本数学推理准确率提升约 8 个百分点，但在极长上下文任务上仍有提升空间。',
        'https://magazine.sebastianraschka.com/', datetime(2026, 9, 1, tzinfo=timezone.utc),
    ),
]

# --- GitHub 热门 ---
github = [
    GithubProject(
        'openclawai/openclaw', 'https://github.com/openclawai/openclaw',
        'Personal AI assistant running entirely on your own devices — connects 50+ integrations (WhatsApp, Telegram, Slack, iMessage, Discord) with major AI models. 5,700+ community skills via ClawHub. 2026\'s fastest-growing open-source project.',
        314000, 25100, 'TypeScript', 2300, []
    ),
    GithubProject(
        'NousResearch/hermes-agent', 'https://github.com/NousResearch/hermes-agent',
        'The agent that grows with you — open-source multi-modal AI agent framework with persistent memory, tool orchestration, and self-improvement loops. 201.8k stars. Built on Hermes-3 model family.',
        201800, 16900, 'Python', 1800, []
    ),
    GithubProject(
        'google-research/timesfm', 'https://github.com/google-research/timesfm',
        'TimesFM (Time Series Foundation Model): zero-shot forecasting for time-series data. TimesFM-3 (330M params) now supports native multivariate forecasting, flexible covariates, and probabilistic outputs.',
        18400, 1500, 'Python', 1200, ['google-research']
    ),
    GithubProject(
        'mendableai/firecrawl', 'https://github.com/mendableai/firecrawl',
        'Turn entire websites into LLM-ready markdown or structured data. The context API for AI agents — scrape, crawl, search, extract, and interact with the web at scale. Used by Claude Code, Cursor, and 50k+ developers.',
        47200, 3900, 'TypeScript', 890, []
    ),
    GithubProject(
        'ollama/ollama', 'https://github.com/ollama/ollama',
        'Get up and running with Llama, DeepSeek, Qwen3.8, Gemma and other large language models locally. Supports GLM-5.3-Flash, Fable 5.1 (via GGUF), and 180+ models. Latest: v0.6.8.',
        169500, 13800, 'Go', 620, []
    ),
    GithubProject(
        'langgenius/dify', 'https://github.com/langgenius/dify',
        'Open-source LLM app development platform. Dify lets you quickly build and operate generative AI applications using visual workflow builder, RAG pipeline, model management, and observability features.',
        146400, 12100, 'TypeScript', 540, []
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
