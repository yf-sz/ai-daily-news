"""生成今日 Jekyll 博客文章 - 2026-11-25"""
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
        '黄仁勋复职引发国会山质疑，司法部长布兰奇反驳国家安全威胁论',
        'https://foxnews.com/live-news/ai-tech-jensen-huang-nvidia-trade-stocks-market-donald-trump-november-24',
        'Fox News / CNBC',
        'industry',
        datetime(2026, 11, 24, tzinfo=timezone.utc),
        'Nvidia CEO 黄仁勋复职后，来自两党的国会议员要求国家情报总监和司法部长就外国情报渗透指控展开独立调查。司法部长 Todd Blanche 随即公开澄清，称媒体对国家安全影响的报道"严重夸大"，并表示黄仁勋在调查期间始终与政府配合。与此同时，特朗普政府多位官员证实曾就此事直接联系 Nvidia 董事会。',
    ),
    NewsItem(
        '联合国秘书长呼吁一年内建立全球 AI 监管框架',
        'https://aljazeera.com/news/2026/11/24/un-chief-calls-for-world-to-agree-on-ai-oversight-within-a-year',
        'Al Jazeera',
        'industry',
        datetime(2026, 11, 24, tzinfo=timezone.utc),
        '联合国秘书长安东尼奥·古特雷斯在巴巴多斯举行的 AI 治理峰会上发表讲话，呼吁各成员国在未来一年内协调行动，建立具有包容性的原则导向型多边 AI 风险管理框架。古特雷斯警告，如果各国政府无法就 AI 监管达成共识，AI 领域的"军备竞赛"将使全球面临不可预测的风险。此次峰会聚焦发展中国家在全球 AI 治理中的代表性问题。',
    ),
    NewsItem(
        '纽约州长 Hochul 拟立法禁售 AI 聊天玩具五年',
        'https://aiweekly.co/ai-news-today',
        'AI Weekly / Axios',
        'industry',
        datetime(2026, 11, 24, tzinfo=timezone.utc),
        '纽约州长 Kathy Hochul 宣布将推动立法，禁止在纽约州销售面向 14 岁以下儿童的 AI 聊天机器人玩具，禁令期限为五年，并要求既有产品在 180 天内下架或关闭 AI 功能。此前加利福尼亚州已出台类似禁令，理由是这类玩具存在引导儿童分享个人信息、模拟亲密关系等安全隐患。纽约此举标志着美国州级 AI 消费者保护立法进入新阶段。',
    ),
    NewsItem(
        'xAI 前创始人成员推出 Epochal：让 AI 代理"穿越时间"浏览历史互联网',
        'https://bloomberg.com/news/articles/2026-11-24/xai-founders-unveil-new-ai-startup-to-predict-future-events',
        'Bloomberg',
        'industry',
        datetime(2026, 11, 24, tzinfo=timezone.utc),
        '三位 xAI 前联合创始人正式发布 Epochal，该平台提供互联网的按日期归档快照，允许 AI 代理以特定历史时间点为视角浏览和分析网页内容，从而复现当时的信息环境。核心产品是"历史浏览器沙箱"，可用于反事实推理、市场分析和新闻溯源等场景。Epochal 获得 2600 万美元种子轮融资，投资方包括 a16z 和 Sequoia。',
    ),
    NewsItem(
        '阿里巴巴新加坡子公司 Apex 被列入美国出口限制清单，涉嫌芯片转口',
        'https://aiweekly.co/ai-news-today',
        'AI Weekly / Reuters',
        'industry',
        datetime(2026, 11, 24, tzinfo=timezone.utc),
        '美国商务部将阿里巴巴旗下新加坡实体 Apex Technology 列入出口管制实体清单，指控其涉嫌向受限实体转口高端 GPU 芯片。这是继今年早些时候多家中东数据中心被调查后，美国政府在 AI 芯片出口管控上的最新行动。阿里巴巴发表声明否认违规，并表示将依法提出申诉。',
    ),
    NewsItem(
        'Tidal 宣布将 AI 生成音乐全面下架，保护原创艺人权益',
        'https://aiweekly.co/ai-news-today',
        'AI Weekly',
        'industry',
        datetime(2026, 11, 24, tzinfo=timezone.utc),
        '流媒体平台 Tidal 宣布将在未来 90 天内下架所有经确认为 AI 完全生成的音乐，并更新条款要求上传者声明作品的 AI 参与程度。Tidal 表示此举旨在维护人类艺术家的权益和平台内容质量，但允许 AI 辅助创作（需明确标注）。这一决定在音乐人和 AI 音乐工具开发者之间引发激烈讨论。',
    ),
    NewsItem(
        'Google DeepMind 发布 AlphaGenome 2，覆盖 68 种组织的基因组 AI 模型',
        'https://aiweekly.co/digest/2026-11-11-afternoon',
        'AI Weekly / DeepMind Blog',
        'research',
        datetime(2026, 11, 11, tzinfo=timezone.utc),
        'Google DeepMind 发布 AlphaGenome 2，训练数据包含超过 1 亿个跨 68 种人体组织的单细胞谱图。模型可预测特定基因组变异对基因表达和调控网络的影响，在稀有变异解读基准上超越前代 60% 以上。研究团队表示该模型将免费向学术机构开放，并已与多家制药公司签署合作协议。',
    ),
]

