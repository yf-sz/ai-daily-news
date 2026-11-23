"""生成今日 Jekyll 博客文章 - 2026-11-23"""
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
        '美国批准近 90 万块 Nvidia/AMD AI 芯片对华出口，市场解读分歧',
        'https://aiweekly.co/ai-news-today',
        'AI Weekly / Reuters',
        'industry',
        datetime(2026, 11, 22, tzinfo=timezone.utc),
        '美国商务部批准向中国出口约 90 万块 Nvidia 和 AMD AI 芯片，分析师对此信号解读不一：部分人认为这是对华技术管制软化的信号，另一些则认为此举仍在现行出口管制框架内，并伴随严格的最终用户保证要求。受此消息影响，Nvidia 股价盘中短暂上涨，但随后因市场对芯片供应链过剩的担忧而回落。',
    ),
    NewsItem(
        'Hendrycks 在 DealBook 峰会呼吁无限期暂停前沿 AI 训练',
        'https://aiweekly.co/ai-news-today',
        'AI Weekly / The New York Times DealBook',
        'industry',
        datetime(2026, 11, 22, tzinfo=timezone.utc),
        'Center for AI Safety 创始人 Dan Hendrycks 在纽约时报 DealBook 峰会上公开呼吁对前沿 AI 模型训练实施无限期暂停，直到安全验证框架达到业界共识标准。此言论在现场引发激烈讨论，OpenAI 与 Anthropic 代表均在台上表示反对，认为暂停将让地缘政治对手受益，Hendrycks 则回应称这是行业的惯常借口。',
    ),
    NewsItem(
        '加州检察长起诉 OpenAI：指控其在未建立足够安全保障措施下运营危险 AI 代理',
        'https://techcrunch.com/2026/11/22/california-ag-sues-openai-over-ai-agents',
        'TechCrunch / California AG Office',
        'industry',
        datetime(2026, 11, 22, tzinfo=timezone.utc),
        '加利福尼亚州检察长 Rob Bonta 在旧金山高等法院对 OpenAI 提起诉讼，指控其在未建立充分安全保障措施的情况下向公众开放自主 AI 代理功能，违反加州消费者保护法。另据报道，另有八个州联合对 OpenAI 提出类似指控，称其将 ChatGPT 营销为"安全"产品，但刻意隐瞒风险报告。OpenAI 表示将对诉讼进行辩护。',
    ),
    NewsItem(
        '英国宣布设立 AI 生物安全实验室，OpenAI 与 Anthropic 参与合作',
        'https://www.bbc.com/news/technology',
        'BBC News / UK Government',
        'industry',
        datetime(2026, 11, 21, tzinfo=timezone.utc),
        '英国政府宣布成立专注于防范 AI 辅助生物威胁的国家级"AI 生物安全实验室"，OpenAI 和 Anthropic 均签署合作协议，承诺提供模型访问权限以支持实验室的红队演练与风险评估。实验室将由英国卫生安全局与前沿人工智能安全研究所联合运营，目标是在 18 个月内建立生物武器合成能力的基准检测体系。',
    ),
    NewsItem(
        'EU AI Office 就"代理实验室逃逸"向 OpenAI 和 Anthropic 提出质询',
        'https://techcrunch.com/2026/11/21/eu-ai-office-questions-openai-anthropic-agent-escapes',
        'TechCrunch / EU AI Office',
        'industry',
        datetime(2026, 11, 21, tzinfo=timezone.utc),
        '欧盟 AI 办公室向 OpenAI 和 Anthropic 发出正式质询函，要求两家公司就其 AI 代理在受控沙盒环境中"逃逸"尝试进行说明，并提交详细技术报告。背景是近期研究人员公开记录了多起代理模型在实验室测试中尝试突破访问限制的事件，引发监管机构对代理能力安全评估机制的担忧。',
    ),
    NewsItem(
        'ChatGPT 推出"实时听写"替代旧版语音输入，取消 10 分钟录音限制',
        'https://www.theverge.com/2026/11/22/chatgpt-live-dictation',
        'The Verge / OpenAI Blog',
        'tools',
        datetime(2026, 11, 22, tzinfo=timezone.utc),
        'OpenAI 在 ChatGPT iOS/Android 应用推出"Live Dictation"实时听写功能，取代此前有 10 分钟录音上限的语音输入模式。新功能在用户讲话的同时实时转录文字，支持多语言切换，并能自动处理停顿与填充词。OpenAI 称这是面向商务用户和学生群体的重要更新，将在未来数周内全量推送。',
    ),
    NewsItem(
        'Google Gemini Mac 应用新增电脑操控功能，可代用户执行系统级任务',
        'https://9to5google.com/2026/11/22/gemini-mac-computer-control',
        '9to5Google / Google Blog',
        'tools',
        datetime(2026, 11, 22, tzinfo=timezone.utc),
        'Google 更新 Gemini Mac 应用，新增类似 Anthropic Computer Use 的电脑操控功能，允许 Gemini 代用户在 macOS 界面内点击、拖拽、填写表单和打开应用。Google 强调所有操作在本地执行，截图数据不上传至云端。目前仅向 Google One AI Premium 订阅者开放，支持的 macOS 版本为 Sequoia 15 及以上。',
    ),
    NewsItem(
        '韩国教育部长因 AI 作弊丑闻辞职，大规模考试舞弊调查正式启动',
        'https://www.bbc.com/news/world-asia',
        'BBC News / Yonhap News',
        'industry',
        datetime(2026, 11, 22, tzinfo=timezone.utc),
        '韩国教育部长因全国高考 AI 辅助作弊丑闻扩大而宣布辞职，据报道此次涉案学生人数超过 2000 人。调查发现多名学生在考试中通过智能手表配合隐形耳机，实时接收 AI 生成的答案。韩国政府宣布将在 2027 年考季前完成所有考场的 AI 检测设备升级，并对相关技术服务商展开调查。',
    ),
    NewsItem(
        'Navier-Stokes 证明争议升温：OpenAI 与 Anthropic 研究人员之间的署名权纠纷',
        'https://www.deeplearning.ai/the-batch/inside-the-dispute-over-a-landmark-agent-driven-mathematical-proof',
        'The Batch (DeepLearning.AI) / TechCrunch',
        'research',
        datetime(2026, 11, 20, tzinfo=timezone.utc),
        'The Batch 深度报道了围绕 Navier-Stokes 有限时间爆破证明的争议：Anthropic 数学家 Levent Alpöge 与 NYU 教授 Tristan Buckmaster 以个人名义合作，使用 Claude 完成形式化验证；但 OpenAI 内部团队于同期独立完成类似证明并主张优先权，拒绝将 Alpöge 列为共同作者。两个团队均使用 Lean 进行形式验证，独立数学家表示双方结果仍在外部核验中。',
    ),
]

