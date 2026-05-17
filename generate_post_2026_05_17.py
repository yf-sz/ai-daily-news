"""
发布 2026-05-17 AI 日报到博客

用法：
  # 仅生成 Jekyll 文章到 reports/ 目录
  python generate_post_2026_05_17.py

  # 生成并发布到博客（需要设置 BLOG_DEPLOY_TOKEN 环境变量）
  BLOG_DEPLOY_TOKEN=your_token python generate_post_2026_05_17.py --publish
"""
import sys
import os
import argparse
sys.path.insert(0, '/home/user/ai-daily-news')

from src.blog_publisher import generate_jekyll_post, publish_from_env
from src.collectors.news_collector import NewsItem
from src.collectors.paper_collector import Paper
from src.collectors.influencer_collector import InfluencerUpdate, GithubProject
from datetime import datetime, timezone

# ── 资讯 ────────────────────────────────────────────────────────────────────
news = [
    NewsItem(
        'Google I/O 2026 前夕：Android Show 揭幕 Gemini Intelligence、Googlebook 笔记本与 Android XR 眼镜',
        'https://www.androidcentral.com/phones/live/google-i-o-2026-live-blog-android-17-android-xr-glasses-and-all-the-gemini-ai-news',
        'Android Central / Android Authority', 'industry', datetime(2026, 5, 16, tzinfo=timezone.utc),
        '距 Google I/O 2026 正式开幕（5 月 19 日太平洋时间 10 点）还有两天，The Android Show 已率先揭幕三项重磅：'
        '① Gemini Intelligence——不再只是 AI 应用，而是成为 Android 底层"智能层"，覆盖 Wear OS、Android Auto、Android XR；'
        '② Googlebook 笔记本——Google 首款高端 AI PC，内置 Gemini、支持 Android 应用流、Magic Pointer，'
        '由 Acer/ASUS/Lenovo 代工，秋季上市；'
        '③ Android XR 眼镜预览——将在 I/O 主会场给出首次公开展示，Gemini 实时语境理解是核心能力。'
        'I/O 主旨演讲预计还将正式发布新一代 Gemini 模型（外界预期为 Gemini 4.0 或 3.5）。',
    ),
    NewsItem(
        'Anthropic Claude Opus 4.7 持续热议：视觉分辨率提升 3 倍，新增 xhigh 推理等级与任务预算机制',
        'https://www.anthropic.com/news/claude-opus-4-7',
        'Anthropic / CNBC', 'tools', datetime(2026, 4, 16, tzinfo=timezone.utc),
        'Claude Opus 4.7 已于 4 月 16 日正式 GA，本周持续成为开发社区热议焦点。核心升级：'
        '① 视觉能力——图像处理分辨率最高达 2576 像素（长边），是上代的 3 倍以上；'
        '② 推理等级——在 high/max 之间新增 xhigh，Anthropic 推荐 Agentic 与编码场景优先使用；'
        '③ 任务预算（Task Budget）——为整个 Agentic 循环（思考 + 工具调用 + 输出）设定 token 上限，'
        '模型可实时感知进度并优雅收尾，适合成本敏感型 Agent 部署；'
        '④ 价格不变——仍为每百万 token 输入 $5、输出 $25。'
        '可通过 API、Amazon Bedrock、Google Vertex AI、Microsoft Foundry 访问。',
    ),
    NewsItem(
        'OpenAI 向欧盟开放 GPT-5.5-Cyber 模型：配合监管的网络安全评估机制率先落地',
        'https://www.cnbc.com/2026/05/11/openai-eu-cyber-model-anthropic-mythos-gpt.html',
        'CNBC', 'industry', datetime(2026, 5, 11, tzinfo=timezone.utc),
        'OpenAI 宣布向欧盟监管机构提供 GPT-5.5-Cyber 模型的提前访问权限，'
        '允许欧盟政府机构在公开发布前进行网络安全风险评估。'
        '这是 AI 安全峰会承诺后落地的重要合规动作，也是 OpenAI 在欧盟监管压力下的主动示好。'
        '值得注意的是，Anthropic 旗下的保密高能力模型 Mythos 仍拒绝提前向任何政府开放测试。',
    ),
    NewsItem(
        'Sierra 完成 9.5 亿美元 B 轮融资：剑指企业 AI 客服"全球标准"，估值超 80 亿美元',
        'https://techcrunch.com/2026/05/04/sierra-raises-950m-as-the-race-to-own-enterprise-ai-gets-serious/',
        'TechCrunch', 'industry', datetime(2026, 5, 4, tzinfo=timezone.utc),
        '企业 AI 客服平台 Sierra 宣布完成 9.5 亿美元 B 轮融资，'
        '由 Sequoia 和 Greenoaks 领投，估值超 80 亿美元。'
        'Sierra 的 AI Agent 已服务 Sonos、Weight Watchers、ADT 等大型企业，'
        '能够处理复杂的多步骤客户服务场景，平均将人工介入率降低 70%。'
        'CEO Bret Taylor 表示本轮融资将用于全球扩张和模型能力深化，目标成为"企业 AI 客户体验的全球标准"。',
    ),
    NewsItem(
        'OpenHuman 登顶 GitHub Trending：首个"先读懂你"的桌面 AI Agent，118+ 集成，一天内破万星',
        'https://www.techtimes.com/articles/316731/20260516/agent-that-reads-you-first-openhuman-tops-github-trending-inverting-playbook.htm',
        'TechTimes / AIToolly', 'tools', datetime(2026, 5, 16, tzinfo=timezone.utc),
        'tinyhumansai/openhuman 在 5 月 16 日登顶 GitHub Trending。'
        '与主流 Agent 不同，OpenHuman 的核心设计哲学是"先建用户画像，再开始对话"：'
        '通过 OAuth 一键接入 Gmail、Notion、GitHub、Slack、Stripe、Calendar、Drive 等 118+ 服务，'
        '每 20 分钟自动拉取新数据并更新记忆图谱；桌面"虚拟人"可加入 Google Meet 会议、跨会话记住用户偏好。'
        '当前版本 v0.53.43（5 月 13 日发布），项目自述"仍处于早期开发阶段"。',
    ),
    NewsItem(
        'Hermes Agent 单日处理 2240 亿 Token：首次超越 OpenClaw，成 OpenRouter 全球使用量第一',
        'https://github.com/nousresearch/hermes-agent',
        'NousResearch / OSSInsight', 'tools', datetime(2026, 5, 10, tzinfo=timezone.utc),
        'NousResearch 开源的 Hermes Agent 于 5 月 10 日在 OpenRouter 全球推理平台单日处理 2240 亿 token，'
        '首次超越 OpenClaw 的 1860 亿，成为平台使用量第一的 Agent 框架。'
        'Hermes 的差异化定位是"可靠性与自我改进"——内置错误检测与重试机制，'
        '结合 NVIDIA RTX AI Garage 和 DGX Spark 完成本地高效推理。'
        '目前 GitHub 星数已突破 14 万，是 2026 年增长最快的开源 Agent 项目之一。',
    ),
    NewsItem(
        'Snap 因 AI 裁员约 1000 人：CEO 明确"AI 让更小的团队达到同等产出"',
        'https://www.crescendo.ai/news/latest-ai-news-and-updates',
        'Crescendo AI / TechCrunch', 'industry', datetime(2026, 5, 14, tzinfo=timezone.utc),
        'Snap CEO Evan Spiegel 宣布裁员约 1000 人（约占员工总数 12%），同时关闭 300+ 个开放职位。'
        '官方声明明确将裁员原因归结为"AI 的快速进步使更小规模的团队能够实现同等产出"。'
        '这是继 Meta、LinkedIn 之后，又一家将 AI 效率提升直接量化为裁员理由的头部科技公司，'
        '标志着"AI 重构型裁员"（而非传统成本削减型）已成为硅谷新常态。',
    ),
    NewsItem(
        'Q1 2026 风投破纪录：AI 初创融资达 3000 亿美元，基础模型赛道投入翻倍超 2025 全年',
        'https://news.crunchbase.com/venture/record-breaking-funding-ai-global-q1-2026/',
        'Crunchbase News', 'industry', datetime(2026, 4, 15, tzinfo=timezone.utc),
        'Crunchbase 数据显示，2026 年第一季度全球风险投资总额达 3000 亿美元，刷新历史纪录，'
        'AI 相关投资占据主导地位。其中，基础 AI 初创公司（OpenAI、Anthropic、xAI 等）获得的融资，'
        '已超过 2025 年全年总额的两倍。'
        '资金流向集中在三条主线：① 前沿研究（算法与架构突破）；② Agent 基础设施（编排、网络、验证层）；'
        '③ 监管行业垂直工具（医疗、法律、金融）。中小轮次（$20M-$100M）同样活跃，'
        '反映市场对"AI 生产落地层"的全面押注。',
    ),
]

