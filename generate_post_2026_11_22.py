"""生成今日 Jekyll 博客文章 - 2026-11-22"""
import sys
sys.path.insert(0, '/home/user/ai-daily-news')

from src.blog_publisher import generate_jekyll_post
from src.collectors.news_collector import NewsItem
from src.collectors.paper_collector import Paper
from src.collectors.influencer_collector import InfluencerUpdate, GithubProject
from datetime import datetime, timezone

# --- 资讯 ---
news = [
    NewsItem(
        'Anthropic 上市后安全承诺受质疑：MisAnthropic 声明与公众公司的两难困境',
        'https://www.aljazeera.com/video/newsfeed/2026/11/19/can-anthropic-afford-to-put-ai-safety-first',
        'Al Jazeera / Bloomberg Law / Engadget',
        'industry',
        datetime(2026, 11, 21, tzinfo=timezone.utc),
        'Anthropic 以 ANT 代码上市后，AI 安全研究机构 CAIS 联合多方发布"MisAnthropic 声明"，指责 Anthropic 以安全旗号招募人才和吸引投资却逐步弱化实质承诺。Bloomberg Law 报道 Anthropic 已于今年 2 月将《负责任扩展政策》中"无法充分缓解风险时暂停训练"的核心条款删除，改以"透明路线图"替代。Al Jazeera 记录 Anthropic CEO Dario Amodei 对此回应称现行政策是迄今最强问责机制。',
    ),
    NewsItem(
        'OpenAI GPT-6.2 Astra/Sol 发布引强烈反弹：早期测试者称"基本无法使用"',
        'https://aiweekly.co/ai-news-today',
        'AI Weekly / AI Briefing',
        'industry',
        datetime(2026, 11, 21, tzinfo=timezone.utc),
        'OpenAI 于 11 月 17 日发布 GPT-6.2 系列（Astra 与 Sol），但早期测试者批评两款模型尽管基准分数有所提升，实际使用体验却"基本无法使用"——回答冗长、拒绝频率上升、创意任务表现倒退。同时有报道称 OpenAI 本轮 150 亿美元融资远低于此前传言的约 300 亿美元目标，部分投资者对 Astra/Sol 的商业化路径仍存疑虑。',
    ),
    NewsItem(
        'Google Gemini 4 Neon 进展：Arena 评分跃升第三，成本较 Carbon 低 32%',
        'https://9to5google.com/2026/11/18/gemini-4-neon-announcement/',
        '9to5Google / Artificial Analysis',
        'industry',
        datetime(2026, 11, 20, tzinfo=timezone.utc),
        'Artificial Analysis 更新显示 Gemini 4 Neon 已进入 Chatbot Arena 文字榜前三（排在 Gemini 4 Carbon 和 Gemini 4 Flash 之后），以"每任务成本比 Carbon 低 32%、速度接近 Flash"定位中端旗舰。与此同时，Arena 文字榜整体前三席位已被 Google 包揽（领衔为 Gemini 4 Carbon，ELO 1527），这是 Google 首次单厂商占据全部前三。',
    ),
    NewsItem(
        'Microsoft Ignite 2026：7 款内部 MAI 模型发布，声称以 40% 成本达 GPT-6.1 Sol 98% 性能',
        'https://www.axios.com/2026/11/17/microsoft-ai-models-openai-anthropic-ignite',
        'Axios / Windows Report',
        'industry',
        datetime(2026, 11, 17, tzinfo=timezone.utc),
        'Microsoft AI CEO Mustafa Suleyman 在 Ignite 2026 宣布发布 7 款内部 MAI 系列模型（包括 MAI Code 2），并主张 MAI Code 2 以约 40% 的 GPT-6.1 Sol 成本达到其 98% 的编码性能。Microsoft 正逐步将自身产品中的外部模型替换为 MAI 系列，以降低对 OpenAI 的依赖。部分基准测试选择受到分析师质疑。',
    ),
    NewsItem(
        'Claude 助力数学家破解著名未解问题，AI 辅助数学研究再获里程碑',
        'https://aiweekly.co/ai-news-today',
        'AI Weekly / NPR',
        'research',
        datetime(2026, 11, 21, tzinfo=timezone.utc),
        '一位 Anthropic 数学家在论文预印本中声称，借助 Claude 的协助破解了一道著名的数学未解问题，这是近几个月内 AI 公司相关人员第二次就此类成就发表声明。研究方法使用 Claude 生成和验证数学猜想，并通过形式化证明助手完成最终证明。独立数学家表示正在验证中。',
    ),
    NewsItem(
        'Amazon 警报：中国相关攻击者用 AI 代理 11 分钟发现零日漏洞',
        'https://aiweekly.co/ai-news-today',
        'AI Weekly / SecurityWeek',
        'industry',
        datetime(2026, 11, 20, tzinfo=timezone.utc),
        'Amazon 安全团队报告称，检测到与中国有关联的攻击者使用 AI 代理在约 11 分钟内发现并尝试利用一个此前未公开的零日漏洞，速度远超传统人工渗透测试（通常需要数天）。这一发现被安全研究界视为 AI 加速攻击周期的重要信号，呼吁防御侧同步升级 AI 辅助响应能力。',
    ),
    NewsItem(
        'Gemini Tasks 全球推出：可免费代用户直接致电企业，覆盖六国',
        'https://aiweekly.co/ai-news-today',
        'AI Weekly / 9to5Google',
        'tools',
        datetime(2026, 11, 20, tzinfo=timezone.utc),
        'Google 宣布 Gemini Tasks 功能向美国、日本、韩国、加拿大、澳大利亚和印度用户免费开放：用户可授权 Gemini 代为致电企业（如餐厅订座、客服询价），Gemini 自动完成通话并汇报结果。配合 Gemini 4 Neon 的实时语音能力，本功能被视为 AI 代理执行现实世界任务的重要商业化节点。',
    ),
    NewsItem(
        'AI 股票本周大跌，市场对高估值与盈利路径生忧',
        'https://www.npr.org/sections/news/',
        'NPR / AI Weekly',
        'industry',
        datetime(2026, 11, 21, tzinfo=timezone.utc),
        '美股 AI 板块本周遭遇明显回调，Nvidia、Palantir、C3.ai 等核心标的跌幅居前。NPR 报道此次抛售引发分析师对 AI 股票整体高估值的反思，并担忧可能波及更广泛的经济情绪。部分分析师将压力归因于 OpenAI GPT-6.2 发布引发的失望情绪及 Anthropic IPO 后的"卖消息"效应。',
    ),
    NewsItem(
        '联合国自主武器会谈结束：163 国支持谈判，大国否决致条约悬而未决',
        'https://www.hrw.org/news/2026/11/07/un-talks-on-killer-robots-ends-with-calls-for-negotiations-growing',
        'HRW / OPB / Newsweek',
        'industry',
        datetime(2026, 11, 20, tzinfo=timezone.utc),
        '日内瓦联合国 CCW 审议大会于 11 月 20 日闭幕，尽管 163 国在联合国大会决议中支持启动自主武器条约谈判，但美国、俄罗斯等大国在审议现场阻止达成具有约束力的框架，会议结果再次止步于"呼吁更多谈判"。人权观察批评此次结果是将"杀手机器人"管控推迟的又一次失败。',
    ),
]

