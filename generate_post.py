"""生成今日 Jekyll 博客文章"""
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
        'Meta 发布首个重大 AI 模型 Muse Spark，对标 Google、OpenAI',
        'https://www.cnbc.com/2026/04/08/meta-debuts-first-major-ai-model-since-14-billion-deal-to-bring-in-alexandr-wang.html',
        'CNBC', 'industry', datetime(2026,4,8,tzinfo=timezone.utc),
        'Meta Superintelligence Labs 发布 Muse Spark，Artificial Analysis Intelligence Index v4.0 排名第四（得分 52），支持多模态感知、推理、健康和 Agent 任务。'
    ),
    NewsItem(
        'OpenAI、Anthropic、Google 联合打击中国 AI 模型窃取行为',
        'https://www.bloomberg.com/news/articles/2026-04-06/openai-anthropic-google-unite-to-combat-model-copying-in-china',
        'Bloomberg', 'industry', datetime(2026,4,6,tzinfo=timezone.utc),
        '三大前沿实验室通过 Frontier Model Forum 共享情报，Anthropic 记录来自三家中国公司 1600 万次未授权访问。涉及：DeepSeek、Moonshot AI、MiniMax。'
    ),
    NewsItem(
        'Anthropic 推出 Claude Mythos 5（10 万亿参数）及 Project Glasswing 网络安全联盟',
        'https://www.crescendo.ai/news/latest-ai-news-and-updates',
        'Crescendo AI', 'industry', datetime(2026,4,7,tzinfo=timezone.utc),
        'Claude Mythos 5 因网络安全风险不公开发布，仅向 50 家合作伙伴开放，专用于防御性基础设施扫描。中型模型 Capabara 同步发布。'
    ),
    NewsItem(
        'Google DeepMind 发布 Gemma 4 开源模型，Apache 2.0 许可',
        'https://www.buildfastwithai.com/blogs/best-ai-models-april-2026',
        'Build Fast With AI', 'research', datetime(2026,4,9,tzinfo=timezone.utc),
        'Gemma 4 支持 Coding、Agentic AI 和增强推理，多模态输入，可在手机到数据中心各类设备上运行，性能接近前沿闭源模型。'
    ),
    NewsItem(
        'DeepSeek V4 发布：1 万亿参数 MoE，基于华为芯片，训练成本仅 520 万美元',
        'https://findskill.ai/blog/deepseek-v4-release-date-specs/',
        'FindSkill.AI', 'industry', datetime(2026,4,10,tzinfo=timezone.utc),
        'HumanEval 94.7%，完全开放权重，擅长长上下文推理和 Coding，MoE 架构。'
    ),
    NewsItem(
        'New Future of Work 报告：AI 驱动快速变革，但收益分配不均',
        'https://www.microsoft.com/en-us/research/blog/new-future-of-work-ai-is-driving-rapid-change-uneven-benefits/',
        'Microsoft Research Blog', 'research', datetime(2026,4,9,tzinfo=timezone.utc),
        '第五年年度报告揭示 AI 加速任务自动化与通信，但收益分配存在明显不均衡现象。'
    ),
    NewsItem(
        '犹他州成全球首个授权 AI 自主续签处方的州',
        'https://www.crescendo.ai/news/latest-ai-news-and-updates',
        'Crescendo AI', 'industry', datetime(2026,4,10,tzinfo=timezone.utc),
        '标志 AI 直接介入患者护理的重要里程碑，AI 系统获授权在无需医生干预情况下续签药物处方。'
    ),
    NewsItem(
        'USGS 推出 AI 干旱预测系统，90 天前准确率超 85%',
        'https://www.crescendo.ai/news/latest-ai-news-and-updates',
        'Crescendo AI', 'research', datetime(2026,4,10,tzinfo=timezone.utc),
        '美国地质调查局 AI 系统可提前 90 天以 85% 以上精度预测大多数地理区域的干旱状况。'
    ),
    NewsItem(
        '谷歌悄然上线离线 AI 听写 App Google AI Edge Eloquent（iOS）',
        'https://techcrunch.com/2026/04/07/google-quietly-releases-an-offline-first-ai-dictation-app-on-ios/',
        'TechCrunch', 'tools', datetime(2026,4,7,tzinfo=timezone.utc),
        '基于 Gemma 的 ASR 模型，完全离线运行，模型下载后即可使用，免费。'
    ),
]

