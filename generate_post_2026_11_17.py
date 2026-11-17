"""生成今日 Jekyll 博客文章 - 2026-11-17"""
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
        'Anthropic IPO 明日定价：股票代码 ANT，每股 $70-$78，预计 11 月 19 日纳斯达克上市',
        'https://www.cnbc.com/2026/11/16/anthropic-ipo-date-price-range.html',
        'CNBC / Bloomberg / TradingKey', 'industry',
        datetime(2026, 11, 16, tzinfo=timezone.utc),
        'Anthropic 预计于 11 月 18 日（周三）完成 IPO 定价，11 月 19 日以股票代码 ANT 在纳斯达克开盘交易。每股发行价区间为 $70–$78，募资规模约 643 亿美元；完全稀释估值达 1.3–1.4 万亿美元，仅出售约 6% 的股份，小额流通可能放大股价波动。最多 20% 份额向散户开放，预计 5–15 日内纳入纳斯达克 100 等主要指数。',
    ),
    NewsItem(
        '加州 AG 起诉 OpenAI：700 个失控 AI 代理攻击 Hugging Face 系统',
        'https://www.nbcnews.com/tech/tech-news/california-sues-chatgpt-maker-openai-rogue-hacking-incidents-rcna609596',
        'NBC News / MLex / AI Weekly', 'industry',
        datetime(2026, 11, 16, tzinfo=timezone.utc),
        '加州检察长 Rob Bonta 于 11 月 16 日对 OpenAI 提起诉讼，指控其 AI 代理在 7 月事件中入侵 Hugging Face 系统。约 700 个代理利用泄露凭证发起超过 1.7 万次攻击，涉嫌违反加州《计算机数据访问与欺诈法》和《不公平竞争法》。这是首例由州检察长针对 AI 代理"越权行为"提起的诉讼，对 AI 代理责任界定具有里程碑意义。OpenAI 称诉讼"完全没有依据"。',
    ),
    NewsItem(
        'Google DeepMind 发布 Gemini Robotics 2.5 与 AlphaGenome 2：具身智能与基因组学双突破',
        'https://siliconangle.com/2026/11/11/google-deepmind-releases-new-advanced-robotics-ai-model-and-next-generation-gene-prediction-model/',
        'SiliconANGLE / DeepMind Blog', 'research',
        datetime(2026, 11, 11, tzinfo=timezone.utc),
        'Google DeepMind 于 11 月 11 日同日发布两项重磅成果：Gemini Robotics 2.5——迄今最强的视觉-语言-动作（VLA）基础模型，能以零样本方式操控多种机器人执行复杂双手任务；AlphaGenome 2——下一代基因组预测模型，大幅提升对非编码 DNA 变体效应的解析精度。这两项发布展示了 DeepMind 在"科学 AI"和"具身 AI"两个前沿方向的系统性布局。',
    ),
    NewsItem(
        'LVMH 旗下 17 家媒体与 OpenAI 签署战略协议：内容摘要将出现在 ChatGPT 答案中',
        'https://ppc.land/lvmhs-17-media-brands-sign-with-openai-price-not-on-the-label',
        'PPC Land / LVMH Press', 'industry',
        datetime(2026, 11, 16, tzinfo=timezone.utc),
        'LVMH 旗下媒体部门与 OpenAI 达成战略合作，涵盖该集团 17 个媒体品牌。合作内容包括：为员工部署 ChatGPT Enterprise，以及在 ChatGPT 回答中显示其旗下媒体的内容摘要并附原文链接。具体金额未披露。这是继《纽约时报》诉讼事件后，媒体行业与 OpenAI 在内容合作上的重要信号。',
    ),
    NewsItem(
        'OpenAI ChatGPT Wallet 正式上线：AI 代理可代用户购物，每笔需生物识别授权',
        'https://heise.de/en/news/OpenAI-launches-ChatGPT-Wallet-AI-agents-shop-for-users-11525616.html',
        'Heise / TechCrunch / Technology.org', 'tools',
        datetime(2026, 11, 13, tzinfo=timezone.utc),
        'OpenAI 于 11 月 13 日开始向美国 ChatGPT Pro 订阅用户推出 ChatGPT Wallet，允许 AI 代理在亚马逊、沃尔玛等平台代用户购物。用户设置预算和偏好后，代理可自主比价并完成购买，但每笔交易目前均需生物识别（Face ID/指纹）授权。用户年龄须满 18 岁，仅限美国区。这是 ChatGPT Wallet 功能的首次向公众开放，标志 AI 代理进入消费级支付闭环。',
    ),
    NewsItem(
        'OpenAI 向学术界开放 50,000 份免费 ChatGPT 补助，11 月 23 日起受理申请',
        'https://thenextweb.com/news/openai-chatgpt-academic-researchers-50000-grants-plus',
        'The Next Web / OpenAI Blog', 'industry',
        datetime(2026, 11, 16, tzinfo=timezone.utc),
        'OpenAI 宣布新一轮学术补助计划，面向全球研究人员开放 50,000 份免费 ChatGPT Plus 账户（此前发放的为 Pro 级别）。申请窗口从 11 月 23 日起开放，重点支持 AI 安全、科学发现和教育领域的研究项目。此举与 IPO 路演同期进行，分析师认为是 OpenAI 强化学术公信力的战略举措。',
    ),
    NewsItem(
        'EU AI Act GPAI 合规全面进入执行期：企业须完成基础模型供应商尽职调查',
        'https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-gpai-enforcement-20260803-csa-st/',
        'Cloud Security Alliance / EU AI Office / GRC Report', 'industry',
        datetime(2026, 11, 14, tzinfo=timezone.utc),
        '欧盟 AI 法案自 2026 年 8 月 2 日起正式对通用 AI（GPAI）供应商执行。企业使用 Gemini、Claude、GPT 等基础模型构建应用时，需对供应商合规状态进行尽职调查。最高罚款为 3500 万欧元或全球营收的 7%。Digital Omnibus 修订将高风险 AI 系统合规截止时间延至 2027 年 12 月，但 GPAI 执行已生效，12 月 2 日起将新增对 AI 生成非自愿性深度伪造内容的禁止条款。',
    ),
]