# --- 论文 ---
papers = [
    Paper(
        'Do LLM Agents Still Need to Be Told How to Self-Improve?',
        'https://arxiv.org/abs/2611.23219',
        '2611.23219',
        ['arXiv Authors'],
        '研究"自我改进"型 LLM 代理是否仍需要人工设计的改进策略。论文通过游戏环境测试发现，当代理拥有足够的上下文探索空间时，完全自主的改进循环（无需预设学习规则）可与人工设计方案相媲美，但在分布外任务上仍存在明显差距。结果表明"自主元学习"已接近实用阈值，但健壮性仍是主要挑战。',
        ['cs.AI', 'cs.LG'],
        datetime(2026, 11, 17, tzinfo=timezone.utc),
        None,
    ),
    Paper(
        'Do LLM Agents Compromise Like Humans? Risk and Responsibility in Dyadic Decision-Making',
        'https://arxiv.org/abs/2611.29069',
        '2611.29069',
        ['arXiv Authors'],
        '在二人风险决策实验中比较 LLM 代理与人类的妥协行为。研究发现 LLM 代理确实会向同伴决策靠拢，但底层动态与人类不同：人类的互惠调整更强，而 LLM 代理的收敛更多由输出分布的统计特性驱动，而非真正的社会推理。论文为多代理协作中的决策对齐问题提供了行为层面的实证基础。',
        ['cs.AI', 'cs.CL'],
        datetime(2026, 11, 21, tzinfo=timezone.utc),
        None,
    ),
    Paper(
        'Towards Identity-Preserving LLM Agents under Model Swaps',
        'https://arxiv.org/abs/2611.10628',
        '2611.10628',
        ['arXiv Authors'],
        '分析在保持角色定义和规则不变的情况下，更换 LLM 后端对代理行为的影响。研究在多个模型对（GPT-4o / Claude 3.7 / Gemini 2.5 Flash）上系统测试，发现行为漂移程度与模型对的"价值对齐距离"显著相关，并提出轻量级行为锚定层，可在不重训的情况下将行为一致性提升约 30%。',
        ['cs.AI', 'cs.SE'],
        datetime(2026, 11, 7, tzinfo=timezone.utc),
        None,
    ),
    Paper(
        'MAS-Guard: Unified Guardrails from Individual Agents to Multi-Agent LLM Systems',
        'https://arxiv.org/pdf/2610.28397',
        '2610.28397',
        ['arXiv Authors'],
        '提出统一的多代理安全护栏框架 MAS-Guard，同时覆盖单代理输入/输出过滤和多代理通信层的安全检查。核心创新是在代理间消息总线中插入轻量级安全分类器，可在不影响吞吐量的情况下拦截跨代理提示注入攻击，在红队测试中将成功攻击率降低约 73%。',
        ['cs.AI', 'cs.CR'],
        datetime(2026, 10, 28, tzinfo=timezone.utc),
        None,
    ),
    Paper(
        'Potential Emergence in LLM Agents: A Statistical Physics Perspective',
        'https://arxiv.org/abs/2611.27618',
        '2611.27618',
        ['Chen et al.'],
        '将多 LLM 代理系统的集体行为建模为统计物理中的相变过程，用配分函数刻画系统状态转移。研究发现代理数量超过特定阈值时，群体推理能力出现类似物理相变的"涌现"现象，提供了预测多代理系统何时产生单代理所不具备能力的理论框架。',
        ['cs.AI', 'cs.MA'],
        datetime(2026, 11, 20, tzinfo=timezone.utc),
        None,
    ),
]

