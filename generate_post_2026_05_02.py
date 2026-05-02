"""
发布 2026-05-02 AI 日报到博客

用法：
  # 仅生成 Jekyll 文章到 reports/ 目录
  python generate_post_2026_05_02.py

  # 生成并发布到博客（需要设置 BLOG_DEPLOY_TOKEN 环境变量）
  BLOG_DEPLOY_TOKEN=your_token python generate_post_2026_05_02.py --publish
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
        '将 AI 部署到 IL6/IL7 级最高机密网络（用于任务规划、情报分析、武器瞄准）。'
        'Anthropic 因坚持要求军方遵守安全护栏（禁止完全自主武器）被特朗普政府认定为"供应链风险"，'
        '联邦法院维持五角大楼禁令，Dario Amodei 随后赴白宫就 Mythos 工具展开磋商。',
    ),
    NewsItem(
        'Anthropic 发布 Claude Opus 4.7：编码提升 13%，引入 xhigh 推理档位',
        'https://www.anthropic.com/news/claude-opus-4-7',
        'Anthropic', 'industry', datetime(2026, 4, 16, tzinfo=timezone.utc),
        'Claude Opus 4.7（4 月 16 日 GA）在 93 个编码任务基准上比 Opus 4.6 提升 13%，'
        '包含 4 项前代无法解决的任务；视觉分辨率大幅提升；新增 xhigh 推理档位（介于 high 与 max 之间）；'
        '引入 task budgets 让开发者精细控制推理时间分配。定价与 Opus 4.6 持平：$5/$25 per M tokens。'
        '网络安全高风险请求自动拦截。支持 API、Bedrock、Vertex AI、Microsoft Foundry 全平台。',
    ),
    NewsItem(
        'GPT-5.5 vs Claude Opus 4.7 vs Gemini 3.1 Pro：三大前沿模型完整横评',
        'https://medium.com/@cognidownunder/openai-gpt-5-5-b6cf7e37668e',
        'Medium / Cogni Down Under', 'industry', datetime(2026, 4, 30, tzinfo=timezone.utc),
        'GPT-5.5（4 月 23 日发布）是 OpenAI 自 GPT-4.5 后首次完整重训基模型，'
        '擅长 Agentic 工作流与多步骤研究；Claude Opus 4.7 领跑精密编码；'
        'Gemini 3.1 Pro 凭借 2M 上下文与多模态成本优势胜出。'
        'DeepSeek V4 Pro 以约 1/7 的价格逼近同等水平，被 Simon Willison 评为"几乎已在前沿"。',
    ),
    NewsItem(
        'Google 宣布向 Anthropic 追加投资至多 400 亿美元，估值 3500 亿美元',
        'https://techcrunch.com/2026/04/24/google-to-invest-up-to-40b-in-anthropic-in-cash-and-compute/',
        'TechCrunch', 'industry', datetime(2026, 4, 24, tzinfo=timezone.utc),
        'Google 计划向 Anthropic 先期投入 100 亿美元（估值 3500 亿），'
        '并约定若 Anthropic 达到特定绩效目标再追加 300 亿，总计最高 400 亿美元。'
        '这与 Amazon 此前宣布的最高 250 亿累计投资形成双轨支持，'
        'Anthropic 现为科技史上融资规模最大的 AI 安全公司。',
    ),
    NewsItem(
        'ICLR 2026 杰出论文公布：MemAgent 实现 8K→350 万 token 上下文外推',
        'https://blog.iclr.cc/2026/04/23/announcing-the-iclr-2026-outstanding-papers/',
        'ICLR Blog', 'research', datetime(2026, 4, 23, tzinfo=timezone.utc),
        'ICLR 2026 共接收超 5300 篇论文，杰出论文包括：'
        '《Transformers are Inherently Succinct》（理论解析 Transformer 比 RNN 更简洁地编码概念）；'
        '《MemAgent》（在 8K 上下文训练后外推至 350 万 token QA，性能损失 <10%）；'
        '《SAM 3》（将 SAM 扩展为可概念提示分割）；《Mamba-3》（亚二次方推理，媲美 Transformer 精度）。',
    ),
    NewsItem(
        'Stanford HAI 发布 2026 AI Index 报告：模型性能超越人类专家，治理滞后',
        'https://hai.stanford.edu/ai-index/2026-ai-index-report',
        'Stanford HAI', 'research', datetime(2026, 4, 25, tzinfo=timezone.utc),
        '斯坦福年度 AI 指数显示：前沿模型已在 PhD 级科学/数学/语言理解基准上超越人类专家；'
        '软件工程基准分数从 2024 年约 60% 跃升至 2025 年接近 100%；'
        '量子计算与物理 AI（机器人）成为 2026 年两大突破性趋势；'
        '同时指出 AI 收益分配不均、治理框架严重滞后于技术发展速度。',
    ),
    NewsItem(
        'Microsoft Agent Framework 正式发布：统一 Python/.NET 多 Agent 编排',
        'https://github.com/microsoft/agent-framework',
        'Microsoft Research', 'tools', datetime(2026, 4, 30, tzinfo=timezone.utc),
        'Microsoft 开源 Agent Framework，支持 Python 与 .NET 双语言，'
        '提供图式工作流、流式输出、检查点（checkpointing）与人在环路（human-in-the-loop）机制，'
        '内置对 OpenAI、Claude、Gemini、DeepSeek 多 LLM 后端的支持，'
        '可与 LangGraph、AutoGen 生态互操作。',
    ),
    NewsItem(
        'Zhipu AI 发布 GLM-5.1：华为昇腾训练，幻觉率仅 1.2%',
        'https://llm-stats.com/ai-news',
        'LLM Stats', 'industry', datetime(2026, 5, 1, tzinfo=timezone.utc),
        'Zhipu AI（智谱 AI）发布 GLM-5.1，完全基于华为昇腾芯片集群训练，'
        '在 TruthfulQA 幻觉评测中仅 1.2%，超越多数闭源模型；'
        '可自托管，硬件门槛适中，成为 2026 年国产开放权重前沿模型的代表性样本。',
    ),
    NewsItem(
        'OpenHands 发布 Software Agent SDK：模块化 Python/REST API 构建编码 Agent',
        'https://openhands.dev/',
        'OpenHands', 'tools', datetime(2026, 5, 1, tzinfo=timezone.utc),
        'OpenHands 推出 Software Agent SDK，提供干净、模块化的 Python 与 REST API，'
        '内置代码执行、文件编辑、浏览器操控与 shell 工具；'
        '支持插拔式 LLM 后端（Claude、GPT-5.5、DeepSeek V4），'
        '是构建复杂多步骤软件开发 Agent 的轻量级基础框架。',
    ),
]

# ── 论文 ────────────────────────────────────────────────────────────────────
papers = [
    Paper(
        'Transformers are Inherently Succinct',
        'https://iclr.cc/virtual/2026/papers.html',
        '2604.TransformersSuccinct',
        ['Pascal Bergsträßer', 'Ryan Cotterell', 'Anthony Widjaja Lin'],
        '🏆 ICLR 2026 杰出论文。通过形式语言理论证明 Transformer 能比 RNN 更简洁地编码特定概念类，'
        '提供了 Transformer 架构能力优势的全新理论视角，而非仅依赖实验结论。',
        ['cs.LG', 'cs.FL'], datetime(2026, 4, 23, tzinfo=timezone.utc),
        'https://iclr.cc/virtual/2026/papers.html',
    ),
    Paper(
        'MemAgent: Superb Long-Context LLM via SFT on Memory-Augmented Agent Tasks',
        'https://iclr.cc/virtual/2026/papers.html',
        '2604.MemAgent',
        ['MemAgent Team'],
        '🏆 ICLR 2026 杰出论文。在 8K 上下文上训练后，MemAgent 可外推至 350 万 token 的长文档 QA，'
        '性能损失 <10%。通过将长文档处理建模为记忆增强 Agent 任务（SFT）实现显著的上下文泛化。',
        ['cs.CL', 'cs.AI'], datetime(2026, 4, 23, tzinfo=timezone.utc),
        'https://iclr.cc/virtual/2026/papers.html',
    ),
    Paper(
        'A-RAG: Scaling Agentic Retrieval-Augmented Generation via Hierarchical Retrieval Interfaces',
        'https://arxiv.org/abs/2602.03442',
        '2602.03442',
        ['A-RAG Team'],
        '提出分层检索接口（关键词搜索 / 语义搜索 / 块读取），让 Agent 自适应地跨粒度检索信息，'
        '在 multi-hop QA 基准上达到 SOTA，是 Agentic RAG 的可扩展新范式。',
        ['cs.IR', 'cs.AI'], datetime(2026, 4, 20, tzinfo=timezone.utc),
        'https://arxiv.org/html/2602.03442v1',
    ),
    Paper(
        'From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review',
        'https://arxiv.org/abs/2504.19678',
        '2504.19678',
        ['Research Team'],
        '2026 年最全面的 LLM Agent 综述：覆盖推理范式演进（CoT → MCTS → Agentic Reasoning）、'
        '工具使用、记忆架构、多 Agent 协作与安全性，整理 200+ 篇文献，提出评估框架与未来研究路线图。',
        ['cs.AI', 'cs.CL'], datetime(2026, 4, 25, tzinfo=timezone.utc),
        'https://arxiv.org/abs/2504.19678',
    ),
    Paper(
        'In-The-Flow Agentic System Optimization (AgentFlow)',
        'https://iclr.cc/virtual/2026/papers.html',
        '2604.AgentFlow',
        ['AgentFlow Team'],
        'ICLR 2026 入选论文。AgentFlow 是可训练的 Agentic 系统：多 Agent 小组在任务流中学习规划与工具调用，'
        '无需人工设计固定工作流，在 WebArena、GAIA 等基准上超越静态 Agent 框架。',
        ['cs.AI', 'cs.LG'], datetime(2026, 4, 23, tzinfo=timezone.utc),
        'https://iclr.cc/virtual/2026/papers.html',
    ),
    Paper(
        'SAM 3: Segment Anything with Concepts',
        'https://iclr.cc/virtual/2026/papers.html',
        '2604.SAM3',
        ['SAM 3 Team'],
        'ICLR 2026 入选论文。将 SAM 1/2 扩展为"可提示概念分割（PCS）"——从文本描述或示例图像'
        '分割目标概念的所有实例，无需类别预设，适用于开放词汇零样本场景。',
        ['cs.CV', 'cs.AI'], datetime(2026, 4, 23, tzinfo=timezone.utc),
        'https://iclr.cc/virtual/2026/papers.html',
    ),
]

# ── 大牛动态 ─────────────────────────────────────────────────────────────────
updates = [
    InfluencerUpdate(
        'Simon Willison', 'Blog',
        '就五角大楼排除 Anthropic 发表深度分析：逐条解析美国国防部"供应链风险"认定的法律与技术依据，'
        '指出这是 AI 安全原则与军事自主武器政策之间首次进入司法层面的公开冲突；'
        '同期发布 DeepSeek V4 后续测评，验证 V4 Pro 在 1M 上下文长文档处理上的实际表现。',
        'https://simonwillison.net/',
        datetime(2026, 5, 1, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Andrej Karpathy', 'X / Blog',
        '赞扬 Simon Willison 坚持 23 年高质量博客写作，并通过 RSS 持续订阅；'
        '分享"autoresearch"系统最新进展：让 Agent 全自动运行数百次实验寻找新技术，'
        '已在 microgpt（200 行纯 Python GPT 训练/推理）基础上发现 3 项效率优化；'
        '同时推进"Claws"愿景：将 AI 从代码助手升级为可自主管理整个软件系统的协作者。',
        'https://karpathy.ai/',
        datetime(2026, 5, 1, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Sebastian Raschka', 'Newsletter (Ahead of AI)',
        '发布《ICLR 2026 精选论文》：深度解读 MemAgent 的记忆增强训练机制、'
        'AgentFlow 的可训练多 Agent 框架设计，以及 Mamba-3 对 Transformer 推理效率壁垒的突破；'
        '同期整理 GPT-5.5 发布以来各大基准评分变化，对比开源 vs 闭源模型差距缩小趋势。',
        'https://magazine.sebastianraschka.com/',
        datetime(2026, 5, 1, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Chip Huyen', 'Blog',
        '新文《AI Agent 可靠性工程：从实验室到生产的 10 个关键教训》：'
        '聚焦企业 Agentic 系统在长任务中的失败模式——幻觉工具调用、中间状态累积错误、'
        '无限重试循环；提出基于可观察性（observability）与失败模式库的系统性调试方法，'
        '配合 OpenHands SDK 和 LangGraph 的实际案例。',
        'https://huyenchip.com/',
        datetime(2026, 5, 1, tzinfo=timezone.utc),
    ),
]

# ── GitHub 热门 ──────────────────────────────────────────────────────────────
github = [
    GithubProject(
        'OpenClaw/openclaw',
        'https://github.com/OpenClaw/openclaw',
        'Personal AI assistant running entirely on your devices — local gateway to 50+ integrations (WhatsApp, Slack, Telegram, Discord, Signal, iMessage)',
        215000, 19400, 'TypeScript', 2100, ['openclaw-core'],
    ),
    GithubProject(
        'open-webui/open-webui',
        'https://github.com/open-webui/open-webui',
        'Self-hosted AI platform (offline-first, 282M+ downloads) — ChatGPT-style UI for Ollama and any OpenAI-compatible API',
        125000, 14800, 'Svelte', 1750, ['tjbck', 'ochen27'],
    ),
    GithubProject(
        'infiniflow/ragflow',
        'https://github.com/infiniflow/ragflow',
        'RAGFlow: open-source RAG engine based on deep document understanding — grounded, traceable AI answers for enterprise knowledge bases',
        71000, 7200, 'Python', 1530, ['kevin-yd', 'liuchanghe'],
    ),
    GithubProject(
        'langchain-ai/langgraph',
        'https://github.com/langchain-ai/langgraph',
        'LangGraph: enterprise multi-agent framework — graph-based stateful workflows, streaming, checkpointing, human-in-the-loop',
        128000, 21000, 'Python', 1240, ['hinthornw', 'efriis'],
    ),
    GithubProject(
        'VoltAgent/voltagent',
        'https://github.com/VoltAgent/voltagent',
        'Open-source TypeScript AI agent engineering platform — memory, tools, multi-step workflows, multi-LLM provider support',
        22000, 1800, 'TypeScript', 1050, ['VoltAgent'],
    ),
    GithubProject(
        'microsoft/agent-framework',
        'https://github.com/microsoft/agent-framework',
        'Microsoft Agent Framework — build, orchestrate and deploy AI agents with Python and .NET; graph workflows, streaming, checkpointing',
        18500, 1420, 'Python', 920, ['microsoft-devs'],
    ),
    GithubProject(
        'ggml-org/llama.cpp',
        'https://github.com/ggml-org/llama.cpp',
        'LLM inference in C/C++ — DeepSeek V4 Pro/Flash support, Vulkan flash attention, Qwen3 audio ASR',
        89500, 13100, 'C++', 850, ['ggerganov', 'slaren'],
    ),
    GithubProject(
        'OpenHands/software-agent-sdk',
        'https://github.com/OpenHands/software-agent-sdk',
        'Clean, modular Python/REST SDK for building AI software agents — code exec, file editing, browser control, shell tools',
        14200, 1100, 'Python', 780, ['OpenHands'],
    ),
]


# ── 主逻辑 ───────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description='生成并可选发布 2026-05-02 AI 日报')
    parser.add_argument('--publish', action='store_true', help='发布到博客（需 BLOG_DEPLOY_TOKEN）')
    args = parser.parse_args()

    filename, content = generate_jekyll_post(news, papers, updates, github)

    # 强制使用今日日期文件名
    filename = '2026-05-02-ai-daily-news.md'
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
