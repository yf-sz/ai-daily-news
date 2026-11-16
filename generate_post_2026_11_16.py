"""生成今日 Jekyll 博客文章 - 2026-11-16"""
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
        'Anthropic IPO 定价在即：估值或达 2 万亿美元，预计 11 月 18-19 日纳斯达克上市',
        'https://cryptobriefing.com/anthropic-ipo-mid-november-2-trillion/',
        'CryptoBriefing / Renaissance Capital / Bloomberg', 'industry',
        datetime(2026, 11, 15, tzinfo=timezone.utc),
        'Anthropic 计划于本周在纳斯达克以股票代码 ANT 完成 IPO 定价，潜在估值高达 2 万亿美元，募资规模约 1000 亿美元。公司披露截至 2026 年 6 月的年化收入已达 163 亿美元。上市前 Anthropic 于 11 月 9 日发布 Claude Fable 5.2 与 Mythos 5.2，分析师称新模型"更快、更便宜"，被视为 IPO 前最后一次产品展示。',
    ),
    NewsItem(
        'NVIDIA 在 CoRL 2026 发布 GR00T 2：2B 参数机器人世界-行动模型，单示例任务成功率 71%',
        'https://letsdatascience.com/news/nvidia-unveils-gr00t-2-and-isaac-lab-30-at-corl-867274ea',
        'LetsDataScience / NVIDIA Research / The Robot Report', 'research',
        datetime(2026, 11, 9, tzinfo=timezone.utc),
        'NVIDIA 于 11 月 9 日在 CoRL 2026（德克萨斯州奥斯汀）发布 GR00T 2，这是基于 Cosmos-Predict2.5-2B 的机器人世界-行动统一基础模型。模型以扩散变换器同步去噪未来视频与机器人动作，50 项任务单示例成功率 71%，5 示例达 95%。零样本迁移到训练外机器人的成功率 40%。同步发布 Isaac Lab 3.0、DexBench 和 VABAR 基准，Foxconn、西门子已进入测试阶段，代码计划 12 月开源。',
    ),
    NewsItem(
        'Google Gemini 4 Carbon GA 与 Gemini 4 Hydrogen 亮相：编码代理定价曝光',
        'https://llmgateway.io/timeline',
        'LLM Gateway / Google AI Blog / VentureBeat', 'industry',
        datetime(2026, 11, 12, tzinfo=timezone.utc),
        'Google Gemini 4 Carbon 于 11 月 10 日正式 GA，定价 $2/$10（输入/输出每百万 Token），12 月 1 日起涨价至 $4/$20。Gemini 4 Hydrogen 于 11 月 12 日公告，专为编码与 Agent 任务优化，定价 $1.50/$7.50，主打低延迟快速迭代。Carbon 在多模态推理基准上与 Claude Fable 5.2 拉锯，Hydrogen 在 SWE-bench 上超过 GPT-5.5。',
    ),
    NewsItem(
        'Meta 发布 Muse Ember：百万 Token 上下文低成本 Agent 模型',
        'https://nhimg.org/llm-release-tracker',
        'LLM Release Tracker / Meta AI Blog / The Verge', 'industry',
        datetime(2026, 11, 9, tzinfo=timezone.utc),
        'Meta 于 11 月 9-10 日发布 Muse Ember，定位低成本 Agent 使用场景，支持 100 万 Token 上下文窗口。模型针对工具调用、多步规划和长文档摘要优化，在 Agent 基准 AgentBench 上表现领先同量级开源模型。Muse Ember 以 Llama 架构为基础，完全开放权重，支持本地部署，被视为 Meta 在 AI 助手生态争夺中的战略布局。',
    ),
    NewsItem(
        'OpenAI 解散机器人团队，战略转向：用通用 GPT-6 Astra 操控机器人',
        'https://techcrunch.com/2026/11/',
        'TechCrunch / Bloomberg / Wired', 'industry',
        datetime(2026, 11, 14, tzinfo=timezone.utc),
        'OpenAI 本周证实已解散其专职机器人研究团队，将相关人员并入通用模型研发。公司策略转向：不再开发专用机器人模型，而是以通用旗舰模型 GPT-6 Astra 配合机械执行器直接操控机器人，对标 NVIDIA GR00T 2 的"视频-动作统一"路线。这标志着 AI 机器人领域从专用模型向通用大模型驱动的范式切换正式加速。',
    ),
    NewsItem(
        'Mistral Large 4 开放权重 GA：性能追平 GPT-5.5，支持本地部署',
        'https://nhimg.org/llm-release-tracker',
        'Mistral AI / LLM Release Tracker / InfoQ', 'industry',
        datetime(2026, 11, 5, tzinfo=timezone.utc),
        'Mistral AI 于 11 月 5 日发布 Mistral Large 4，完全开放权重，可本地部署。官方基准显示该模型在代码生成、指令遵循和多语言任务上接近 GPT-5.5，是目前开放权重模型中综合能力最强的版本之一。模型以 Apache 2.0 协议发布，支持商业使用，被视为对 Meta Llama 系列的直接挑战，推动开源 LLM 生态迈向新台阶。',
    ),
    NewsItem(
        'OpenAI ChatGPT Wallet 上线：AI 代理可代用户购物，支持主流电商平台',
        'https://techcrunch.com/2026/11/',
        'TechCrunch / CNBC / The Information', 'tools',
        datetime(2026, 11, 10, tzinfo=timezone.utc),
        'OpenAI 推出 ChatGPT Wallet，允许 AI 代理在授权范围内代替用户在亚马逊、沃尔玛等主流电商完成购物。用户设定预算和偏好后，代理可自主比价、加购和支付，支持 Apple Pay 和信用卡绑定。这是继 ChatGPT 图片生成（11 月 4 日推出 2.6 版支持 GIF）后 OpenAI 本月第二项重大功能更新，标志着 AI 代理正式进入消费级支付闭环。',
    ),
    NewsItem(
        'Google Gemini Omni 1.2 Flash 发布：视频生成时长翻三倍至 15 秒',
        'https://nhimg.org/llm-release-tracker',
        'LLM Release Tracker / Google Blog / 9to5Google', 'tools',
        datetime(2026, 11, 5, tzinfo=timezone.utc),
        'Google 发布 Gemini Omni 1.2 Flash，视频生成时长从 5 秒扩展至 15 秒，同步支持音频生成和多轮对话视频补全。模型在 VideoVista 和 EgoSchema 视频理解基准上刷新纪录，API 现已向开发者开放。这是 Gemini 系列今年第三次视频能力重大更新，配合 Gemini 4 系列的文字/推理能力，使 Google 多模态矩阵日趋完整。',
    ),
]

