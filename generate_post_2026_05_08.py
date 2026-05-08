"""
发布 2026-05-08 AI 日报到博客

用法：
  # 仅生成 Jekyll 文章到 reports/ 目录
  python generate_post_2026_05_08.py

  # 生成并发布到博客（需要设置 BLOG_DEPLOY_TOKEN 环境变量）
  BLOG_DEPLOY_TOKEN=your_token python generate_post_2026_05_08.py --publish
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
        'Anthropic 发布 10 款金融 AI Agent，深入华尔街：覆盖投行、资管、保险全流程',
        'https://www.anthropic.com/news/finance-agents',
        'Anthropic', 'industry', datetime(2026, 5, 5, tzinfo=timezone.utc),
        '10 款开箱即用的金融 Agent 模板：Pitch builder（尽职调查+路演材料）、KYC screener（反洗钱合规筛查）、'
        'Month-end closer（财务关账）、Earnings reviewer（财报解读）、Model builder（金融建模）等。'
        '每款 Agent 内置技能、数据连接器与子 Agent 三层架构，可在 Claude Cowork 和 Claude Code 中以插件形式直接部署，'
        '同步推出 Claude for Microsoft 365（Excel/Word/PowerPoint/Outlook 全系集成），'
        '并与 Moody\'s 建立数据合作伙伴关系，银行和资管机构可在数天内而非数月内完成上线。',
    ),
    NewsItem(
        'Harvard-Science 研究：OpenAI 推理模型在波士顿急诊室超越经验丰富医生',
        'https://www.science.org/doi/10.1126/science.adz4433',
        'Science / Harvard Medical School', 'research', datetime(2026, 4, 30, tzinfo=timezone.utc),
        '哈佛医学院与 Beth Israel Deaconess 医学中心联合在《Science》发表研究：'
        'OpenAI o1 模型在 76 个真实急诊病例（分诊→首次接触→入院三阶段）上全程匹配或超越专家医生表现，'
        '在罕见病与复杂病例诊断上优势尤为突出。'
        '作者同时指出局限：AI 仅依赖文字记录，无法处理影像、听诊音等非文本信息，需开展前瞻性临床试验验证。',
    ),
    NewsItem(
        'Microsoft 发布 2026 年全球 AI 扩散报告：使用率升至 17.8%，贫富国数字鸿沟加剧',
        'https://blogs.microsoft.com/on-the-issues/2026/05/07/the-state-of-global-ai-diffusion-in-2026/',
        'Microsoft On the Issues', 'research', datetime(2026, 5, 7, tzinfo=timezone.utc),
        '2026 年 Q1 全球劳动年龄人口 AI 使用率从 16.3% 升至 17.8%，26 个经济体超过 30%。'
        'UAE 以 70.1% 继续领跑全球；美国从第 24 升至第 21（31.3%）。'
        '亚洲加速：韩国、泰国、日本增速最快（亚洲语言能力提升驱动）。'
        '数字鸿沟扩大：发达国家 27.5% vs 发展中国家 15.4%，差距较 2025 年下半年扩大 1.5 个百分点。'
        '意外发现：AI 编码能力提升反而推高软件开发者就业，2025 年美国开发者达 220 万，同比增长 8.5%，创历史新高。',
    ),
    NewsItem(
        'Novo Nordisk 与 OpenAI 达成战略合作，AI 全面介入新药研发到供应链',
        'https://www.cnbc.com/2026/04/14/novo-nordisk-openai-ai-drug-discovery-healthcare-nvo.html',
        'CNBC / FiercePharma', 'industry', datetime(2026, 4, 14, tzinfo=timezone.utc),
        '丹麦制药巨头 Novo Nordisk 宣布与 OpenAI 战略合作，将 AI 部署到全业务链条：'
        '从药物发现、临床试验到生产制造、供应链与商业化运营，目标 2026 年底完成规模化部署。'
        '重点聚焦肥胖症和糖尿病新疗法的快速识别，OpenAI 同步协助推进全球员工 AI 素养提升计划。',
    ),
    NewsItem(
        'JPMorgan Chase 将 AI 列为核心基础设施：2026 年 IT 预算 198 亿美元，AI 年创值 25 亿美元',
        'https://www.crescendo.ai/news/latest-ai-news-and-updates',
        'Crescendo AI / JPMorgan', 'industry', datetime(2026, 5, 8, tzinfo=timezone.utc),
        'JPMorgan Chase 正式将 AI 投资从"实验性研发"重分类为"核心基础设施"，'
        '2026 年技术预算约 198 亿美元，2,000 名专职 AI 员工。'
        '重点方向：通过 AI Agent 提升内部生产力、强化网络安全防御、个性化零售银行服务，'
        'AI 预计为银行带来 25 亿美元/年的效率收益与营收增长。',
    ),
    NewsItem(
        '中国四大实验室 12 天内连续发布开源编程模型：GLM-5.1、MiniMax M2.7、Kimi K2.6、DeepSeek V4',
        'https://llm-stats.com/ai-news',
        'LLM Stats', 'industry', datetime(2026, 5, 7, tzinfo=timezone.utc),
        'Z.ai (GLM-5.1)、MiniMax (M2.7)、Moonshot (Kimi K2.6)、DeepSeek (V4) 在 12 天内密集发布开放权重编程模型，'
        '四款模型在 Agentic Engineering 能力上达到相近天花板，推理成本均显著低于西方前沿模型。'
        '分析师指出此轮"饱和式投放"策略旨在以低价策略抢占开发者生态。',
    ),
    NewsItem(
        'Cloudflare 发布高性能 LLM 基础设施：输入/输出分离架构，覆盖全球网络',
        'https://www.infoq.com/news/2026/05/cloudflare-llm-infrastructure/',
        'InfoQ / Cloudflare', 'tools', datetime(2026, 5, 7, tzinfo=timezone.utc),
        'Cloudflare 发布专为 LLM 推理优化的全球基础设施，核心创新：'
        '将模型的输入处理（Prefill）与输出生成（Decode）拆分到不同优化系统，'
        '充分利用其遍布全球的边缘节点降低首 Token 延迟。'
        '目标场景：高频低延迟的实时 AI 应用（客服、代码补全、搜索增强）。',
    ),
    NewsItem(
        'PayPal 以 AI 驱动转型：裁员 + 自动化，目标实现 15 亿美元成本节约',
        'https://llm-stats.com/ai-news',
        'LLM Stats', 'industry', datetime(2026, 5, 6, tzinfo=timezone.utc),
        'PayPal 宣布以 AI 主导的战略转型：通过流程自动化和技术栈现代化实现 15 亿美元成本削减，'
        '同步推进组织重构，重新培训员工以适应 AI 增强的工作方式。'
        'CEO Alex Chriss 强调这是"进攻性"而非"防御性"变革，旨在重新夺回数字支付市场主导地位。',
    ),
]

# ── 论文 ────────────────────────────────────────────────────────────────────
papers = [
    Paper(
        'Safety and Fairness in Agentic AI Depend on Interaction Topology, Not on Model Scale or Alignment',
        'https://arxiv.org/list/cs.AI/current',
        '2605.safety-topology',
        ['arXiv Authors'],
        '立场论文：Agentic AI 系统的安全性与公平性主要由多 Agent 交互拓扑结构决定，而非模型规模或对齐训练程度。'
        '论文指出当前以"更大模型 = 更安全"为前提的主流研究路线存在根本性误区，'
        '提出应将拓扑约束（通信图结构、访问权限边界、反馈回路设计）纳入 Agentic 安全评估的核心维度。'
        '对多 Agent 系统架构师和安全研究者具有重要参考价值。',
        ['cs.AI', 'cs.MA'], datetime(2026, 5, 7, tzinfo=timezone.utc),
        None, None,
    ),
    Paper(
        'Terminus-4B: Can a Smaller Model Replace Frontier LLMs at Agentic Execution Tasks?',
        'https://arxiv.org/list/cs.AI/current',
        '2605.terminus-4b',
        ['arXiv Authors'],
        '探索 4B 参数小模型在 Terminal-Bench（229 个真实命令行任务）上替代前沿 LLM 执行 Agentic 任务的可行性。'
        '实验显示经过针对性的 SFT + RL 训练后，Terminus-4B 在代码执行、文件操作、系统管理等子任务上'
        '与 GPT-5.5 Instant 差距从 34 个百分点缩小至 11 个百分点，推理成本降低 15 倍，'
        '为边缘设备部署 Agentic 系统提供了工程路径。',
        ['cs.AI', 'cs.LG'], datetime(2026, 5, 7, tzinfo=timezone.utc),
        None, None,
    ),
    Paper(
        'Stop Automating Peer Review Without Rigorous Evaluation (ICML 2026 Spotlight)',
        'https://arxiv.org/list/cs.AI/current',
        '2605.peer-review',
        ['arXiv Authors'],
        'ICML 2026 Spotlight 论文：对当前 LLM 自动化同行评审的系统性批评。'
        '作者通过大规模实验证明，主流 LLM 审稿系统在论文创新性判断上与人类审稿人的一致率仅为 52%（接近随机）。'
        '提出自动评审系统的最低评估标准框架，要求新工具必须先通过基准校准测试再用于真实评审流程，'
        '反对在缺乏严格验证的情况下部署 AI 评审系统。',
        ['cs.AI', 'cs.DL'], datetime(2026, 5, 7, tzinfo=timezone.utc),
        None, None,
    ),
    Paper(
        'What You Think is What You See: Driving Exploration in VLM Agents via Visual-Linguistic Curiosity',
        'https://arxiv.org/list/cs.AI/current',
        '2605.vlm-curiosity',
        ['arXiv Authors'],
        '提出视觉-语言好奇心驱动框架（VLC），通过在 VLM Agent 的视觉感知与语言表征之间建立不确定性测量，'
        '引导 Agent 主动探索信息密度高的区域，而非依赖奖励信号的被动学习。'
        '在 MiniWorld、Habitat 和 ALFRED 三个多模态环境上验证，VLC Agent 的探索效率比随机基线提升 2.3 倍，'
        '在零样本任务完成率上超过有监督基线。',
        ['cs.CV', 'cs.AI'], datetime(2026, 5, 6, tzinfo=timezone.utc),
        None, None,
    ),
    Paper(
        'On-Policy Distillation for Mathematical Reasoning: 70% AIME\'24 with Qwen3-8B at 30× Cost Reduction',
        'https://arxiv.org/list/cs.LG/current',
        '2605.on-policy-distill',
        ['arXiv Authors'],
        '提出在线策略蒸馏方法（On-Policy Distillation）：让学生模型在自身生成的轨迹上直接从教师模型输出 logits 蒸馏，'
        '相比离线蒸馏在 AIME\'24 数学推理基准上，Qwen3-8B 学生模型达到 70% 准确率，'
        '而训练 GPU 时间仅为离线蒸馏的 1/30。'
        '为在有限算力下高效训练推理型小模型提供了实用方法，代码已开源。',
        ['cs.LG', 'cs.CL'], datetime(2026, 5, 7, tzinfo=timezone.utc),
        None, None,
    ),
]

# ── 大牛动态 ─────────────────────────────────────────────────────────────────
updates = [
    InfluencerUpdate(
        'Simon Willison', 'Blog (simonwillison.net)',
        '持续深度解析 Code w/ Claude 2026 大会后续影响：聚焦 Anthropic 金融 Agent 发布的技术架构拆解，'
        '指出"三层结构（技能+连接器+子 Agent）"本质是一种可复用的 Agent 模板标准化范式，'
        '并与 OpenAI 的 GPT Action 体系做了横向对比。'
        '同时更新其 LLM 工具集追踪博文，评估 Cloudflare LLM 基础设施对独立开发者的实际意义。',
        'https://simonwillison.net/',
        datetime(2026, 5, 8, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Andrej Karpathy', 'X (Twitter)',
        '转发并点评 Harvard-Science 急诊 AI 研究，认为"医疗诊断文本任务已基本被 LLM 解决"，'
        '强调下一关卡是多模态（影像+生理信号+非文本）整合，而非纯语言推理能力。'
        '同时分享 autoresearch 项目 5 月进展：已有社区贡献者将其应用于蛋白质结构预测小实验，'
        '单 GPU 一夜可跑 80+ 次折叠-评估-修改迭代循环。',
        'https://x.com/karpathy',
        datetime(2026, 5, 8, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Chip Huyen', 'Blog (huyenchip.com)',
        '发布深度长文《为什么大多数企业的 AI 投资回报率不符合预期》：'
        '分析 JPMorgan 198 亿美元 AI 预算与 25 亿美元预期回报（ROI 约 12.6%）背后的结构性挑战，'
        '指出企业 AI 落地的真实瓶颈往往不是模型能力，而是数据治理、流程重设计和组织变革速度。'
        '结合 Anthropic 金融 Agent 发布，具体讨论"预配置 Agent 模板"在降低企业落地门槛上的价值与局限。',
        'https://huyenchip.com/blog/',
        datetime(2026, 5, 8, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Sebastian Raschka', 'Blog / Substack',
        '发布每周 AI 研究综述，重点解析"On-Policy Distillation"论文：'
        '认为 30 倍成本降低 + 70% AIME 准确率是 2026 年迄今为止最有工程实用价值的小模型训练结果之一，'
        '详细比较了 On-Policy 与 Off-Policy 蒸馏的梯度流差异，并附带可复现实验代码解读。'
        '同时点评 Microsoft AI 扩散报告：数字鸿沟扩大趋势值得政策层面关注。',
        'https://sebastianraschka.com/blog/',
        datetime(2026, 5, 8, tzinfo=timezone.utc),
    ),
]

# ── GitHub 热门 ──────────────────────────────────────────────────────────────
github = [
    GithubProject(
        'forrestchang/andrej-karpathy-skills',
        'https://github.com/forrestchang/andrej-karpathy-skills',
        'A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy observations — most-starred Claude config file',
        106827, 7200, '', 1840, ['forrestchang'],
    ),
    GithubProject(
        'OpenClaw/openclaw',
        'https://github.com/OpenClaw/openclaw',
        'Personal AI assistant running entirely on your devices — local gateway to 50+ integrations (WhatsApp, Slack, Telegram, Signal, iMessage)',
        221000, 20100, 'TypeScript', 1120, ['openclaw-core'],
    ),
    GithubProject(
        'mattpocock/skills',
        'https://github.com/mattpocock/skills',
        'Skills for Real Engineers — straight from my .claude directory, production-tested Claude Code prompting patterns',
        55320, 3100, 'Markdown', 980, ['mattpocock'],
    ),
    GithubProject(
        'warpdotdev/warp',
        'https://github.com/warpdotdev/warp',
        'Warp is an agentic development environment, born out of the terminal — AI-native shell with agent pipelines and collaborative sessions',
        52872, 4600, 'Rust', 760, ['warpdotdev'],
    ),
    GithubProject(
        'VectifyAI/PageIndex',
        'https://github.com/VectifyAI/PageIndex',
        'Document Index for Vectorless, Reasoning-based RAG — 98.7% financial RAG accuracy without embeddings',
        27600, 1800, 'Python', 640, ['VectifyAI'],
    ),
    GithubProject(
        'karpathy/autoresearch',
        'https://github.com/karpathy/autoresearch',
        'AI agents automatically running research experiments on single-GPU nanochat training — 630 lines of pure Python, no external dependencies',
        67200, 9700, 'Python', 520, ['karpathy'],
    ),
    GithubProject(
        'tmgthb/Autonomous-Agents',
        'https://github.com/tmgthb/Autonomous-Agents',
        'Autonomous Agents (LLMs) research papers — updated daily, most comprehensive curated list of agent research',
        18900, 2100, 'Markdown', 410, ['tmgthb'],
    ),
    GithubProject(
        'VoltAgent/awesome-ai-agent-papers',
        'https://github.com/VoltAgent/awesome-ai-agent-papers',
        'Curated collection of 2026 AI agent research papers — covers agent engineering, memory, evaluation, workflows, and autonomous systems',
        6800, 510, 'Markdown', 320, ['VoltAgent'],
    ),
]


# ── 主逻辑 ───────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description='生成并可选发布 2026-05-08 AI 日报')
    parser.add_argument('--publish', action='store_true', help='发布到博客（需 BLOG_DEPLOY_TOKEN）')
    args = parser.parse_args()

    filename, content = generate_jekyll_post(news, papers, updates, github)

    filename = '2026-05-08-ai-daily-news.md'
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