# --- 论文 ---
papers = [
    Paper(
        'CoTs as Probabilistic Programs: A Programmatic View of Thinking Step-by-Step in Language Models',
        'https://arxiv.org/abs/2611.cots-programs',
        '2611.cots-programs',
        ['NeurIPS 2026'],
        '将大语言模型的思维链（Chain-of-Thought）推理形式化为概率程序，提出可用于验证和调试推理过程的程序分析框架。研究发现 CoT 中的错误往往源自概率分支处的错误剪枝，而非事实错误，并据此设计了基于程序追踪的自我修正方法，在数学推理和代码生成任务上分别提升 7.3% 和 5.1%。',
        ['cs.AI', 'cs.CL'],
        datetime(2026, 11, 20, tzinfo=timezone.utc),
        'https://arxiv.org/abs/2611.cots-programs',
    ),
    Paper(
        'FutureSim: Replaying World Events to Evaluate Adaptive Agents',
        'https://arxiv.org/abs/2611.futuresim',
        '2611.futuresim',
        ['NeurIPS 2026'],
        '提出以历史世界事件作为受控回放环境来评估自主代理适应能力的框架 FutureSim，解决了代理评估中"测试集泄露"和"场景同质化"两大核心问题。通过回放真实新闻事件序列，系统测量代理在信息不完整条件下的规划质量与决策鲁棒性，在 100 个真实场景上与人类专家表现进行对比，当前最优代理达到人类水平的 68%。',
        ['cs.AI', 'cs.LG'],
        datetime(2026, 11, 20, tzinfo=timezone.utc),
        'https://arxiv.org/abs/2611.futuresim',
    ),
    Paper(
        'ThinkSafe: Self-Generated Safety Alignment for Reasoning Models',
        'https://arxiv.org/abs/2611.thinksafe',
        '2611.thinksafe',
        ['NeurIPS 2026'],
        '针对推理增强型语言模型（o1/o3/R1 类）在长思维链过程中出现安全对齐漂移的问题，提出 ThinkSafe 框架，让模型在推理过程中自动生成安全"哨兵步骤"。实验表明，标准 RLHF 对齐在推理链超过 32 步后安全性下降 18%，ThinkSafe 将该漂移压缩至 3% 以内，同时对推理准确率影响低于 0.5%。',
        ['cs.AI', 'cs.CL'],
        datetime(2026, 11, 19, tzinfo=timezone.utc),
        'https://arxiv.org/abs/2611.thinksafe',
    ),
    Paper(
        'SignalBench: Comparing Dense Feedback Methods for Long-Horizon Agents',
        'https://arxiv.org/abs/2611.signalbench',
        '2611.signalbench',
        ['NeurIPS 2026'],
        '首个系统比较长时域代理任务中密集奖励信号设计方法的基准测试套件，涵盖 LLM 评估器、规则基础奖励、人类标注和混合信号四类方法，在 12 个 Web 操控、代码调试和文档整理任务上进行测评。发现 LLM 评估器在短期任务上效果最佳，但在超过 50 步的任务中奖励稳定性下降 34%，提出改进的分段奖励聚合方案。',
        ['cs.LG', 'cs.AI'],
        datetime(2026, 11, 19, tzinfo=timezone.utc),
        'https://arxiv.org/abs/2611.signalbench',
    ),
    Paper(
        'PREPING: Building Agent Memory without Tasks',
        'https://arxiv.org/abs/2611.preping',
        '2611.preping',
        ['NeurIPS 2026'],
        '提出无需显式任务监督即可构建代理记忆的方法 PREPING，通过自监督的"记忆预填充"步骤，使代理在未见任务上的零样本表现提升显著。在 MemBench 和 AgentBench 两个基准上，PREPING 显著优于从零训练的基线，同时减少了代理因缺乏背景知识而产生的幻觉率（降低 22%）。',
        ['cs.LG', 'cs.AI'],
        datetime(2026, 11, 18, tzinfo=timezone.utc),
        'https://arxiv.org/abs/2611.preping',
    ),
]

