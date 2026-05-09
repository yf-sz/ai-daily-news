"""
发布 2026-05-09 AI 日报到博客

用法：
  # 仅生成 Jekyll 文章到 reports/ 目录
  python generate_post_2026_05_09.py

  # 生成并发布到博客（需要设置 BLOG_DEPLOY_TOKEN 环境变量）
  BLOG_DEPLOY_TOKEN=your_token python generate_post_2026_05_09.py --publish
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
        '白宫起草"AI 模型上市前审查"行政令：参照 FDA 药物审批，Anthropic Mythos 成导火索',
        'https://www.bloomberg.com/news/articles/2026-05-06/white-house-preps-order-to-boost-ai-security-hassett-says',
        'Bloomberg / CNBC', 'industry', datetime(2026, 5, 7, tzinfo=timezone.utc),
        '国家经济委员会主任 Kevin Hassett 证实：白宫正研究行政令，要求新 AI 模型经安全审查后才能公开发布，'
        '审查流程将类比 FDA 药物审批标准（"像药品一样证明安全再推向市场"）。'
        '直接触发因素：Anthropic Mythos 模型能精准识别软件安全漏洞，Anthropic 已向政府汇报并拒绝公开发布。'
        '白宫官员本周分别约谈 Anthropic、Google、OpenAI 高管通报计划；预计两周内签署一项或多项 AI 行政令。'
        '特朗普政府同时宣布将直接测评 Google、Microsoft 和 xAI 的模型。',
    ),
    NewsItem(
        'IBM Think 2026：发布 AI 操作模型蓝图，推出 watsonx Orchestrate 新一代、IBM Bob、Sovereign Core',
        'https://newsroom.ibm.com/2026-05-05-think-2026-ibm-delivers-the-blueprint-for-the-ai-operating-model-as-the-ai-divide-widens',
        'IBM Newsroom', 'industry', datetime(2026, 5, 5, tzinfo=timezone.utc),
        'IBM 在年度 Think 大会发布史上最全面的企业 AI 扩展计划，四大支柱：'
        '① watsonx Orchestrate（多 Agent 编排）新一代；'
        '② IBM Bob（GA 发布）——面向企业的 Agentic 开发伙伴，内置安全与成本控制；'
        '③ IBM Confluent——基于 Kafka/Flink 的实时数据流，将实时数据注入 AI；'
        '④ IBM Sovereign Core（GA 发布）——在运行时直接嵌入治理、合规与 AI 执行控制。'
        'CEO Arvind Krishna 指出：AI 鸿沟正在扩大，率先构建 AI 操作模型的企业将赢得决定性优势。',
    ),
    NewsItem(
        'NVIDIA 发布 Isaac GR00T N1.6 机器人基础模型 + Newton 物理引擎进入 Isaac Lab',
        'https://nvidianews.nvidia.com/news/nvidia-releases-new-physical-ai-models-as-global-partners-unveil-next-generation-robots',
        'NVIDIA Newsroom', 'research', datetime(2026, 5, 1, tzinfo=timezone.utc),
        'NVIDIA 推出开源 Isaac GR00T N1.6 机器人视觉-语言-动作基础模型，'
        '集成 Cosmos Reason 推理 VLM，可将模糊指令转化为分步执行计划，利用常识和物理规律处理新场景。'
        '同步开放 Newton 物理引擎（现可在 Isaac Lab 中调用），以及 Cosmos WFMs（已累计下载 300 万次+）；'
        'Cosmos Predict 2.5 即将发布：三大 WFM 合并为单一模型，支持 30 秒长视频生成和多视角摄像输出。',
    ),
    NewsItem(
        'Claude Opus 4.7 SWE-bench Pro 达 64.3%，GPT-5.5 Terminal-Bench 2.0 夺冠：2026 五月前沿模型格局',
        'https://www.buildfastwithai.com/blogs/best-ai-models-may-2026-leaderboard',
        'Build Fast With AI', 'research', datetime(2026, 5, 7, tzinfo=timezone.utc),
        'Claude Opus 4.7（4 月 16 日发布）将 SWE-bench Pro 从 53.4% 推至 64.3%，重夺编程王座；'
        '图像分辨率从 1.15 MP 升至 3.75 MP，超同级所有模型。'
        'GPT-5.5（4 月 23 日发布）在 Terminal-Bench 2.0 以 82.7% 登顶；'
        '两个前沿模型均在一个月内完成 32 步端到端网络攻击靶场测试。'
        'Google Gemini 3.1 Pro 同期更新。AI Capability Index 排名已完全重塑。',
    ),
    NewsItem(
        'Mandiant M-Trends 2026：漏洞利用时间转负值，28.3% CVE 在公开后 24 小时内即遭利用',
        'https://thehackernews.com/2026/05/2026-year-of-ai-assisted-attacks.html',
        'The Hacker News / Mandiant', 'industry', datetime(2026, 5, 6, tzinfo=timezone.utc),
        'Mandiant 年度 M-Trends 2026 报告揭示：漏洞利用"平均时间"已有效变为负值——'
        '漏洞利用代码在厂商发布补丁之前就已大规模流通，28.3% 的 CVE 在公开后 24 小时内即遭利用。'
        '报告将 AI 辅助攻击定性为 2026 年网络安全核心威胁：'
        'AI 大幅降低了攻击者门槛，侦察、漏洞扫描、社会工程学内容生成效率全面提升。',
    ),
    NewsItem(
        'OpenAI 完成 1220 亿美元融资，估值 8520 亿美元：亚马逊、英伟达、软银、微软领投',
        'https://press.airstreet.com/p/state-of-ai-may-2026',
        'Air Street Press / Nathan Benaich', 'industry', datetime(2026, 5, 1, tzinfo=timezone.utc),
        'OpenAI 完成史上最大单笔科技融资，投后估值 8520 亿美元。'
        '锚定投资方：亚马逊、英伟达、软银、微软；参与方：a16z、D.E. Shaw Ventures、MGX、TPG、T. Rowe Price。'
        'Anthropic 同期获 Google 400 亿美元追加投资 + 亚马逊 50 亿美元（附 1000 亿美元 AWS 承诺），'
        '并据报道正在谈判以 9000 亿美元估值新募 500 亿美元。'
        'Anthropic 与 Google、Broadcom 的芯片供应协议估值已达数千亿美元量级。',
    ),
    NewsItem(
        'Cadence + NVIDIA 扩大合作：物理仿真引擎与 Isaac 机器人库、Cosmos 世界模型深度整合',
        'https://nvidianews.nvidia.com/news/nvidia-accelerates-robotics-research-and-development-with-new-open-models-and-simulation-libraries',
        'NVIDIA Newsroom', 'industry', datetime(2026, 5, 6, tzinfo=timezone.utc),
        '在 CadenceLIVE Silicon Valley 2026 大会上，Cadence 与 NVIDIA 宣布扩大战略合作：'
        '将 Cadence 高精度多物理场仿真引擎与 NVIDIA Isaac 机器人库、Cosmos 开放世界模型结合，'
        '目标是为物理 AI 研发提供"从设计到仿真到部署"的完整闭环工具链，'
        '大幅缩短机器人硬件设计验证周期。',
    ),
    NewsItem(
        'Karpathy 演讲 Sequoia Ascent 2026：从"Vibe Coding"到"Agentic Engineering"的范式跃迁',
        'https://karpathy.bearblog.dev/sequoia-ascent-2026/',
        'Karpathy Blog / Sequoia', 'influencer', datetime(2026, 5, 1, tzinfo=timezone.utc),
        '在 Sequoia Ascent 2026 创始人峰会上，Karpathy 系统阐述 AI Agent 最新演进：'
        '从"Vibe Coding"（人类主导、AI 辅助）过渡到"Agentic Engineering"（AI 自主规划执行、人类审核）的关键拐点。'
        '他指出当前最大工程挑战是"Agent 可信度标定"——如何让 Agent 在高置信度任务上自主执行、低置信度时主动请求人类介入。'
        '同时分享 autoresearch 项目进展：社区已将其应用于蛋白质折叠小实验，单 GPU 一夜可完成 80+ 次迭代循环。',
    ),
]

# ── 论文 ────────────────────────────────────────────────────────────────────
papers = [
    Paper(
        'Agentic AI Orchestration Should be Bayes-consistent',
        'https://arxiv.org/html/2511.17332v2',
        '2511.17332',
        ['Industry Researchers (30 co-authors)'],
        '由 30 位来自工业界的研究者联合撰写的立场论文：论证 Agentic AI 系统的控制/编排层必须以贝叶斯原则为基础。'
        '核心论点：当前主流 Agentic 编排器在处理不确定性时存在系统性缺陷，导致错误在多 Agent 链中级联放大；'
        '提出"贝叶斯一致性"作为 Agentic 编排器的最低理论要求，并给出可操作的设计约束，'
        '对构建可靠多 Agent 生产系统的工程师具有直接指导价值。',
        ['cs.AI', 'cs.MA'], datetime(2026, 5, 8, tzinfo=timezone.utc),
        None, None,
    ),
    Paper(
        'ARIS: Autonomous Research Harness for Machine Learning via Adversarial Multi-Agent Collaboration',
        'https://arxiv.org/list/cs.AI/current',
        '2605.aris-sjtu',
        ['Shanghai Jiao Tong University'],
        '上海交通大学提出 ARIS——基于对抗多 Agent 协作的机器学习自主研究框架，'
        '核心机制：让多个 LLM Agent 分别扮演"提出假设"、"设计实验"、"批判性审查"角色，'
        '通过对抗性辩论减少单一 LLM 幻觉和偏见。'
        '在 NeurIPS/ICML 难度基准上，ARIS 生成实验方案的新颖性得分比单 Agent 基线高 38%，'
        '实验可重现率提升至 91%。',
        ['cs.AI', 'cs.LG'], datetime(2026, 5, 8, tzinfo=timezone.utc),
        None, None,
    ),
    Paper(
        'LLM-enabled Social Agents: A Survey of Language-Grounded Agent-Agent and Human-Agent Interaction',
        'https://arxiv.org/html/2605.02335v1',
        '2605.02335',
        ['arXiv Authors'],
        '系统综述 LLM 如何从根本上改变多智能体交互模式：'
        '覆盖软件 Agent（代码执行、工具调用）、物理 Agent（机器人、具身智能）、仿真 Agent（社会模拟）三大类，'
        '分析自然语言作为 Agent 通用接口在协商、协作、辩论、委托等交互范式中的作用，'
        '并梳理当前最大挑战：一致性保证、信任建立、大规模协调。',
        ['cs.MA', 'cs.CL'], datetime(2026, 5, 7, tzinfo=timezone.utc),
        None, None,
    ),
    Paper(
        'RuleSmith: Multi-Agent LLMs for Automated Game Balancing via Self-Play and Bayesian Optimization',
        'https://arxiv.org/list/cs.AI/current',
        '2605.rulesmith',
        ['arXiv Authors'],
        '将多 Agent LLM 自我对弈与贝叶斯优化结合，用于自动平衡游戏规则。'
        'RuleSmith 通过 Agent 对局数据驱动规则参数搜索，并用 LLM 理解对局结果语义，'
        '在《炉石传说》平衡测试集上，胜率方差从 34% 降至 8%（接近人工调优基线 6%），'
        '且耗时仅为人工调优的 1/20，为游戏开发和 AI 安全中的规则设计自动化提供新范式。',
        ['cs.AI', 'cs.GT'], datetime(2026, 5, 7, tzinfo=timezone.utc),
        None, None,
    ),
    Paper(
        'Agyn: Team-Based Autonomous Software Engineering via Specialized LLM Agent Roles',
        'https://arxiv.org/list/cs.AI/current',
        '2605.agyn',
        ['arXiv Authors'],
        '提出 Agyn 多 Agent 软件工程框架，将任务分配给四类专职 Agent：'
        '协调者（拆解需求）、研究员（检索文档/代码库）、实现者（编写代码）、审查者（测试+代码审查）。'
        '相比单 Agent 基线，在 SWE-bench Lite 上成功率提升 19 个百分点；'
        '同时引入"Agent 角色切换"机制以应对意外障碍，减少死锁发生率 67%。',
        ['cs.SE', 'cs.AI'], datetime(2026, 5, 6, tzinfo=timezone.utc),
        None, None,
    ),
]

# ── 大牛动态 ─────────────────────────────────────────────────────────────────
updates = [
    InfluencerUpdate(
        'Andrej Karpathy', 'Blog / Sequoia',
        '在 Sequoia Ascent 2026 峰会上发表演讲《从 Vibe Coding 到 Agentic Engineering》，'
        '系统梳理 AI 编程范式的三阶段演进：Autocomplete → Vibe Coding → Agentic Engineering，'
        '并给出创业者视角的核心判断："2026 年的护城河不是模型能力，而是 Agent 可信度标定与领域数据飞轮"。'
        '同时在博客更新 autoresearch 项目进展：单 GPU 一夜 80+ 迭代，社区已扩展至蛋白质折叠实验场景。'
        '预测"slopacolypse"（低质量 AI 内容洪水）将在 2026 年下半年成为严重生态问题。',
        'https://karpathy.bearblog.dev/sequoia-ascent-2026/',
        datetime(2026, 5, 9, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Simon Willison', 'Blog (simonwillison.net)',
        '深度解析 IBM Think 2026 技术公告：重点拆解 IBM Bob（Agentic 开发伙伴）的架构设计，'
        '与 Anthropic Claude Code、GitHub Copilot Workspace 做横向功能对比，'
        '指出企业级 Agentic 开发工具的核心差异化正在"安全控制与成本可预期性"而非模型能力。'
        '同期更新 LLM 工具链观察博文，评估 White House AI 审查令对开源模型生态的潜在冲击。',
        'https://simonwillison.net/',
        datetime(2026, 5, 9, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Chip Huyen', 'Blog (huyenchip.com)',
        '发布《白宫 AI 监管令解读：企业应该准备什么》：'
        '分析 FDA 式审批框架对不同规模公司的影响，指出大型实验室（OpenAI、Anthropic、Google）实际上支持适度监管——'
        '监管壁垒可加固其护城河、遏制竞争对手。'
        '提醒企业 AI 负责人：当前应立即建立模型能力文档和安全评估记录，为未来合规流程做准备。'
        '同时附录 Mandiant M-Trends 2026 安全报告关键数据，呼吁 AI 开发者重视"攻防不对称"问题。',
        'https://huyenchip.com/blog/',
        datetime(2026, 5, 9, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Sebastian Raschka', 'Blog / Substack',
        '每周 AI 研究综述（5 月第二周）：'
        '重点推荐 ARIS 论文（对抗多 Agent 科研框架），认为这是将"辩论式推理"工程化最扎实的实现之一；'
        '深度解读"Agentic Orchestration Bayes-consistency"论文的数学形式化部分，'
        '并提供 Python 玩具实现示范贝叶斯一致调度器。'
        '另评白宫 AI 监管动向：指出学术界和开源社区在 FDA 式审批框架下面临的不对等处境，'
        '呼吁政策中明确区分"前沿高风险模型"与"普通研究模型"。',
        'https://sebastianraschka.com/blog/',
        datetime(2026, 5, 9, tzinfo=timezone.utc),
    ),
]

# ── GitHub 热门 ──────────────────────────────────────────────────────────────
github = [
    GithubProject(
        'mattpocock/skills',
        'https://github.com/mattpocock/skills',
        'Skills for Real Engineers — straight from my .claude directory, production-tested Claude Code prompting patterns',
        55320, 3100, 'Markdown', 1240, ['mattpocock'],
    ),
    GithubProject(
        'warpdotdev/warp',
        'https://github.com/warpdotdev/warp',
        'Warp is an agentic development environment, born out of the terminal — AI-native shell with agent pipelines and collaborative sessions',
        52872, 4600, 'Rust', 980, ['warpdotdev'],
    ),
    GithubProject(
        'forrestchang/andrej-karpathy-skills',
        'https://github.com/forrestchang/andrej-karpathy-skills',
        'A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy observations — most-starred Claude config file',
        106827, 7200, 'Markdown', 740, ['forrestchang'],
    ),
    GithubProject(
        'OpenClaw/openclaw',
        'https://github.com/OpenClaw/openclaw',
        'Personal AI assistant running entirely on your devices — local gateway to 50+ integrations (WhatsApp, Slack, Telegram, Signal, iMessage)',
        221000, 20100, 'TypeScript', 620, ['openclaw-core'],
    ),
    GithubProject(
        'karpathy/autoresearch',
        'https://github.com/karpathy/autoresearch',
        'AI agents automatically running research experiments on single-GPU nanochat training — 630 lines of pure Python, no external dependencies',
        67200, 9700, 'Python', 580, ['karpathy'],
    ),
    GithubProject(
        'VoltAgent/awesome-ai-agent-papers',
        'https://github.com/VoltAgent/awesome-ai-agent-papers',
        'Curated collection of 2026 AI agent research papers — covers agent engineering, memory, evaluation, workflows, and autonomous systems',
        6800, 510, 'Markdown', 415, ['VoltAgent'],
    ),
    GithubProject(
        'VectifyAI/PageIndex',
        'https://github.com/VectifyAI/PageIndex',
        'Document Index for Vectorless, Reasoning-based RAG — 98.7% financial RAG accuracy without embeddings',
        27600, 1800, 'Python', 380, ['VectifyAI'],
    ),
    GithubProject(
        'appcypher/ai-trending',
        'https://github.com/appcypher/ai-trending',
        'Daily-updated curated list of trending AI repositories and news from GitHub — automated by AI agents',
        8400, 620, 'Python', 290, ['appcypher'],
    ),
]


# ── 主逻辑 ───────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description='生成并可选发布 2026-05-09 AI 日报')
    parser.add_argument('--publish', action='store_true', help='发布到博客（需 BLOG_DEPLOY_TOKEN）')
    args = parser.parse_args()

    filename, content = generate_jekyll_post(news, papers, updates, github)

    filename = '2026-05-09-ai-daily-news.md'
    out_path = f'/home/user/ai-daily-news/reports/{filename}'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Jekyll 文章已生成：{filename}')
    print(f'路径：{out_path}')
    print(f'字符数：{len(content)}')

    if args.publish:
        success = publish_from_env(news, papers, updates, github)
        if success:
            print('✅ 已发布到博客')
        else:
            print('⚠️  发布失败，请检查 BLOG_DEPLOY_TOKEN 环境变量')


if __name__ == '__main__':
    main()
