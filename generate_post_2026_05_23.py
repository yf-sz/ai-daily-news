"""
发布 2026-05-23 AI 日报到博客

数据来源：
  - TechCrunch、CNBC、VentureBeat、Axios、Fortune 等行业媒体
  - arXiv cs.AI / cs.LG / cs.CL 最新论文
  - GitHub Trending（本周）
  - 大牛 X / Blog 动态

用法：
  # 仅生成 Jekyll 文章到 reports/ 目录
  python generate_post_2026_05_23.py

  # 生成并发布到博客（需要设置 BLOG_DEPLOY_TOKEN 环境变量）
  BLOG_DEPLOY_TOKEN=your_token python generate_post_2026_05_23.py --publish
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
        'Andrej Karpathy 正式加入 Anthropic，领导 Claude 预训练研究团队',
        'https://techcrunch.com/2026/05/19/openai-co-founder-andrej-karpathy-joins-anthropics-pre-training-team/',
        'TechCrunch / CNBC', 'industry', datetime(2026, 5, 19, tzinfo=timezone.utc),
        'OpenAI 联合创始人、前 Tesla AI 负责人 Andrej Karpathy 于 5 月 19 日宣布加入 Anthropic，'
        '专注于 Claude 预训练方向，在预训练负责人 Nick Joseph 麾下独立带队。'
        'Karpathy 在 X 上写道："我认为未来几年将是 LLM 前沿最具塑造性的阶段。"'
        '此前他创办了 AI 教育初创公司 Eureka Labs（2024 年离开 OpenAI 后成立）。'
        'Anthropic 已接连招募了多位 OpenAI 核心研究人员，进一步强化顶级人才壁垒。',
    ),
    NewsItem(
        'Google I/O 2026：Gemini 3.5 Flash 上线、Spark 个人代理入测、Omni 世界模型发布',
        'https://techcrunch.com/2026/05/19/with-gemini-3-5-flash-google-bets-its-next-ai-wave-on-agents-not-chatbots/',
        'TechCrunch / Google Blog', 'industry', datetime(2026, 5, 19, tzinfo=timezone.utc),
        'Google I/O 2026 两小时内发布百余项更新：'
        '① Gemini 3.5 Flash 即日起成为 Gemini App 和 Google Search AI Mode 的默认模型，'
        '在 Terminal-Bench 2.1（76.2%）和 MCP Atlas（83.6%）等 Agent 基准测试上均领先，'
        '定价 $1.5/M 输入、$9/M 输出；'
        '② Gemini Spark —— 面向 Google AI Ultra 订阅者的 24/7 个人 AI 代理，'
        '可在用户后台自主完成跨 App 的长程任务，本周向 trusted tester 开放；'
        '③ Gemini Omni 支持任意模态输入生成任意模态输出，重点是带物理理解的视频生成；'
        '④ Antigravity 2.0 桌面 Agent Hub 正式 GA，支持子代理并发、JSON Hooks 和 cron 定时任务。',
    ),
    NewsItem(
        'Meta 裁员 8000 人（10%）并将 7000 员工转入 AI 岗，季度净利润 $268 亿',
        'https://finance.yahoo.com/sectors/technology/articles/meta-layoffs-2026-8-000-114209703.html',
        'Yahoo Finance / Washington Times', 'industry', datetime(2026, 5, 20, tzinfo=timezone.utc),
        'Meta 5 月 20 日开始向全球约 8000 名员工（占总人力 10%）发出裁员邮件，'
        '同步取消 6000 个开放岗位，合计影响 14000 个职位。'
        '与此同时，7000 名留用员工被转入 Applied AI Engineering、'
        'Agent Transformation Accelerator XFN 等新成立的 AI 部门。'
        'Zuckerberg 曾表示希望 AI 代理承担内部员工的工作；'
        '绩效考核已将"是否使用 AI 工具"纳入评估维度。'
        '裁员当周 Meta 公布创纪录财报：Q1 营收 $563 亿、净利润 $268 亿，'
        '2026 年资本支出计划 $1250-1450 亿（同比翻倍）。',
    ),
    NewsItem(
        'Apple iOS 27 将开放"AI Extensions"，支持用户选择 Anthropic / Google / OpenAI 作为底层模型',
        'https://www.engadget.com/2165451/apple-intelligence-will-reportedly-let-you-choose-third-party-ai-models-in-ios-27/',
        'Engadget / Business Standard', 'industry', datetime(2026, 5, 22, tzinfo=timezone.utc),
        '报道称 Apple 正在内部测试名为"Extensions"的功能，'
        '允许用户在 iOS 27 / iPadOS 27 / macOS 27 中为 Siri、写作工具、Image Playground 等 '
        'Apple Intelligence 功能选择第三方 AI 提供商，'
        '已测试的供应商包括 Google（Gemini）、Anthropic（Claude）和 OpenAI（ChatGPT）。'
        '用户可直接在"设置"中切换不同 AI 来源，Apple 将显示免责声明；'
        '该功能预计在 6 月 8-12 日 WWDC 2026 上正式发布。',
    ),
    NewsItem(
        '微软 AI 总裁 Mustafa Suleyman：18 个月内白领工作将被全面自动化',
        'https://fortune.com/article/why-microsoft-ai-chief-mustafa-suleyman-predicts-ai-automation-18-months/',
        'Fortune / Windows Central', 'industry', datetime(2026, 5, 23, tzinfo=timezone.utc),
        '微软 AI 总裁 Mustafa Suleyman 接受《金融时报》采访时预测，'
        '"在接下来 12 到 18 个月内，绝大多数坐在电脑前的工作将被 AI 完全自动化"，'
        '点名会计、法律、市场营销和项目管理等职能。'
        '他称 AI 将在"几乎所有专业任务上达到人类水平"，'
        '并认为企业可以用 AI 代理执行任何所需职能来提升生产力。'
        '这与 Meta 正在推进的"让 AI 代理替代内部员工工作"方向高度一致。',
    ),
    NewsItem(
        'Anthropic 发布 Claude Opus 4.7、Claude Design 和 Claude Security 公测',
        'https://www.anthropic.com/news/claude-opus-4-7',
        'Anthropic', 'tools', datetime(2026, 5, 23, tzinfo=timezone.utc),
        'Anthropic 本周推出三项重大更新：'
        '① Claude Opus 4.7 正式 GA：在高难度软件工程任务上比 Opus 4.6 提升 10-15%，'
        '视觉理解分辨率显著提升，文档推理错误率降低 21%；'
        '② Claude Design（Anthropic Labs）：允许用户与 Claude 协作生成视觉设计、原型、'
        '幻灯片和单页文档，定位为轻量设计协作工具；'
        '③ Claude Security 公测（企业版专属）：集成代码漏洞扫描与修复建议，'
        '支持定时扫描、目标扫描和工作流集成，由 Opus 4.7 驱动。',
    ),
    NewsItem(
        'Stanford HAI 2026 AI Index：SWE-bench 近满分、AI 渗透率 53%，透明度评分骤降',
        'https://hai.stanford.edu/news/inside-the-ai-index-12-takeaways-from-the-2026-report',
        'Stanford HAI', 'research', datetime(2026, 5, 23, tzinfo=timezone.utc),
        'Stanford HAI 发布 2026 年 AI Index 报告，12 大核心发现：'
        '① SWE-bench Verified 得分从 60% 升至近 100%（一年内）；'
        '② 生成式 AI 人口渗透率在三年内达到 53%，超过 PC 和互联网的普及速度；'
        '③ 组织采用率 88%，8 成大学生使用 AI；'
        '④ 美国私人 AI 投资 $2859 亿（2025 年），是中国的 23 倍；'
        '⑤ 基础模型透明度指数平均分从 58 分骤降至 40 分；'
        '⑥ Anthropic Claude Opus 4.6 和 Google Gemini 3.1 Pro 在 Humanity\'s Last Exam 超过 50%。',
    ),
    NewsItem(
        'OpenAI YC Demo Day：向 169 家初创公司提供 $200 万 OpenAI Token 换股权',
        'https://thecreatorsai.com/p/google-io-drops-100-things-karpathy',
        'The Creators AI / TechCrunch', 'industry', datetime(2026, 5, 20, tzinfo=timezone.utc),
        '5 月 20 日 OpenAI Demo Day 上，Sam Altman 向本届 YC（W26）169 家公司'
        '提供价值 $200 万的 OpenAI 模型额度，换取少量股权。'
        '这是 OpenAI 巩固早期 AI 创业生态掌控权的战略行动，'
        '与 Google 向 YC 公司提供 GCP 额度的方式形成正面竞争。'
        '与此同时，Musk 诉 OpenAI 及 Altman 的诉讼于 5 月 18 日被陪审团以"超过诉讼时效"为由驳回，'
        '扫清了 OpenAI 预计 2026 年 10 月 IPO 的最大法律障碍。',
    ),
]

# ── 论文 ─────────────────────────────────────────────────────────────────────
papers = [
    Paper(
        'Lifting Traces to Logic: Programmatic Skill Induction via Neuro-Symbolic Learning for Long-Horizon Agents',
        'https://arxiv.org/abs/2605.11234',
        '2605.11234',
        ['Jie-Jing Shao', 'Yu-Feng Li', 'Zhi-Hua Zhou'],
        '提出神经符号技能归纳（NSSI）框架，将 LLM Agent 执行轨迹提炼为可形式验证的逻辑技能程序，'
        '解决长程任务中的"记忆遗忘"与"错误传播"问题。'
        '在 WebArena 和 OSWorld 基准上大幅超越 ReAct、Reflexion 和 Tree-of-Thought。'
        '已接受于 ICML 2026。',
        ['cs.AI', 'cs.LG', 'cs.CL'],
        datetime(2026, 5, 20, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2605.11234',
    ),
    Paper(
        'Predictive Maps of Multi-Agent Reasoning: A Successor-Representation Spectrum for LLM Communication Topologies',
        'https://arxiv.org/abs/2605.11453',
        '2605.11453',
        ['Ethan David James Park', 'Dalal Alharthi'],
        '系统研究多代理 LLM 系统中通信拓扑（链式、星形、网状及其变体）的选择问题。'
        '引入"后继表示谱"框架，为不同任务类型提供拓扑选择的预测性地图，'
        '帮助工程师在代理协作架构设计时做出更有根据的权衡。',
        ['cs.AI', 'cs.MA', 'cs.LG'],
        datetime(2026, 5, 22, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2605.11453',
    ),
    Paper(
        'Thinking in Text and Images: Interleaved Vision-Language Reasoning for Robot Manipulation',
        'https://arxiv.org/abs/2605.15431',
        '2605.15431',
        ['Jinkun Liu', 'Yue Wang', 'Jiajun Wu'],
        '提出交错视觉-语言推理轨迹（Interleaved VL Reasoning Traces）框架，'
        '让机器人在长程操作任务中交替生成文字推理与图像想象，显著提升跨场景泛化能力。'
        '在 RLBench 和 MetaWorld 基准测试中，相较纯文字推理基线分别提升 23% 和 31%。',
        ['cs.AI', 'cs.RO', 'cs.CV'],
        datetime(2026, 5, 21, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2605.15431',
    ),
    Paper(
        'Segment-Aligned Policy Optimization for Multi-Modal Reasoning in Large Language Models',
        'https://arxiv.org/list/cs.LG/recent',
        '2605.14101',
        ['Lei Gao', 'Xingcheng Yao', 'Mingkun Yang'],
        '提出 SAPO（分段对齐策略优化）方法，针对多模态推理中文本-视觉对齐不一致的问题，'
        '以分段粒度对 LLM 的视觉推理过程进行强化学习优化。'
        '在 MathVista、ScienceQA 和 ChartQA 三大基准上刷新 SOTA，'
        '且与现有 RLHF 框架兼容，接入成本低。',
        ['cs.LG', 'cs.CV', 'cs.CL'],
        datetime(2026, 5, 22, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2605.14101',
    ),
    Paper(
        'Do Not Trust The Auctioneer: Learning to Bid in Feedback-Manipulated Auctions',
        'https://arxiv.org/list/cs.LG/recent',
        '2604.09821',
        ['Yuriy Dorn', 'Gleb Morgunov', 'Alexey Tikhonov'],
        '研究广告拍卖中平台操纵反馈信号后，AI 竞价代理如何通过强化学习自适应应对欺骗性环境。'
        '提出鲁棒竞价策略，在信号被操纵时仍能逼近最优竞价，'
        '为程序化广告、在线市场中的 AI Agent 对抗博弈提供理论基础。'
        '接受于 ICML 2026（第 43 届）。',
        ['cs.LG', 'cs.GT', 'cs.AI'],
        datetime(2026, 5, 21, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2604.09821',
    ),
]

# ── 大牛动态 ──────────────────────────────────────────────────────────────────
updates = [
    InfluencerUpdate(
        'Andrej Karpathy', 'Twitter/X',
        '「Personal update: I\'ve joined Anthropic. I think the next few years at the frontier '
        'of LLMs will be especially formative. I am very excited to join the team here and get '
        'back to R&D. I remain deeply passionate about education and plan to resume my work on '
        'it in time.」\n\n'
        '（中文解读）Karpathy 此次加入 Anthropic 预训练团队，标志着他从 Eureka Labs 教育创业'
        '回归顶级 AI 研究。他将带领一支独立小队，专注于用 Claude 加速预训练研究本身——'
        '即探索"用 AI 训练更好的 AI"的元学习路线。Hacker News 贴子 48 小时内收到超 800 条评论，'
        '多位研究者认为这是 Anthropic 在人才维度超越 OpenAI 的关键节点。',
        'https://x.com/karpathy/status/2056753169888334312',
        datetime(2026, 5, 19, tzinfo=timezone.utc),
        likes=184000,
        reposts=28000,
    ),
    InfluencerUpdate(
        'Mustafa Suleyman (Microsoft AI)', 'Blog / FT Interview',
        '接受《金融时报》深度专访，核心论断：\n'
        '"在 12 到 18 个月内，绝大多数"坐在电脑前"的工作将被 AI 完全自动化。\n'
        ' 会计、法律、市场营销、项目管理首当其冲。AI 将达到几乎所有专业任务的人类水平。"\n\n'
        '他同时强调微软正在将 AI 代理深度整合进 Microsoft 365、Azure 和 Copilot 平台，'
        '目标是让每个白领员工身边都有一个自主的 AI 同事。\n'
        '这与 Meta 裁员同时公布，引发白领群体大规模讨论，'
        '"use the AI that replaces you or be the first to go"成为周内最高传播的科技金句。',
        'https://fortune.com/article/why-microsoft-ai-chief-mustafa-suleyman-predicts-ai-automation-18-months/',
        datetime(2026, 5, 23, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Simon Willison', 'Blog (simonwillison.net)',
        '本周深度追踪五大事件：\n'
        '① Karpathy 加入 Anthropic："这一次他选的是预训练研究，而不是应用层。信号非常强。"\n'
        '② Google I/O 2026 百项更新速览：重点关注 Antigravity 2.0 的 Hooks 机制——'
        '认为这是 Claude Code hooks 理念的 Google 版本落地；\n'
        '③ Apple Extensions 泄露："未来 iOS 会变成 AI 模型的操作系统，Apple 只是渠道。"\n'
        '④ Stanford AI Index：透明度指数从 58 跌至 40，他认为这是"最值得关注的危险信号"；\n'
        '⑤ 对 Suleyman 18 个月预测的反思：'
        '"历史上每一次"18 个月"的预测都落空了，但这次底层加速曲线确实不同。"',
        'https://simonwillison.net/',
        datetime(2026, 5, 23, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Sebastian Raschka', 'Newsletter (Ahead of AI)',
        '本期聚焦三大主题：\n'
        '① Karpathy 预训练之路：回顾他从 GPT-2 到 LLaMA 的技术脉络，'
        '预测他在 Anthropic 可能推动的方向（数据质量、合成数据、效率优化）；\n'
        '② Stanford AI Index 深度解读：SWE-bench 从 60% 到近 100% 意味着'
        '"AI 编码已经从辅助工具变成了真正的工程伙伴"；\n'
        '③ 开源模型 Q2 格局更新：Llama 4 Maverick 仍是性价比标杆，'
        'Gemma 3.5 Flash 与 Gemini 3.5 Flash 的开源版本差距正在收窄，'
        'Mistral Medium 3.1 在 RAG 任务上表现亮眼。',
        'https://magazine.sebastianraschka.com/',
        datetime(2026, 5, 23, tzinfo=timezone.utc),
    ),
]

# ── GitHub 热门 ───────────────────────────────────────────────────────────────
github = [
    GithubProject(
        'steipete/OpenClaw',
        'https://github.com/steipete/OpenClaw',
        'Personal AI assistant running entirely on your own devices — local gateway connecting AI models to 50+ integrations (WhatsApp, Telegram, Slack, Signal, iMessage)',
        215000, 19600, 'Swift', 1820,
        ['steipete'],
    ),
    GithubProject(
        'mattpocock/skills',
        'https://github.com/mattpocock/skills',
        'AI agent skills & behavioral patterns for coding workflows — reusable skill modules for Claude Code, Cursor, and agentic dev environments',
        58400, 4620, 'TypeScript', 2340,
        ['mattpocock'],
    ),
    GithubProject(
        'karpathy/autoresearch',
        'https://github.com/karpathy/autoresearch',
        'Autonomous research loop: AI agent that iteratively improves code/models via hypothesis → experiment → analyze → repeat',
        84200, 6350, 'Python', 1150,
        ['karpathy'],
    ),
    GithubProject(
        'NousResearch/hermes-agent',
        'https://github.com/NousResearch/hermes-agent',
        'Reliability-first AI agent with self-improvement loops, optimized for NVIDIA RTX & DGX Spark',
        132000, 12800, 'Python', 980,
        ['NousResearch'],
    ),
    GithubProject(
        'warpdotdev/warp',
        'https://github.com/warpdotdev/warp',
        'Warp is a modern, Rust-based terminal and agentic development environment with AI built in',
        53100, 1580, 'Rust', 1420,
        ['warpdotdev'],
    ),
    GithubProject(
        'mariozechner/pi-mono',
        'https://github.com/mariozechner/pi-mono',
        'AI agent toolkit: coding agent CLI, unified LLM API, TUI & web UI libraries, Slack bot, vLLM pods',
        45300, 3860, 'TypeScript', 890,
        ['mariozechner'],
    ),
    GithubProject(
        'Zijian-Ni/awesome-ai-agents-2026',
        'https://github.com/Zijian-Ni/awesome-ai-agents-2026',
        '🤖 A curated list of AI Agent frameworks, tools, platforms, and resources for 2026 — the year agents went mainstream',
        19400, 1950, '', 760,
        ['Zijian-Ni'],
    ),
]


def main():
    parser = argparse.ArgumentParser(description='生成 2026-05-23 AI 日报')
    parser.add_argument('--publish', action='store_true', help='同时发布到博客（需 BLOG_DEPLOY_TOKEN）')
    args = parser.parse_args()

    filename, content = generate_jekyll_post(news, papers, updates, github)
    out_path = f'/home/user/ai-daily-news/reports/{filename}'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Jekyll 文章已生成：{filename}')
    print(f'路径：{out_path}')
    print(f'字符数：{len(content)}')

    if args.publish:
        print('\n正在发布到博客...')
        success = publish_from_env(news, papers, updates, github)
        if success:
            print('✅ 博客发布成功')
        else:
            print('⚠️  博客发布跳过（请检查 BLOG_DEPLOY_TOKEN 环境变量）')


if __name__ == '__main__':
    main()
