"""
发布 2026-05-22 AI 日报到博客

数据来源：
  - Bloomberg、CNBC、TechCrunch、Axios 等行业媒体
  - arXiv cs.AI / cs.LG / cs.CL 最新论文
  - GitHub Trending（本周）
  - 大牛 X / Blog 动态

用法：
  # 仅生成 Jekyll 文章到 reports/ 目录
  python generate_post_2026_05_22.py

  # 生成并发布到博客（需要设置 BLOG_DEPLOY_TOKEN 环境变量）
  BLOG_DEPLOY_TOKEN=your_token python generate_post_2026_05_22.py --publish
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
        'OpenAI 秘密提交 IPO S-1，目标 9 月上市，估值最高 $1 万亿',
        'https://www.cnbc.com/2026/05/20/openai-ipo-filing.html',
        'CNBC / Bloomberg', 'industry', datetime(2026, 5, 22, tzinfo=timezone.utc),
        'OpenAI 正在联合高盛和摩根士丹利，准备在数日或数周内向 SEC 提交保密 IPO 申请，'
        '目标 2026 年 9 月在纽交所上市，估值区间 $8520 亿至 $1 万亿。'
        '此次上市将是全球科技史上最大 IPO 之一，与 SpaceX（已于 5 月 20 日提交公开 S-1，估值 $1.75 万亿）同场竞技。',
    ),
    NewsItem(
        'SpaceX 公开提交 Nasdaq IPO（SPCX），估值 $1.75 万亿，史上最大 IPO',
        'https://techcrunch.com/2026/05/20/the-spacex-ipo-filing-ai-bets-starship-dreams-elon-musk/',
        'TechCrunch / Bloomberg', 'industry', datetime(2026, 5, 20, tzinfo=timezone.utc),
        'SpaceX 于 5 月 20 日向 SEC 提交 S-1，拟在 Nasdaq 以代码 SPCX 上市，目标融资 $750 亿，目标日期 6 月 12 日。'
        'Elon Musk 保留 85.1% 投票权（B 类股 10 票/股）。Starlink 占营收逾三分之二，最近一季利润 $12 亿。'
        'S-1 披露 SpaceX 在 AI 方面重注：xAI（现 SpaceXAI 部门）、Colossus 数据中心租赁给 Anthropic。',
    ),
    NewsItem(
        'Anthropic Q2 营收预计 $109 亿，首次实现季度经营盈利',
        'https://www.buildfastwithai.com/blogs/ai-news-today-may-22-2026',
        'Build Fast With AI', 'industry', datetime(2026, 5, 22, tzinfo=timezone.utc),
        'Anthropic 向投资者披露 Q2（截至 2026 年 6 月）财务预测：营收 $109 亿（环比 Q1 $48 亿增长 130%），'
        '预计首次实现季度经营盈利约 $5.59 亿。'
        'Claude Code 及其开发者生态已成为企业 Agentic 编码工具的主导者，为高利润率 API 营收提供持续动力。'
        '年化收入（ARR）已超 $300 亿，千余家企业年消费超 $100 万。',
    ),
    NewsItem(
        'Google 发布 Antigravity 2.0：脱离 IDE 的全代理体验桌面应用',
        'https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/cloud-next-2026-sundar-pichai/',
        'Google Blog', 'tools', datetime(2026, 5, 21, tzinfo=timezone.utc),
        'Google 推出 Antigravity 2.0，取代 IDE 中心的 Agent Manager，提供 macOS / Linux / Windows 全平台支持。'
        '新特性：动态子代理、异步任务管理、JSON Hooks、cron 定时任务，新增 /goal 和 /grill-me 等斜线命令。'
        '由最新 Gemini 模型驱动，面向企业扩展至通用知识工作，同步提供 CLI、SDK 和 API。',
    ),
    NewsItem(
        'OpenAI × 马耳他：全球首个向全体公民提供 ChatGPT Plus 的国家级计划',
        'https://aitoolsrecap.com/Blog/MayNews2026.aspx',
        'AI Tools Recap', 'industry', datetime(2026, 5, 19, tzinfo=timezone.utc),
        'OpenAI 与马耳他政府合作，推出"AI for All"计划：公民完成马耳他大学免费 AI 素养课程后，'
        '即可免费获得一年 ChatGPT Plus 订阅。这是 OpenAI"OpenAI for Countries"计划的首批落地，'
        '同类伙伴还包括爱沙尼亚和希腊。',
    ),
    NewsItem(
        'Anthropic 与 Google、Broadcom 签订 3.5GW TPU 算力扩容协议',
        'https://www.anthropic.com/news/google-broadcom-partnership-compute',
        'Anthropic', 'industry', datetime(2026, 5, 22, tzinfo=timezone.utc),
        'Anthropic 宣布与 Google 和 Broadcom 扩大战略合作，锁定约 3.5GW 算力扩容规模，'
        '新 TPU 基础设施将于 2027 年起逐步上线。Google 此前已承诺以 $350 亿估值投资 $100 亿，'
        '并在 Anthropic 达成绩效目标后追加 $300 亿（总计高达 $400 亿）。',
    ),
    NewsItem(
        'Karpathy 在 Sequoia Ascent 2026 提出 Software 3.0：Agentic Engineering 重塑软件开发',
        'https://karpathy.bearblog.dev/sequoia-ascent-2026/',
        'Andrej Karpathy Blog', 'research', datetime(2026, 5, 15, tzinfo=timezone.utc),
        'Karpathy 在 Sequoia Ascent 2026 火炉访谈中提出 Software 3.0 概念：'
        'AI 不只是加速已有工作流，而是创造全新可能（如 LLM 驱动知识库重构）。'
        'Vibe Coding 抬高地板，Agentic Engineering 抬高天花板——2025 年 12 月是代理编码工具从"有用但混乱"到"持续产出正确代码"的临界点。'
        '他还强调下一波基础设施应"代理原生"，文档、配置、API 为 Agent 而设计。',
    ),
    NewsItem(
        'Nvidia Q1 FY2027 营收 $443 亿（+69% YoY），数据中心业务占 $391 亿',
        'https://fortune.com/2026/05/21/rollout-complete-spacex-files-ipo-prospectus/',
        'Fortune', 'industry', datetime(2026, 5, 21, tzinfo=timezone.utc),
        'Nvidia 公布 Q1 FY2027（截至 4 月）财报：营收 $443 亿，同比增长 69%，超市场预期 $432 亿。'
        '数据中心业务营收 $391 亿（+73%），Blackwell 架构芯片出货加速。'
        '公司同时公布 AI 推断优化的新一代 NVLink 架构路线图，预计 H2 2026 推出。',
    ),
]

# ── 论文 ─────────────────────────────────────────────────────────────────────
papers = [
    Paper(
        'Thinking in Text and Images: Interleaved Vision-Language Reasoning for Robot Manipulation',
        'https://arxiv.org/list/cs.AI/current',
        '2605.15431',
        ['Jinkun Liu', 'Yue Wang', 'Jiajun Wu'],
        '提出交错视觉-语言推理轨迹（Interleaved VL Reasoning Traces）框架，'
        '让机器人在操作长程任务时交替生成文字推理与图像想象，显著提升跨场景泛化能力。'
        '在 RLBench 和 MetaWorld 基准测试中，相较纯文字推理基线分别提升 23% 和 31%。',
        ['cs.AI', 'cs.RO', 'cs.CV'],
        datetime(2026, 5, 21, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2605.15431',
    ),
    Paper(
        'Lifting Traces to Logic: Programmatic Skill Induction via Neuro-Symbolic Learning for Long-Horizon Agents',
        'https://arxiv.org/abs/2605.11234',
        '2605.11234',
        ['Jie-Jing Shao', 'Yu-Feng Li', 'Zhi-Hua Zhou'],
        '提出神经符号技能归纳（NSSI）框架，将 LLM Agent 执行轨迹提炼为可形式验证的逻辑技能程序，'
        '解决长程任务中的"记忆遗忘"与"错误传播"问题。'
        '在 WebArena 和 OSWorld 基准上大幅超越 ReAct、Reflexion 和 Tree-of-Thought。',
        ['cs.AI', 'cs.LG', 'cs.CL'],
        datetime(2026, 5, 20, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2605.11234',
    ),
    Paper(
        'Less Back-and-Forth: A Comparative Study of Structured Prompting for LLMs',
        'https://arxiv.org/list/cs.CL/current',
        '2605.14832',
        ['Saurav Ghosh', 'Gabriella Polach', 'Abdou Sow'],
        '系统比较主流结构化提示技术（思维链 CoT、XML 标签、JSON 输出约束、角色设定等），'
        '在代码生成、数学推理和文本摘要三类任务上量化各方法的效果与成本。'
        '结论：XML 标签结构对代码任务最有效；CoT 在推理任务上仍不可替代，但引入 JSON 约束可减少 40% 往复轮数。',
        ['cs.CL', 'cs.AI'],
        datetime(2026, 5, 21, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2605.14832',
    ),
    Paper(
        'S2Aligner: Pair-Efficient and Transferable Pre-Training for Sparse Text-Attributed Graphs',
        'https://arxiv.org/list/cs.LG/current',
        '2605.13987',
        ['Yuhan Wang', 'Zhenbang Ling', 'Zihao Li'],
        '提出 S2Aligner 预训练框架，通过稀疏文本属性图（TAG）的高效对齐学习，'
        '使 LLM 能以更少标注样本完成图表示迁移。'
        '在学术引用网络和电商推荐图上均取得最优 zero-shot/few-shot 表现，'
        '训练效率比 GraphCL 提升 3.8×。',
        ['cs.LG', 'cs.CL', 'cs.IR'],
        datetime(2026, 5, 22, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2605.13987',
    ),
    Paper(
        'AI Agents for Sustainable SMEs: A Green ESG Assessment Framework via Agentic RAG',
        'https://arxiv.org/list/cs.AI/current',
        '2605.15102',
        ['Research Group on Sustainable AI'],
        '构建面向中小企业的 AI Agent 驱动 ESG 评估框架，结合 Agentic RAG 自动抓取公开财务与运营数据，'
        '生成符合 GRI 标准的可持续发展报告。在 200 家欧洲 SME 上验证，与人工审计结论一致率 87%，耗时减少 70%。',
        ['cs.AI', 'cs.IR'],
        datetime(2026, 5, 21, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2605.15102',
    ),
]

# ── 大牛动态 ──────────────────────────────────────────────────────────────────
updates = [
    InfluencerUpdate(
        'Andrej Karpathy', 'Blog (karpathy.bearblog.dev)',
        'Karpathy 在 Sequoia Ascent 2026 的 Software 3.0 演讲引发广泛转发，并在博客发布完整摘要。\n'
        '核心观点：\n'
        '"Vibe coding 抬高了地板（任何人都能写代码），而 Agentic Engineering 抬高了天花板（专家能做的事指数增长）。\n'
        ' 2025 年 12 月是临界点——从那以后我几乎不再纠正 AI 的代码输出。"\n'
        '他还预言下一波基础设施将是"Agent-native"：文档、配置和 API 为 Agent 设计，而非人类。\n'
        '该演讲被 Sequoia 合伙人称为"本届 Ascent 最受欢迎的分享"。',
        'https://karpathy.bearblog.dev/sequoia-ascent-2026/',
        datetime(2026, 5, 15, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Yann LeCun', 'LinkedIn / AMI Labs',
        'LeCun 持续发声反对当前 LLM 路线，并披露 AMI Labs 进展：\n'
        '"OpenAI 的 IPO 准备再次证明：市场愿意为"下一个 token 预测"赋予万亿估值。'
        '但物理世界需要的是在潜在空间建模的世界模型，不是统计相关性的极致放大。"\n'
        'JEPA-4 第二阶段训练已引入多模态时序数据（视频 + 传感器流）联合预训练，'
        '目标让世界模型具备真正的"物理直觉"。LeCun 表示：预计 2026 年底展示初步成果。',
        'https://www.linkedin.com/in/yann-lecun/',
        datetime(2026, 5, 21, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Simon Willison', 'Blog (simonwillison.net)',
        '本周深度追踪三件大事：\n'
        '① SpaceX S-1 中的 AI 押注：将 xAI / Grok / Colossus 并入 SpaceX 的战略含义；\n'
        '② Google Antigravity 2.0 的 Hooks 机制——他认为这是"Claude Code hooks 理念的 Google 版落地"；\n'
        '③ OpenAI IPO 前夕的企业 API 策略（Guaranteed Capacity + 国家级合作）。\n'
        '引用 Karpathy 的 "Agent-native infrastructure" 概念，补充道：\n'
        '"未来每一个 SaaS 产品的文档都需要一份 machine-readable 版本，这会成为新的 SEO。"',
        'https://simonwillison.net/',
        datetime(2026, 5, 22, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Sebastian Raschka', 'Newsletter (Ahead of AI)',
        '本期 Newsletter 聚焦两大主题：\n'
        '① 深入解析 NSSI（Lifting Traces to Logic）——他认为这是"将 LLM Agent 的行为形式化验证的重要一步"；\n'
        '② 回顾 Q2 2026 开源模型格局：Llama 4 Maverick 仍是性价比标杆，但 Gemma 3.5 系列正快速追赶。\n'
        '对 Karpathy 的 Software 3.0 框架补充了学习曲线视角：\n'
        '"对于 ML 研究者，Agentic Engineering 意味着实验设计 → 代码生成 → 结果分析全程代理化，'
        '但假设质量仍是人类的护城河。"',
        'https://magazine.sebastianraschka.com/',
        datetime(2026, 5, 21, tzinfo=timezone.utc),
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
        'NousResearch/hermes-agent',
        'https://github.com/NousResearch/hermes-agent',
        'The agent that grows with you — reliability-first AI agent with self-improvement, optimized for NVIDIA RTX & DGX Spark',
        130000, 12400, 'Python', 1540,
        ['NousResearch'],
    ),
    GithubProject(
        'mattpocock/skills',
        'https://github.com/mattpocock/skills',
        'AI agent skills & behavioral patterns for coding workflows — Skills for Real Engineers',
        55320, 4210, 'TypeScript', 2130,
        ['mattpocock'],
    ),
    GithubProject(
        'warpdotdev/warp',
        'https://github.com/warpdotdev/warp',
        'Warp is a modern, Rust-based terminal and agentic development environment with AI built in',
        52872, 1540, 'Rust', 1680,
        ['warpdotdev'],
    ),
    GithubProject(
        'mariozechner/pi-mono',
        'https://github.com/mariozechner/pi-mono',
        'AI agent toolkit: coding agent CLI, unified LLM API, TUI & web UI libraries, Slack bot, vLLM pods',
        44900, 3800, 'TypeScript', 1120,
        ['mariozechner'],
    ),
    GithubProject(
        'karpathy/autoresearch',
        'https://github.com/karpathy/autoresearch',
        'Autonomous research loop: AI agent that iteratively improves code/models via hypothesis → experiment → analyze → repeat',
        83500, 6200, 'Python', 760,
        ['karpathy'],
    ),
    GithubProject(
        'Zijian-Ni/awesome-ai-agents-2026',
        'https://github.com/Zijian-Ni/awesome-ai-agents-2026',
        '🤖 A curated list of AI Agent frameworks, tools, platforms, and resources for 2026 — the year agents went mainstream',
        18700, 1820, '', 940,
        ['Zijian-Ni'],
    ),
]


def main():
    parser = argparse.ArgumentParser(description='生成 2026-05-22 AI 日报')
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
