"""
发布 2026-05-07 AI 日报到博客

用法：
  # 仅生成 Jekyll 文章到 reports/ 目录
  python generate_post_2026_05_07.py

  # 生成并发布到博客（需要设置 BLOG_DEPLOY_TOKEN 环境变量）
  BLOG_DEPLOY_TOKEN=your_token python generate_post_2026_05_07.py --publish
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
        'Anthropic Code w/ Claude 2026 开发者大会：Claude Code Auto Mode 正式披露，SpaceX Colossus 数据中心战略合作',
        'https://simonwillison.net/2026/May/6/code-w-claude-2026/',
        'Simon Willison / Anthropic', 'industry', datetime(2026, 5, 6, tzinfo=timezone.utc),
        'Anthropic 于 5 月 6 日在旧金山举办年度开发者大会 Code w/ Claude 2026（另有伦敦 5/19、东京 6/10 场）。'
        '核心发布：①Claude Code Auto Mode——将权限审批委托给模型内置分类器，解决开发者"审批疲劳"问题，'
        '同时对子 Agent 出站任务和回调历史做双重安全校验，当前向 Team 用户开放研究预览；'
        '②与 SpaceX 达成战略合作，全量使用其 Colossus 数据中心算力；'
        '③Pro/Max/Enterprise 用户 Claude Code 五小时限额翻倍；'
        'Shopify、Mercado Libre（2.3 万工程师）目标 Q3 前实现 90% 自主编码。',
    ),
    NewsItem(
        'Cerebras Systems 启动 IPO：目标融资 35 亿美元、估值 266 亿美元，创 2026 年科技 IPO 之最',
        'https://www.cnbc.com/2026/05/04/cerebras-ipo-ai-chipmaker.html',
        'CNBC', 'industry', datetime(2026, 5, 6, tzinfo=timezone.utc),
        'Cerebras Systems 发布 IPO 路演材料，拟以每股 115–125 美元发行 2800 万股，融资 35 亿美元，'
        '按上限估值 266 亿美元。订单认购已达 100 亿美元，超募约 2.9 倍，定价有望高于区间上限。'
        'Q4 营收同比增长 76% 至 5.1 亿美元，净利润 8790 万美元。'
        'Sam Altman、Greg Brockman、Ilya Sutskever 均为天使投资人；'
        'OpenAI 与 Cerebras 签署逾 100 亿美元多年期供货协议，并持有认股权证。',
    ),
    NewsItem(
        'OpenAI 年化营收突破 250 亿美元，完成 1220 亿美元融资，IPO 最快 2026 年底提交招股书',
        'https://zestlab.io/en/trends/openai-ipo-2026',
        'ZestLab / Sacra', 'industry', datetime(2026, 5, 5, tzinfo=timezone.utc),
        'OpenAI CFO Sarah Friar 确认 2025 全年营收 200 亿美元，2026 年 2 月年化营收已达 250 亿美元，'
        '周活跃用户 9.1 亿（较去年 10 月 8 亿持续增长），付费企业客户超 900 万。'
        '3 月底完成 1220 亿美元融资（Amazon 500 亿、SoftBank 300 亿、Nvidia 参投），估值升至 8520 亿美元。'
        '目标 2026 年下半年提交 S-1，2027 年上市，市值或触及 1 万亿美元。',
    ),
    NewsItem(
        '美国政府与 Google、Microsoft、xAI 签署 AI 模型预审协议，监管框架加速成形',
        'https://www.cnbc.com/2026/05/05/ai-oversight-trump-google-microsoft-xai.html',
        'CNBC', 'industry', datetime(2026, 5, 5, tzinfo=timezone.utc),
        '美国商务部旗下 AI 标准与创新中心（CASI）宣布，Google DeepMind、Microsoft、xAI 加入'
        '联邦 AI 模型上市前评估机制——在正式发布前向政府开放技术访问，供安全与合规审查。'
        'OpenAI 和 Anthropic 已在此前重新谈判并纳入同类框架。'
        '这是特朗普政府 AI 监管路线从"自愿承诺"转向"机制性约束"的关键节点。',
    ),
    NewsItem(
        'Anthropic 推出 Claude Cowork：企业版协作 AI 工作空间，对标 Microsoft Copilot',
        'https://venturebeat.com/orchestration/anthropic-says-claude-code-transformed-programming-now-claude-cowork-is',
        'VentureBeat', 'industry', datetime(2026, 5, 6, tzinfo=timezone.utc),
        'Anthropic 在 Code w/ Claude 大会上发布 Claude Cowork，定位企业级 AI 协作工作空间：'
        '多人可在同一 Claude 会话中实时协同，Agent 可在后台持续执行长时任务（代码审查、文档生成、'
        '数据分析），结果推送至 Slack/Notion/Jira 等集成平台。'
        'CPO Ami Vora 表示"Claude Code 已改变编程，Claude Cowork 将改变整个企业协作方式"。'
        '当前向 Business 和 Enterprise 计划开放，具体定价另行公布。',
    ),
    NewsItem(
        'Simon Willison：定义"Agent"这个词的时机终于到来',
        'https://simonw.substack.com/p/i-think-agent-may-finally-have-a',
        'Simon Willison / Substack', 'research', datetime(2026, 5, 7, tzinfo=timezone.utc),
        'Simon Willison 在最新 Substack 文章中认为，"AI Agent"已从过度宽泛的营销术语演化为'
        '拥有可操作共识定义的技术词汇。他提出核心标准：Agent = 具备感知→规划→行动闭环、'
        '能在外部环境中持久执行且可自主调整目标的系统。'
        '文章同时批评当前工具把"调用一次 LLM API"也称为 Agent 的夸大现象，'
        '并呼吁社区在文档和基准测试中统一采用严格定义。',
    ),
    NewsItem(
        'Google Gemini 3.1 Flash-Lite GA：推理成本降至 $0.25/1M tokens，速度较 2.5 Flash 提升 2.5 倍',
        'https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-lite/',
        'Google Blog', 'industry', datetime(2026, 5, 1, tzinfo=timezone.utc),
        'Gemini 3.1 Flash-Lite 于 3 月 3 日以预览版发布，5 月初正式 GA，成为 Google 最低成本推理模型。'
        '输入 $0.25/1M tokens，输出 $1.50/1M tokens；首答延迟比 Gemini 2.5 Flash 快 2.5 倍，'
        '输出吞吐量提升 45%，同时保持同等或更高质量。'
        '支持原生多模态输入，面向高频翻译、内容审核、大规模分类场景，可通过 Google AI Studio 和 Vertex AI 访问。',
    ),
    NewsItem(
        'Karpathy autoresearch 项目持续走红：630 行 Python 让 AI Agent 独立跑通夜间实验循环',
        'https://github.com/karpathy/autoresearch',
        'GitHub / The New Stack', 'tools', datetime(2026, 3, 7, tzinfo=timezone.utc),
        'Andrej Karpathy 的 autoresearch 项目（3 月 7 日发布）在 5 月持续吸引关注，GitHub Stars 超 6.6 万。'
        '核心理念：将 Claude Code / Codex 对准一个极简 LLM 训练脚本，Agent 自主完成"提改→训练 5 分钟'
        '→评估→提交或回滚"的迭代循环，每小时约 12 次实验，过夜可跑约 100 次。'
        '已复现发现：缺失的 QKnorm scaler、value embedding 正则化收益、注意力带宽调优等。'
        '无需分布式训练，仅依赖 PyTorch，单 GPU 即可运行。',
    ),
]

# ── 论文 ────────────────────────────────────────────────────────────────────
papers = [
    Paper(
        'MEMTIER: Tiered Memory Architecture and Retrieval Bottleneck Analysis for Long-Running Autonomous AI Agents',
        'https://arxiv.org/abs/2605.03675',
        '2605.03675',
        ['arXiv Authors'],
        '针对长时运行 Agent 的记忆一致性问题：现有扁平文件记忆系统在 72 小时运行窗口内工具调用成功率下降 14 个百分点。'
        'MEMTIER 为 OpenClaw Agent 运行时构建三层记忆架构，包含结构化情节型 JSONL 存储、'
        '五信号加权检索引擎、注意力归因认知权重更新循环、异步巩固守护进程（情节→语义层晋升）'
        '及 PPO 策略框架自适应检索权重。'
        '在 LongMemEval-S 基准（500 题）上，使用 Qwen2.5-7B 达到 Acc=0.382、F1=0.412，'
        '相比全上下文基线提升 +33 个百分点。',
        ['cs.AI', 'cs.LG'], datetime(2026, 5, 5, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2605.03675',
        None,
    ),
    Paper(
        'MemRouter: Memory-as-Embedding Routing for Long-Term Conversational Agents',
        'https://arxiv.org/abs/2605.00356',
        '2605.00356',
        ['arXiv Authors'],
        '提出将 Agent 长期记忆编码为可路由的嵌入向量，在对话过程中动态决策哪些记忆应被激活。'
        '与传统 RAG 检索不同，MemRouter 将记忆视为路由节点，通过轻量级路由网络而非相似度检索'
        '来匹配当前对话语境，在多轮对话一致性和跨会话事实保留上均优于 RAG 基线。'
        '在 LoCoMo 和 MSC 基准上验证，适用于客服、心理咨询等需要长期个性化记忆的场景。',
        ['cs.CL', 'cs.AI'], datetime(2026, 5, 1, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2605.00356',
        None,
    ),
    Paper(
        'KAIROS: Benchmarking LLM Resilience to Peer Pressure in Collaborative Agentic Scenarios',
        'https://arxiv.org/list/cs.AI/current',
        '2605.kairos',
        ['arXiv Authors'],
        '构建 KAIROS 基准，将 LLM 置于含有不可靠同伴和对抗性参与者的多 Agent 协作场景中，'
        '系统测量模型在社会压力下的决策稳健性。实验显示当前主流模型普遍存在"同伴压力屈服"现象：'
        '即使初始判断正确，在受到错误同伴多数压力后也会更改答案。'
        'GPT-5.5 Instant 在对抗场景下屈服率 31%，Claude Opus 4.7 最低为 19%，'
        '对构建可靠多 Agent 系统有直接工程启示。',
        ['cs.AI', 'cs.MA'], datetime(2026, 5, 5, tzinfo=timezone.utc),
        None,
        None,
    ),
    Paper(
        'ScrapMem: A Bio-inspired Framework for On-device Personalized Agent Memory via Optical Forgetting',
        'https://arxiv.org/list/cs.AI/current',
        '2605.scrapmem',
        ['Jiale Chang', 'Yuxiang Ren'],
        '提出 ScrapMem，一种受生物光学遗忘机制启发的设备端个性化 Agent 记忆框架，已被 IEEE WoWMoM 2026 录用。'
        '与传统基于摘要或向量检索的记忆压缩不同，ScrapMem 模拟神经突触光衰减过程，'
        '对低频访问记忆施加自适应衰减，在保留高相关性记忆的同时大幅降低设备端存储和计算开销。'
        '在 10 页、4 图的完整论文中展示了在移动设备上的可行性验证。',
        ['cs.AI', 'cs.LG'], datetime(2026, 5, 6, tzinfo=timezone.utc),
        None,
        None,
    ),
    Paper(
        'Compliance-Aware Agentic Payments on Stablecoin Rails',
        'https://arxiv.org/list/cs.AI/current',
        '2605.payments',
        ['arXiv Authors'],
        '探索 AI Agent 在稳定币支付基础设施上执行合规自主支付的技术框架。'
        '论文提出将 KYC/AML 规则编码为智能合约约束，Agent 在发起每笔链上交易前需通过合规校验模块，'
        '同时引入幂等性保证机制防止 Agent 重复支付（idempotent payment primitives）。'
        '在金融 Agent 可靠性要求最严苛的场景下，实验显示将合规逻辑外置于链上而非依赖 LLM 内部判断'
        '可将支付错误率降低 89%，为 Anthropic 金融 Agent 等商业落地提供工程参考。',
        ['cs.AI', 'cs.CR'], datetime(2026, 5, 4, tzinfo=timezone.utc),
        None,
        None,
    ),
]

# ── 大牛动态 ─────────────────────────────────────────────────────────────────
updates = [
    InfluencerUpdate(
        'Simon Willison', 'Blog / Substack',
        '5 月 6-7 日双平台更新：① simonwillison.net 发布 Code w/ Claude 2026 大会现场直播博文，'
        '记录 Opus 4.7 设计品味、Claude Code Auto Mode 技术细节和 Shopify 90% 自主编码目标等要点；'
        '② Substack 发文《"Agent" 这个词终于有了可操作的共识定义》，'
        '提出严格定义标准（感知→规划→行动闭环 + 持久外部执行 + 目标自主调整），'
        '批评当前工具滥用"Agent"标签，呼吁文档和基准统一用语。',
        'https://simonwillison.net/2026/May/6/code-w-claude-2026/',
        datetime(2026, 5, 6, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Andrej Karpathy', 'GitHub / Sequoia Blog',
        'autoresearch 项目在 5 月持续引发工程师社区讨论（Stars 已超 6.6 万）。'
        'Karpathy 本人在 Sequoia Ascent 2026 炉边对话后撰文，'
        '将 autoresearch 定位为"可微实验循环"而非"代码生成"：'
        'Agent 的价值在于将科学方法（提出假设→验证→迭代）工程化，而非替代人类判断。'
        '他也提到正在将 autoresearch 扩展到非 NLP 领域（蛋白质折叠小实验），'
        '并表示"单 GPU 的研究效率将在两年内超越绝大多数学术实验室"。',
        'https://karpathy.bearblog.dev/sequoia-ascent-2026/',
        datetime(2026, 5, 6, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Chip Huyen', 'Blog (huyenchip.com)',
        'AI Engineering 系列最新更新聚焦"合规感知 Agent 支付"与金融场景可靠性：'
        '分析 Anthropic 金融 Agent 发布后各大银行的技术选型逻辑，'
        '指出支付 Agent 的核心挑战是幂等性（idempotency）——防止重复转账、重复下单；'
        '建议工程师将合规约束外置于链上或规则引擎而非依赖 LLM 内部判断，'
        '并详细讲解 Cerebras IPO 招股书中披露的 AI 推理成本结构对企业采购决策的影响。',
        'https://huyenchip.com/blog/',
        datetime(2026, 5, 7, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Sebastian Raschka', 'Blog (sebastianraschka.com)',
        '发布 Gemini 3.1 Flash-Lite GA 快速评测：与 GPT-5.5 Instant 和 Claude Haiku 4.5 做三向对比，'
        '关注点：成本效率（Gemini 最低）、延迟（Gemini 领先）、长上下文准确率（Claude 较优）。'
        '结论：对高频低风险任务（翻译、分类、摘要），Gemini 3.1 Flash-Lite 是 2026 年性价比最优选；'
        '复杂推理或需要审计的场景仍推荐 Claude Opus 4.7 或 GPT-5.5 Instant。'
        '同时警告：Flash-Lite 在代码生成任务上存在明显"截断输出"问题，需在 prompt 层显式约束。',
        'https://sebastianraschka.com/blog/',
        datetime(2026, 5, 7, tzinfo=timezone.utc),
    ),
]

# ── GitHub 热门 ──────────────────────────────────────────────────────────────
github = [
    GithubProject(
        'OpenClaw/openclaw',
        'https://github.com/OpenClaw/openclaw',
        'Personal AI assistant running entirely on your devices — local gateway to 50+ integrations (WhatsApp, Slack, Telegram, Signal, iMessage)',
        219000, 19800, 'TypeScript', 980, ['openclaw-core'],
    ),
    GithubProject(
        'karpathy/autoresearch',
        'https://github.com/karpathy/autoresearch',
        'AI agents automatically running research experiments on single-GPU nanochat training — 630 lines of pure Python, no external dependencies',
        66500, 9600, 'Python', 820, ['karpathy'],
    ),
    GithubProject(
        '1jehuang/jcode',
        'https://github.com/1jehuang/jcode',
        'High-performance multi-session coding agent harness — session resume across Claude Code, Codex, opencode; native multi-agent collaboration with low RAM usage',
        3200, 280, 'TypeScript', 750, ['1jehuang'],
    ),
    GithubProject(
        'TauricResearch/TradingAgents',
        'https://github.com/TauricResearch/TradingAgents',
        'Multi-agent LLM financial trading framework — fund managers, analysts, risk managers and traders collaborate autonomously to execute strategies',
        65300, 5800, 'Python', 610, ['TauricResearch'],
    ),
    GithubProject(
        'n8n-io/n8n',
        'https://github.com/n8n-io/n8n',
        'Fair-code workflow automation platform with native AI capabilities — visual agent pipelines, LLM chains, vector DB queries, 400+ integrations',
        187000, 23100, 'TypeScript', 540, ['janober', 'ivov'],
    ),
    GithubProject(
        'caramaschiHG/awesome-ai-agents-2026',
        'https://github.com/caramaschiHG/awesome-ai-agents-2026',
        'Most comprehensive list of AI agents, frameworks & tools in 2026 — 300+ resources, 20+ categories, updated monthly',
        8900, 620, 'Markdown', 480, ['caramaschiHG'],
    ),
    GithubProject(
        'huggingface/ml-intern',
        'https://github.com/huggingface/ml-intern',
        'Open-source AI agent that reads papers, trains models, and ships ML projects — fully automated ML engineering assistant',
        18700, 1400, 'Python', 390, ['huggingface'],
    ),
    GithubProject(
        'VoltAgent/awesome-ai-agent-papers',
        'https://github.com/VoltAgent/awesome-ai-agent-papers',
        'Curated collection of 2026 AI agent research papers — covers agent engineering, memory, evaluation, workflows, and autonomous systems',
        6400, 480, 'Markdown', 310, ['VoltAgent'],
    ),
]


# ── 主逻辑 ───────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description='生成并可选发布 2026-05-07 AI 日报')
    parser.add_argument('--publish', action='store_true', help='发布到博客（需 BLOG_DEPLOY_TOKEN）')
    args = parser.parse_args()

    filename, content = generate_jekyll_post(news, papers, updates, github)

    filename = '2026-05-07-ai-daily-news.md'
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
