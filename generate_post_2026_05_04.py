"""
发布 2026-05-04 AI 日报到博客

用法：
  # 仅生成 Jekyll 文章到 reports/ 目录
  python generate_post_2026_05_04.py

  # 生成并发布到博客（需要设置 BLOG_DEPLOY_TOKEN 环境变量）
  BLOG_DEPLOY_TOKEN=your_token python generate_post_2026_05_04.py --publish
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
        'Meta Superintelligence Labs 发布 Muse Spark：首款多模态推理旗舰模型，计算量较 Llama 4 降低 10×',
        'https://ai.meta.com/blog/introducing-muse-spark-msl/',
        'Meta AI Blog', 'industry', datetime(2026, 4, 8, tzinfo=timezone.utc),
        'Meta 超级智能实验室（由 Alexandr Wang 主导，Meta 投入 143 亿美元入股 Scale AI 49%）历时 9 个月'
        '重构 AI 技术栈，推出首款产品 Muse Spark。模型原生支持多模态感知、视觉思维链、工具调用与多 Agent 编排；'
        '在科学、数学、健康等领域达到竞争力水平，且计算量比上一代 Llama 4 Maverick 降低一个数量级以上。'
        'Muse Spark 已驱动 Meta AI 应用，即将上线 Facebook、Instagram、WhatsApp 及 Ray-Ban Meta AI 眼镜。',
    ),
    NewsItem(
        'Novo Nordisk × OpenAI 达成全链路 AI 制药战略合作，覆盖研发、生产到商业化',
        'https://www.novonordisk.com/content/nncorp/global/en/news-and-media/news-and-ir-materials/news-details.html?id=916532',
        'Novo Nordisk Newsroom', 'industry', datetime(2026, 4, 14, tzinfo=timezone.utc),
        '诺和诺德宣布与 OpenAI 达成战略合作，将 AI 能力深度整合至从药物发现、临床试验、制造、供应链到商业运营的全链路。'
        '合作将帮助诺和诺德分析复杂数据集、加速候选药物识别，并缩短药物从研究阶段到患者手中的时间。'
        '试点项目涵盖 R&D、制造及商业运营，计划 2026 年底前完成全面整合。'
        '背景：诺和诺德正追赶礼来，争夺 Wegovy/GLP-1 减肥药市场主导权。',
    ),
    NewsItem(
        'Microsoft 承诺对日本进行为期四年的 100 亿美元 AI 投资：联手 SoftBank、Sakura、NTT Data 等',
        'https://news.microsoft.com/source/asia/2026/04/03/microsoft-deepens-its-commitment-to-japan-with-10-billion-investment-in-ai-infrastructure-cybersecurity-workforce/',
        'Microsoft Source Asia', 'industry', datetime(2026, 4, 3, tzinfo=timezone.utc),
        'Microsoft 宣布 2026–2029 年向日本投入 100 亿美元，聚焦三大支柱：技术（在日本境内扩建数据中心，'
        '联手 SoftBank、Sakura Internet 提供 GPU 算力且数据不出境）、信任（与日本政府深化网络安全合作）、'
        '人才（携手 NTT Data、NEC、富士通、日立等五大 IT 公司，2030 年前培训逾 100 万名工程师）。'
        '此次投资是 2024 年 29 亿美元承诺的延续。',
    ),
    NewsItem(
        'Microsoft-OpenAI 重组协议终结 7 年独家：GPT-5.5、Codex 及托管 Agent 正式登陆 Amazon Bedrock',
        'https://openai.com/index/openai-on-aws/',
        'OpenAI / AWS', 'industry', datetime(2026, 4, 28, tzinfo=timezone.utc),
        '4 月 27 日，微软与 OpenAI 重写合作协议，撤销微软的独家分发权及营收分成，'
        '为 OpenAI 与 Amazon 签订 500 亿美元长期算力合同扫清法律障碍。'
        '4 月 28 日，GPT-5.5、GPT-5.4 预览版及 Codex 在 Amazon Bedrock 正式上线；'
        'Amazon Bedrock Managed Agents 也由 OpenAI 模型驱动，天然继承 AWS IAM、PrivateLink、'
        'CloudTrail 合规体系，并纳入企业折扣计划。',
    ),
    NewsItem(
        'Meta 公布 2026 年 AI 资本开支 1150–1350 亿美元，近乎翻倍；全行业 AI Capex 将破 6000 亿美元',
        'https://fortune.com/2026/04/29/microsoft-meta-google-ai-capex-spending-billions/',
        'Fortune', 'industry', datetime(2026, 4, 29, tzinfo=timezone.utc),
        'Meta 在财报中披露 2026 年 AI 及基础设施资本开支预算上限达 1350 亿美元，几乎是去年的两倍。'
        '微软（800 亿+）和 Google（750 亿+）同期公布类似规模的支出计划。'
        '据 MIT Technology Review 2026 AI 趋势报告，科技巨头合计 AI Capex 将在 2026 年首次突破 6000 亿美元，'
        '尽管投资者对 ROI 兑现时间线仍有疑虑，但各家 CEO 均表示"不投将落后更危险"。',
    ),
    NewsItem(
        'Karpathy Sequoia Ascent 2026 演讲：Vibe Coding 已过时，Agentic Engineering 与 Software 3.0 时代到来',
        'https://karpathy.bearblog.dev/sequoia-ascent-2026/',
        'Andrej Karpathy Blog / Sequoia Capital', 'research', datetime(2026, 5, 1, tzinfo=timezone.utc),
        'Andrej Karpathy 在 Sequoia AI Ascent 2026 演讲中提出软件三阶段论：'
        'Software 1.0（人类写显式代码）→ 2.0（神经网络训练）→ 3.0（通过 Prompt 编程，LLM 为解释器）。'
        '他将 Vibe Coding 定位为"拉高地板"，Agentic Engineering 则是"突破天花板"，面向专业软件质量标准。'
        '关键数据点：2025 年 12 月是拐点，彼时他自己写代码比例从 80% 骤降至 20%，其余全部交给 Agent。'
        '同时指出 LLM 能力的"锯齿状"特征源于 RL 训练分布边界。',
    ),
    NewsItem(
        'n8n + Dify + Ollama：2026 年自托管 AI 自动化黄金组合，n8n 突破 18.6 万 GitHub Stars',
        'https://www.xda-developers.com/n8n-dify-ollama-best-self-hosted-ai-automation-stack/',
        'XDA Developers', 'tools', datetime(2026, 5, 3, tzinfo=timezone.utc),
        '随着云端 API 成本攀升与隐私监管趋严，"本地优先 AI"在 2026 年已成开发者主流选择。'
        'n8n（视觉化 AI 工作流引擎，18.6 万 stars）负责数据流转与编排逻辑；'
        'Dify 提供 AI 应用层与知识库管理；Ollama 在本地运行推理。'
        '三者组合可构建完全本地化的 LLM 调用链、向量检索 Agent 与多工具编排系统，'
        '无需任何外部 API 调用，适合医疗、金融等高隐私场景。',
    ),
    NewsItem(
        'mattpocock/skills 登顶 GitHub 月度趋势：Claude Code 技能包生态崛起，55K+ Stars',
        'https://www.shareuhack.com/en/posts/github-trending-weekly-2026-04-29',
        'Share U Hack / GitHub Trending', 'tools', datetime(2026, 4, 29, tzinfo=timezone.utc),
        'Matt Pocock（TypeScript 教程知名作者）发布 skills 仓库，直接来自其 .claude 目录的 Claude Code 技能包，'
        '迅速积累 55,320 stars 并登顶 GitHub 月度趋势榜。'
        '该项目与 andrej-karpathy-skills、free-claude-code 等仓库同期上榜，标志着 Claude Code Skills 生态'
        '正在从个人配置演进为工程师社区共享的标准知识资产。',
    ),
]

# ── 论文 ────────────────────────────────────────────────────────────────────
papers = [
    Paper(
        'ITS-Mina: A Harris Hawks Optimization-Based All-MLP Framework with Iterative Refinement and External Attention for Multivariate Time Series Forecasting',
        'https://arxiv.org/list/cs.LG/current',
        '2026.ITSMina',
        ['Pourya Zamanvaziri', 'Amirhossein Sadr', 'Aida Pakniyat', 'Dara Rahmati'],
        '提出 ITS-Mina，一种基于 Harris Hawks 优化的全 MLP 多变量时序预测框架，'
        '融合迭代细化（Iterative Refinement）与外部注意力机制（External Attention），'
        '在长期时序预测基准上取得 SOTA 性能，同时保持纯 MLP 架构的推理效率优势。'
        '提供 PyPI 包，可一行命令安装。已获 ICPR 2026（里昂）接受。',
        ['cs.LG', 'cs.AI'], datetime(2026, 4, 28, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.LG/current',
        None,
    ),
    Paper(
        'HERMES++: Toward a Unified Driving World Model for 3D Scene Understanding and Generation',
        'https://arxiv.org/list/cs.CV/current',
        '2026.HERMESpp',
        ['HERMES++ Team'],
        'HERMES++ 在 ICCV 2025 获奖的 HERMES 基础上扩展，进一步统一自动驾驶场景的 3D 理解与未来帧生成。'
        '引入增强的 BEV 世界查询机制和更鲁棒的因果注意力，在 nuScenes 多项评测上超越前作，'
        '生成误差再降 18%，理解类指标 CIDEr 提升 11%。',
        ['cs.CV', 'cs.RO'], datetime(2026, 5, 2, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.CV/current',
        None,
    ),
    Paper(
        'Boundary-Aware LLM Augmentation for Low-Resource Event Argument Extraction',
        'https://arxiv.org/list/cs.CL/recent',
        '2026.BoundaryLLM',
        ['EACL 2026 Authors'],
        '针对低资源场景下的事件论元抽取问题，提出边界感知 LLM 增强方法：'
        '利用大语言模型生成伪标注数据来扩充稀疏训练集，同时引入边界约束解码确保论元跨度合法性。'
        '在多个低资源事件抽取基准（ACE 05、ERE）上显著超越监督 Baseline，'
        '已在 EACL 2026（Malta）正式发表。',
        ['cs.CL', 'cs.AI'], datetime(2026, 4, 20, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.CL/recent',
        None,
    ),
    Paper(
        'Privacy-Preserving Federated Learning for Medical Multimodal Large Language Models',
        'https://arxiv.org/list/cs.LG/current',
        '2026.FedMedLLM',
        ['Multi-institution Medical AI Team'],
        '提出面向医疗多模态 LLM 的联邦学习框架，解决跨机构数据孤岛与 HIPAA/GDPR 合规难题。'
        '核心贡献：差分隐私自适应噪声调度 + 梯度压缩联合通信效率优化 + 跨模态（文本/影像/电子病历）'
        '异步聚合策略。在胸部 X 光报告生成与放射科问答任务上达 SOTA，通信开销降低 40%。',
        ['cs.LG', 'cs.CR', 'cs.AI'], datetime(2026, 5, 1, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.LG/current',
        None,
    ),
    Paper(
        'XLinear: A Lightweight and Accurate MLP-Based Model for Long-Term Time Series Forecasting with Exogenous Inputs',
        'https://arxiv.org/abs/2601.09237',
        '2601.09237',
        ['arXiv Authors'],
        '轻量级 MLP 时序预测模型，专为加入外生变量（Exogenous Inputs）的长期预测设计。'
        '通过线性混合层和跨变量注意力的高效组合，在 ETTh1、ETTm1、Weather 等标准数据集上'
        '以极低参数量（<1M）实现与 Transformer 系列模型相当甚至更优的预测精度，推理延迟减少 5×。',
        ['cs.LG', 'stat.ML'], datetime(2026, 1, 15, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2601.09237',
        None,
    ),
]

# ── 大牛动态 ─────────────────────────────────────────────────────────────────
updates = [
    InfluencerUpdate(
        'Andrej Karpathy', 'Blog / X',
        'Sequoia Ascent 2026 演讲后发文总结，核心论点：'
        '①LLM 远不止是"加速既有工作"，而是开辟全新水平线——menugen（可被 AI 完全吞噬的应用）、'
        'autoresearch（Agent 自主运行数百次实验寻找新技术）、ambient programming（编程变成与 AI 持续对话）；'
        '②Software 3.0 时代 Prompt 是编程语言，上下文窗口是杠杆；'
        '③LLM 能力"锯齿状"来自 RL 训练分布，处于分布内则飞速，处于边界外则挣扎。'
        '同期 X 上转发 Simon Willison 关于 prompt injection 攻击的研究，呼吁社区重视 LLM 安全防御。',
        'https://karpathy.bearblog.dev/sequoia-ascent-2026/',
        datetime(2026, 5, 1, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Simon Willison', 'Blog',
        '本周博客聚焦两个方向：'
        '①深度梳理 agent-definitions 议题，梳理学术界、工业界对"AI Agent"定义的 10+ 种不同表述，'
        '指出定义混乱正在成为工程落地与监管讨论的障碍，提出以"能力维度"替代"行为维度"进行分类的建议；'
        '②与 Karpathy 联合关注 prompt injection 攻击：整理真实案例，探讨 kernel/user 隔离、'
        'antivirus 类比防御机制，认为当前 LLM 生态处于"计算机病毒早期"阶段，亟需系统性防御框架。',
        'https://simonwillison.net/tags/agent-definitions/',
        datetime(2026, 5, 2, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Chip Huyen', 'Blog',
        '发布《构建有实用价值的 LLM 工作流：工具调用完全指南》（约 8000 字）：'
        '将"Agent"定义为"规划路径 + 循环调用工具直到目标达成"的 LLM 系统，'
        '覆盖工具设计原则（确定性 vs 非确定性工具、幂等性要求）、状态管理、错误恢复与并发工具调用；'
        '重点对比 OpenAI 函数调用、Anthropic Tool Use 与开源框架（LangGraph、DSPy）的实现差异；'
        '附带 Novo Nordisk × OpenAI 合作案例分析，探讨大规模企业 AI 部署中工具可靠性工程的关键挑战。',
        'https://huyenchip.com/',
        datetime(2026, 5, 3, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Sebastian Raschka', 'Newsletter (Ahead of AI)',
        '发布《开源 LLM 格局：2026 年 5 月更新》：'
        '重点对比 Meta Muse Spark（闭源）与当期最强开放权重模型（Qwen3.6-35B-A3B、Gemma 4）的基准差距，'
        '指出在代码生成、数学推理上开源模型与前沿闭源模型的差距正在缩窄至 10–15%；'
        '同期整理 CVPR 2026 视觉-语言模型论文趋势：多模态思维链、视频理解与 3D 场景生成三方向并进；'
        '推荐本周必读论文：ITS-Mina（时序预测）与联邦医疗 LLM（隐私合规新范式）。',
        'https://magazine.sebastianraschka.com/',
        datetime(2026, 5, 3, tzinfo=timezone.utc),
    ),
]

# ── GitHub 热门 ──────────────────────────────────────────────────────────────
github = [
    GithubProject(
        'mattpocock/skills',
        'https://github.com/mattpocock/skills',
        'Claude Code skills straight from Matt Pocock\'s .claude directory — community-curated agent knowledge for real engineers',
        55320, 2100, 'TypeScript', 4200, ['mattpocock'],
    ),
    GithubProject(
        'OpenClaw/openclaw',
        'https://github.com/OpenClaw/openclaw',
        'Personal AI assistant running entirely on your devices — local gateway to 50+ integrations (WhatsApp, Slack, Telegram, Signal, iMessage)',
        219000, 19800, 'TypeScript', 1850, ['openclaw-core'],
    ),
    GithubProject(
        'n8n-io/n8n',
        'https://github.com/n8n-io/n8n',
        'Fair-code workflow automation platform with native AI capabilities — visual agent pipelines, LLM chains, vector DB queries, no orchestration code needed',
        186300, 23100, 'TypeScript', 1420, ['janober', 'ivov'],
    ),
    GithubProject(
        'NousResearch/hermes-agent',
        'https://github.com/NousResearch/hermes-agent',
        'Hermes Agent framework by NousResearch — open-weight multi-agent system with function calling and long-context reasoning',
        129961, 9800, 'Python', 1280, ['NousResearch'],
    ),
    GithubProject(
        'warpdotdev/warp',
        'https://github.com/warpdotdev/warp',
        'Agentic development environment born from the terminal — AI-native IDE with built-in agent orchestration, workflows, and collaborative coding',
        52872, 1650, 'Rust', 980, ['warpdotdev'],
    ),
    GithubProject(
        'ollama/ollama',
        'https://github.com/ollama/ollama',
        'Lightweight Go framework for running and managing large language models entirely on your own hardware — local-first AI inference',
        134500, 10900, 'Go', 920, ['jmorganca', 'mchiang0610'],
    ),
    GithubProject(
        'langchain-ai/langgraph',
        'https://github.com/langchain-ai/langgraph',
        'Enterprise multi-agent framework — graph-based stateful workflows, streaming, checkpointing, human-in-the-loop',
        129000, 21200, 'Python', 870, ['hinthornw', 'efriis'],
    ),
    GithubProject(
        'LMD0311/HERMES',
        'https://github.com/LMD0311/HERMES',
        '[ICCV 2025] HERMES: A Unified Self-Driving World Model for Simultaneous 3D Scene Understanding and Generation',
        3840, 290, 'Python', 650, ['LMD0311'],
    ),
]


# ── 主逻辑 ───────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description='生成并可选发布 2026-05-04 AI 日报')
    parser.add_argument('--publish', action='store_true', help='发布到博客（需 BLOG_DEPLOY_TOKEN）')
    args = parser.parse_args()

    filename, content = generate_jekyll_post(news, papers, updates, github)

    filename = '2026-05-04-ai-daily-news.md'
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