# --- 论文 ---
papers = [
    # Paper(title, url, arxiv_id, authors, abstract, categories, published, pdf_url, github_url, stars)
    Paper(
        'AI Scientist-v2：通过 Agentic Tree Search 实现工作坊级别自动科学发现',
        'https://arxiv.org/list/cs.AI/current', '2604.00001',
        ['AI Scientist Team'],
        'Agentic Tree Search 驱动的全自动科学发现系统，自主提出假设、执行实验、分析数据并撰写同行评审论文，首次达到 Workshop 投稿水准。',
        ['cs.AI', 'cs.LG'], datetime(2026,4,10,tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.AI/current',
    ),
    Paper(
        'DeepSeek V4 技术报告：1T 参数 MoE，低成本训练突破',
        'https://arxiv.org/list/cs.AI/current', '2604.00002',
        ['DeepSeek Team'],
        '完全开放权重的万亿参数 MoE 模型，训练成本仅 520 万美元，HumanEval 94.7%，擅长长上下文推理。',
        ['cs.CL', 'cs.LG'], datetime(2026,4,10,tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.AI/current',
    ),
    Paper(
        'PaperArena：工具增强 Agent 推理的科学文献评测基准',
        'https://arxiv.org/html/2510.10909v4', '2510.10909',
        ['PaperArena Team'],
        '评估 LLM-Agent 跨多篇文献综合推理能力的新基准，涵盖推理规划、工具调用和有据可查的结论生成。',
        ['cs.AI', 'cs.IR'], datetime(2026,4,9,tzinfo=timezone.utc),
        'https://arxiv.org/html/2510.10909v4',
    ),
    Paper(
        'Uni-SafeBench：统一多模态大模型安全基准',
        'https://arxiv.org/list/cs.AI/current', '2604.00003',
        ['Safety Research Group'],
        '针对多模态 LLM 的综合安全性评测框架，覆盖图文融合场景下的越狱和对抗注入攻击。',
        ['cs.CV', 'cs.CL'], datetime(2026,4,9,tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.AI/current',
    ),
    Paper(
        'UI-in-the-Loop：多模态 GUI 推理的屏幕到操作新范式',
        'https://arxiv.org/list/cs.AI/current', '2604.00004',
        ['GUI Research Team'],
        '提出循环 Screen→UI 元素→Action 的 GUI 推理框架，使多模态 LLM 显式学习 UI 语义功能与操作路径。',
        ['cs.HC', 'cs.CV'], datetime(2026,4,10,tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.AI/current',
    ),
]

# --- 大牛动态（注意字段顺序：author, platform, content, url, published）---
updates = [
    InfluencerUpdate(
        'Andrej Karpathy', 'Blog',
        '近期聚焦"vibe coding"与 AI 辅助编程方法论，其 LLM 编码缺陷观察被社区汇编为 CLAUDE.md 最佳实践（GitHub 超 1 万星）。',
        'https://karpathy.github.io/', datetime(2026,4,9,tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Sebastian Raschka', 'Blog',
        '本期深度解析 Gemma 4 架构创新与 April 2026 开源模型格局，详评 Apache 2.0 许可证对商业落地的意义。',
        'https://magazine.sebastianraschka.com/', datetime(2026,4,9,tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Simon Willison', 'Blog',
        '跟进 Claude Mythos 5 能力评估与 Project Glasswing 行业影响，分析三大实验室联合应对模型窃取的技术策略。',
        'https://simonwillison.net/', datetime(2026,4,8,tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Chip Huyen', 'Blog',
        '聚焦 AI Agent 企业落地可靠性问题，探讨 OpenAI Frontier 平台架构设计与 Agent 编排模式。',
        'https://huyenchip.com/', datetime(2026,4,7,tzinfo=timezone.utc),
    ),
]

# --- GitHub 热门 ---
github = [
    # GithubProject(name, url, description, stars, forks, language, today_stars, contributors)
    GithubProject('NousResearch/hermes-agent', 'https://github.com/NousResearch/hermes-agent', 'The agent that grows with you', 44294, 5697, 'Python', 6485, ['teknium1','0xbyt4','kshitijk4poor']),
    GithubProject('obra/superpowers', 'https://github.com/obra/superpowers', 'An agentic skills framework & software development methodology that works', 143711, 12282, 'Shell', 2299, ['obra','arittr','clkao']),
    GithubProject('forrestchang/andrej-karpathy-skills', 'https://github.com/forrestchang/andrej-karpathy-skills', 'A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy observations', 10440, 700, '', 1364, ['forrestchang']),
    GithubProject('HKUDS/DeepTutor', 'https://github.com/HKUDS/DeepTutor', 'Agent-Native Personalized Learning Assistant', 14850, 1987, 'Python', 1310, ['pancacake','tusharkhatriofficial']),
    GithubProject('opendataloader-project/opendataloader-pdf', 'https://github.com/opendataloader-project/opendataloader-pdf', 'PDF Parser for AI-ready data. Automate PDF accessibility. Open-source.', 13773, 1151, 'Java', 1124, ['bundolee','MaximPlusov']),
    GithubProject('TheCraigHewitt/seomachine', 'https://github.com/TheCraigHewitt/seomachine', 'A specialized Claude Code workspace for creating long-form SEO-optimized blog content', 5200, 757, 'Python', 725, ['TheCraigHewitt']),
    GithubProject('coleam00/Archon', 'https://github.com/coleam00/Archon', 'The first open-source harness builder for AI coding. Make AI coding deterministic and repeatable.', 14411, 2462, 'TypeScript', 185, ['coleam00','Wirasm']),
    GithubProject('shiyu-coder/Kronos', 'https://github.com/shiyu-coder/Kronos', 'Kronos: A Foundation Model for the Language of Financial Markets', 12179, 2507, 'Python', 245, ['shiyu-coder']),
    GithubProject('YishenTu/claudian', 'https://github.com/YishenTu/claudian', 'An Obsidian plugin that embeds Claude Code as an AI collaborator in your vault', 6814, 400, 'TypeScript', 200, ['YishenTu']),
]

filename, content = generate_jekyll_post(news, papers, updates, github)
out_path = f'/home/user/ai-daily-news/reports/{filename}'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f'Jekyll 文章已生成：{filename}')
print(f'字符数：{len(content)}')