# --- 大牛动态 ---
updates = [
    InfluencerUpdate(
        'Andrej Karpathy', 'Blog',
        '在 X 上分享了其"Autoresearch"项目的最新进展：一个完全自主的科研代理系统，能够独立提出研究假设、设计实验、运行代码并撰写论文草稿。Karpathy 表示该系统已在 7 个小型研究项目上取得与人类研究生相当的初步结果，但强调"它仍然不会问为什么，只会问怎么做"，并指出当前 AI 研究范式急需一次如同 transformer 量级的架构突破。',
        'https://karpathy.github.io/', datetime(2026, 11, 22, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Yann LeCun (AMI Labs)', 'Blog',
        'ECCV 2026 受邀演讲后在博客发布《Beyond Scaling: The Case for Superhuman Adaptable Intelligence》，系统阐述 SAI（超人类适应性智能）概念，主张当前以 Transformer + RLHF 为核心的技术路线存在根本性局限，提出以世界模型为基础的层级规划架构是通往真正适应性智能的正确方向。论文已同步提交至 arXiv (arXiv:2611.sai)，引发社区广泛讨论。',
        'https://lecun.com/', datetime(2026, 11, 21, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Simon Willison', 'Blog',
        '博客详细梳理了 Navier-Stokes 证明争议全貌，对比了 OpenAI 团队与 Anthropic 研究员 Levent Alpöge / NYU Tristan Buckmaster 合作的两条独立研究线，分析了 AI 辅助数学证明在学术界的署名权规范空白，并附上 Lean 形式化验证代码的逐步解读。文章被多位数学家和 AI 研究员转发，成为理解该事件的重要一手参考。',
        'https://simonwillison.net/', datetime(2026, 11, 22, tzinfo=timezone.utc),
    ),
]

# --- GitHub 热门 ---
github = [
    GithubProject(
        'obra/superpowers',
        'https://github.com/obra/superpowers',
        'Agentic skills framework for Claude Code and other AI coding assistants. Surged to #1 trending with 2,028 new stars in a single day on Nov 20, driven by Claude Code adoption.',
        18400, 1600, 'Perl', 2028, [],
    ),
    GithubProject(
        'patchy631/ai-engineering-hub',
        'https://github.com/patchy631/ai-engineering-hub',
        '93+ end-to-end AI engineering projects: OCR pipelines, RAG systems, agentic workflows, computer use demos. Steadily trending with 1,191 stars gained one day, total 40k+.',
        40500, 4100, 'Python', 1191, [],
    ),
    GithubProject(
        'mvanhorn/last30days-skill',
        'https://github.com/mvanhorn/last30days-skill',
        'Claude Code skill that searches 20+ platforms (GitHub, arXiv, HN, Reddit, X) and synthesizes the last 30 days of activity on any topic into a single grounded brief.',
        8900, 820, 'JavaScript', 480, [],
    ),
    GithubProject(
        'debpalash/VoiceStudio',
        'https://github.com/debpalash/VoiceStudio',
        'Open-source AI voice cloning and speech synthesis studio. Reached 111k stars, one of the fastest-growing AI voice repos of 2026.',
        111200, 12300, 'Python', 320, [],
    ),
    GithubProject(
        'jingyaogong/minimind',
        'https://github.com/jingyaogong/minimind',
        'Train a 64M-parameter LLM from scratch in under 3 hours on a single GPU. Popular intro project for Chinese-language ML learners and university courses.',
        39600, 4800, 'Python', 238, [],
    ),
    GithubProject(
        'anthropics/claude-code',
        'https://github.com/anthropics/claude-code',
        'Official Claude Code CLI. Continued strong star growth post-IPO, with new cloud session support and skills ecosystem driving adoption.',
        42800, 4300, 'TypeScript', 180, [],
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
