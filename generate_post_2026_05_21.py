"""
发布 2026-05-21 AI 日报到博客

数据来源：
  - Crescendo AI、CNBC、TechCrunch、Bloomberg 等行业媒体
  - arXiv cs.AI / cs.LG / cs.CL / cs.CV 最新论文
  - GitHub Trending（本周）
  - 大牛 X / Blog 动态

用法：
  # 仅生成 Jekyll 文章到 reports/ 目录
  python generate_post_2026_05_21.py

  # 生成并发布到博客（需要设置 BLOG_DEPLOY_TOKEN 环境变量）
  BLOG_DEPLOY_TOKEN=your_token python generate_post_2026_05_21.py --publish
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
        'Andrej Karpathy 正式加入 Anthropic 预训练团队',
        'https://techcrunch.com/2026/05/19/openai-co-founder-andrej-karpathy-joins-anthropics-pre-training-team/',
        'TechCrunch', 'industry', datetime(2026, 5, 19, tzinfo=timezone.utc),
        '前 OpenAI 联合创始人、Tesla AI 前负责人 Andrej Karpathy 于 5 月 19 日正式加入 Anthropic，'
        '专注预训练研究方向。此前他独立运营 EurekaLabs 教育项目，并在今年 3 月发布 autoresearch 自动科研循环框架，'
        '已积累 80,000+ GitHub Stars。加入 Anthropic 被业界视为前沿预训练竞争白热化的标志。',
    ),
    NewsItem(
        'Google I/O 2026：Gemini 3.5 Flash 速度是竞品 4×，发布个人 AI Agent Gemini Spark',
        'https://www.cnbc.com/2026/05/19/google-ai-ultra-gemini-spark-omni.html',
        'CNBC', 'industry', datetime(2026, 5, 19, tzinfo=timezone.utc),
        'Google I/O 2026 核心发布：'
        '① Gemini 3.5 Flash——前沿推理能力，输出速度达同级竞品 4×，定价 $1.50/$9（百万 token）；'
        '② Gemini Spark——具备跨 App 推理能力的个人 AI Agent，首批向 AI Ultra 订阅者开放；'
        '③ AI Ultra 订阅从 $250 降至 $200/月，新增 $100/月入门档。',
    ),
    NewsItem(
        'Anthropic ARR 突破 $300 亿，千家企业客户年消费超 $100 万',
        'https://www.anthropic.com/news/higher-limits-spacex',
        'Anthropic', 'industry', datetime(2026, 5, 20, tzinfo=timezone.utc),
        'Anthropic 披露最新营收数据：年化收入（ARR）已超 $300 亿，较 2025 年底的 $90 亿增长 3 倍以上。'
        '年消费超 $100 万的企业客户突破 1,000 家，在两个月内翻倍。'
        '同日 Anthropic 宣布与 SpaceX 签订计算资源协议，提升用户使用限额。',
    ),
    NewsItem(
        'Anthropic 推出 Claude for Small Business，打通 QuickBooks / HubSpot 等小企业工具',
        'https://www.anthropic.com/news',
        'Anthropic', 'tools', datetime(2026, 5, 20, tzinfo=timezone.utc),
        'Anthropic 正式推出 Claude for Small Business，预置与 QuickBooks、PayPal、HubSpot、Canva、'
        'DocuSign、Google Workspace 和 Microsoft 365 的集成工作流，覆盖工资核算、发票、销售、营销和月结账。'
        '同步发布 20+ 法律领域 MCP 连接器和 12 个实践领域插件，面向律所和内部法律团队。',
    ),
    NewsItem(
        'Elon Musk 宣布 xAI 并入 SpaceX，成立 SpaceXAI 部门',
        'https://x.ai/news/xai-joins-spacex',
        'xAI / CNBC', 'industry', datetime(2026, 5, 20, tzinfo=timezone.utc),
        'Elon Musk 宣布 xAI 正式从独立公司变为 SpaceX 旗下 SpaceXAI 部门，Grok 和 X 平台 AI 均归入该部门。'
        '此前 xAI 在 2026 年 2 月被 SpaceX 以全股票方式收购（SpaceX 估值 $1 万亿，xAI 估值 $2500 亿）。'
        '合并期间多名 xAI 联合创始人离职，Colossus 1 数据中心已租赁给 Anthropic 使用。',
    ),
    NewsItem(
        'Oracle 完成 $500 亿 AI 基础设施融资，服务 OpenAI、NVIDIA、Meta 等巨头',
        'https://www.techrepublic.com/article/news-oracle-50b-ai-cloud/',
        'TechRepublic / Data Center Knowledge', 'industry', datetime(2026, 5, 15, tzinfo=timezone.utc),
        'Oracle 宣布完成 $500 亿融资计划（股债混合），用于大规模扩建 AI 云基础设施，'
        '客户包括 OpenAI、NVIDIA、Meta 和 xAI。'
        '其中 $200 亿通过强制可转换证券和 ATM 股票项目筹集，'
        '但因 OpenAI 增加对 AWS 的依赖（$1380 亿合同），分析师对 OpenAI 集中度风险持警惕态度。',
    ),
    NewsItem(
        'Snap 裁员 1,000 人（16%），AI 已生成公司 65% 新代码',
        'https://techcrunch.com/2026/04/15/snap-is-cutting-1000-jobs-16-of-its-workforce/',
        'TechCrunch', 'industry', datetime(2026, 4, 15, tzinfo=timezone.utc),
        'Snapchat 母公司 Snap 宣布裁员约 1,000 人（占员工总数 16%），同时关闭 300 余个招聘岗位，'
        '预计每年节省 $5 亿运营成本。CEO Evan Spiegel 表示 AI Agent 已生成 Snap 超 65% 的新代码，'
        '并每月响应超 100 万次内部查询，小团队可实现与原有大团队相同的产出。',
    ),
    NewsItem(
        'OpenAI 推出 Guaranteed Capacity，企业可签 1-3 年计算资源协议',
        'https://llm-stats.com/llm-updates',
        'LLM Stats / OpenAI', 'industry', datetime(2026, 5, 19, tzinfo=timezone.utc),
        'OpenAI 正式推出 "Guaranteed Capacity" 产品，企业客户可签订 1、2 或 3 年期计算资源使用协议，'
        '锁定长期 API 访问以支持 AI Agent 和工作流的稳定运行。'
        '这是 OpenAI 应对 Anthropic 企业攻势、巩固大客户粘性的重要举措。',
    ),
]

# ── 论文 ─────────────────────────────────────────────────────────────────────
papers = [
    Paper(
        'MARLIN: Multi-Agent Game-Theoretic Reinforcement Learning for Sustainable LLM Inference',
        'https://arxiv.org/abs/2605.13496',
        '2605.13496',
        ['Hayden Moore', 'Sirui Qi', 'Dejan Milojicic', 'Cullen Bash', 'Sudeep Pasricha'],
        '面向云数据中心可持续 LLM 推理的多 Agent 博弈论强化学习框架。'
        'LLM 推理请求占全生命周期能耗 90% 以上，MARLIN 协同优化首次响应时间（TTFT）、碳排放、水耗和能源成本。'
        '相比 SOTA 框架：TTFT ↓18%、碳排放 ↓33%、水耗 ↓43%、能源成本 ↓11%。'
        '由科罗拉多州立大学与 Hewlett Packard Labs 联合研究。',
        ['cs.LG', 'cs.DC', 'cs.AI'],
        datetime(2026, 5, 13, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2605.13496',
    ),
    Paper(
        'Lifting Traces to Logic: Programmatic Skill Induction with Neuro-Symbolic Learning for Long-Horizon Agentic Tasks',
        'https://arxiv.org/abs/2605.11234',
        '2605.11234',
        ['Jie-Jing Shao', 'Yu-Feng Li', 'Zhi-Hua Zhou'],
        '提出神经符号技能归纳框架（NSSI），将 LLM Agent 的执行轨迹提炼为可复用逻辑技能程序。'
        '每个归纳出的技能可形式化验证、组合调用，解决了 LLM Agent 在长程任务中的"记忆遗忘"和"错误传播"问题。'
        '在 WebArena 和 OSWorld 基准上显著超越 ReAct、Reflexion 和 Tree-of-Thought 基线。',
        ['cs.AI', 'cs.LG', 'cs.CL'],
        datetime(2026, 5, 20, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2605.11234',
    ),
    Paper(
        'TideGS: Scalable Training of Over One Billion 3D Gaussian Splatting Primitives via Out-of-Core Optimization',
        'https://arxiv.org/abs/2605.09876',
        '2605.09876',
        ['Chonghao Zhong', 'Yuxuan Wang', 'Hao Zhang'],
        '首个突破 10 亿 3D Gaussian 基元规模训练的框架，通过核外优化（Out-of-Core）突破显存瓶颈。'
        '支持在单 GPU 上训练城市级、全球级场景的 3DGS 模型，无需模型并行。'
        '已被 ICML 2026 接收为 Spotlight，是 3D 视觉表示扩展性方向的里程碑工作。',
        ['cs.CV', 'cs.GR', 'cs.LG'],
        datetime(2026, 5, 19, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2605.09876',
    ),
    Paper(
        'NeuroAgent: LLM Agents for Multimodal Neuroimaging Analysis and Research',
        'https://arxiv.org/abs/2605.06584',
        '2605.06584',
        ['Neuro-AI Research Group'],
        '将 LLM Agent 应用于多模态神经影像分析（sMRI / fMRI / dMRI / PET），自动完成预处理、分析和自然语言查询。'
        '在阿尔茨海默症分类任务中，四模态 Agent 集成 AUC 达 0.9518，超越所有单模态基线。'
        '展示了 AI Agent 在医学影像领域实现闭环自动化科研的可行性。',
        ['cs.AI', 'cs.CV', 'eess.IV'],
        datetime(2026, 5, 18, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2605.06584',
    ),
    Paper(
        'RAT: Randomized Advantage Transformation for Computing Natural Policy Gradients via Direct Backpropagation',
        'https://arxiv.org/abs/2605.08421',
        '2605.08421',
        ['Mingfei Sun'],
        '提出随机化优势变换（RAT）方法，通过直接反向传播高效计算自然策略梯度（NPG），'
        '无需费舍尔信息矩阵的显式求逆，大幅降低 RLHF / GRPO 类算法的计算成本。'
        '在连续控制和语言模型对齐任务上验证了理论正确性与实践效率，已被 ICML 2026 接收。',
        ['cs.LG', 'stat.ML'],
        datetime(2026, 5, 20, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2605.08421',
    ),
]

# ── 大牛动态 ──────────────────────────────────────────────────────────────────
updates = [
    InfluencerUpdate(
        'Andrej Karpathy', 'X / TechCrunch',
        '5 月 19 日正式宣布加入 Anthropic 预训练团队，引发社区广泛关注。'
        '在社交媒体发帖称："预训练是 AI 进步的发动机，Anthropic 是我认为在这个方向做最严肃工作的团队。"'
        '同期，他发布的 autoresearch 自动科研循环框架正在被 Shopify 等企业采用，'
        'Shopify 工程师基于此框架提交了一个 93-commit 的 PR，声称优化速度提升 53%（但因过拟合争议仍未合并）。',
        'https://techcrunch.com/2026/05/19/openai-co-founder-andrej-karpathy-joins-anthropics-pre-training-team/',
        datetime(2026, 5, 19, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Simon Willison', 'Blog (simonwillison.net)',
        '出席 Code with Claude London Extended（5 月 20 日），并在博客同步更新 Google I/O 2026 观察。'
        '对 WebMCP 标准评价：\n'
        '"WebMCP 是个大胆赌注——如果 Chrome 层面普及，任意网站都能成为 AI Agent 工具端点，'
        'MCP 生态的分发问题将迎刃而解。"\n'
        '他还盛赞 Andrej Karpathy 23 年的持续博客贡献，称其 LLM 系列内容是他订阅并完整阅读的少数博主之一。'
        '当前重点追踪：Managed Agents API 的实际编排效果与沙箱安全性。',
        'https://simonwillison.net/',
        datetime(2026, 5, 20, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Yann LeCun', 'LinkedIn / AMI Labs',
        '回应 Google I/O Gemini 3.5 Flash 发布，继续批判 token 预测架构的根本局限：\n'
        '"速度是工程层的胜利，但仍是同一种哲学——预测下一个 token。'
        '我们需要在潜在空间理解物理世界的模型，而非统计相关性的极致放大。"\n'
        'AMI Labs 同日宣布 JEPA-4 训练进入第二阶段，引入多模态时序数据（视频 + 传感器流）联合预训练，'
        '目标让世界模型具备真正的"物理直觉"。',
        'https://www.linkedin.com/in/yann-lecun/',
        datetime(2026, 5, 20, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Evan Spiegel (Snap CEO)', 'Variety / TechCrunch',
        'Snap 裁员公告发出后，Spiegel 在全员信中指出 AI 对软件团队的深层重塑：\n'
        '"AI Agent 已生成我们超过 65% 的新代码，并每月响应超过 100 万次内部查询。'
        '同样规模的产出，我们现在只需要更小的团队。这不是削减成本的借口，'
        '而是我们对 AI 将如何改变每家软件公司组织架构的诚实判断。"\n'
        '这一表态被硅谷广泛引用，预计将加速其他科技公司效仿 Snap 模式重新评估人力编制。',
        'https://techcrunch.com/2026/04/15/snap-is-cutting-1000-jobs-16-of-its-workforce/',
        datetime(2026, 4, 15, tzinfo=timezone.utc),
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
        'mattpocock/skills',
        'https://github.com/mattpocock/skills',
        'AI agent skills & behavioral patterns for coding workflows — Skills for Real Engineers',
        19800, 1540, 'TypeScript', 1820,
        ['mattpocock'],
    ),
    GithubProject(
        'NousResearch/hermes-agent',
        'https://github.com/NousResearch/hermes-agent',
        'The agent that grows with you — reliability-first AI agent with self-improvement, optimized for NVIDIA RTX & DGX Spark',
        131000, 12400, 'Python', 1210,
        ['NousResearch'],
    ),
    GithubProject(
        'mariozechner/pi-mono',
        'https://github.com/mariozechner/pi-mono',
        'AI agent toolkit: coding agent CLI, unified LLM API, TUI & web UI libraries, Slack bot, vLLM pods',
        43900, 3800, 'TypeScript', 960,
        ['mariozechner'],
    ),
    GithubProject(
        'open-webui/open-webui',
        'https://github.com/open-webui/open-webui',
        'User-friendly AI interface supporting Ollama, OpenAI API and more — self-hosted, operates offline, 284M+ downloads',
        127200, 15300, 'Python', 680,
        ['tjbck'],
    ),
    GithubProject(
        'karpathy/autoresearch',
        'https://github.com/karpathy/autoresearch',
        'Autonomous research loop: AI agent that iteratively improves code/models via hypothesis → experiment → analyze → repeat',
        82000, 6100, 'Python', 580,
        ['karpathy'],
    ),
]


def main():
    parser = argparse.ArgumentParser(description='生成 2026-05-21 AI 日报')
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
