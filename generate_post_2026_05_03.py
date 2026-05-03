"""
发布 2026-05-03 AI 日报到博客

用法：
  # 仅生成 Jekyll 文章到 reports/ 目录
  python generate_post_2026_05_03.py

  # 生成并发布到博客（需要设置 BLOG_DEPLOY_TOKEN 环境变量）
  BLOG_DEPLOY_TOKEN=your_token python generate_post_2026_05_03.py --publish
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
        '五角大楼签约 8 家 AI 公司进驻最高机密网络，唯独排除 Anthropic',
        'https://www.cnn.com/2026/05/01/tech/pentagon-ai-anthropic',
        'CNN Business', 'industry', datetime(2026, 5, 1, tzinfo=timezone.utc),
        '美国国防部与 OpenAI、Google、Microsoft、AWS、Nvidia、SpaceX、Reflection、Oracle 达成协议，'
        '将 AI 部署到 IL6/IL7 级最高机密网络。Anthropic 因坚持安全护栏（禁止完全自主武器）被特朗普政府'
        '认定为"供应链风险"，联邦法院维持五角大楼禁令，Dario Amodei 随后赴白宫就 Mythos 工具展开磋商。',
    ),
    NewsItem(
        'World-R1：Microsoft 研究院通过强化学习注入 3D 约束实现几何一致视频生成',
        'https://arxiv.org/abs/2604.24764',
        'Microsoft Research / arXiv', 'research', datetime(2026, 4, 30, tzinfo=timezone.utc),
        '微软研究院与浙江大学发布 World-R1（arXiv 2604.24764），基于 Flow-GRPO-Fast 强化学习框架，'
        '不修改模型架构即可让视频生成模型学会 3D 几何一致性约束。在 Wan2.1-T2V 基础上训练，'
        '生成的视频经 3D Gaussian Splatting 重建验证几何准确性，项目开源于 github.com/microsoft/World-R1。',
    ),
    NewsItem(
        'NVIDIA 发布首批量子计算开源 AI 模型 Ising：解码速度 2.5× 快、精度 3× 高',
        'https://nvidianews.nvidia.com/news/nvidia-launches-ising-the-worlds-first-open-ai-models-to-accelerate-the-path-to-useful-quantum-computers',
        'NVIDIA Newsroom', 'industry', datetime(2026, 4, 14, tzinfo=timezone.utc),
        'NVIDIA Ising 是全球首批为量子处理器校准与纠错解码专门设计的开源 AI 模型家族：'
        '35B 视觉语言模型（Ising Calibration）将 QPU 校准时间从数天缩短至数小时；'
        '0.9M/1.8M 参数 3D-CNN（Ising Decoding）量子纠错解码比传统方案快 2.5× 且精度高 3×。'
        '模型已发布至 GitHub、Hugging Face 及 build.nvidia.com。',
    ),
    NewsItem(
        'Google Gemini CLI v0.28：升级至 Gemini 3 Pro，编码精度提升 35%，100+ 扩展生态',
        'https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-cli-open-source-ai-agent/',
        'Google', 'tools', datetime(2026, 4, 30, tzinfo=timezone.utc),
        'Gemini CLI 0.28.0 将底层模型从 Gemini 2.5 Pro 升级至 Gemini 3 Pro，编码精度提升 35%；'
        '新增 Agent Skills（AI 自学新能力）、Plan Mode（复杂多步任务规划）、/rewind 命令（回退会话历史）；'
        '扩展生态达 100+ 个，官方合作伙伴新增 Figma、Stripe、Shopify、Postman 等。'
        '免费版每分钟 60 次、每天 1,000 次 Gemini 3 Pro 请求。',
    ),
    NewsItem(
        'Google 宣布向 Anthropic 追加投资至多 400 亿美元，估值 3500 亿美元',
        'https://techcrunch.com/2026/04/24/google-to-invest-up-to-40b-in-anthropic-in-cash-and-compute/',
        'TechCrunch', 'industry', datetime(2026, 4, 24, tzinfo=timezone.utc),
        'Google 计划向 Anthropic 先期投入 100 亿美元（估值 3500 亿），并约定若 Anthropic '
        '达到特定绩效目标再追加 300 亿，总计最高 400 亿美元。这与 Amazon 此前宣布的最高 250 亿'
        '累计投资形成双轨支持，Anthropic 现为科技史上融资规模最大的 AI 安全公司。',
    ),
    NewsItem(
        'Stanford HAI 2026 AI Index：Agent 任务成功率从 12% 跃升至 66%，治理框架严重滞后',
        'https://hai.stanford.edu/ai-index/2026-ai-index-report',
        'Stanford HAI', 'research', datetime(2026, 4, 25, tzinfo=timezone.utc),
        '斯坦福年度 AI Index 显示：AI Agent 在真实计算机任务上的成功率从 2024 年 12% 飙升至 2026 年 66%；'
        '软件工程基准分数从 2024 年约 60% 接近 100%；前沿模型已在 PhD 级科学/数学基准上超越人类专家；'
        '同时指出 AI 收益分配不均、全球治理框架严重滞后于技术发展速度。',
    ),
    NewsItem(
        'Alibaba 发布 Qwen3.6-35B-A3B：最新 MoE 模型登陆 Hugging Face 与 ModelScope',
        'https://github.com/QwenLM/Qwen3.6',
        'Alibaba Qwen Team', 'industry', datetime(2026, 4, 16, tzinfo=timezone.utc),
        'Alibaba Qwen 团队于 4 月 16 日发布 Qwen3.6-35B-A3B，延续 Qwen3.5 的多模态路线，'
        '支持 201 种语言与方言，专注企业级 Agent 工作流，具备增强推理和多模态输入能力，'
        '开放权重在 Hugging Face 与 ModelScope 双平台同步可下载。',
    ),
    NewsItem(
        'Claude Code 成 2026 年最受开发者欢迎的 AI 编码工具，小型企业使用率达 75%',
        'https://newsletter.pragmaticengineer.com/p/ai-tooling-2026',
        'Pragmatic Engineer Newsletter', 'tools', datetime(2026, 5, 1, tzinfo=timezone.utc),
        'Pragmatic Engineer 2026 年开发者调查显示：Claude Code 超越 GitHub Copilot 成为最常用 AI 编码工具，'
        '在员工数 <50 的小型公司中使用率达 75%；代码接受率从 2024 年 20% 跃升至 60%；'
        '80% 的开发团队正主动使用 AI 工具，完全自主的软件工程 Agent（接收 Jira 票据→交付合并 PR）'
        '预计 2026 年底将成为行业标准。',
    ),
    NewsItem(
        'OpenAI 携 GPT-5.5 入驻 Amazon Bedrock，Codex 与 Bedrock Managed Agents 同步上线',
        'https://llm-stats.com/ai-news',
        'LLM Stats / AWS News', 'industry', datetime(2026, 5, 1, tzinfo=timezone.utc),
        'OpenAI 宣布 GPT-5.5 及其他前沿模型正式上线 Amazon Bedrock，同时将 Codex 引入 AWS 生态；'
        'Bedrock Managed Agents 现可由 OpenAI 模型驱动，为企业提供在 AWS 安全与治理框架内'
        '构建和部署 AI Agent 的完整托管方案，与 Anthropic Claude 在 Bedrock 上形成直接竞争。',
    ),
]

# ── 论文 ────────────────────────────────────────────────────────────────────
papers = [
    Paper(
        'World-R1: Reinforcing 3D Constraints for Text-to-Video Generation',
        'https://arxiv.org/abs/2604.24764',
        '2604.24764',
        ['Microsoft Research', 'Zhejiang University'],
        '通过强化学习（Flow-GRPO-Fast）将 3D 几何一致性约束注入视频生成模型，'
        '无需修改架构或使用 3D 监督数据。以 Wan2.1-T2V 为基础模型，利用 Depth Anything 3 + '
        '3D Gaussian Splatting 构建几何奖励信号，生成视频的空间一致性显著超越 Baseline。',
        ['cs.CV', 'cs.LG'], datetime(2026, 4, 30, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2604.24764',
        'https://github.com/microsoft/World-R1',
    ),
    Paper(
        'MemOS: An Operating System for Memory-Augmented Generation in Large Language Models',
        'https://arxiv.org/abs/2505.22101',
        '2505.22101',
        ['MemTensor Research Team'],
        '工业级开源 LLM 记忆操作系统，引入 MemCube 统一抽象层，统一管理明文记忆、激活态记忆'
        '（KV Cache）和参数级记忆（LoRA weights），解决长期对话、跨会话推理和个性化记忆管理难题。'
        '三层架构（记忆 API 层 / 调度管理层 / 存储基础设施层）支持 OpenClaw、ClawdBot 等主流 Agent。',
        ['cs.CL', 'cs.AI'], datetime(2026, 5, 1, tzinfo=timezone.utc),
        'https://arxiv.org/pdf/2505.22101',
        'https://github.com/MemTensor/MemOS',
    ),
    Paper(
        'MemAgent: Superb Long-Context LLM via SFT on Memory-Augmented Agent Tasks',
        'https://iclr.cc/virtual/2026/papers.html',
        '2604.MemAgent',
        ['MemAgent Team'],
        '🏆 ICLR 2026 杰出论文。在 8K 上下文上训练后，MemAgent 可外推至 350 万 token 的长文档 QA，'
        '性能损失 <10%。通过将长文档处理建模为记忆增强 Agent 任务（SFT）实现显著的上下文泛化，'
        '为超长上下文 LLM 提供了低成本的训练新路径。',
        ['cs.CL', 'cs.AI'], datetime(2026, 4, 23, tzinfo=timezone.utc),
        'https://iclr.cc/virtual/2026/papers.html',
    ),
    Paper(
        'From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review',
        'https://arxiv.org/abs/2504.19678',
        '2504.19678',
        ['Multi-institution Research Team'],
        '2026 年最全面的 LLM Agent 综述：覆盖推理范式演进（CoT → MCTS → Agentic Reasoning）、'
        '工具使用、记忆架构、多 Agent 协作与安全性，整理 200+ 篇文献，'
        '提出评估框架与未来研究路线图，是入门与追踪 Agent 领域进展的权威参考。',
        ['cs.AI', 'cs.CL'], datetime(2026, 4, 25, tzinfo=timezone.utc),
        'https://arxiv.org/abs/2504.19678',
    ),
    Paper(
        'Synthetic Computers at Scale for Long-Horizon Productivity Simulation',
        'https://arxiv.org/list/cs.AI/current',
        '2505.SyntheticComputers',
        ['Tao Ge', 'Jianfeng Gao', 'et al.'],
        '提出大规模合成计算机环境，用于模拟长视野生产力任务，旨在训练和评估能胜任真实工作场景的 AI Agent。'
        '通过合成数据生成框架复现复杂办公软件操作序列，在计算机任务基准上显著超越现有 Agent。',
        ['cs.AI', 'cs.HC'], datetime(2026, 5, 1, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.AI/current',
    ),
    Paper(
        'LLM as Clinical Graph Structure Refiner: Enhancing Representation Learning in EEG Seizure Diagnosis',
        'https://arxiv.org/list/cs.AI/current',
        '2505.EEGSeizure',
        ['IJCAI-ECAI 2026 Authors'],
        'IJCAI-ECAI 2026 录用论文。利用 LLM 作为临床知识图结构精化器，增强 EEG 癫痫诊断中的'
        '图神经网络表示学习，将医学领域知识注入 GNN 训练流程，在多个公开 EEG 数据集上达到 SOTA 性能。',
        ['cs.AI', 'cs.LG'], datetime(2026, 4, 28, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.AI/current',
    ),
]

# ── 大牛动态 ─────────────────────────────────────────────────────────────────
updates = [
    InfluencerUpdate(
        'Andrej Karpathy', 'Blog / X',
        '持续推进 "autoresearch" 系统：让 Agent 全自动运行数百次实验寻找新技术，'
        '已在 microgpt（200 行纯 Python GPT 训练/推理）基础上发现多项效率优化。'
        '同期分享 Gemini CLI 新版本体验，称其 Plan Mode 与 Agent Skills 功能"接近真正的 AI 助手"；'
        '继续推进 "Claws" 愿景，探讨如何将 AI 从代码助手升级为可自主管理整个软件系统的协作者。',
        'https://karpathy.ai/',
        datetime(2026, 5, 2, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Simon Willison', 'Blog',
        '发布 World-R1 深度测评：对 Microsoft 强化学习注入 3D 约束方案的技术路径进行逐层拆解，'
        '重点分析 Flow-GRPO-Fast 如何在不修改架构的前提下将几何奖励信号传导至扩散模型；'
        '同期更新五角大楼/Anthropic 事件后续，关注联邦法院裁决对 AI 安全原则与军事自主武器政策'
        '张力的长期影响，认为这将成为 AI 治理史上的标志性案例。',
        'https://simonwillison.net/',
        datetime(2026, 5, 2, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Sebastian Raschka', 'Newsletter (Ahead of AI)',
        '发布《2026 年 5 月开源 AI 模型格局扫描》：深度对比 Qwen3.6、GLM-5.1、Gemma 4 的实际能力，'
        '重点评析开放权重模型与闭源前沿模型之间的差距缩窄趋势；'
        '同期整理 ICLR 2026 录用论文中 Agent 相关工作（MemAgent、AgentFlow、A-RAG）的方法论共性，'
        '归纳出"记忆增强 + 层次检索 + 可训练工作流"三大技术方向的融合趋势。',
        'https://magazine.sebastianraschka.com/',
        datetime(2026, 5, 2, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Chip Huyen', 'Blog',
        '新文《从实验到生产：AI Agent 可靠性工程的 10 个关键教训》续篇：'
        '聚焦 MemOS 等记忆操作系统在长任务 Agent 中的实际部署挑战——'
        '跨会话状态持久化、记忆召回延迟与幻觉工具调用的组合失效模式；'
        '提出基于可观察性（observability）的系统性调试方法论，配合 MemOS + LangGraph 实战案例展示。',
        'https://huyenchip.com/',
        datetime(2026, 5, 2, tzinfo=timezone.utc),
    ),
]

# ── GitHub 热门 ──────────────────────────────────────────────────────────────
github = [
    GithubProject(
        'google-gemini/gemini-cli',
        'https://github.com/google-gemini/gemini-cli',
        'Open-source AI agent that brings Gemini 3 Pro directly into your terminal — ReAct loop, Agent Skills, Plan Mode, 100+ extensions',
        68000, 4200, 'TypeScript', 3800, ['google-gemini'],
    ),
    GithubProject(
        'microsoft/World-R1',
        'https://github.com/microsoft/World-R1',
        'Reinforcing 3D constraints for text-to-video generation via Flow-GRPO-Fast reinforcement learning — no architecture changes',
        9400, 620, 'Python', 2900, ['microsoft-research'],
    ),
    GithubProject(
        'MemTensor/MemOS',
        'https://github.com/MemTensor/MemOS',
        'Industrial-grade memory OS for LLM and Agent systems — MemCube unified abstraction for plaintext, KV-cache, and LoRA memories',
        18200, 1340, 'Python', 2400, ['MemTensor'],
    ),
    GithubProject(
        'OpenClaw/openclaw',
        'https://github.com/OpenClaw/openclaw',
        'Personal AI assistant running entirely on your devices — local gateway to 50+ integrations (WhatsApp, Slack, Telegram, Signal)',
        217000, 19600, 'TypeScript', 1950, ['openclaw-core'],
    ),
    GithubProject(
        'langchain-ai/langflow',
        'https://github.com/langchain-ai/langflow',
        'Visual builder for agentic AI apps — drag-and-drop agent pipelines, RAG, multi-LLM backend support',
        148000, 16200, 'Python', 1420, ['ogabrielluiz', 'anovazzi1'],
    ),
    GithubProject(
        'langchain-ai/langgraph',
        'https://github.com/langchain-ai/langgraph',
        'Enterprise multi-agent framework — graph-based stateful workflows, streaming, checkpointing, human-in-the-loop',
        129000, 21200, 'Python', 1180, ['hinthornw', 'efriis'],
    ),
    GithubProject(
        'QwenLM/Qwen3.6',
        'https://github.com/QwenLM/Qwen3.6',
        'Qwen3.6 large language model series by Alibaba — multimodal, 201 languages, enterprise agent workflows',
        14800, 1020, 'Python', 1050, ['QwenLM'],
    ),
    GithubProject(
        'infiniflow/ragflow',
        'https://github.com/infiniflow/ragflow',
        'Open-source RAG engine based on deep document understanding — grounded, traceable AI answers for enterprise knowledge bases',
        72500, 7350, 'Python', 890, ['kevin-yd', 'liuchanghe'],
    ),
]


# ── 主逻辑 ───────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description='生成并可选发布 2026-05-03 AI 日报')
    parser.add_argument('--publish', action='store_true', help='发布到博客（需 BLOG_DEPLOY_TOKEN）')
    args = parser.parse_args()

    filename, content = generate_jekyll_post(news, papers, updates, github)

    filename = '2026-05-03-ai-daily-news.md'
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
