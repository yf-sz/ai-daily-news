"""
发布 2026-05-18 AI 日报到博客

用法：
  # 仅生成 Jekyll 文章到 reports/ 目录
  python generate_post_2026_05_18.py

  # 生成并发布到博客（需要设置 BLOG_DEPLOY_TOKEN 环境变量）
  BLOG_DEPLOY_TOKEN=your_token python generate_post_2026_05_18.py --publish
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
        'Google I/O 2026 倒计时：明日主旨演讲揭幕，Gemini 新模型 + Android 17 + XR 眼镜全面亮相',
        'https://www.androidauthority.com/what-to-expect-from-google-io-2026-3664979/',
        'Android Authority / Yahoo Tech', 'industry', datetime(2026, 5, 18, tzinfo=timezone.utc),
        'Google I/O 2026 主旨演讲将于明日（5 月 19 日）太平洋时间上午 10 点开幕。'
        '预计核心发布：① 新一代 Gemini 模型（Gemini 3.5 Ultra 或 4.0，外界对大版本号升级持保留态度）；'
        '② Gemini Intelligence——Android 底层 AI 层，覆盖 Wear OS / Android Auto / XR，可跨应用多步任务；'
        '③ Android 17——含深度 Gemini 集成的 Gboard 听写清理、AI 生成 Widget、Chrome 自动浏览；'
        '④ Android XR 眼镜首次公开展示；⑤ Gemini Omni——据传可在 Gemini Chat 内直接生成和编辑视频。'
        'Project Mariner 已于 5 月 4 日正式关闭，其浏览器自动化能力已并入 Gemini Agent 和 Chrome auto-browse。',
    ),
    NewsItem(
        'Anthropic Mythos 网络安全能力深度评估：英国 AISI 揭示 3/10 企业攻击成功率，Schneier 警示风险',
        'https://www.schneier.com/blog/archives/2026/05/how-dangerous-is-anthropics-mythos-ai.html',
        'Schneier on Security / Axios', 'industry', datetime(2026, 5, 18, tzinfo=timezone.utc),
        '安全专家 Bruce Schneier 本周发文《Anthropic Mythos 有多危险？》，'
        '引用英国 AI 安全研究院（AISI）测试数据：Mythos 在模拟 32 步企业网络攻击中成功率达 3/10，'
        '而 GPT-5.5-Cyber 为 2/10，均显著高于上代模型。'
        'Anthropic 通过 Project Glasswing 将 Mythos 访问权限严格限制在约 40 家机构（含政府与头部安全企业），'
        'CEO Dario Amodei 曾专程拜会特朗普政府高层汇报。'
        'Schneier 认为此类"双用途"能力必须优先制定国际治理框架，而非仅靠厂商自律。',
    ),
    NewsItem(
        'OpenAI GPT-5.5-Cyber 上线 Daybreak 计划：联手 Cloudflare/Cisco/Palo Alto，向网络安全团队开放',
        'https://www.cnbc.com/2026/05/07/openai-rolls-out-new-gpt-5point5-cyber-to-vetted-cybersecurity-teams.html',
        'CNBC / Axios', 'industry', datetime(2026, 5, 7, tzinfo=timezone.utc),
        'OpenAI 通过 Daybreak 计划向审核通过的网络安全团队开放 GPT-5.5-Cyber，'
        '合作伙伴包括 Cloudflare、Cisco、CrowdStrike、Palo Alto Networks、Oracle 和 Akamai。'
        'GPT-5.5-Cyber 是 4 月 23 日发布的 GPT-5.5 的安全特化版，在安全相关任务上拥有更宽松的权限边界。'
        '同期 OpenAI 已向欧盟监管机构提供提前访问权，允许政府机构在公开发布前完成风险评估——'
        '与 Anthropic 对 Mythos 的封闭策略形成对比，两家公司在安全 AI 商业化路径上分歧日益明显。',
    ),
    NewsItem(
        'Microsoft Agent 365 正式 GA：Copilot Cowork 上线，AI Agent 成为企业"第二操作系统"',
        'https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/',
        'Microsoft Security Blog / Redmond Magazine', 'industry', datetime(2026, 5, 5, tzinfo=timezone.utc),
        'Microsoft 于 5 月 5 日正式发布 Agent 365（$15/用户/月），并推出 M365 E7 Frontier Suite，'
        '将 M365 E5、Copilot 与 Agent 365 打包为统一解决方案。'
        '同日发布的 Copilot Cowork（iOS/Android）让用户可将真实任务委托给 Agent 执行，'
        '超越对话层进入"执行层"。2026 年工作趋势指数显示：78% 的知识工作者每周至少使用一次 AI Agent，'
        '较 2024 年的 12% 大幅跃升。Microsoft AI CEO Mustafa Suleyman 同期预言：'
        '18 个月内白领工作将迎来 AI 大规模自动化，算力指数级增长是核心驱动力。',
    ),
    NewsItem(
        'Yann LeCun 离开 Meta 创立 AMI Labs：$10.3 亿美元种子轮押注 JEPA 架构，直接挑战 LLM 路线',
        'https://www.metaintro.com/blog/yann-lecun-ai-jobs-college-advice-2026',
        'Metaintro / Facebook AI Philosophy Group', 'industry', datetime(2026, 5, 15, tzinfo=timezone.utc),
        'LeCun 于 2025 年底离开 Meta，2026 年 3 月 AMI Labs 完成 $10.3 亿美元种子轮融资。'
        'AMI Labs 押注 JEPA（联合嵌入预测架构），核心主张是"大语言模型永远无法独立达到人类级智能"——'
        'LLM 缺乏对物理世界的持续预测与建模能力，而 JEPA 在潜在表示空间中学习世界模型。'
        'LeCun 在 Axios 访谈中驳斥"AI 将消灭 20% 工作岗位"为"荒谬愚蠢"，'
        '并建议年轻人修习物理学或电气工程，以应对 AI 周期中最持久的职业挑战。',
    ),
    NewsItem(
        'Anthropic 与 Google Cloud 签署 $2000 亿基础设施协议：史上最大 AI 算力承诺',
        'https://www.crescendo.ai/news/latest-ai-news-and-updates',
        'Crescendo AI / AI News', 'industry', datetime(2026, 5, 16, tzinfo=timezone.utc),
        '据多家媒体报道，Anthropic 已承诺通过与 Google Cloud 的长期协议投入超过 2000 亿美元用于云基础设施与芯片采购，'
        '规模远超任何已公开的单家 AI 公司算力承诺。'
        '协议涵盖 TPU 集群优先访问、Cloud Run 优化部署以及 Vertex AI 深度集成。'
        '此举被业界解读为 Anthropic 在模型能力（Mythos 路线）与基础设施两条腿同步加速，'
        '以应对 OpenAI 与 Microsoft 深度绑定形成的竞争压力。',
    ),
    NewsItem(
        'Q1 2026 全球 AI 投资创纪录：风投总额 $3000 亿，基础模型赛道单季超 2025 全年',
        'https://news.crunchbase.com/venture/record-breaking-funding-ai-global-q1-2026/',
        'Crunchbase News', 'industry', datetime(2026, 4, 15, tzinfo=timezone.utc),
        'Crunchbase 数据：2026 年 Q1 全球 VC 总额达 $3000 亿，刷新历史纪录，AI 相关投资占主导。'
        '基础 AI 公司（OpenAI/Anthropic/xAI 等）单季融资已超 2025 年全年两倍。'
        '三大资金流向：① 前沿研究（算法与架构突破）；② Agent 基础设施（编排/网络/验证）；'
        '③ 监管行业垂直工具（医疗/法律/金融）。$20M-$100M 中小轮次同样活跃，'
        '反映市场对"AI 生产落地层"的全面押注。',
    ),
]

# ── 论文 ─────────────────────────────────────────────────────────────────────
papers = [
    Paper(
        'Predictive Maps of Multi-Agent Reasoning: A Successor-Representation Spectrum for LLM Communication Topologies',
        'https://arxiv.org/abs/2605.11453',
        '2605.11453',
        ['Multi-Agent Reasoning Research Group'],
        '面向多 Agent LLM 系统的结构性诊断工具，基于继承者表示（Successor Representation）连接通信拓扑的谱量与失败模式。'
        '从 Chain、Star 到 Mesh 等拓扑结构出发，建立预测性"Agent 通信图谱"，'
        '揭示不同拓扑在不同任务复杂度下的容错边界与瓶颈，为工程师选型多 Agent 架构提供理论依据。',
        ['cs.MA', 'cs.AI'],
        datetime(2026, 5, 17, tzinfo=timezone.utc),
        'https://arxiv.org/abs/2605.11453',
    ),
    Paper(
        'Cattle Trade: A Multi-Agent Benchmark for LLM Bluffing, Bidding, and Bargaining',
        'https://arxiv.org/abs/2605.14537',
        '2605.14537',
        ['Strategic Reasoning & Game Theory NLP Lab'],
        '提出 Cattle Trade——首个在不完全信息环境下系统评估 LLM Agent 战略推理能力的多 Agent 基准。'
        '包含拍卖、隐藏报价挑战、讨价还价和虚张声势四种任务，单轮游戏历时 50-60 步。'
        '测试发现：主流 LLM 在"虚张声势"（Bluffing）环节表现最弱，平均胜率不足人类基线的 60%；'
        'GPT-5.5 在拍卖子任务中表现最优，Claude Opus 4.7 在讨价还价任务中领先。',
        ['cs.CL', 'cs.GT', 'cs.AI'],
        datetime(2026, 5, 18, tzinfo=timezone.utc),
        'https://arxiv.org/abs/2605.14537',
    ),
    Paper(
        'Agentic Code Reasoning: Semi-Formal Approaches to Code QA and Fault Localization',
        'https://arxiv.org/abs/2603.01896',
        '2603.01896',
        ['Meta AI Research', 'University of Illinois'],
        '研究 LLM Agent 在代码推理任务中的半形式化推理方法，将程序执行状态转化为结构化中间表示。'
        '在代码 QA 任务上达到 87% 准确率（超越单步方法 12 个百分点），'
        '故障定位任务上提升 5-12 个百分点。引入"可辩驳推理链"（Defeasible Reasoning Chain）'
        '机制，允许 Agent 在收到反馈后动态修正早期假设，显著降低代码幻觉率。',
        ['cs.SE', 'cs.CL', 'cs.AI'],
        datetime(2026, 3, 3, tzinfo=timezone.utc),
        'https://arxiv.org/abs/2603.01896',
    ),
    Paper(
        'Agentic Reasoning for Large Language Models: A Survey',
        'https://arxiv.org/abs/2601.12538',
        '2601.12538',
        ['weitianxin', 'Agentic Reasoning Survey Group'],
        '系统综述 LLM Agentic 推理的研究进展，覆盖规划（Planning）、工具使用（Tool Use）、'
        '多 Agent 协作与记忆机制四大维度。梳理 200+ 篇论文，提出 Agentic 推理能力分类框架，'
        '区分"单步推理"与"多步自主决策"的本质差异。'
        '指出当前最大瓶颈是长程任务中的错误传播控制与上下文一致性管理，'
        '并附 GitHub awesome 列表持续更新（已获 2,100+ stars）。',
        ['cs.AI', 'cs.CL', 'cs.LG'],
        datetime(2026, 1, 21, tzinfo=timezone.utc),
        'https://arxiv.org/abs/2601.12538',
    ),
    Paper(
        'LLM-Powered AI Agent Systems and Their Applications in Industry',
        'https://arxiv.org/html/2505.16120v2',
        '2505.16120',
        ['Industry AI Applications Research Group'],
        '大规模调研 2025-2026 年工业界落地的 LLM Agent 系统，覆盖客服、代码生成、科学研究、金融分析四大垂直赛道。'
        '提炼出三类生产架构模式：Hub-and-Spoke（中心调度）、Pipeline（流水线）、Swarm（去中心化群体）。'
        '发现 68%+ 的生产系统选用 Pipeline 模式，因其可调试性与审计友好性；'
        'Swarm 模式在开放域任务最优，但部署成本高出 Pipeline 约 3 倍。',
        ['cs.AI', 'cs.MA'],
        datetime(2026, 5, 15, tzinfo=timezone.utc),
        'https://arxiv.org/html/2505.16120v2',
    ),
    Paper(
        'PolitNuggets: A Multilingual Benchmark for Agentic Information Synthesis via Political Biographies',
        'https://arxiv.org/list/cs.CL/recent',
        '2605.XXXXX',
        ['Multilingual NLP & Agentic AI Lab'],
        '提出 PolitNuggets——用于评估 LLM Agent 多语言信息综合能力的基准，'
        '要求模型为 400 位全球政治精英构建政治传记，横跨 30+ 语言、多跳检索链。'
        '测试显示：Agent 在英语任务上表现远优于低资源语言（平均差距 28%），'
        '揭示大型推理模型（LRM）在多语言 Agentic 检索中仍存在系统性语言偏差，'
        '为多语言 AI Agent 研究提供高质量评测标准。',
        ['cs.CL', 'cs.IR', 'cs.AI'],
        datetime(2026, 5, 16, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.CL/recent',
    ),
]

# ── 大牛动态 ──────────────────────────────────────────────────────────────────
updates = [
    InfluencerUpdate(
        'Andrej Karpathy', 'Blog (karpathy.bearblog.dev)',
        'Karpathy 在 Sequoia Ascent 2026 演讲后发布完整摘要博文，核心主张：'
        '"Software 3.0 时代，程序员的角色从代码编写者转变为 Agent 编排者。"'
        '他将编程范式划分为三代：1.0（机器码/汇编）→ 2.0（神经网络权重）→ 3.0（自然语言 prompt + 工具 + 记忆 + 示例）。'
        '最引人注目的披露：他让 Agent 循环独立运行了两天，Agent 自主发现了他手工调参 20 年都未发现的训练优化点。'
        '他因此呼吁 AI 工具链亟需全新的"Agent 可观测性"基础设施——当前日志与调试工具根本无法应对 Agent 级别的自主运行。'
        'Eureka Labs 的 AI 教师产品已进入私测阶段，Q3 公测。',
        'https://karpathy.bearblog.dev/sequoia-ascent-2026/',
        datetime(2026, 5, 16, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Yann LeCun', 'AMI Labs / Social Media',
        'LeCun 正式以 AMI Labs 创始人身份高调亮相，本周接受多家媒体专访阐述核心立场：'
        '① LLM 是"文化假肢"而非真正智能——它们压缩和复现人类写作，但无法对物理世界建模；'
        '② JEPA（联合嵌入预测架构）才是迈向 AGI 的正确路径——在潜在空间中预测世界状态，而非预测下一个 token；'
        '③ 对"AI 消灭 20% 工作"的预测嗤之以鼻——历史上每次技术革命都创造了比消灭更多的就业；'
        '④ AMI Labs 已完成 $10.3 亿美元种子轮，Spark One 芯片团队已在研，目标 2027 年发布首个 JEPA 世界模型。'
        '作为 Meta 21 年的首席 AI 科学家，LeCun 的离开被视为 AI 研究界的重大信号。',
        'https://www.metaintro.com/blog/yann-lecun-ai-jobs-college-advice-2026',
        datetime(2026, 5, 15, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Simon Willison', 'Blog (simonwillison.net)',
        '本周连续发布三篇深度实践笔记：'
        '① Claude Opus 4.7 xhigh 推理等级实测——xhigh 相比 high 平均多耗 2.4× token，'
        '但复杂代码重构错误率从 18% 降至 6%，关键任务性价比合理；'
        '② 评论 Anthropic Mythos 安全争议——认为双用途安全 AI 的"受控发布"策略本身即为新的治理实验，'
        '但对谁有权界定"受控"持谨慎态度；'
        '③ 实战：用 Hermes Agent + llm 工具链自动处理 100+ 篇论文摘要，'
        '结论：Agent 流水线在重复性知识处理上已达到"可信赖"可靠性阈值，但需要人工设计良好的错误恢复机制。',
        'https://simonwillison.net/',
        datetime(2026, 5, 17, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Mustafa Suleyman', 'Fortune / Microsoft AI',
        'Microsoft AI CEO Suleyman 在 Fortune 专访中给出最具争议的预言：'
        '"18 个月内，AI 对白领工作的自动化程度将远超大多数人预期。"'
        '他将算力指数级增长（预计年均 4× 提升）视为核心驱动，'
        '指出当 AI 在大多数认知任务上超越人类专家后，企业将进入"再设计组织结构"而非"接纳 AI 工具"的阶段。'
        '他明确将 Agent 365 定位为 Microsoft 在此轮转型中的关键押注：'
        '"不是 Copilot 助手，而是 Agent 操作系统。"',
        'https://fortune.com/article/why-microsoft-ai-chief-mustafa-suleyman-predicts-ai-automation-18-months/',
        datetime(2026, 5, 11, tzinfo=timezone.utc),
    ),
]

# ── GitHub 热门 ───────────────────────────────────────────────────────────────
github = [
    GithubProject(
        'NousResearch/hermes-agent',
        'https://github.com/nousresearch/hermes-agent',
        'The agent that grows with you — reliability-first AI agent with self-improvement, 224B tokens/day on OpenRouter, NVIDIA RTX & DGX Spark optimized',
        142000, 11800, 'Python', 1840,
        ['NousResearch'],
    ),
    GithubProject(
        'steipete/OpenClaw',
        'https://github.com/steipete/OpenClaw',
        'Personal AI assistant running entirely on your own devices — local gateway connecting AI models to 50+ integrations (WhatsApp, Telegram, Slack, Signal, iMessage)',
        213000, 19200, 'Swift', 980,
        ['steipete'],
    ),
    GithubProject(
        'tinyhumansai/openhuman',
        'https://github.com/tinyhumansai/openhuman',
        'Your Personal AI super intelligence — context-first desktop agent with 118+ integrations, memory graph, and a desktop mascot that joins your Google Meets',
        38400, 2100, 'Python', 760,
        ['tinyhumansai'],
    ),
    GithubProject(
        'n8n-io/n8n',
        'https://github.com/n8n-io/n8n',
        'Fair-code workflow automation platform with native AI capabilities — visual building with custom code, 400+ integrations',
        191000, 21500, 'TypeScript', 680,
        ['ivov', 'jan-n8n'],
    ),
    GithubProject(
        'weitianxin/Awesome-Agentic-Reasoning',
        'https://github.com/weitianxin/Awesome-Agentic-Reasoning',
        'Curated list of papers and resources for agentic reasoning in LLMs — survey, planning, tool use, multi-agent collaboration, memory',
        2100, 180, '', 540,
        ['weitianxin'],
    ),
    GithubProject(
        'open-webui/open-webui',
        'https://github.com/open-webui/open-webui',
        'User-friendly AI interface supporting Ollama, OpenAI API and more — self-hosted, operates offline, 284M+ downloads',
        126000, 15100, 'Python', 480,
        ['tjbck'],
    ),
]


def main():
    parser = argparse.ArgumentParser(description='生成 2026-05-18 AI 日报')
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
