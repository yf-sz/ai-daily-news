"""
发布 2026-05-19 AI 日报到博客

用法：
  # 仅生成 Jekyll 文章到 reports/ 目录
  python generate_post_2026_05_19.py

  # 生成并发布到博客（需要设置 BLOG_DEPLOY_TOKEN 环境变量）
  BLOG_DEPLOY_TOKEN=your_token python generate_post_2026_05_19.py --publish
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
        'Google I/O 2026 主旨演讲：Gemini 4.0、Gemini Omni、Android XR 眼镜全面亮相',
        'https://www.androidcentral.com/phones/live/google-i-o-2026-live-blog-android-17-android-xr-glasses-and-all-the-gemini-ai-news',
        'Android Central / The Next Web', 'industry', datetime(2026, 5, 19, tzinfo=timezone.utc),
        'Google I/O 2026 于今日（5 月 19 日）太平洋时间上午 10 点正式开幕。核心发布：'
        '① Gemini 4.0——相较 3.x 系列实质性升级，深度整合 Android 与 ChromeOS（内部代号"Gemini Intelligence"）；'
        '② Gemini Omni——统一文本/图像/视频生成管道，支持视频混剪、上下文内编辑，基于 Veo 架构演进；'
        '③ Android XR 眼镜首次公开展示，四大硬件合作伙伴上台（三星"Jinju"、XREAL Project Aura、Warby Parker、Gentle Monster）；'
        '④ Googlebooks——全新 Android 笔记本品类，秋季上市，Acer/ASUS/Lenovo 首批入局；'
        '⑤ Android 17 Beta 4 公布，正式版 6 月发布，Gboard Rambler 语音听写清理、AI Widget 生成等新功能上线。',
    ),
    NewsItem(
        '马斯克诉 OpenAI 案联邦陪审团驳回全部索赔：不足两小时裁定，$1500 亿赔偿请求落空',
        'https://www.nbcnews.com/tech/tech-news/openai-elon-musk-case-verdict-rcna345655',
        'NBC News / US News', 'industry', datetime(2026, 5, 18, tzinfo=timezone.utc),
        '联邦陪审团于 5 月 18 日周一以不足两小时审议，一致裁定马斯克诉 OpenAI 及 CEO Sam Altman 案件因超出诉讼时效而全部不成立。'
        '马斯克曾寻求约 $1500 亿美元赔偿，主张 Altman 与总裁 Brockman 违反将 OpenAI 维持非营利性承诺。'
        '陪审团同时驳回马斯克关于微软协助违约的指控。马斯克法律团队表示将提起上诉。'
        '此案是 AI 治理领域里程碑式司法事件，涉及初创承诺与商业化转型之间的法律边界。',
    ),
    NewsItem(
        'Cursor Composer 2.5 发布：基于 Kimi K2.5，25× 合成任务训练，对标 Opus 4.7 与 GPT-5.5',
        'https://the-decoder.com/cursors-composer-2-5-matches-opus-4-7-and-gpt-5-5-benchmarks-at-a-fraction-of-the-cost/',
        'The Decoder / Winbuzzer', 'tools', datetime(2026, 5, 18, tzinfo=timezone.utc),
        'Cursor 发布 Composer 2.5——以 Moonshot AI 开源 Kimi K2.5（MoE 架构）为底座，'
        '85% 算力预算投入额外训练与强化学习，合成任务量达前代 25 倍。'
        'SWE-Bench Multilingual 得分 79.8%、CursorBench v3.1 得分 63.2%，对标 Opus 4.7 与 GPT-5.5 旗舰性能，'
        '定价仅 $0.5/MTok 输入、$2.50/MTok 输出，大幅低于同级别闭源模型。'
        '此次发布再度引发开源中国底座模型在商业 AI 工具链中的话题讨论。',
    ),
    NewsItem(
        'Anthropic Claude Managed Agents 更新：新增"Dreaming"记忆、多 Agent 编排与 AWS 原生部署',
        'https://9to5mac.com/2026/05/07/anthropic-updates-claude-managed-agents-with-three-new-features/',
        '9to5Mac / InfoQ', 'industry', datetime(2026, 5, 7, tzinfo=timezone.utc),
        'Anthropic Claude Managed Agents 新增三大特性：'
        '① Dreaming——跨 session 回顾历史对话以发现模式，实现 Agent 自我改进的记忆扩展机制；'
        '② 多 Agent 编排——原生支持 Agent 间协调与子任务委派；'
        '③ Agent Skills——可复用的技能插件机制，内置 20+ 法律 MCP 连接器与 12 个专业领域插件。'
        '同日推出 Claude Platform on AWS，通过 AWS 账单与 IAM 鉴权直接访问 Claude API、Files API 与 Message Batches API，'
        '以及 Claude for Small Business（集成 QuickBooks/HubSpot/Canva/Docusign 等）。',
    ),
    NewsItem(
        'Anthropic 为 Claude Code 推出 Routines：定时/事件驱动自动化编码工作流',
        'https://www.infoq.com/news/2026/05/anthropic-routines-claude/',
        'InfoQ / Anthropic', 'tools', datetime(2026, 5, 19, tzinfo=timezone.utc),
        'Anthropic 正式发布 Claude Code Routines——开发者可配置在定时计划、API 调用或外部事件触发时自动执行的编码工作流。'
        '同期上线 Agent View，支持从单个 CLI 界面管理多并发 Claude Code 会话：启动 Agent、后台运行、状态预览、按需跳入。'
        '此功能将 Claude Code 从交互式助手推进至可调度的自动化工程基础设施阶段，'
        '契合"Software 3.0"时代对 Agent 可观测性与编排能力的核心诉求。',
    ),
    NewsItem(
        'DeepMind AI 协同数学家攻克 60 年悬案：牛津数学家借助 Agent 解决 Kourovka Notebook 第 21.10 题',
        'https://asanify.com/blog/news/ai-mathematical-reasoning-may-12-2026/',
        'Asanify / arXiv', 'research', datetime(2026, 5, 12, tzinfo=timezone.utc),
        'DeepMind 于 arXiv 发布 AI Co-Mathematician（2605.06651），一个面向开放性数学研究的 Agentic 工作台。'
        '系统提供异步有状态工作空间，整合假设生成、文献搜索、计算探索与定理证明。'
        '牛津数学家 Marc Lackenby 借助该系统解决了群论领域悬置 60 年的 Kourovka Notebook 第 21.10 题，'
        '并在 FrontierMath Tier 4 上达到 48% 得分——标志 AI 在前沿数学研究中实质性参与的新里程碑。',
    ),
]

# ── 论文 ─────────────────────────────────────────────────────────────────────
papers = [
    Paper(
        'AI co-mathematician: Accelerating mathematicians with agentic AI',
        'https://arxiv.org/abs/2605.06651',
        '2605.06651',
        ['Google DeepMind', 'Oxford Mathematics'],
        '面向开放性数学研究的 Agentic 工作台。系统提供异步有状态工作空间，整合假设生成、文献搜索、'
        '计算探索、定理证明与理论构建，映射真实数学家协作流程中的不确定性管理与迭代求精过程。'
        '早期测试中协助解决公开问题、发现新研究方向，并还原被忽视的文献引用。'
        'FrontierMath Tier 4 得分 48%；牛津数学家 Marc Lackenby 利用该系统解决了 Kourovka Notebook 第 21.10 题——'
        '一道困扰群论界 60 年的公开难题。',
        ['cs.AI', 'math.GR'],
        datetime(2026, 5, 7, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2605.06651',
    ),
    Paper(
        'Predictive Maps of Multi-Agent Reasoning: A Successor-Representation Spectrum for LLM Communication Topologies',
        'https://arxiv.org/abs/2605.11453',
        '2605.11453',
        ['Multi-Agent Reasoning Research Group'],
        '面向多 Agent LLM 系统的结构性诊断工具，基于继承者表示（Successor Representation）'
        '连接通信拓扑的谱量与失败模式。从 Chain、Star 到 Mesh 等拓扑结构出发，'
        '建立预测性"Agent 通信图谱"，揭示不同拓扑在不同任务复杂度下的容错边界与瓶颈，'
        '为工程师选型多 Agent 架构提供理论依据。',
        ['cs.MA', 'cs.AI'],
        datetime(2026, 5, 17, tzinfo=timezone.utc),
        'https://arxiv.org/abs/2605.11453',
    ),
    Paper(
        'Cattle Trade: A Multi-Agent Benchmark for LLM Bluffing, Bidding, and Bargaining',
        'https://arxiv.org/abs/2605.14537',
        '2605.14537',
        ['Strategic Reasoning & Game Theory NLP Lab'],
        '首个在不完全信息环境下系统评估 LLM Agent 战略推理能力的多 Agent 基准。'
        '包含拍卖、隐藏报价挑战、讨价还价和虚张声势四种任务，单轮游戏历时 50-60 步。'
        '测试发现主流 LLM 在"虚张声势"（Bluffing）环节表现最弱，平均胜率不足人类基线的 60%；'
        'GPT-5.5 在拍卖子任务中表现最优，Claude Opus 4.7 在讨价还价任务中领先。',
        ['cs.CL', 'cs.GT', 'cs.AI'],
        datetime(2026, 5, 18, tzinfo=timezone.utc),
        'https://arxiv.org/abs/2605.14537',
    ),
    Paper(
        'LLM-Powered AI Agent Systems and Their Applications in Industry',
        'https://arxiv.org/html/2505.16120v2',
        '2505.16120',
        ['Industry AI Applications Research Group'],
        '大规模调研 2025-2026 年工业界落地的 LLM Agent 系统，覆盖客服、代码生成、科学研究、金融分析四大垂直赛道。'
        '提炼三类生产架构模式：Hub-and-Spoke（中心调度）、Pipeline（流水线）、Swarm（去中心化群体）。'
        '发现 68%+ 的生产系统选用 Pipeline 模式，因其可调试性与审计友好性；'
        'Swarm 模式在开放域任务最优，但部署成本高出 Pipeline 约 3 倍。',
        ['cs.AI', 'cs.MA'],
        datetime(2026, 5, 15, tzinfo=timezone.utc),
        'https://arxiv.org/html/2505.16120v2',
    ),
    Paper(
        'Agentic Code Reasoning: Semi-Formal Approaches to Code QA and Fault Localization',
        'https://arxiv.org/abs/2603.01896',
        '2603.01896',
        ['Meta AI Research', 'University of Illinois'],
        '研究 LLM Agent 在代码推理任务中的半形式化方法，将程序执行状态转化为结构化中间表示。'
        '代码 QA 任务准确率 87%（超越单步方法 12 个百分点），故障定位提升 5-12 个百分点。'
        '引入"可辩驳推理链"（Defeasible Reasoning Chain），允许 Agent 在收到反馈后动态修正早期假设，'
        '显著降低代码幻觉率。',
        ['cs.SE', 'cs.CL', 'cs.AI'],
        datetime(2026, 3, 3, tzinfo=timezone.utc),
        'https://arxiv.org/abs/2603.01896',
    ),
]

# ── 大牛动态 ──────────────────────────────────────────────────────────────────
updates = [
    InfluencerUpdate(
        'Sundar Pichai / Google DeepMind', 'Google I/O Keynote',
        'Pichai 在 Google I/O 2026 主旨演讲中高调宣布 Gemini 全线升级：'
        '"我们今天发布的不是单个模型，而是一个贯穿 Android、搜索、Chrome 和开发者工具的智能层。"'
        'Gemini Intelligence 被定位为"Android 的第二大脑"，覆盖 Wear OS / Android Auto / XR；'
        'Gemini Omni 视频生成能力被描述为"在 Gemini Chat 中直接完成从创意到成片的全流程"。'
        'CEO 明确指出 Google 在 AI 能力排名上目前落后于 Anthropic Mythos 与 OpenAI GPT-5.5，'
        '但强调 Google 的优势在于"覆盖 30 亿设备的分发能力与最大的第一方数据生态"。',
        'https://io.google/2026/',
        datetime(2026, 5, 19, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Andrej Karpathy', 'Blog (karpathy.bearblog.dev)',
        '今日在 Google I/O 期间于社交媒体发文评论 Gemini 4.0 发布：'
        '"Gemini Intelligence 是 Google 对 Software 3.0 的战略回应——把 AI 从对话框下沉到操作系统层，'
        '这才是真正的平台级卡位。"同时转发了 I/O 开发者专题内容，关注 Gemini API 新增的 Agent 原生端点。'
        '他指出 Google 的 XR 眼镜路线（先无显示器、再加显示器）与 Meta 的"全功能优先"战略形成鲜明对比，'
        '"无显示器版正好验证 AI 语音 Agent 对硬件的最低依赖假设。"',
        'https://karpathy.bearblog.dev/',
        datetime(2026, 5, 19, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Simon Willison', 'Blog (simonwillison.net)',
        '发布 Musk vs OpenAI 庭审结果速评：'
        '"陪审团两小时结束审议，这个速度本身就说明问题——Musk 的时效论据从未真正站稳脚跟。"'
        '他对判决实质意义的评估：此案更像是一场关于 AI 治理话语权的公开战，而非可胜诉的法律主张。'
        '同日发布 Cursor Composer 2.5 上手笔记：在多文件重构任务中 Composer 2.5 比 Opus 4.7 快 40%，'
        '成本低 6×，"对于日常编码任务，这已经是‘足够好’的门槛。"',
        'https://simonwillison.net/',
        datetime(2026, 5, 19, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Yann LeCun', 'AMI Labs / LinkedIn',
        'LeCun 今日发文回应 Google I/O 的 Gemini Omni 发布，维持一贯立场：'
        '"无论是 Gemini Omni 还是 GPT-5.5，都是在扩大同一类架构的规模——预测 Token。'
        'JEPA 的赌注是：真正的感知-行动闭环需要在潜在空间预测世界状态，而不是在词汇表上做概率分布。"'
        'AMI Labs 同期披露 Spark One 推理芯片研发进展：'
        '"目标是让 JEPA 世界模型在边缘设备上以 <10ms 延迟运行，2027 年见。"',
        'https://www.linkedin.com/in/yann-lecun/',
        datetime(2026, 5, 19, tzinfo=timezone.utc),
    ),
]

# ── GitHub 热门 ───────────────────────────────────────────────────────────────
github = [
    GithubProject(
        'steipete/OpenClaw',
        'https://github.com/steipete/OpenClaw',
        'Personal AI assistant running entirely on your own devices — local gateway connecting AI models to 50+ integrations (WhatsApp, Telegram, Slack, Signal, iMessage)',
        213000, 19200, 'Swift', 1240,
        ['steipete'],
    ),
    GithubProject(
        'NousResearch/hermes-agent',
        'https://github.com/nousresearch/hermes-agent',
        'The agent that grows with you — reliability-first AI agent with self-improvement, optimized for NVIDIA RTX & DGX Spark',
        147000, 12100, 'Python', 980,
        ['NousResearch'],
    ),
    GithubProject(
        'mattpocock/skills',
        'https://github.com/mattpocock/skills',
        'AI agent skills & behavioral patterns for coding workflows — the fastest-growing repo in the Claude Code ecosystem',
        18600, 1420, 'TypeScript', 1618,
        ['mattpocock'],
    ),
    GithubProject(
        'tinyhumansai/openhuman',
        'https://github.com/tinyhumansai/openhuman',
        'Your Personal AI super intelligence — context-first desktop agent with 118+ integrations, memory graph, and a desktop mascot that joins your Google Meets',
        40200, 2180, 'Python', 860,
        ['tinyhumansai'],
    ),
    GithubProject(
        'open-webui/open-webui',
        'https://github.com/open-webui/open-webui',
        'User-friendly AI interface supporting Ollama, OpenAI API and more — self-hosted, operates offline, 284M+ downloads',
        126000, 15100, 'Python', 520,
        ['tjbck'],
    ),
    GithubProject(
        'VoltAgent/awesome-ai-agent-papers',
        'https://github.com/VoltAgent/awesome-ai-agent-papers',
        'Curated collection of AI agent research papers 2026 — agent engineering, memory, evaluation, workflows, autonomous systems',
        4800, 380, '', 490,
        ['VoltAgent'],
    ),
]


def main():
    parser = argparse.ArgumentParser(description='生成 2026-05-19 AI 日报')
    parser.add_argument('--publish', action='store_true', help='同时发布到博客（需 BLOG_DEPLOY_TOKEN）')
    args = parser.parse_args()

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