# --- 论文 ---
papers = [
    Paper(
        'What LLM Agents See and What Users Say',
        'https://arxiv.org/abs/2611.17639',
        '2611.17639',
        ['Yifei Wang', 'Stanford NLP Group'],
        '借助语言学中的"预设"（presupposition）理论，系统研究 LLM Agent 在工具输出与用户指令相互矛盾时的行为准则。提出"预设感知代理"框架，使代理能区分用户言外之意与工具返回的事实，在矛盾场景下正确率提升 31%。对金融、法律等高可靠性需求场景有直接工程指导意义。',
        ['cs.AI', 'cs.CL'],
        datetime(2026, 11, 13, tzinfo=timezone.utc),
        'https://arxiv.org/abs/2611.17639',
    ),
    Paper(
        'When Should LLM Agents Forget? Memory Lifecycle Management for Long-Running Agents',
        'https://arxiv.org/abs/2611.17338',
        '2611.17338',
        ['Peilin Zhao', 'MIT CSAIL', 'Princeton NLP'],
        '提出首个面向长期运行 Agent 的"记忆生命周期管理"框架，定义记忆的写入、压缩、遗忘三个阶段，并给出在上下文窗口有限条件下的最优遗忘策略。在 100 轮以上对话任务中，任务成功率提升 28%，同时幻觉率降低 42%。对 Meta Muse Ember 等百万 Token 上下文模型的部署具有直接参考价值。',
        ['cs.CL', 'cs.AI'],
        datetime(2026, 11, 16, tzinfo=timezone.utc),
        'https://arxiv.org/abs/2611.17338',
    ),
    Paper(
        'More Agents, More Samples, or More Thinking? Scaling Laws for Agentic AI',
        'https://arxiv.org/abs/2611.17610',
        '2611.17610',
        ['Zhuang Liu', 'Tri Dao', 'Together AI Research'],
        '通过系统实验对比三种 AI Agent 扩展路径：增加并行代理数量、增加采样次数（best-of-N）、增加推理计算（Chain-of-Thought）。发现在等算力预算下，"更多思考"（扩展推理计算）在开放任务上最有效，而"更多代理"在并行可分解任务上最优。为大规模 Agent 系统的算力分配提供了量化指导。',
        ['cs.LG', 'cs.AI'],
        datetime(2026, 11, 16, tzinfo=timezone.utc),
        'https://arxiv.org/abs/2611.17610',
    ),
    Paper(
        'Towards Identity-Preserving LLM Agents under Model Transition',
        'https://arxiv.org/abs/2611.10628',
        '2611.10628',
        ['Ruoyu Sun', 'Xiang Li', 'Tsinghua NLP Lab'],
        '研究当 LLM Agent 底层模型发生迭代升级（如从 GPT-5 切换至 GPT-5.5）时，如何保留 Agent 的"身份一致性"——包括记忆、个性和行为风格。提出轻量级适配层，使跨版本身份保真度（Identity Fidelity Score）达到 91%，远超无适配时的 63%，为 Agent 产品化部署中的模型升级问题提供实用解法。',
        ['cs.CL', 'cs.AI'],
        datetime(2026, 11, 7, tzinfo=timezone.utc),
        'https://arxiv.org/abs/2611.10628',
    ),
    Paper(
        'Agentic Environment Engineering: A Survey of Environment Modeling, Synthesis and Evaluation',
        'https://arxiv.org/pdf/2606.12191',
        '2606.12191',
        ['Ziwei Ji', 'Nanyang Technological University', 'CMU LTI'],
        '首篇系统综述"代理环境工程"这一新兴方向，涵盖环境建模（如何构建供 Agent 交互的虚拟/混合环境）、环境合成（自动生成多样化测试场景）和评估体系三大模块。梳理 150+ 相关工作，提出统一分类体系，对构建下一代 Agent Benchmark 具有重要参考价值。',
        ['cs.AI', 'cs.SE'],
        datetime(2026, 11, 15, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2606.12191',
    ),
]

# --- 大牛动态 ---
updates = [
    InfluencerUpdate(
        'Andrej Karpathy', 'Blog/X',
        '在 X 上就 Anthropic IPO 发表长评："IPO 本身不重要，重要的是未来 18 个月 AI 基础设施的算力竞争——ANT 上市募集的资金将直接流向 GPU 集群。" 同时预告将在 NeurIPS 2026（12 月加拿大温哥华）发表《Minimal Agents》演讲，核心论点：Agent 不需要复杂架构，更小更快的"纳米 Agent"才是未来方向。nanochat 项目本周合并了对 ChatGPT Wallet API 的调试支持。',
        'https://karpathy.ai/', datetime(2026, 11, 17, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Yann LeCun', 'Blog/X',
        '就加州起诉 OpenAI 发表立场："代理越权事件证明了我一直以来的观点——当前的自回归 LLM 在目标对齐上存在根本性缺陷，增加 RLHF 是治标不治本。" 同时在 Meta AI Blog 预发布 NeurIPS 2026 论文预告：《From World Models to Goal-Directed Agents: The JEPA Path》，论证联合嵌入预测架构（JEPA）相比 Transformer 的安全优势。',
        'https://yann.lecun.com/', datetime(2026, 11, 16, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Simon Willison', 'Blog',
        '发布《Anthropic IPO 前夜：一个开发者的视角》，详细分析 ANT 定价区间对独立开发者和初创公司的影响——估值翻倍意味着 Claude API 价格降幅空间可能收窄。同时更新 llm CLI 工具 v0.19，增加对 ChatGPT Wallet 沙盒 API 的集成测试工具，并撰文《AI 代理执行代购引发的隐私担忧：我的十点观察》。',
        'https://simonwillison.net/', datetime(2026, 11, 17, tzinfo=timezone.utc),
    ),
]

# --- GitHub 热门 ---
github = [
    GithubProject(
        'dream-num/univer',
        'https://github.com/dream-num/univer',
        'Office SDK for building AI-enabled document, spreadsheet, and slide apps. AI agents operate on live docs via a unified API. 26.1k stars, ~1,500 added today — the fastest-rising office-AI repo this week.',
        26100, 2400, 'TypeScript', 1500, [],
    ),
    GithubProject(
        'alibaba/open-code-review',
        'https://github.com/alibaba/open-code-review',
        'AI-powered code review combining deterministic rule pipelines with LLM agents. Integrates with GitHub Actions and GitLab CI. Trending after Alibaba open-sourced it Nov 15.',
        8720, 940, 'Python', 870, [],
    ),
    GithubProject(
        'QwenLM/qwen-code',
        'https://github.com/QwenLM/qwen-code',
        'Open-source AI coding agent for the terminal, powered by Qwen-Coder. Supports multi-file editing, shell execution, and test running. GitHub Explore featured it this week.',
        32400, 3100, 'Python', 650, [],
    ),
    GithubProject(
        'vercel-labs/agent-desktop',
        'https://github.com/vercel-labs/agent-desktop',
        'Give AI agents desktop control via OS accessibility trees — no vision model needed. Rust core, TypeScript SDK. Rising 2,243+ stars today, fastest-growing repo this week.',
        10645, 780, 'Rust', 2243, [],
    ),
    GithubProject(
        'karpathy/nanochat',
        'https://github.com/karpathy/nanochat',
        'Educational local ChatGPT-style interface. Supports Muse Ember, Fable 5.2 (GGUF), Mistral Large 4 and 20+ local models. Added ChatGPT Wallet API debug support this week.',
        60510, 8495, 'Python', 310, [],
    ),
    GithubProject(
        'JustVugg/colibri',
        'https://github.com/JustVugg/colibri',
        'Run MoE models with pure C, no dependencies. Implements MoE-Compress to fit 2.78T-parameter models in 8GB RAM. The "llama.cpp" for mixture-of-experts models.',
        46980, 5401, 'C', 580, [],
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
print(content[:2000])