# --- 大牛动态 ---
updates = [
    InfluencerUpdate(
        'António Guterres (UN)', 'Blog',
        '在巴巴多斯 AI 治理峰会发表主旨演讲，强调"AI 治理真空"是当前全球最紧迫的技术政策挑战之一，并呼吁在联合国框架内设立专门的 AI 监督机构。古特雷斯表示愿意担任推动各方达成共识的斡旋者角色，并将向安理会提交相关建议。',
        'https://aljazeera.com/news/2026/11/24/un-chief-calls-for-world-to-agree-on-ai-oversight-within-a-year',
        datetime(2026, 11, 24, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Kathy Hochul (NY Governor)', 'Blog',
        '宣布推动"儿童 AI 安全法案"，不仅针对 AI 玩具，还拟要求所有面向未成年人的 AI 产品强制披露训练数据来源、设置互动时长上限，并建立第三方审计机制。Hochul 表示："我们不能等到伤害发生后再行动，AI 时代需要超前立法。"',
        'https://aiweekly.co/ai-news-today',
        datetime(2026, 11, 24, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Simon Willison', 'Blog',
        '在个人博客发布长文《AI 代理的权限边界：从最小权限原则重新思考工具设计》，深入探讨 AI 代理在执行文件读写、网络请求、代码执行等工具调用时应如何设置权限沙箱。文章系统梳理了六种主流代理框架的权限模型差异，并提出"能力声明清单"设计模式。',
        'https://simonwillison.net/',
        datetime(2026, 11, 24, tzinfo=timezone.utc),
    ),
]

# --- GitHub 热门 ---
github = [
    GithubProject(
        'addyosmani/agent-skills',
        'https://github.com/addyosmani/agent-skills',
        'Curated collection of AI agent skills and tools for Claude Code, Cursor and GitHub Copilot. Surged to 116K+ stars, top AI skills engineering hub on GitHub.',
        116800, 9200, 'JavaScript', 430, [],
    ),
    GithubProject(
        'obra/superpowers',
        'https://github.com/obra/superpowers',
        'Agentic skills framework for Claude Code and other AI coding assistants. Consistently trending since last week\'s #1 spike, now at 325K+ total stars.',
        325400, 28100, 'Perl', 210, [],
    ),
    GithubProject(
        'debpalash/VoiceStudio',
        'https://github.com/debpalash/VoiceStudio',
        'Local AI voice cloning and dubbing tool. Zero cloud dependency, runs entirely on local GPU. #1 trending AI voice repo Nov 2026.',
        117200, 11600, 'Python', 380, [],
    ),
    GithubProject(
        'elementalsouls/Claude-BugHunter',
        'https://github.com/elementalsouls/Claude-BugHunter',
        'Automated bug hunting skill for Claude Code. Runs static analysis, fuzzing and AI-powered code review in one workflow.',
        20800, 1900, 'TypeScript', 290, [],
    ),
    GithubProject(
        'NY1024/AgentSafety-Papers',
        'https://github.com/NY1024/AgentSafety-Papers',
        'Daily auto-updated list of LLM agent security papers on arXiv, covering prompt injection, credential leakage, sandbox escape, and adversarial attacks.',
        9100, 780, 'Python', 240, [],
    ),
    GithubProject(
        'huggingface/transformers',
        'https://github.com/huggingface/transformers',
        'State-of-the-art ML models for PyTorch, TensorFlow, and JAX. Consistently trending as new model releases keep adding integrations.',
        149200, 29400, 'Python', 155, [],
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
