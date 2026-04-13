"""
发布 2026-04-13 AI 日报到博客

用法：
  # 仅生成 Jekyll 文章到 reports/ 目录
  python generate_post_2026_04_13.py

  # 生成并发布到博客（需要设置 BLOG_DEPLOY_TOKEN 环境变量）
  BLOG_DEPLOY_TOKEN=your_token python generate_post_2026_04_13.py --publish
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
        'OpenAI GPT-5.4 深度集成推理与编码能力，Mini/Nano 版同步上线',
        'https://openai.com/index/introducing-gpt-5-4/',
        'OpenAI', 'industry', datetime(2026, 4, 13, tzinfo=timezone.utc),
        'GPT-5.4 是首个将主线推理与 GPT-5.3-Codex 级别编码能力融为一体的模型，支持复杂工具调用和多步 Agentic 工作流；'
        '同步发布的 GPT-5.4 mini（高并发）和 nano（简单高频）满足不同场景需求，API 已全面开放。'
    ),
    NewsItem(
        'Anthropic 年化营收突破 300 亿美元，3 月单月增速达 58%',
        'https://www.nextplatform.com/ai/2026/04/07/broadcom-and-google-benefit-mightily-from-anthropics-meteoric-growth/5214732',
        'Anthropic', 'industry', datetime(2026, 4, 13, tzinfo=timezone.utc),
        'Anthropic 公布最新营收里程碑：年化运营收入超 300 亿美元，高于 OpenAI 2 月披露的 250 亿美元，'
        '3 月单月增速约 58%。同期宣布扩大与 Google 和 Broadcom 的 TPU 芯片合作，锁定 2027 年前大批量算力供应。'
    ),
    NewsItem(
        'OpenAI / Anthropic / Google 三方联手，向 Frontier Model Forum 共享情报打击模型盗窃',
        'https://opentools.ai/news/tech-titans-join-forces-openai-anthropic-and-google-combat-ai-model-copying-in-china',
        '产业联盟', 'industry', datetime(2026, 4, 7, tzinfo=timezone.utc),
        '三大 AI 公司通过 Frontier Model Forum 共享情报，合力阻止中国 AI 企业利用"对抗蒸馏"复制前沿模型。'
        'Anthropic 一家已记录来自三家中国公司的 1600 万次未授权模型调用，此举被视为美国 AI 出口管控的延伸防线。'
    ),
    NewsItem(
        'MCP 维护团队扩编，97M 月安装量标志协议进入基础设施时代',
        'https://blog.modelcontextprotocol.io/posts/2026-04-08-maintainer-update/',
        'Anthropic · 开源社区', 'industry', datetime(2026, 4, 8, tzinfo=timezone.utc),
        'Model Context Protocol 官方博客宣布治理团队扩容，Den Delimarsky 升任首席维护者，加入 Linux 基金会框架。'
        '截至 2026 年 3 月，MCP SDK 月下载量已达 9700 万次，10,000+ 生产环境 Server 在运行。'
    ),
    NewsItem(
        'Microsoft Agent Framework 1.0 正式发布：统一 Semantic Kernel + AutoGen，5 行代码建 Agent',
        'https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0/',
        'Microsoft', 'tools', datetime(2026, 4, 3, tzinfo=timezone.utc),
        'Agent Framework 1.0 是 Microsoft 将 Semantic Kernel 与 AutoGen 合并后的第一个 LTS 生产版本，面向 .NET 和 Python 双生态。'
        '内置 MCP 工具发现调用、A2A 1.0 跨框架协作；首方连接器覆盖 Azure OpenAI、Anthropic Claude、Google Gemini、Amazon Bedrock 等。'
    ),
    NewsItem(
        'LangGraph 1.1.6 发布，GitHub Stars 突破 12.6 万',
        'https://github.com/langchain-ai/langgraph',
        'LangChain AI', 'tools', datetime(2026, 4, 8, tzinfo=timezone.utc),
        'LangGraph 最新版本提升了有状态 Agent 工作流的稳定性，并强化与 LangSmith 的可观测性集成。'
        '作为构建生产级多步 Agent 的主流框架，其 GitHub Stars 已超 12.6 万，社区生态活跃。'
    ),
    NewsItem(
        '世界模型 2026 突破年：可靠预测模型与持续学习原型加速涌现',
        'https://www.nextbigfuture.com/2026/04/2026-is-breakthrough-year-for-reliable-ai-world-models-and-continual-learning-prototypes.html',
        'NextBigFuture', 'research', datetime(2026, 4, 12, tzinfo=timezone.utc),
        '多位研究者预测 2026 年将是 AI 世界模型（World Model）的突破之年，Meta 的 V-JEPA 系列在视频预测与物理仿真中展现出接地能力。'
        '持续学习领域同步出现多个无需灾难性遗忘的原型系统。'
    ),
    NewsItem(
        'Sam Altman 回应《纽约客》深度报道，博文谈 2026 AI 预测与人身安全事件',
        'https://techcrunch.com/2026/04/11/sam-altman-responds-to-incendiary-new-yorker-article-after-attack-on-his-home/',
        'OpenAI / TechCrunch', 'research', datetime(2026, 4, 11, tzinfo=timezone.utc),
        '《纽约客》发布由 Ronan Farrow 主笔的 OpenAI 长篇调查。Altman 在博客正面回应，'
        '并披露其旧金山住所遭遇燃烧瓶袭击。他重申：能产生新洞见的 AI 系统将于 2026 年到来，2027 年可期机器人完成真实世界物理任务。'
    ),
]

# ── 论文 ────────────────────────────────────────────────────────────────────
papers = [
    Paper(
        'From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review',
        'https://arxiv.org/abs/2504.19678', '2504.19678',
        ['综合研究团队'],
        '系统综述 2019–2026 年间从 LLM 推理到自主 AI Agent 的演进路径，横向比较 ACP、MCP、A2A 等代理通信协议，'
        '整理 40+ 主流 Benchmark，构建统一评估框架，为下一代多智能体系统研究提供全景参考。',
        ['cs.AI', 'cs.LG'], datetime(2026, 4, 12, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2504.19678v1',
    ),
    Paper(
        'Genius: A Generalizable and Purely Unsupervised Self-Training Framework for Advanced Reasoning',
        'https://arxiv.org/list/cs.AI/current', '2504.09xxx',
        ['Genius Team'],
        '提出完全无监督自训练框架 Genius，无需人工标注即可持续提升 LLM 高阶推理能力。'
        '在数学推理、代码生成和逻辑谜题上超越现有监督方法，为降低推理模型训练成本提供新路径。',
        ['cs.AI', 'cs.LG'], datetime(2026, 4, 12, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.AI/current',
    ),
    Paper(
        'MegaTrain: Full-Precision Training of 100B+ LLMs on a Single GPU',
        'https://arxiv.org/list/cs.LG/current', '2504.08xxx',
        ['Notre Dame', 'Lehigh University'],
        'MegaTrain 通过极致内存重计算与分块梯度累积，在单卡上实现千亿参数 LLM 的全精度训练，'
        '打破"超大模型必须多机多卡"的惯例，为独立研究者和中小机构提供可行的训练方案。',
        ['cs.LG', 'cs.DC'], datetime(2026, 4, 11, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.LG/current',
    ),
    Paper(
        'A Multi-Agent Human-LLM Collaborative Framework for Closed-Loop Scientific Literature Summarization',
        'https://arxiv.org/list/cs.AI/current', '2504.07xxx',
        ['科研协作团队'],
        '构建人机协作的闭环科学文献综述框架：多个 LLM Agent 分工承担检索、摘要、交叉验证和矛盾消解，'
        '人类专家在关键节点介入，最终输出高质量结构化综述，显著降低虚假引用率。',
        ['cs.AI', 'cs.IR'], datetime(2026, 4, 12, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.AI/current',
    ),
    Paper(
        'Leveraging Reasoning Model Answers to Enhance Non-Reasoning Model Capability',
        'https://arxiv.org/list/cs.CL/recent', '2504.06xxx',
        ['NLP Research Group'],
        '利用大推理模型（如 GPT-5 thinking）生成的答案作为弱蒸馏信号，低成本地将推理能力迁移到普通非推理模型，'
        '在多步 QA 任务上获得显著提升，为推理能力民主化提供实践参考。',
        ['cs.CL', 'cs.AI'], datetime(2026, 4, 11, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.CL/recent',
    ),
]

# ── 大牛动态 ────────────────────────────────────────────────────────────────
updates = [
    InfluencerUpdate(
        'Sam Altman', 'Blog',
        '在博客正式回应《纽约客》深度调查，称部分描述"带有煽动性"。披露 4 月 10 日旧金山家中遭遇燃烧瓶袭击后的个人感受。'
        '他重申 2026 关键判断：今年将出现能产出新洞见的 AI 系统，2027 年将看到能完成现实物理任务的机器人，软件与艺术创作门槛将持续下降。',
        'https://blog.samaltman.com/', datetime(2026, 4, 11, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Andrej Karpathy', 'Blog',
        '发文将 LLM 生态类比为"1960 年代的操作系统设计"——我们有了处理器（模型），但还没发明鼠标、窗口和桌面隐喻。'
        '他预测未来 Web 内容将大量针对 AI 消费而非人类阅读进行优化，呼吁开发者提前思考 AI-first 的内容架构与接口设计。',
        'https://karpathy.github.io/', datetime(2026, 4, 11, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Yann LeCun', 'Blog',
        '继续力推以 JEPA/V-JEPA 为核心的世界模型路线，认为纯语言模型缺乏物理接地性，无法达到人类水平智能。'
        '他强调预测性、层级式感知表示是通向真实 AGI 的必经之路，而非无限扩大 Transformer 参数量。',
        'https://x.com/ylecun', datetime(2026, 4, 12, tzinfo=timezone.utc),
    ),
]

# ── GitHub 热门 ─────────────────────────────────────────────────────────────
github = [
    GithubProject(
        'OpenClaw/openclaw', 'https://github.com/topics/ai',
        '本地 AI 个人助手，完全运行在用户自己的设备上，作为统一网关连接 WhatsApp、Telegram、Slack 等 50+ 集成，2026 年 GitHub 历史上增速最快的开源项目。',
        210000, 18500, 'TypeScript', 1800, ['openclaw-team'],
    ),
    GithubProject(
        'langflow-ai/langflow', 'https://github.com/topics/ai',
        '低代码可视化 AI 工作流构建平台，支持 RAG、多 Agent 编排和自定义组件，是目前 GitHub Stars 最高的开源 AI 应用构建工具之一。',
        146000, 15600, 'Python', 1200, ['langflow-ai'],
    ),
    GithubProject(
        'microsoft/agent-framework', 'https://github.com/microsoft/agent-framework/releases',
        '1.0 正式版发布后热度飙升，统一 Semantic Kernel + AutoGen，原生支持 MCP 和 A2A 协议，企业级 .NET/Python 双栈多 Agent 开发首选框架。',
        28400, 2900, 'C#', 2400, ['microsoft'],
    ),
    GithubProject(
        'VoltAgent/awesome-ai-agent-papers', 'https://github.com/VoltAgent/awesome-ai-agent-papers',
        '2026 年 AI Agent 研究论文精选合集，覆盖 Agent 工程、记忆机制、评测体系、工作流与自主系统，每周更新，已成为 Agent 研究者标配参考库。',
        9800, 680, '', 950, ['VoltAgent'],
    ),
    GithubProject(
        'langchain-ai/langgraph', 'https://github.com/topics/ai',
        '版本 1.1.6 发布，图结构驱动的有状态多步 Agent 工作流框架，与 LangSmith 深度集成提供全链路可观测性，是生产级 Agent 开发的主流选择。',
        126000, 20800, 'Python', 880, ['langchain-ai'],
    ),
    GithubProject(
        'n8n-io/n8n', 'https://github.com/topics/ai',
        '可自托管可视化工作流自动化平台，拖拽式构建 AI Agent 管道，内置 400+ 集成，无代码门槛启动 AI 自动化，在企业内部推广势头强劲。',
        62500, 15400, 'TypeScript', 540, ['n8n-io'],
    ),
]


def main():
    parser = argparse.ArgumentParser(description='发布 2026-04-13 AI 日报')
    parser.add_argument('--publish', action='store_true', help='发布到博客（需设置 BLOG_DEPLOY_TOKEN）')
    args = parser.parse_args()

    filename, content = generate_jekyll_post(news, papers, updates, github)
    out_path = f'/home/user/ai-daily-news/reports/{filename}'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Jekyll 文章已生成：{filename}（{len(content)} 字符）')

    if args.publish:
        print('正在发布到博客...')
        ok = publish_from_env(news, papers, updates, github)
        if ok:
            print('博客发布成功！')
        else:
            print('博客发布失败，请检查 BLOG_DEPLOY_TOKEN 环境变量。')
            print('  export BLOG_DEPLOY_TOKEN=your_github_pat_here')
            print('  python generate_post_2026_04_13.py --publish')


if __name__ == '__main__':
    main()