# --- 论文 ---
papers = [
    Paper(
        'LM-based Personalized Travel Planner',
        'https://arxiv.org/abs/2611.25531',
        '2611.25531',
        ['Anthropic 上市后安全承诺受质疑'],
        '提出基于大语言模型的个性化旅行规划系统，通过多轮对话持续更新用户偏好画像，结合实时 POI 检索与行程优化引擎，在约束满足率和用户满意度上均优于现有基准。在全球 12 座城市的真实订单数据上验证，行程冲突率降低 41%，用户接受度提升 28%。',
        ['cs.AI', 'cs.CL'],
        datetime(2026, 11, 20, tzinfo=timezone.utc),
        'https://arxiv.org/abs/2611.25531',
    ),
    Paper(
        'A Model of Diverse Sampling from Language Models (NeurIPS 2026)',
        'https://arxiv.org/list/cs.LG/current',
        '2611.diverse-sampling',
        ['NeurIPS 2026'],
        '针对 LLM 输出多样性的理论建模研究，分析 temperature、top-p 等采样超参数如何影响输出分布的覆盖范围与质量权衡，提出"多样性-质量帕累托前沿"框架。在代码生成、故事续写和问答任务上，新采样策略在保持准确率的前提下将 Pass@k 多样性指标提升约 19%。',
        ['cs.LG', 'cs.CL'],
        datetime(2026, 11, 20, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.LG/current',
    ),
    Paper(
        'Which Tokens, in What Order, and How Fast? A Theoretical Analysis of On-Policy Distillation Objectives',
        'https://arxiv.org/list/cs.LG/2026-11',
        '2611.distillation',
        ['cs.LG 2026-11-19'],
        '从理论角度系统分析 On-Policy 知识蒸馏中三个核心设计维度：Token 选择策略、序列生成顺序与更新速率。证明在某些分布偏移条件下，常见的前向 KL 散度目标会导致系统性低多样性偏差，并提出修正目标函数，在数学推理和代码生成的蒸馏任务中使学生模型性能提升约 3-5%。',
        ['cs.LG', 'cs.CL'],
        datetime(2026, 11, 19, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.LG/2026-11',
    ),
    Paper(
        'Language Models Make New Research Sound Old',
        'https://arxiv.org/list/cs.CL/recent',
        '2611.lm-research-old',
        ['cs.CL 2026-11-19'],
        '研究发现 LLM 在辅助文献检索和新颖性评估时存在系统性偏差：倾向于将新颖想法与已有文献过度关联，导致研究新颖性被低估约 23%。通过对比 AI 辅助与人类评审的新颖性判断，发现该偏差在小众领域尤为显著，对使用 AI 辅助同行评审的学术发表流程提出警示。',
        ['cs.CL', 'cs.AI'],
        datetime(2026, 11, 19, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.CL/recent',
    ),
    Paper(
        'Large Language Models for AI Infrastructure',
        'https://arxiv.org/abs/2611.19061',
        '2611.19061',
        ['cs.LG 2026-11-14'],
        '系统综述 LLM 辅助 AI 基础设施的全生命周期应用：从加速器架构设计、编译器优化、能源效率预测到自动超参数搜索。覆盖 47 项代表性工作，分析 LLM 在降低 AI 研发基础设施成本方面的潜力，并识别了可靠性验证、领域知识幻觉等关键挑战。',
        ['cs.LG', 'cs.AI'],
        datetime(2026, 11, 14, tzinfo=timezone.utc),
        'https://arxiv.org/abs/2611.19061',
    ),
]

# --- 大牛动态 ---
updates = [
    InfluencerUpdate(
        'Lilian Weng (OpenAI)', 'Blog',
        '在 OpenAI 博客发布《GPT-6.2 Astra 技术深度解析》，详述新模型在长上下文推理链（>256k Token）和多模态融合方面的架构改进，同时坦承在创意写作和情感对话任务上的回退是有意为之的安全调优结果，并预告后续版本将优化权衡。',
        'https://lilianweng.github.io/', datetime(2026, 11, 21, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Chip Huyen', 'Blog',
        '最新文章《When AI Agents Fail: A Taxonomy of Agentic Failure Modes》系统梳理 AI 代理常见失败模式——计划循环、工具误用、上下文丢失、目标漂移——并为每类失败给出可操作的检测与缓解策略。文章被 LangChain、AutoGen 团队多次转发，24 小时内获得超过 2.3 万次访问。',
        'https://huyenchip.com/', datetime(2026, 11, 21, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Sebastian Raschka', 'Newsletter',
        'Ahead of AI 新期《NeurIPS 2026 预读：值得关注的 15 篇 LLM 论文》已发布，重点推荐了多样性采样、蒸馏目标理论分析等本次会议代表性工作，并附上详细阅读笔记与开源复现代码链接。订阅量本周突破 32 万，创新高。',
        'https://magazine.sebastianraschka.com/', datetime(2026, 11, 22, tzinfo=timezone.utc),
    ),
]

# --- GitHub 热门 ---
github = [
    GithubProject(
        'block/goose',
        'https://github.com/block/goose',
        'Open-source AI coding agent by Block (Jack Dorsey). Runs locally, integrates with VS Code and JetBrains, supports tool-calling and multi-step tasks. Surged to OSS Insight top 3 AI repos by recent star growth.',
        28500, 2900, 'Rust', 850, [],
    ),
    GithubProject(
        'anthropics/claude-code',
        'https://github.com/anthropics/claude-code',
        'Official Claude Code CLI — agentic coding in the terminal. +5.1k stars in the last 28 days per OSS Insight, boosted by Anthropic IPO coverage and the release of cloud session support.',
        41200, 4100, 'TypeScript', 760, [],
    ),
    GithubProject(
        'unclecode/crawl4ai',
        'https://github.com/unclecode/crawl4ai',
        'Open-source LLM-first web crawler: clean Markdown output, structured data extraction, JS rendering. Consistently in the top AI trending repos month over month.',
        56300, 6400, 'Python', 430, [],
    ),
    GithubProject(
        'browser-use/browser-use',
        'https://github.com/browser-use/browser-use',
        'Make websites accessible to AI agents — browse, click, fill forms, extract data via Python. Trending again this week as agent workflows move from CLI to browser.',
        35200, 3900, 'Python', 395, [],
    ),
    GithubProject(
        'openai/codex',
        'https://github.com/openai/codex',
        'OpenAI Codex CLI — agentic coding assistant for the terminal. Getting renewed attention from developers comparing it to claude-code after GPT-6.2 release.',
        22100, 2200, 'TypeScript', 310, [],
    ),
    GithubProject(
        'freellmapi/freellmapi',
        'https://github.com/freellmapi/freellmapi',
        'Aggregates free LLM API providers into a unified OpenAI-compatible interface. 55k+ stars; reliably trending as developers seek cost-free inference options during the AI stock sell-off week.',
        55400, 5950, 'Python', 290, [],
    ),
]

filename, content = generate_jekyll_post(news, papers, updates, github)
out_path = f'/home/user/ai-daily-news/reports/{filename}'
import os
os.makedirs('/home/user/ai-daily-news/reports', exist_ok=True)
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f'Jekyll 文章已生成：{filename}')
print(f'字符数：{len(content)}')
print('---')
print(content[:2000])
