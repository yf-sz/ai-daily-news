"""
发布 2026-05-20 AI 日报到博客

用法：
  # 仅生成 Jekyll 文章到 reports/ 目录
  python generate_post_2026_05_20.py

  # 生成并发布到博客（需要设置 BLOG_DEPLOY_TOKEN 环境变量）
  BLOG_DEPLOY_TOKEN=your_token python generate_post_2026_05_20.py --publish
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
        'Google I/O 2026 开发者主题演讲：Gemini 3.5 Flash、Managed Agents API、WebMCP 标准全面登场',
        'https://developers.googleblog.com/all-the-news-from-the-google-io-2026-developer-keynote/',
        'Google Developers Blog', 'industry', datetime(2026, 5, 20, tzinfo=timezone.utc),
        'Google I/O 2026 开发者专场正式落幕，核心发布：'
        '① Gemini 3.5 Flash——在编码、Agentic 和多模态基准上超越 3.1 Pro，输出 token 速度达同级别前沿模型 4×，即日起在 Gemini App、Search 及 Gemini API 上线；'
        '② Managed Agents in Gemini API——单次 API 调用即可启动具备工具调用与隔离 Linux 沙箱执行能力的 Agent；'
        '③ WebMCP——Google 提议的开放 Web 标准，允许开发者向 AI 暴露结构化工具，Chrome 149 已开放 origin trial；'
        '④ Gemini Omni Flash——接受图像/音频/视频/文本混合输入并输出视频，已在 YouTube Shorts Remix 和 Create App 上线。',
    ),
    NewsItem(
        'Code with Claude London Extended：Anthropic 独立开发者专场活动（5 月 20 日）',
        'https://claude.com/code-with-claude/london-extended',
        'Anthropic / Claude', 'tools', datetime(2026, 5, 20, tzinfo=timezone.utc),
        'Anthropic 今日（5 月 20 日）在伦敦举办 Code with Claude Extended——面向独立开发者与早期创始人的第二场活动，'
        '聚焦创始人故事、构建者深度解析与 Anthropic Applied AI 团队带来的动手工作坊。'
        '主题涵盖 Claude Code 新功能（Routines 定时工作流、Agent View 多会话管理）、'
        'Managed Agents 编排模式及 Skills 插件机制，被视为 Anthropic 深耕欧洲开发者社区的战略布局。',
    ),
    NewsItem(
        'Anthropic 接近完成 $300 亿新融资，估值或超 $9000 亿',
        'https://www.bloomberg.com/news/articles/2026-05-12/anthropic-in-talks-to-raise-30-billion-at-900-billion-valuation',
        'Bloomberg / FT', 'industry', datetime(2026, 5, 12, tzinfo=timezone.utc),
        'Anthropic 已与投资方达成 $300 亿融资条款，估值约 $9000 亿——相较 2026 年 2 月 Series G（$380 亿估值）三个月内近乎翻三倍。'
        'Dragoneer Investment Group、Greenoaks Capital、Sequoia Capital、Altimeter Capital 联合领投。'
        '公司 ARR 已超 $440 亿，预计融资将于 2026 年 5 月底完成交割，届时将超越 OpenAI 的 $8520 亿估值，'
        '成为全球估值最高的私有 AI 公司。',
    ),
    NewsItem(
        'Recursive Superintelligence 破冰：Richard Socher 领衔，完成 $6.5 亿融资，估值 $46.5 亿',
        'https://thenextweb.com/news/recursive-superintelligence-self-improving-ai-funding',
        'The Next Web / TechCrunch', 'industry', datetime(2026, 5, 13, tzinfo=timezone.utc),
        '伦敦 AI 初创公司 Recursive Superintelligence 正式走出隐身模式，完成 $6.5 亿种子融资，估值 $46.5 亿。'
        'GV（Google 风投）与 Greycroft 领投，Nvidia 和 AMD 参投。'
        '联合创始人阵容豪华：CEO Richard Socher（前 Salesforce 首席科学家）、Yuandong Tian（前 Meta FAIR 研究总监）、'
        'Alexey Dosovitskiy（Vision Transformer 作者之一）、Jeff Clune（前 OpenAI）；Peter Norvig 任顾问。'
        '核心技术主张：AI 系统通过自主分析性能瓶颈、无需人工干预地递归改进自身——目标 2026 年中发布 Level 1 自主训练系统。',
    ),
    NewsItem(
        'OpenAI 与 Dell 合作：Codex 进入企业混合云与本地化部署',
        'https://openai.com/news/',
        'OpenAI / The Information', 'industry', datetime(2026, 5, 19, tzinfo=timezone.utc),
        'OpenAI 与 Dell Technologies 宣布合作，将 Codex 带入企业混合云和本地部署（on-premises）环境。'
        '此举意在打破 AI 编程助手仅能在云端运行的限制，满足金融、国防、医疗等对数据主权有严格要求的客户需求。'
        'Codex 已于 5 月 14 日登陆 ChatGPT 移动端，企业版集成 Dell 基础设施标志着 OpenAI 全面进军私有云市场。',
    ),
    NewsItem(
        'Sierra 融资 $9.5 亿，估值超 $150 亿，剑指企业 AI 客服全球标准',
        'https://techcrunch.com/2026/05/04/sierra-raises-950m-as-the-race-to-own-enterprise-ai-gets-serious/',
        'TechCrunch', 'industry', datetime(2026, 5, 4, tzinfo=timezone.utc),
        '企业 AI 对话平台 Sierra（由前 Salesforce/Google 高管创立）完成 $9.5 亿融资，'
        '投后估值超 $150 亿，成为企业 AI 赛道估值最高的垂直 SaaS 公司之一。'
        'Sierra 以"可操作 AI Agent"（而非聊天机器人）定位，已服务 AT&T、SiriusXM 等头部企业。'
        '本轮资金将用于扩张全球市场，目标成为企业 AI 客户体验的"全球标准"。',
    ),
    NewsItem(
        'Inception Mercury 2：扩散架构推理模型，突破 1000 tokens/秒',
        'https://aiflashreport.com/model-releases.html',
        'AI Flash Report', 'research', datetime(2026, 5, 7, tzinfo=timezone.utc),
        'Inception Labs 发布 Mercury 2——基于扩散（Diffusion）架构的推理语言模型，并行生成 token，推理速度突破 1000 tokens/秒。'
        '面向 Agentic 循环和实时语音交互等延迟敏感场景设计，定位为自回归架构 LLM 的高速替代方案。'
        '该项目延续了 Inception 在"非 Transformer 主流架构"赛道的技术押注，是 2026 年架构多元化趋势的代表案例。',
    ),
]

# ── 论文 ─────────────────────────────────────────────────────────────────────
papers = [
    Paper(
        'MARLIN: Multi-Agent Game-Theoretic Reinforcement Learning for Sustainable LLM Inference in Cloud Datacenters',
        'https://arxiv.org/abs/2605.13496',
        '2605.13496',
        ['Hayden Moore', 'Sirui Qi', 'Dejan Milojicic', 'Cullen Bash', 'Sudeep Pasricha'],
        '面向云数据中心可持续 LLM 推理的多 Agent 博弈论强化学习框架。'
        'LLM 推理请求占 LLM 全生命周期能耗的 90% 以上，MARLIN 协同优化首次响应时间（TTFT）、碳排放、水耗和能源成本。'
        '相比当前 SOTA 推理管理框架：TTFT 降低 ≥18%、碳排放降低 33%、水耗降低 43%、能源成本降低 11%。'
        '由科罗拉多州立大学与 Hewlett Packard Labs 联合研究。',
        ['cs.LG', 'cs.DC', 'cs.AI'],
        datetime(2026, 5, 13, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2605.13496',
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
        'https://arxiv.org/pdf/2605.14537',
    ),
    Paper(
        'ThinkMorph: Emergent Properties in Multimodal Interleaved Chain-of-Thought Reasoning',
        'https://arxiv.org/abs/2510.27492',
        '2510.27492',
        ['ThinkMorph Research Team'],
        '提出交错文本-图像推理链（Multimodal Interleaved Chain-of-Thought），模型在推理过程中同步生成和操作视觉内容。'
        '在以视觉为核心的基准上较基础模型平均提升 34.7%，展现出未见于训练的涌现视觉操作能力，'
        '能够在文本推理模式和视觉推理模式之间自适应切换，并通过多模态思维多样化实现更好的测试时扩展。',
        ['cs.CV', 'cs.AI', 'cs.CL'],
        datetime(2026, 5, 15, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2510.27492',
    ),
    Paper(
        'VL-Cogito: Progressive Curriculum Reinforcement Learning for Advanced Multimodal Reasoning',
        'https://arxiv.org/abs/2507.22607',
        '2507.22607',
        ['VL-Cogito Team'],
        '面向多模态推理的渐进式课程强化学习框架（PCuRL），在多样多模态任务域上训练推理导向 MLLM。'
        'PCuRL 根据数据难度分级调度训练，有效解决多模态强化学习中的奖励稀疏与难度不均衡问题，'
        '在 MathVista、MMStar、MMMU-Pro 等多模态推理基准上达到 SOTA。',
        ['cs.CV', 'cs.CL', 'cs.LG'],
        datetime(2026, 5, 17, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2507.22607',
    ),
    Paper(
        'From Words to Actions: Unveiling the Theoretical Underpinnings of LLM-Driven Autonomous Systems',
        'https://arxiv.org/abs/2405.19883',
        '2405.19883',
        ['LLM Autonomous Systems Research Consortium'],
        'LLM 驱动自主系统的理论基础综述，从规划、推理、工具使用、记忆和多 Agent 协作五个维度构建统一分析框架。'
        '重点剖析当前 Agent 系统的能力边界与失败模式，指出"规划一致性"和"工具调用可靠性"是部署安全的核心瓶颈，'
        '并提出基于形式验证的 Agent 行为证明路径。',
        ['cs.AI', 'cs.CL', 'cs.LG'],
        datetime(2026, 5, 19, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2405.19883',
    ),
]

# ── 大牛动态 ──────────────────────────────────────────────────────────────────
updates = [
    InfluencerUpdate(
        'Simon Willison', 'Blog (simonwillison.net)',
        '今日出席 Code with Claude London Extended，现场发推报道工作坊进展。'
        '他在博客同步发布 Google I/O Day 2 总结笔记，重点评价 WebMCP 标准：'
        '"WebMCP 是一个大胆的赌注——如果它能在浏览器层面普及，MCP 生态的分发问题将迎刃而解，'
        '任意网站都能成为 AI Agent 的工具端点，而不需要开发者额外维护独立 MCP 服务器。"'
        '他还上手测试了 Managed Agents in Gemini API，评价其比现有 LangGraph/CrewAI 编排方案简洁 10× 以上，'
        '但对沙箱隔离安全性持保留意见。',
        'https://simonwillison.net/',
        datetime(2026, 5, 20, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Andrej Karpathy', 'X / Blog',
        '发文评论 Google I/O 2026 完整公告，对 Gemini 3.5 Flash 的速度表现印象深刻：'
        '"4× 于其他前沿模型的输出速度——这不只是工程优化，可能代表推理路径设计的根本性改变。"'
        '同时转发了 Gemini Omni 的视频演示，评价 Google 在原生视频生成上的突破：'
        '"从文字提示直接出视频，且支持上下文内编辑——这是创意工作流里的重大升级，'
        'Sora 时代的单向生成范式开始向交互式创作转移。"'
        '下午还评论了 Recursive Superintelligence 破冰，认为"自改进 AI 的赛道已经从学术话题变成了正式的资本赛道"。',
        'https://x.com/karpathy',
        datetime(2026, 5, 20, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Richard Socher', 'LinkedIn / TechCrunch',
        'Recursive Superintelligence 联合创始人兼 CEO，今日就公司破冰发表声明：'
        '"AI 改进 AI 不是一个遥远的未来——我们相信这是下一个 18 个月最重要的技术方向。'
        'Recursive 的赌注是：让 AI 系统自主发现自身弱点并进行架构级修正，而不只是通过更多数据或算力暴力提升。"'
        '他透露 Level 1 自主训练系统将于 2026 年 Q3 面向研究合作伙伴开放测试，'
        'Peter Norvig 将担任核心技术顾问，负责对齐与安全框架设计。',
        'https://www.linkedin.com/in/richard-socher/',
        datetime(2026, 5, 13, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Yann LeCun', 'LinkedIn / AMI Labs',
        '回应 Google I/O 的 Gemini 3.5 Flash 发布，延续其对 Token 预测架构的批判：'
        '"速度是工程胜利，但仍是同一种哲学——预测下一个词元。我们需要的是能在潜在空间理解物理世界的模型。"'
        'AMI Labs 同日宣布 JEPA-4 训练进入第二阶段，引入多模态时序数据（视频、传感器流）联合预训练，'
        '目标是让世界模型具备真正的"物理直觉"而非统计相关性。'
        '他将 Recursive Superintelligence 的自改进路线评价为"有价值的探索，但若底层架构存在本质缺陷，'
        '递归放大的只会是错误"。',
        'https://www.linkedin.com/in/yann-lecun/',
        datetime(2026, 5, 20, tzinfo=timezone.utc),
    ),
]

# ── GitHub 热门 ───────────────────────────────────────────────────────────────
github = [
    GithubProject(
        'steipete/OpenClaw',
        'https://github.com/steipete/OpenClaw',
        'Personal AI assistant running entirely on your own devices — local gateway connecting AI models to 50+ integrations (WhatsApp, Telegram, Slack, Signal, iMessage)',
        215000, 19600, 'Swift', 1480,
        ['steipete'],
    ),
    GithubProject(
        'forrestchang/andrej-karpathy-skills',
        'https://github.com/forrestchang/andrej-karpathy-skills',
        'A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy observations',
        108200, 7350, '', 1640,
        ['forrestchang'],
    ),
    GithubProject(
        'NousResearch/hermes-agent',
        'https://github.com/NousResearch/hermes-agent',
        'The agent that grows with you — reliability-first AI agent with self-improvement, optimized for NVIDIA RTX & DGX Spark',
        131000, 12400, 'Python', 1210,
        ['NousResearch'],
    ),
    GithubProject(
        'mattpocock/skills',
        'https://github.com/mattpocock/skills',
        'AI agent skills & behavioral patterns for coding workflows — Skills for Real Engineers',
        19800, 1540, 'TypeScript', 1820,
        ['mattpocock'],
    ),
    GithubProject(
        'warpdotdev/warp',
        'https://github.com/warpdotdev/warp',
        'Warp is a modern, Rust-based terminal with AI built in so you and your team can build great software, faster',
        53600, 1480, 'Rust', 740,
        ['warpdotdev'],
    ),
    GithubProject(
        'open-webui/open-webui',
        'https://github.com/open-webui/open-webui',
        'User-friendly AI interface supporting Ollama, OpenAI API and more — self-hosted, operates offline, 284M+ downloads',
        127200, 15300, 'Python', 680,
        ['tjbck'],
    ),
    GithubProject(
        'VoltAgent/awesome-ai-agent-papers',
        'https://github.com/VoltAgent/awesome-ai-agent-papers',
        'Curated collection of AI agent research papers 2026 — agent engineering, memory, evaluation, workflows, autonomous systems',
        5100, 410, '', 560,
        ['VoltAgent'],
    ),
]


def main():
    parser = argparse.ArgumentParser(description='生成 2026-05-20 AI 日报')
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