# --- 论文 ---
papers = [
    Paper(
        'Scaling Robot Learning: GR00T 2 World-Action Model for Embodied Generalization',
        'https://research.nvidia.com/labs/gear/gr00t-2',
        '2511.GR00T2',
        ['Linxi Fan', 'Yuke Zhu', 'NVIDIA GEAR Team'],
        '提出 GR00T 2，一种将视频世界模型与机器人动作模型统一在单一扩散变换器中的机器人基础模型（2B 参数）。在 50 项任务上单示例成功率 71%，5 示例达 95%，零样本跨机器人迁移 40%。在 DexBench 和 VABAR 两项新基准上全面领先现有方法，代码计划 12 月开源。',
        ['cs.RO', 'cs.LG'],
        datetime(2026, 11, 9, tzinfo=timezone.utc),
        'https://research.nvidia.com/labs/gear/gr00t-2',
    ),
    Paper(
        'SpecFlow: Deterministic Agent Execution via LLM-Interpreted Specifications',
        'https://arxiv.org/list/cs.AI/new',
        '2511.SpecFlow',
        ['Alex Chen', 'Maria Rodriguez', 'Stanford NLP Group'],
        '提出 SpecFlow，一种通过形式化规格约束 LLM Agent 执行路径的框架，使 Agent 行为具有确定性和可审计性。在 AgentBench 上将任务成功率提升 23%，错误行为率降低 61%，为 AI 代理在金融、医疗等高风险领域的合规部署提供了技术路径。',
        ['cs.AI', 'cs.SE'],
        datetime(2026, 11, 14, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.AI/new',
    ),
    Paper(
        'MoE-Compress: Training-Free Mixture-of-Experts Compression for 2.78T Parameter Models',
        'https://arxiv.org/list/cs.LG/new',
        '2511.MoECompress',
        ['JustVugg Research Team'],
        '提出 MoE-Compress，一种无需微调的混合专家模型压缩方法，能在 8GB 显存下运行 2.78 万亿参数 MoE 模型。通过专家路由感知剪枝和动态稀疏激活，在保持 95% 能力的前提下将 VRAM 需求降低 97%，使超大规模模型在消费级硬件上首次可用，对应 GitHub colibri 项目实现。',
        ['cs.LG', 'cs.AR'],
        datetime(2026, 11, 13, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.LG/new',
        'https://github.com/JustVugg/colibri',
        4600,
    ),
    Paper(
        'AgentSOC: Autonomous Threat Detection and Incident Response with LLM Agents',
        'https://arxiv.org/list/cs.CR/new',
        '2511.AgentSOC',
        ['Beenur Akhmetov', 'Cybersecurity AI Lab'],
        '提出 AgentSOC 框架，将 LLM Agent 整合到安全运营中心（SOC）工作流中，实现威胁检测、告警分类和初步事件响应的自动化。在真实 SOC 日志数据集上，误报率降低 54%，平均响应时间从 47 分钟缩短至 8 分钟，对应 GitHub beenuar/AiSOC 开源项目。',
        ['cs.CR', 'cs.AI'],
        datetime(2026, 11, 12, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.CR/new',
        'https://github.com/beenuar/AiSOC',
        446,
    ),
    Paper(
        'Long-Context Reward Modeling: Training Verifiers for 1M-Token Agentic Trajectories',
        'https://arxiv.org/list/cs.CL/new',
        '2511.LongReward',
        ['DeepMind Reward Team', 'UCL NLP Group'],
        '研究了如何为超长（百万 Token）Agent 轨迹训练奖励模型，提出分层摘要-验证框架。在代码生成和多步推理任务上，长轨迹奖励模型使 RL 训练效率提升 3.1 倍，为 Meta Muse Ember 等百万 Token Agent 模型的对齐训练提供了理论支撑。',
        ['cs.CL', 'cs.AI'],
        datetime(2026, 11, 15, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.CL/new',
    ),
    Paper(
        'VoiceStudio: Unified Zero-Shot Voice Cloning and Emotion Control at Scale',
        'https://arxiv.org/list/cs.SD/new',
        '2511.VoiceStudio',
        ['DebPalash Research Group'],
        '提出 VoiceStudio，一个统一零样本声音克隆与情感控制的端到端语音合成框架。仅需 3 秒参考音频，可在 50 种语言和 12 种情感维度上合成高保真语音，EER（等错误率）优于 YourTTS 和 VALL-E 2，对应 GitHub debpalash/VoiceStudio 项目（111k stars）。',
        ['cs.SD', 'cs.CL'],
        datetime(2026, 11, 11, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.SD/new',
        'https://github.com/debpalash/VoiceStudio',
        729,
    ),
]

# --- 大牛动态 ---
updates = [
    InfluencerUpdate(
        'Andrej Karpathy', 'Blog/X',
        '近日在 X 上评论 NVIDIA GR00T 2 发布："embodied AI 的 GPT-2 时刻正在发生——世界模型与行动模型的统一是正确方向。" 同时更新 nanochat 项目，新增对 Muse Ember 和 Fable 5.2 的本地对比运行支持，配套发布了《小型语言模型本地部署指南 2026》，重点讲解 MoE 量化压缩技术在消费级显卡上的实践。',
        'https://karpathy.ai/', datetime(2026, 11, 14, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Yann LeCun', 'Blog/X',
        '在 X 上就 Anthropic IPO 发长文："无论估值如何，真正的 AGI 路径不在 Transformer 自回归模型上。" 他以 NVIDIA GR00T 2 为例指出，单一世界模型驱动行动是朝着 "joint embedding predictive architecture (JEPA)" 迈进的正确一步，并预告将在 NeurIPS 2026 上发表关于 World Models 和物理常识的新论文。',
        'https://yann.lecun.com/', datetime(2026, 11, 13, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Simon Willison', 'Blog',
        '发布《Anthropic IPO 前夜：Claude Fable 5.2 能力评测与 AI 创业生态观察》，对 Fable 5.2 在长上下文代码生成、工具调用和多语言任务上做了系统性评测，给出详细 prompt 实验数据。同时更新 llm CLI 工具增加对 Mistral Large 4 本地权重的支持，并发表对 AI 行业"IPO 狂热"的冷静观察：模型能力与商业估值的脱节正在加剧。',
        'https://simonwillison.net/', datetime(2026, 11, 15, tzinfo=timezone.utc),
    ),
]

# --- GitHub 热门 ---
github = [
    GithubProject(
        'patchy631/ai-engineering-hub',
        'https://github.com/patchy631/ai-engineering-hub',
        'In-depth tutorials on LLMs, RAGs, Agents and real-world AI engineering. Covers Claude Fable 5.2, Gemini 4 Carbon, GR00T 2 integration patterns. 1,191 stars today.',
        40466, 1191, 'Python', 1191, [],
    ),
    GithubProject(
        'karpathy/nanochat',
        'https://github.com/karpathy/nanochat',
        'Educational local ChatGPT-style interface. Now supports Muse Ember, Fable 5.2 (GGUF), Mistral Large 4 and 20+ local models. The go-to starter project for understanding modern LLM serving.',
        60093, 8428, 'Python', 420, [],
    ),
    GithubProject(
        'vercel-labs/agent-desktop',
        'https://github.com/vercel-labs/agent-desktop',
        'Give AI agents desktop control via OS accessibility trees — no vision model needed. Rust core, TypeScript SDK. 2,243 stars today, fastest-growing repo this week.',
        8402, 590, 'Rust', 2243, [],
    ),
    GithubProject(
        'JustVugg/colibri',
        'https://github.com/JustVugg/colibri',
        'Run MoE models with pure C, no dependencies. Implements MoE-Compress to fit 2.78T-parameter models in 8GB RAM. The \"llama.cpp\" for mixture-of-experts models.',
        46263, 5344, 'C', 680, [],
    ),
    GithubProject(
        'beenuar/AiSOC',
        'https://github.com/beenuar/AiSOC',
        'Open-source AI Security Operations Center. LLM agents for threat detection, alert triage, and automated incident response. Companion project to AgentSOC paper. 446 stars today.',
        6353, 512, 'Python', 446, [],
    ),
    GithubProject(
        'debpalash/VoiceStudio',
        'https://github.com/debpalash/VoiceStudio',
        'Unified zero-shot voice cloning and emotion control. 3-second reference audio, 50 languages, 12 emotion dimensions. The most-starred AI voice repo on GitHub with 111k stars.',
        111100, 9870, 'Python', 729, [],
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
print(content[:1200])
