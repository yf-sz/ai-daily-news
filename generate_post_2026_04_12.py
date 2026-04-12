"""
发布 2026-04-12 AI 日报到博客

用法：
  # 仅生成 Jekyll 文章到 reports/ 目录
  python generate_post_2026_04_12.py

  # 生成并发布到博客（需要设置 BLOG_DEPLOY_TOKEN 环境变量）
  BLOG_DEPLOY_TOKEN=your_token python generate_post_2026_04_12.py --publish
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
        'Google 发布 Gemini 3.1 Ultra 与 Flash-Lite：2M Token 上下文，原生多模态',
        'https://llm-stats.com/ai-news',
        'Google DeepMind', 'industry', datetime(2026, 4, 12, tzinfo=timezone.utc),
        'Gemini 3.1 Ultra 支持 200 万 Token 上下文，可原生处理文本、图像、音频、视频，无需转录中间层。'
        'Flash-Lite 效率版响应速度提升 2.5 倍、输出速度快 45%，价格仅 $0.25/M 输入 Token。'
    ),
    NewsItem(
        'Microsoft 发布 MAI-Transcribe-1：当前最精准语音转文字模型',
        'https://www.geekwire.com/2026/microsoft-releases-new-ai-models-to-further-expand-beyond-openai/',
        'Microsoft', 'industry', datetime(2026, 4, 12, tzinfo=timezone.utc),
        'MAI-Transcribe-1 被微软称为目前精度最高的 STT 模型，同批次发布的还有面向广泛商用的'
        ' MAI-Voice-1（语音生成）与 MAI-Image-2（图像生成），标志微软在 AI 基础模型上进一步脱离对 OpenAI 的依赖。'
    ),
    NewsItem(
        'Anthropic 探索自研 AI 芯片：Claude 年化营收突破 300 亿美元',
        'https://techbriefly.com/2026/04/10/anthropic-explores-custom-ai-chip-design-to-power-claude-models/',
        'Anthropic', 'industry', datetime(2026, 4, 10, tzinfo=timezone.utc),
        'Claude 需求激增推动 Anthropic 进入早期芯片设计探讨阶段，目标是减少对外部供应商依赖。'
        '设计一款先进 AI 芯片约需 5 亿美元投入，Meta 和 OpenAI 已先行一步。'
        '公司年化营收从 2025 年底约 90 亿美元飙升至逾 300 亿美元。'
    ),
    NewsItem(
        'Anthropic 推出 Claude Managed Agents：大幅降低企业 Agent 开发门槛',
        'https://blog.ibvl.in/index.php/2026/04/09/new-anthropic-tool-speeds-up-ai-agent-development-for-enterprises/',
        'Anthropic', 'industry', datetime(2026, 4, 9, tzinfo=timezone.utc),
        '全新 Claude Managed Agents 工具减少开发者自建 AI Agent 所需时间，'
        '为企业提供生产就绪的 Agent 编排基础设施，包括 inbox 配置、实时 Hook 和工作流集成。'
    ),
    NewsItem(
        'OpenAI 估值达 8520 亿美元，推出 ChatGPT 超级应用',
        'https://www.marketingprofs.com/opinions/2026/54530/ai-update-april-10-2026-ai-news-and-views-from-the-past-week',
        'OpenAI', 'industry', datetime(2026, 4, 10, tzinfo=timezone.utc),
        'OpenAI 完成新一轮融资，估值 8520 亿美元。新版 ChatGPT 超级应用整合聊天、代码、搜索与 Agent 能力。'
        '公司预测 2026 年广告营收达 25 亿美元，2030 年可达 1000 亿美元。'
    ),
    NewsItem(
        'NASA 火星车 Perseverance 完成首次 AI 自主规划驾驶',
        'https://www.jpl.nasa.gov/news/nasas-perseverance-rover-completes-first-ai-planned-drive-on-mars/',
        'NASA JPL × Anthropic', 'research', datetime(2026, 4, 12, tzinfo=timezone.utc),
        'Claude 使用视觉-语言能力分析轨道图像和地形数据，自主生成安全路径点，'
        '驱动火星车完成历史首次 AI 规划行驶（210 米 + 246 米两段）。每次指令经超 50 万变量仿真验证。'
    ),
    NewsItem(
        'Google TurboQuant：KV Cache 内存压缩超 6 倍，在 ICLR 2026 亮相',
        'https://research.google/blog/rss/',
        'Google Research', 'research', datetime(2026, 4, 12, tzinfo=timezone.utc),
        'TurboQuant 算法将 LLM 推理时最大瓶颈之一——KV Cache 内存占用——压缩超过 6 倍，'
        '不损失显著精度，为大规模推理部署提供关键效率突破。'
    ),
    NewsItem(
        'Google AI Edge Gallery 上线 GitHub：设备端 ML/GenAI 开放展示库',
        'https://aitoolly.com/ai-news/article/2026-04-09-google-ai-edge-gallery-a-new-repository-for-on-device-machine-learning-and-generative-ai-use-cases',
        'Google', 'tools', datetime(2026, 4, 9, tzinfo=timezone.utc),
        'Google AI Edge 在 GitHub 开放"Gallery"仓库，展示可在本地设备运行的 ML 和 GenAI 应用案例，'
        '开发者可直接探索、测试并集成各类端侧模型。'
    ),
    NewsItem(
        'OpenClaw 突破 21 万星：本地 AI 助手成 2026 最快增长开源项目',
        'https://blog.bytebytego.com/p/top-ai-github-repositories-in-2026',
        '开源社区', 'tools', datetime(2026, 4, 12, tzinfo=timezone.utc),
        'OpenClaw 从 2026 年初 9,000 星飙升至 21 万+，成 GitHub 历史增速最快开源项目。'
        '作为本地 AI 网关连接 WhatsApp、Telegram、Slack、Discord 等 50+ 集成，完全在用户设备运行。'
    ),
]

# ── 论文 ────────────────────────────────────────────────────────────────────
papers = [
    Paper(
        'Uni-SafeBench：统一多模态大模型安全基准',
        'https://arxiv.org/list/cs.AI/current', '2604.00010',
        ['Zixiang Peng', 'Safety Research Group'],
        '针对多模态 LLM 的综合安全评测框架，覆盖图文融合场景下的越狱攻击（jailbreak）与对抗注入，'
        '系统性评估主流模型在统一多模态输入下的安全边界。',
        ['cs.CV', 'cs.CL'], datetime(2026, 4, 11, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.AI/current',
    ),
    Paper(
        'BloClaw：面向下一代科学发现的全知多模态智能工作台',
        'https://arxiv.org/list/cs.AI/current', '2604.00011',
        ['Yao Qin', 'BloClaw Team'],
        '提出一套全模态感知的 Agentic 科学研究工作台，集成文献检索、实验规划、多模态数据分析和结论生成，'
        '旨在加速跨学科科学发现。',
        ['cs.AI', 'cs.LG'], datetime(2026, 4, 11, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.AI/current',
    ),
    Paper(
        'PolySwarm：用于预测市场交易与延迟套利的多 Agent LLM 框架',
        'https://arxiv.org/html/2604.03888v1', '2604.03888',
        ['PolySwarm Team'],
        '构建基于多 Agent LLM 协同的预测市场交易系统，Agent 分别承担信息收集、概率估计与交易执行角色，'
        '在低延迟场景下实现套利策略。',
        ['cs.AI', 'cs.MA'], datetime(2026, 4, 10, tzinfo=timezone.utc),
        'https://arxiv.org/html/2604.03888v1',
    ),
    Paper(
        'Silo-Bench：多 Agent LLM 分布式协调能力可扩展评测环境',
        'https://arxiv.org/list/cs.MA/recent', '2604.00012',
        ['Silo Research Team'],
        '专为评估多 Agent LLM 系统在分布式、无中央协调场景下的协作能力而设计的基准，'
        '包含可扩展至数百 Agent 的仿真环境及评测指标。',
        ['cs.MA', 'cs.AI'], datetime(2026, 4, 11, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.MA/recent',
    ),
    Paper(
        '企业级神经符号推理：基于本体约束的 AI Agent 架构',
        'https://arxiv.org/list/cs.AI/current', '2604.00013',
        ['Enterprise AI Research Group'],
        '将知识本体约束引入神经网络推理流程，构建可审计、可解释的企业级 AI Agent 架构，'
        '覆盖金融、医疗、法律等 5 个强监管行业的实证评估。',
        ['cs.AI', 'cs.SE'], datetime(2026, 4, 11, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.AI/current',
    ),
]

# ── 大牛动态 ────────────────────────────────────────────────────────────────
updates = [
    InfluencerUpdate(
        'Andrej Karpathy', 'Blog',
        '停止用 AI 写代码，转而将 AI 打造为"第二大脑"。他将原始研究材料投入文件夹，'
        '让 LLM 自动构建并维护相互链接的个人知识 Wiki——AI 负责撰写文章、建立反向链接、持续更新知识图谱。'
        '这一工作流被认为是 "vibe coding" 之后 AI 辅助认知的下一个范式转变。',
        'https://karpathy.github.io/', datetime(2026, 4, 3, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Yann LeCun', 'Blog',
        '与 Sam Altman 展开 AGI 时间线公开讨论。LeCun 认为人类级 AI 仍需"数年乃至十年"，'
        'Altman 的"数千天"与之基本一致，但 LeCun 强调分布有长尾，可能远超预期。'
        '两人在推理时间缩放（inference-time scaling）、Agentic 循环与记忆增强路线上存在共识。',
        'https://x.com/ylecun', datetime(2026, 4, 12, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Sam Altman', 'Blog',
        '博客预测 2026 年关键节点：能发现新洞见的 AI 系统将在今年出现，'
        '2027 年将看到能完成物理世界任务的机器人，软件与艺术创作的门槛将进一步降低。'
        '同时证实 ChatGPT 超级应用正式上线，整合了编码、搜索与 Agent 能力。',
        'https://blog.samaltman.com/', datetime(2026, 4, 10, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Sebastian Raschka', 'Blog',
        '最新通讯深度解析 Gemini 3.1 架构创新与 2026 年 4 月开源模型全景，'
        '详评 Apache 2.0 许可证对商业落地的战略意义，'
        '并梳理 Gemma 4、Phi-4-mini-flash 等近期开源模型的能力边界与适用场景。',
        'https://magazine.sebastianraschka.com/', datetime(2026, 4, 12, tzinfo=timezone.utc),
    ),
]

# ── GitHub 热门 ─────────────────────────────────────────────────────────────
github = [
    GithubProject(
        'OpenClaw/openclaw', 'https://github.com/topics/ai',
        '本地 AI 个人助手，完全运行在用户设备上，作为统一网关连接 WhatsApp、Telegram、Slack 等 50+ 集成，2026 年 GitHub 增速最快开源项目。',
        210000, 18000, 'TypeScript', 2100, ['openclaw-team'],
    ),
    GithubProject(
        'google/ai-edge-gallery', 'https://github.com/topics/ai',
        'Google AI Edge 官方展示库，收录可在手机、平板等终端设备本地运行的 ML 和 GenAI 用例。',
        8400, 620, 'Python', 1850, ['google'],
    ),
    GithubProject(
        'langchain-ai/langgraph', 'https://github.com/topics/ai',
        'LangChain 官方扩展，支持有状态复杂 AI Agent 工作流，是构建可靠生产级多步 Agent 的主流框架。',
        42000, 6800, 'Python', 980, ['langchain-ai'],
    ),
    GithubProject(
        'infiniflow/ragflow', 'https://github.com/topics/ai',
        '领先开源 RAG 引擎，将深度文档理解与 Agent 能力融合，提供卓越的上下文检索层。',
        38500, 3900, 'Python', 760, ['infiniflow'],
    ),
    GithubProject(
        'caramaschiHG/awesome-ai-agents-2026', 'https://github.com/caramaschiHG/awesome-ai-agents-2026',
        '2026 年最全面的 AI Agent 框架与工具精选列表，覆盖 300+ 资源、20+ 分类，每月更新。',
        14200, 980, '', 640, ['caramaschiHG'],
    ),
    GithubProject(
        'n8n-io/n8n', 'https://github.com/topics/ai',
        '可自托管的可视化工作流自动化平台，拖拽式设计 AI Agent 管道，降低非 ML 工程师构建 AI 应用门槛。',
        61000, 15200, 'TypeScript', 520, ['n8n-io'],
    ),
]


def main():
    parser = argparse.ArgumentParser(description='发布 2026-04-12 AI 日报')
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
            print('  python generate_post_2026_04_12.py --publish')


if __name__ == '__main__':
    main()
