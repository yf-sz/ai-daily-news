"""
发布 2026-05-06 AI 日报到博客

用法：
  # 仅生成 Jekyll 文章到 reports/ 目录
  python generate_post_2026_05_06.py

  # 生成并发布到博客（需要设置 BLOG_DEPLOY_TOKEN 环境变量）
  BLOG_DEPLOY_TOKEN=your_token python generate_post_2026_05_06.py --publish
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
        'OpenAI 发布 GPT-5.5 Instant：幻觉减少 52.5%，成为 ChatGPT 新默认模型',
        'https://openai.com/index/gpt-5-5-instant/',
        'OpenAI', 'industry', datetime(2026, 5, 5, tzinfo=timezone.utc),
        'OpenAI 于 5 月 5 日推出 GPT-5.5 Instant，取代 GPT-5.3 Instant 成为 ChatGPT 默认模型。'
        '在高风险领域（医疗、法律、金融）幻觉率下降 52.5%，AIME 2025 数学测试从 65.4 提升至 81.2，'
        'MMMU-Pro 多模态基准从 69.2 提升至 76。新模型同步向所有 ChatGPT 用户和 API（chat-latest）推出，'
        'Plus/Pro 用户率先获得增强个性化功能；同日模型也上线 Amazon Bedrock。',
    ),
    NewsItem(
        'Anthropic 推出 10 款金融行业 AI Agent 及 Claude Opus 4.7，全面进军华尔街',
        'https://www.anthropic.com/news/finance-agents',
        'Anthropic', 'industry', datetime(2026, 5, 5, tzinfo=timezone.utc),
        'Anthropic 发布 10 款预配置金融 AI Agent，覆盖投资银行、资产管理和保险场景：'
        '包括 Pitch builder（路演材料生成）、KYC screener（合规初筛）、Statement auditor（财务审计）等。'
        '同步发布 Claude Opus 4.7——在 Vals AI Finance Agent 基准以 64.37% 排名第一。'
        '全面集成 Microsoft 365（Excel、PowerPoint、Word、Outlook），'
        '已在 JPMorganChase、Goldman Sachs、Citi、AIG、Visa 等机构部署上线。',
    ),
    NewsItem(
        '五角大楼向 8 家 AI 公司开放绝密网络合同，Anthropic 因"使用限制"争议遭拒',
        'https://defensescoop.com/2026/05/01/dod-expands-classified-ai-work-with-8-companies-excluding-anthropic/',
        'DefenseScoop', 'industry', datetime(2026, 5, 1, tzinfo=timezone.utc),
        '美国国防部（DoD）与 OpenAI、Google、Microsoft、Amazon、Oracle、Nvidia、SpaceX 及'
        '新兴初创 Reflection AI 签署 IL6/IL7 保密级别 AI 合同，允许在美军分类网络上部署 AI。'
        'Anthropic 因拒绝授权将 Claude 用于"所有合法目的"（可能涵盖全自主武器或国内大规模监控）而被排除在外，'
        '被正式列入供应链风险名单。Reflection AI 由前 Google DeepMind 研究人员创立，'
        '已完成逾 20 亿美元融资，尚未发布商用模型。',
    ),
    NewsItem(
        'Google I/O 2026 定档 5 月 19 日：Gemini 4.0（2M Token 上下文）、Android XR、Aluminum OS 齐亮相',
        'https://android.gadgethacks.com/news/what-to-expect-from-google-io-2026-dates-gemini-android-17/',
        'Gadget Hacks', 'industry', datetime(2026, 5, 5, tzinfo=timezone.utc),
        'Google I/O 2026 将于 5 月 19–20 日在加州山景城举办。'
        '预期核心发布：①Gemini 4.0——支持 200 万 Token 上下文，含合规模式；'
        '②Android 17 深度 Gemini 集成；③Android XR 智能眼镜；'
        '④传闻中的 Aluminum OS；⑤Veo 视频、Lyria 音乐、Gemma 轻量化开源模型均有望更新。'
        '所有主题演讲和分会场均可在 io.google 免费直播。',
    ),
    NewsItem(
        'Anthropic Workspace Agents 正式开始积分计费：企业版 Custom GPT 继任者进入商业化',
        'https://openai.com/index/introducing-workspace-agents-in-chatgpt/',
        'OpenAI / Anthropic', 'industry', datetime(2026, 5, 6, tzinfo=timezone.utc),
        'OpenAI 的 Workspace Agents 免费期于 5 月 6 日结束，正式启动积分计费。'
        'Workspace Agents 基于 Codex 驱动，允许企业团队在 Slack、Salesforce 等平台共建共用 Agent，'
        '支持报告生成、代码编写、消息处理等长时任务，在云端持续运行无需人工守候。'
        '目前向 Business、Enterprise、Edu 及 Teachers 计划开放，具体积分单价尚未完全公布。',
    ),
    NewsItem(
        'Simon Willison 推出 llm-echo 0.5a0：用于自动化测试的假 LLM 插件，支持 thinking 选项',
        'https://simonwillison.net/2026/May/5/llm-echo/',
        'Simon Willison', 'tools', datetime(2026, 5, 5, tzinfo=timezone.utc),
        'Simon Willison 发布 llm-echo 0.5a0，这是一款为 LLM CLI 工具提供的"假模型"插件，'
        '不调用任何真实语言模型——输出即为输入的回显，专为自动化测试设计。'
        '新版本新增 -o thinking 选项，兼容 LLM 0.32a0 及以上版本的思维链测试场景，'
        '可在无网络和无 API 密钥的 CI 环境中稳定运行。',
    ),
    NewsItem(
        'DeepSeek-TUI 登上 GitHub Trending：终端原生编程 Agent，专为 DeepSeek V4 百万 Token 优化',
        'https://github.com/Hmbown/DeepSeek-TUI',
        'GitHub Trending', 'tools', datetime(2026, 5, 5, tzinfo=timezone.utc),
        'DeepSeek-TUI 是 Hunter Bown 独立开发的 Rust 编写终端编程 Agent，'
        '绕过 Node/Python 运行时，以单一二进制文件直接集成 MCP 客户端、沙箱和持久任务队列。'
        '支持 Plan（只读探索）、Agent（逐步审批）和 YOLO（全自动）三种执行模式，'
        'RLM 模式可将子任务分发给 DeepSeek V4 Flash 降低成本。'
        '上线不足四个月已完成 37 次版本迭代，近期因功能完整度迅速上升至 GitHub Trending。',
    ),
    NewsItem(
        '大模型幻觉 2026 年基准：GPT-5.5 Instant 领跑，医疗法律金融三领域首次低于 10%',
        'https://suprmind.ai/hub/ai-hallucination-rates-and-benchmarks/',
        'Suprmind', 'research', datetime(2026, 5, 5, tzinfo=timezone.utc),
        'Suprmind 最新幻觉基准测试显示，GPT-5.5 Instant 在高风险领域幻觉率已降至个位数，'
        '是首批在医疗、法律、金融三个敏感垂类全部突破 10% 以下的商用模型之一。'
        '报告同时指出，Claude Opus 4.7 在长上下文事实一致性上优于同期竞品，'
        '而 Gemini 3.1 Pro 在多模态幻觉（图文不符）方面仍有显著改进空间。',
    ),
]

# ── 论文 ────────────────────────────────────────────────────────────────────
papers = [
    Paper(
        'Towards Multi-Agent Autonomous Reasoning in Hydrodynamics',
        'https://arxiv.org/abs/2605.01102',
        '2605.01102',
        ['arXiv Authors'],
        '提出用于流体动力学领域的多 Agent 自主推理系统（MAS），以层执行图（Layer Execution Graph, LEG）'
        '协调专业化 Agent。解决单 Agent 系统随工具和轨迹积累而上下文空间压缩的可靠性瓶颈：'
        '规划 Agent 从自然语言路由启发式中构建查询特定的执行拓扑，'
        '专业 Agent 在严格工具白名单下运行，从而实现复杂物理模拟任务的端到端自动化推理。',
        ['cs.AI', 'cs.CE'], datetime(2026, 5, 1, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2605.01102',
        None,
    ),
    Paper(
        'From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review',
        'https://arxiv.org/abs/2504.19678',
        '2504.19678',
        ['arXiv Authors'],
        '系统综述 LLM 从单步推理演进至自主 AI Agent 的技术路径。'
        '论文界定 Agentic AI 的核心要素：感知、推理、规划与行动的闭环；'
        '梳理 ReAct、Reflexion、AutoGPT、LangGraph 等主流框架的能力边界；'
        '分析记忆管理（短期/长期/外部向量库）、工具调用可靠性和多 Agent 协作通信协议三大开放挑战，'
        '并提出评估 Agent 端到端可靠性的统一指标体系。',
        ['cs.AI', 'cs.CL'], datetime(2026, 4, 28, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2504.19678',
        None,
    ),
    Paper(
        'Evaluating Large Language Models in Scientific Discovery',
        'https://arxiv.org/abs/2512.15567',
        '2512.15567',
        ['arXiv Authors'],
        '构建覆盖生命科学、物理、材料科学的科学发现评估基准，'
        '测试 LLM 在假设生成、实验设计和结果解读三个阶段的表现。'
        '研究发现顶级模型在假设生成上接近领域专家水平，但在实验设计可行性判断上仍存在显著差距；'
        '引入"科学幻觉"（scientifically-plausible but factually wrong）新维度进行量化评估，'
        '呼吁社区建立面向科学推理的专项 Red-teaming 基准。',
        ['cs.AI', 'cs.LG'], datetime(2025, 12, 20, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2512.15567',
        None,
    ),
    Paper(
        'Agentopic: Agent-Based Workflow for Explainable Topic Modeling via LLMs',
        'https://arxiv.org/list/cs.AI/current',
        '2505.agentopic',
        ['arXiv Authors'],
        '提出 Agentopic，一种基于 LLM Agent 的可解释主题建模工作流。'
        '与传统 LDA/BERTopic 相比，Agentopic 将主题发现拆解为文档采样、概念归纳、'
        '标签验证三个 Agent 角色的协作任务，可自动生成人类可读的主题标签和理由链，'
        '在新闻、学术论文、社交媒体三类语料上均显著优于基线方法，且输出可被领域专家直接审查修改。',
        ['cs.CL', 'cs.AI'], datetime(2026, 5, 4, tzinfo=timezone.utc),
        None,
        None,
    ),
    Paper(
        'Why Do LLMs Struggle in Strategic Play? Broken Links Between Observation, Belief, and Action',
        'https://arxiv.org/list/cs.AI/current',
        '2505.strategic',
        ['arXiv Authors'],
        '分析大语言模型在博弈论与策略游戏场景中持续表现不佳的根本原因：'
        '观察→信念更新→行动决策三个认知环节之间存在系统性断链。'
        '实验覆盖德州扑克、外交、围棋残局等多类策略任务，'
        '发现 LLM 的主要失误来自信念状态维护失败（而非推理错误），'
        '即模型无法可靠地追踪多步交互后对手的内部状态，'
        '对 Agent 系统的长程规划可靠性有重要启示。',
        ['cs.AI', 'cs.GT'], datetime(2026, 5, 3, tzinfo=timezone.utc),
        None,
        None,
    ),
]

# ── 大牛动态 ─────────────────────────────────────────────────────────────────
updates = [
    InfluencerUpdate(
        'Simon Willison', 'Blog',
        '5 月 5 日连续发布两则更新：'
        '① 发布 llm-echo 0.5a0——为 LLM CLI 工具链提供"零成本"假模型，'
        '输出即输入回显，新增 -o thinking 选项支持思维链测试场景，'
        '让 CI 环境中的 LLM 集成测试无需真实 API；'
        '② 录制 High Leverage 播客第 9 期《The AI Coding Paradigm Shift》，'
        '与主持人 Joe Ruscio 深入探讨：编程 Agent 从"氛围编码"到"工程化 Agent"的演进，'
        '2025 年是 LLM 编程能力无可争议爆发的一年，'
        '以及为何经验丰富的工程师在 AI 辅助开发时反而更具优势。',
        'https://simonwillison.net/2026/May/5/llm-echo/',
        datetime(2026, 5, 5, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Andrej Karpathy', 'Blog / X',
        'Medium 深度报道《Karpathy：我已停止用 AI 写代码，而是用它构建第二大脑》引发广泛讨论。'
        'Karpathy 透露：他正在将 LLM 用于构建个人知识管理与记忆系统，'
        '而非单纯代码生成——目标是让 AI 在跨时间、跨项目中维持一致的背景知识和上下文，'
        '相当于一个"可编程的第二大脑"。他强调这不是放弃代码辅助，'
        '而是认为当前最缺乏且最有价值的突破方向在于长期记忆与个人上下文管理，'
        '而非继续在单次对话的代码生成上内卷。',
        'https://medium.com/neuralnotions/andrej-karpathy-stopped-using-ai-to-write-code-hes-using-it-to-build-a-second-brain-instead-cddceadc5df5',
        datetime(2026, 5, 4, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Chip Huyen', 'Blog (huyenchip.com)',
        '持续更新《AI Engineering》系列。近期重点关注 Anthropic 金融 AI Agent 发布案例：'
        '分析"预配置 Agent 模板"商业模式——通过降低 Agent 部署门槛，'
        '将企业客户从 API 调用者升级为业务流程共建者；'
        '指出金融场景的工具调用幂等性（避免重复下单/重复汇款）是 Agent 系统最严苛的可靠性挑战，'
        '而目前主流框架对此几乎没有原生支持；'
        '同时呼吁 AI 工程师将"Agent 审计日志"列为生产部署的必要条件，'
        '而非可选的调试辅助。',
        'https://huyenchip.com/blog/',
        datetime(2026, 5, 5, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Sebastian Raschka', 'Blog (sebastianraschka.com)',
        '在 GPT-5.5 Instant 发布后第一时间发布快速评测笔记：'
        '对比 GPT-5.5 Instant 与 Claude Opus 4.7 在数学推理（AIME 2025）、'
        '代码生成（HumanEval+ 变体）和长上下文事实回溯三类任务上的表现；'
        '总结：数学推理上 GPT-5.5 有明显优势（81.2 vs 约 74），'
        '代码生成两者相当，长上下文 Claude 仍占优。'
        '同时提醒：基准测试与实际生产表现之间存在显著"基准污染"风险，'
        '建议工程师用自己的垂类任务做内部 A/B 测试再决策。',
        'https://sebastianraschka.com/blog/',
        datetime(2026, 5, 6, tzinfo=timezone.utc),
    ),
]

# ── GitHub 热门 ──────────────────────────────────────────────────────────────
github = [
    GithubProject(
        'OpenClaw/openclaw',
        'https://github.com/OpenClaw/openclaw',
        'Personal AI assistant running entirely on your devices — local gateway to 50+ integrations (WhatsApp, Slack, Telegram, Signal, iMessage)',
        219000, 19800, 'TypeScript', 1150, ['openclaw-core'],
    ),
    GithubProject(
        'Hmbown/DeepSeek-TUI',
        'https://github.com/Hmbown/DeepSeek-TUI',
        'Terminal-native coding agent for DeepSeek V4 — 1M-token context, prefix caching, MCP client, sandbox, durable task queue, single Rust binary',
        2300, 180, 'Rust', 980, ['Hmbown'],
    ),
    GithubProject(
        'TauricResearch/TradingAgents',
        'https://github.com/TauricResearch/TradingAgents',
        'Multi-agent LLM financial trading framework — fund managers, analysts, risk managers and traders collaborate autonomously to execute strategies',
        65300, 5800, 'Python', 870, ['TauricResearch'],
    ),
    GithubProject(
        'n8n-io/n8n',
        'https://github.com/n8n-io/n8n',
        'Fair-code workflow automation platform with native AI capabilities — visual agent pipelines, LLM chains, vector DB queries, 400+ integrations',
        187000, 23100, 'TypeScript', 720, ['janober', 'ivov'],
    ),
    GithubProject(
        'alvinreal/awesome-opensource-ai',
        'https://github.com/alvinreal/awesome-opensource-ai',
        'Curated list of the best truly open-source AI projects, models, tools, and infrastructure',
        12400, 890, 'Markdown', 650, ['alvinreal'],
    ),
    GithubProject(
        'VoltAgent/awesome-ai-agent-papers',
        'https://github.com/VoltAgent/awesome-ai-agent-papers',
        'Curated collection of 2026 AI agent research papers — covers agent engineering, memory, evaluation, workflows, and autonomous systems',
        6400, 480, 'Markdown', 580, ['VoltAgent'],
    ),
    GithubProject(
        'huggingface/ml-intern',
        'https://github.com/huggingface/ml-intern',
        'Open-source AI agent that reads papers, trains models, and ships ML projects — fully automated ML engineering assistant',
        18700, 1400, 'Python', 490, ['huggingface'],
    ),
    GithubProject(
        'weitianxin/Awesome-Agentic-Reasoning',
        'https://github.com/weitianxin/Awesome-Agentic-Reasoning',
        'Curated list of papers and resources on agentic reasoning for LLMs — tracks the survey "Agentic Reasoning for Large Language Models"',
        3200, 240, 'Markdown', 310, ['weitianxin'],
    ),
]


# ── 主逻辑 ───────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description='生成并可选发布 2026-05-06 AI 日报')
    parser.add_argument('--publish', action='store_true', help='发布到博客（需 BLOG_DEPLOY_TOKEN）')
    args = parser.parse_args()

    filename, content = generate_jekyll_post(news, papers, updates, github)

    filename = '2026-05-06-ai-daily-news.md'
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