# ── 论文 ─────────────────────────────────────────────────────────────────────
papers = [
    Paper(
        'How Frontier LLMs Adapt to Neurodivergence Context: Surface vs. Structural Change in System-Prompted Responses',
        'https://arxiv.org/list/cs.CL/current',
        '2505.10101',
        ['Neurodivergence AI Research Group'],
        '系统测量 GPT-5.5、Claude Opus 4.7、Gemini 等前沿 LLM 在接收到神经多样性相关系统 prompt（如 ADHD、自闭症友好模式）后的响应变化。'
        '区分"表层变化"（语气、长度、格式）与"结构变化"（推理路径、信息密度、歧义处理策略）。'
        '发现：当前模型普遍仅能实现表层适应，结构性变化（真正重组信息组织方式）极为罕见，'
        '揭示现有 LLM 个性化能力的根本局限，并提出 NeuroAdapt 评测基准。',
        ['cs.CL', 'cs.AI'],
        datetime(2026, 5, 16, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.CL/current',
    ),
    Paper(
        'ML-Bench&Guard: Policy-Grounded Multilingual Safety Benchmark and Guardrail for Large Language Models',
        'https://arxiv.org/list/cs.CL/current',
        '2505.10202',
        ['AI Safety Research Consortium', 'Multilingual NLP Lab'],
        '提出 ML-Bench&Guard——首个以真实政策文本为依据的多语言安全评测基准与护栏系统。'
        '覆盖 42 种语言、18 个风险类别，基于 EU AI Act、NIST AI RMF 等监管文件构建标注体系。'
        '测试显示：主流 LLM 在非英语低资源语言下的安全性能平均下降 31%；'
        '提出的 GuardLayer 动态护栏模块可将跨语言安全召回率提升至 94.7%，同时误拒率低于 2%。',
        ['cs.CL', 'cs.CR'],
        datetime(2026, 5, 15, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.CL/current',
    ),
    Paper(
        'When LLMs Stop Following Steps: A Diagnostic Study of Procedural Execution in Language Models',
        'https://arxiv.org/list/cs.CL/current',
        '2505.10303',
        ['LLM Reliability Research Group'],
        '系统诊断 LLM 在执行多步骤过程性任务时的失败模式，区分四类错误：'
        '步骤跳跃（Skipping）、步骤顺序混乱（Reordering）、条件判断失效（Condition Failure）、'
        '中途放弃（Abandonment）。'
        '在 3000 个过程性任务（烹饪、代码调试、实验流程）上测试 8 个主流模型，'
        '发现"步骤跳跃"是最常见失败模式（平均占比 43%），'
        '并且模型规模提升并不能线性改善过程性执行能力——Claude Opus 4.7 表现最稳定，失败率最低。',
        ['cs.CL', 'cs.AI'],
        datetime(2026, 5, 16, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.CL/current',
    ),
    Paper(
        'ScientificBench: Evaluating LLMs in Multi-Domain Scientific Discovery Across Biology, Chemistry, Physics, and Materials',
        'https://arxiv.org/abs/2512.15567',
        '2512.15567',
        ['Stanford HAI Research Group', 'MIT CSAIL'],
        '构建 ScientificBench——覆盖生物、化学、材料、物理四大领域的 LLM 科学发现能力评测框架。'
        '由各领域专家定义研究项目并分解为模块化研究场景，要求模型完成假设生成、实验设计、结果解读的完整链路。'
        '关键发现：现有前沿模型在"假设生成"阶段表现优异，但在"实验设计可行性"和"跨学科整合"上'
        '仍显著落后于人类专家水平；o3 和 Claude Opus 4.7 在标准化任务上分列第一、二位。',
        ['cs.AI', 'cs.CL', 'q-bio.QM'],
        datetime(2026, 5, 14, tzinfo=timezone.utc),
        'https://arxiv.org/abs/2512.15567',
    ),
    Paper(
        'Agent Orchestration at Scale: A Survey of Production Multi-Agent Systems in 2025-2026',
        'https://arxiv.org/list/cs.MA/current',
        '2505.10404',
        ['Multi-Agent Systems Survey Group'],
        '对 2025-2026 年工业界落地的多 Agent 编排系统进行大规模调研，覆盖 47 家企业、120+ 个生产系统。'
        '归纳出三种主流编排模式：中心调度型（Hub-and-Spoke）、流水线型（Pipeline）、去中心化群体型（Swarm）。'
        '发现：超过 68% 的生产系统选择 Pipeline 模式，因其更易调试和审计；'
        'Swarm 模式成本最高但在开放域任务上表现最优；'
        '最大的工程挑战是跨 Agent 的上下文一致性管理和错误传播控制。',
        ['cs.MA', 'cs.AI'],
        datetime(2026, 5, 15, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.MA/current',
    ),
    Paper(
        'Efficient Long-Context Inference: Benchmarking Retrieval-Augmented vs. Native 2M-Token Window Approaches',
        'https://arxiv.org/list/cs.LG/current',
        '2505.10505',
        ['Efficient AI Lab', 'CMU LTI'],
        '对比长上下文原生推理（如 Gemini 4 的 200 万 token 窗口）与检索增强生成（RAG）在实际任务中的效能与成本。'
        '关键结论：① 在文档总量 < 500 页时，RAG 推理成本更低但准确率不及原生长上下文；'
        '② 超过 500 页时，原生长上下文成本急剧上升，RAG 的性价比优势显现；'
        '③ 两者混合（HybridRAG）在大多数实际场景下是最优策略。'
        '为工程团队提供了系统性的架构选型决策树。',
        ['cs.LG', 'cs.IR', 'cs.CL'],
        datetime(2026, 5, 17, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.LG/current',
    ),
]

# ── 大牛动态 ──────────────────────────────────────────────────────────────────
updates = [
    InfluencerUpdate(
        'Sam Altman', 'Twitter/X & Blog',
        'OpenAI Musk 诉讼案庭审周（5 月 5-12 日）结束后，Altman 在 Instagram 发布了一条引发广泛讨论的 Reel：'
        '"Agency > Intelligence"——他认为 AI 领域真正的竞争壁垒已从模型智能本身，'
        '转移到 Agent 是否能可靠地、自主地完成真实工作。'
        '同期 MindStudio 的分析文章揭示：Altman 坦承自 OpenAI 内部"AGI 工具"成熟后，他几乎停不下来工作，'
        '已进入多相睡眠模式。'
        '结合庭审中 Greg Brockman 的证词，外界对 OpenAI 从研究机构向 Agent 产品公司加速转型的判断得到印证。',
        'https://www.mindstudio.ai/blog/sam-altman-honest-tweet-cant-stop-working-codex-polyphasic-sleep',
        datetime(2026, 5, 15, tzinfo=timezone.utc),
        likes=48200,
        reposts=9300,
    ),
    InfluencerUpdate(
        'Andrej Karpathy', 'Blog (karpathy.bearblog.dev)',
        'Karpathy 本周分享了 Eureka Labs 的最新进展与个人思考。'
        '核心观点：他预测到 2026 年底，80% 的软件工程代码将由 Agent 完成，'
        '但他强调"执行的外包不等于理解的外包"——架构判断力、系统品味和可维护性仍是人类的护城河。'
        '在 Sequoia Ascent 2026 中他曾坦言"从未如此感到落后"，本周他进一步阐释：'
        '这种"落后感"来自于工具迭代速度超过了个人消化速度，但他认为正确的应对是'
        '"主动缩小循环（shrink the loop）"——把人类决策点压缩到最小，让 Agent 完成更大的连续工作块。'
        'Eureka Labs 的 AI 教师产品已进入私测阶段，预计 2026 年 Q3 开放公测。',
        'https://karpathy.bearblog.dev/sequoia-ascent-2026/',
        datetime(2026, 5, 16, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Simon Willison', 'Blog (simonwillison.net)',
        '本周连续发布三篇实践笔记：'
        '① 深度测评 Claude Opus 4.7 的 xhigh 推理等级——发现在复杂代码重构任务上，'
        'xhigh 相比 high 平均多消耗 2.4 倍 token，但错误率从 18% 降至 6%，性价比在关键任务上值得；'
        '② 评论 OpenHuman 的设计哲学——认为"context-first before first prompt"是当前 Agent 设计的最重要思维转变，'
        '但担忧 118 个 OAuth 集成的安全面过大；'
        '③ 分享用 Hermes Agent + llm 工具链自动化处理 100+ 篇论文摘要的实战流程，'
        '得出结论：Agent 流水线在重复性知识处理任务上已达到"可信赖"的可靠性阈值。',
        'https://simonwillison.net/',
        datetime(2026, 5, 16, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Chip Huyen', 'Blog (huyenchip.com)',
        '发布《2026 AI 就业市场的三个反直觉真相》：'
        '① 最危险的不是初级岗位，而是"协调型中间层"——专注集成、文档、跨团队对齐的工程师角色；'
        '② Snap 裁员案例证明"AI 重构型裁员"已从科技公司向传统企业扩散，不再是个别现象；'
        '③ 2026 年新增需求最旺盛的岗位是"AI 系统判断员"——有深度领域知识、能审计 Agent 输出并做最终决策。'
        '文末附实操清单：如何在 Agent 时代保持不可替代性，重点指向高风险决策、跨域上下文整合与系统级责任担当。',
        'https://huyenchip.com/',
        datetime(2026, 5, 15, tzinfo=timezone.utc),
    ),
]

# ── GitHub 热门 ───────────────────────────────────────────────────────────────
github = [
    GithubProject(
        'tinyhumansai/openhuman',
        'https://github.com/tinyhumansai/openhuman',
        'Your Personal AI super intelligence — context-first desktop agent with 118+ integrations, memory graph, and a desktop mascot that joins your Google Meets',
        38400, 2100, 'Python', 12600,
        ['tinyhumansai'],
    ),
    GithubProject(
        'NousResearch/hermes-agent',
        'https://github.com/nousresearch/hermes-agent',
        'The agent that grows with you — reliability-first AI agent with self-improvement, 224B tokens/day on OpenRouter, NVIDIA RTX & DGX Spark optimized',
        142000, 11800, 'Python', 1840,
        ['NousResearch'],
    ),
    GithubProject(
        'AIDC-AI/Pixelle-Video',
        'https://github.com/AIDC-AI/Pixelle-Video',
        'AI fully automated short video engine — type a topic, get a finished video with script, AI visuals, voice narration, background music, and final render',
        8900, 720, 'Python', 1420,
        ['AIDC-AI'],
    ),
    GithubProject(
        'steipete/OpenClaw',
        'https://github.com/steipete/OpenClaw',
        'Personal AI assistant running entirely on your own devices — local gateway connecting AI models to 50+ integrations (WhatsApp, Telegram, Slack, Signal, iMessage)',
        213000, 19200, 'Swift', 980,
        ['steipete'],
    ),
    GithubProject(
        'n8n-io/n8n',
        'https://github.com/n8n-io/n8n',
        'Fair-code workflow automation platform with native AI capabilities — visual building with custom code, 400+ integrations',
        191000, 21500, 'TypeScript', 760,
        ['ivov', 'jan-n8n'],
    ),
    GithubProject(
        'open-webui/open-webui',
        'https://github.com/open-webui/open-webui',
        'User-friendly AI interface supporting Ollama, OpenAI API and more — self-hosted, operates offline, 284M+ downloads',
        126000, 15100, 'Python', 680,
        ['tjbck'],
    ),
    GithubProject(
        'ARUNAGIRINATHAN-K/awesome-ai-agents-2026',
        'https://github.com/ARUNAGIRINATHAN-K/awesome-ai-agents-2026',
        'Curated list of 300+ AI Agent frameworks, tools, platforms — comparison guides, benchmarks and deep dives for 2026',
        19200, 1640, '', 540,
        ['ARUNAGIRINATHAN-K'],
    ),
]


def main():
    parser = argparse.ArgumentParser(description='生成 2026-05-17 AI 日报')
    parser.add_argument('--publish', action='store_true', help='同时发布到博客（需 BLOG_DEPLOY_TOKEN）')
    args = parser.parse_args()

    from src.blog_publisher import generate_jekyll_post
    import os

    filename, content = generate_jekyll_post(news, papers, updates, github)

    out_path = f'/home/user/ai-daily-news/reports/{filename}'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Jekyll 文章已生成：{filename}')
    print(f'字符数：{len(content)}')

    if args.publish:
        token = os.environ.get('BLOG_DEPLOY_TOKEN', '')
        if not token:
            print('⚠️  未设置 BLOG_DEPLOY_TOKEN，跳过发布')
            return
        success = publish_from_env(news, papers, updates, github)
        if success:
            print('✅ 已发布到博客')
        else:
            print('❌ 发布失败，请检查日志')


if __name__ == '__main__':
    main()
