---
layout: post
title: "AI 日报 · 2026年06月27日"
date: 2026-06-27 00:00:00 +0000
categories:
  - "AI日报"
tags:
  - "AI日报"
  - "人工智能"
  - "每日新闻"
  - "LLM"
  - "AI Agent"
  - "OpenAI"
  - "Anthropic"
  - "Apple"
description: "今日 AI 速报：6 条资讯 · 5 篇论文 · 4 条大牛动态 · 6 个热门项目。OpenAI GPT-4.5 今日正式退役；SpaceX 600 亿美元收购 Cursor；Apple WWDC 开放 Claude/Gemini 替换 Siri"
toc: true
---

> **今日 AI 速报：6 条资讯 · 5 篇论文 · 4 条大牛动态 · 6 个热门项目**
> 数据来源：Web Search · arXiv · GitHub Trending
> 生成时间：2026-06-27 00:00 UTC

---

## 📰 今日 AI 资讯

### 🏭 产业动态

- **[OpenAI GPT-4.5 今日正式退役，API 用户须迁移至 GPT-5 系列](https://witho2.com/news/openai-gpt-4-5-retirement-june-2026-migration-guide)**
  `TechRadar / OpenAI Help Center` · 06-27
  OpenAI GPT-4.5 于今日（6 月 27 日）正式下线，结束 30 天过渡期。该模型 2 月推出时被定位为"最具知识广度的旗舰模型"，却在短短四个月内被 GPT-5、GPT-5.3-Codex 及 GPT-5.5 Instant 全面取代，创下 OpenAI 最短在役纪录。API 开发者须立即迁移至 GPT-5 或 GPT-5.3-Codex；ChatGPT 默认模型自 5 月起已切换为 GPT-5.5 Instant，o3 将于 8 月 26 日再行退役。这标志着 GPT-4 时代的彻底落幕。

- **[SpaceX 以 600 亿美元全股票方案收购 AI 编程工具 Cursor](https://techcrunch.com/2026/06/16/spacex-to-acquire-cursor-for-60b-in-stock-days-after-blockbuster-ipo/)**
  `TechCrunch / CNBC` · 06-16
  SpaceX IPO 挂牌纳斯达克（历史最大 IPO）数日后，随即宣布以 600 亿美元股票收购 AI 编程助手 Cursor，占 SpaceX IPO 估值约 3.4%，预计今年第三季度完成交割。Cursor 成立于 2022 年，年化收入已突破 10 亿美元，为开发者提供代码生成、编辑与审查能力。本次收购将并入 SpaceX 与 xAI 合并后的 AI 业务部门，旨在追赶 OpenAI Codex 与 Anthropic Claude Code 在编程工具市场的领先地位。

- **[Apple WWDC 2026：iOS 27 Extensions 框架开放 Claude、Gemini、ChatGPT 替换 Siri](https://aiweekly.co/node/2611)**
  `AI Weekly / 9to5Mac / Tom's Guide` · 06-08
  苹果在 WWDC 2026 主题演讲（6 月 8 日）发布 iOS 27 Extensions 智能扩展框架，允许用户在系统设置中将 Siri 背后的 AI 引擎切换为 Claude（Anthropic）、ChatGPT（OpenAI）、Google Gemini 或 Grok，覆盖 Siri 对话、写作工具和 Image Playground 全部场景。Gemini 为默认选项，Claude 首次正式成为 iPhone 原生 AI 选项。开发者 Beta 已于发布当日提供，公开 Beta 预计 7 月发布，正式版随 iOS 27 于秋季推出。

- **[GitHub Copilot 全面转向 AI Credits 计费，行内补全继续免费](https://www.ghacks.net/2026/06/03/openai-upgrades-gpt-5-5-instant-and-confirms-retirement-of-o3-and-gpt-4-5-models/)**
  `gHacks / Microsoft` · 06-03
  GitHub Copilot 全面启用基于 token 的 AI Credits 计费体系：1 个 Credits = $0.01，适用于所有付费套餐。内联代码补全保持免费不变；Agent 会话、高级代码审查及使用 Claude/GPT-5 的 Copilot Chat 将按 Credits 计量扣费。此举使开发者可自由组合多种 AI 模型，但重度 Agent 用户的月账单将有明显上升，被业内视为 AI 工具订阅向"用量付费"转型的重要信号。

### 🌐 AI 治理

- **[Amodei、Hassabis 联合呼吁建立美国主导的国际 AI 治理联盟](https://fortune.com/2026/01/23/deepmind-demis-hassabis-anthropic-dario-amodei-yann-lecun-ai-davos/)**
  `Fortune / Reuters` · 06-17
  在 6 月 17 日的闭门峰会上，Anthropic CEO Dario Amodei 与 Google DeepMind CEO Demis Hassabis 联合发出呼声，主张由美国牵头建立类似 IAEA 的国际 AI 治理机构，负责协调跨国 AI 安全标准、共享高风险模型评估结果，并对超大规模训练运行实施登记监督。这是两大前沿实验室首次在正式场合共同就多边治理框架表态，引发欧盟委员会和多国政府的积极回应。

### 🔬 研究前沿

- **[Yann LeCun 炮轰 xAI"基本算是失败"，11 位联合创始人全部出走](https://lumicharts.com/blog/agi-timeline-2026-expert-predictions-what-it-means)**
  `CNBC / Fortune` · 06-18
  Meta 首席 AI 科学家 Yann LeCun 接受 CNBC 采访时直言 Elon Musk 的 xAI"坦率地说基本算是失败"，理由是 xAI 最初 11 位非 Musk 联合创始人已全部离职，认为这说明组织文化和技术路线存在根本性问题。LeCun 同时重申自己对"LLM 无法通向 AGI"的一贯立场，并预测 2026—2027 年将看到基于世界模型（World Model）的新架构在实体智能领域取得突破，届时 LLM 范式的局限将更加凸显。

---

## 📄 最新论文速览

**1. [ScaleToT: Generalizing Structured LLM Reasoning for Billion-Scale Low-Activity User Modeling](https://arxiv.org/abs/2606.24605)**
  👤 Yuduo Li 等 &nbsp;|&nbsp; 📂 `cs.LG` · `cs.AI` &nbsp;|&nbsp; 🗓 2026-06-24
  [PDF](https://arxiv.org/pdf/2606.24605)

  > 提出 ScaleToT 框架，通过结构化树状思维（Tree-of-Thought）提示策略，将大型语言模型的推理能力迁移至十亿级低活跃用户建模场景。核心创新在于以层次化摘要替代原始行为序列，显著降低 token 消耗，在电商推荐和内容分发基准上取得业界领先结果，证明结构化推理可实现工业级规模落地。

**2. [RAFT: Data Refinement and Adaptive Distillation for Domain Fine-Tuning with Alleviated Forgetting](https://arxiv.org/abs/2606.08507)**
  👤 Yuduo Li 等 &nbsp;|&nbsp; 📂 `cs.LG` · `cs.CL` &nbsp;|&nbsp; 🗓 2026-06-10
  [PDF](https://arxiv.org/pdf/2606.08507)

  > RAFT 提出结合数据精炼与自适应蒸馏的领域微调新范式，同步解决灾难性遗忘与知识迁移两大核心难题。通过动态调整教师模型输出分布，RAFT 在医疗、法律等垂直领域微调实验中，以更少数据量实现更低遗忘率，被 ICML 2026 接收为 Oral 报告。

**3. [RealityTest: How People Probe AI Identity and Whether Models Disclose It](https://arxiv.org/list/cs.CL/current)**
  👤 Anna Gausen 等 &nbsp;|&nbsp; 📂 `cs.CL` · `cs.HC` &nbsp;|&nbsp; 🗓 2026-06-25
  [PDF](https://arxiv.org/list/cs.CL/current)

  > 系统研究用户在真实对话中如何探测 AI 身份，以及 LLM 是否如实披露自身 AI 属性。跨 8 种语言、4 个主流模型的大规模实验显示，用户探测策略因文化背景差异显著，而多数模型在隐性角色扮演情境下存在"选择性不披露"行为，对 AI 透明度政策制定具有直接政策意义。

**4. [Reasoning by Superposition: A Theoretical Perspective on Chain of Continuous Thought](https://arxiv.org/abs/2505.12514)**
  👤 Multiple Authors &nbsp;|&nbsp; 📂 `cs.AI` · `cs.LG` &nbsp;|&nbsp; 🗓 2026-05-19
  [PDF](https://arxiv.org/pdf/2505.12514)

  > 从信息论角度建立连续思维链（Continuous Chain-of-Thought）的理论框架，证明在特定条件下"思维叠加"机制可以大幅提升模型在复杂推理任务中的表达能力上界。研究为当前"隐式推理"与"显式 CoT"之争提供了严格的理论参照，被引用为 ICML 2026 最佳理论论文候选。

**5. [On Wednesdays, We Ask Questions: Optimizing Active Listening in Automated Legal Triage and Referral](https://arxiv.org/list/cs.AI/current)**
  👤 Multiple Authors &nbsp;|&nbsp; 📂 `cs.AI` · `cs.CL` &nbsp;|&nbsp; 🗓 2026-06-23
  [PDF](https://arxiv.org/list/cs.AI/current)

  > 面向自动化法律援助场景，设计"主动倾听"优化策略，通过强化学习训练 LLM 在法律咨询对话中动态决策何时追问、何时转介专业律师。实验证明该策略将用户问题完整捕获率提升 34%，同时减少不必要转介，已被提交至 AI 与法律国际会议（AIDA2J @ ICAIL 2026）。

---

## 🧑‍🔬 大牛动态

### Twitter/X

**[Yann LeCun](https://www.cnbc.com/2026/06/18/yann-lecun-xi-ai-failure.html)** · 06-18 UTC

接受 CNBC 采访时罕见措辞强烈地批评 xAI，并重申 LLM 架构无法实现 AGI 的核心观点。他指出当前行业过度依赖 Scaling Law 与 RLHF 微调，预测"世界模型"范式将在 2027 年前后迎来实质性突破，重新定义通用 AI 的技术路线。

### Blog

**[Andrej Karpathy @ Anthropic](https://techcrunch.com/2026/05/19/openai-co-founder-andrej-karpathy-joins-anthropics-pre-training-team/)** · 06-25 UTC

在 X 和 Anthropic 内部分享了"Karpathy Loop"自动研究项目最新进展：他领导的预训练研究团队在 Anthropic 内部运行 700 次小规模自动化训练实验、历时 2 天自我发现 20 项优化，将训练速度提升 11%。他表示目标是将该循环完全嵌入 Claude 下一代预训练流程，实现"AI 加速 AI 研究"的完整闭环。

**[Demis Hassabis](https://fortune.com/2026/01/23/deepmind-demis-hassabis-anthropic-dario-amodei-yann-lecun-ai-davos/)** · 06-17 UTC

与 Dario Amodei 联合出席 AI 治理峰会并发表联合声明，呼吁建立类 IAEA 的国际 AI 监督机制。Hassabis 强调 DeepMind 的科学安全研究方法已为此类治理框架提供了技术基础，并表示 AlphaFold 系列在医学领域的成功证明了"负责任的前沿 AI"是完全可行的。

### Newsletter

**[Sebastian Raschka](https://magazine.sebastianraschka.com/p/llm-research-papers-2026-part1)** · 06-2026

在 Ahead of AI 上更新 2026 年 LLM 研究论文跟踪报告，本周重点聚焦三个趋势：① 自动研究（Autoresearch）范式的工业化落地；② 多模态推理模型在视觉-语言统一任务上的快速进步；③ 长上下文压缩技术（超 100 万 token 的高效窗口管理）。文章已成为社区公认的 2026 上半年论文导航地图。

---

## 🔥 GitHub 热门 AI 项目

**1. [openclaw/openclaw](https://github.com/openclaw/openclaw)**
  ⭐ 250,000+ &nbsp;·&nbsp; 🍴 36,000+ &nbsp;·&nbsp; `TypeScript` · 今日 **+1,200** ⭐
  2026 年增长最快的开源 AI 项目，一月下旬从 9000 星飙升至 6 万星，此后持续增长突破 25 万。本地运行的个人 AI 助手，通过统一网关接入 WhatsApp、Telegram、Slack、Discord、Signal 等 50+ 平台，支持 OpenAI、Anthropic、Ollama 等任意 AI 模型，零云端、零 API 成本。

**2. [ollama/ollama](https://github.com/ollama/ollama)**
  ⭐ 174,000 &nbsp;·&nbsp; 🍴 14,600 &nbsp;·&nbsp; `Go` · 今日 **+340** ⭐
  本地运行大模型的首选工具，支持 Llama、Mistral、Gemma、DeepSeek、Qwen 等主流模型，一行命令启动推理服务。2026 年大幅扩展硬件支持至 AMD、Intel Arc 及 TPU，最新版已支持 Kimi-K2.6 和 GLM-5.1。

**3. [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)**
  ⭐ 106,000 &nbsp;·&nbsp; 🍴 14,200 &nbsp;·&nbsp; `TypeScript` · 今日 **+890** ⭐
  Google 官方开源 AI 终端代理，将 Gemini 2.5 Pro（100 万 token 上下文）直接嵌入命令行，内置文件操作、Shell 命令、Web 搜索和 MCP 工具支持，与 Claude Code 形成直接竞争。Apache 2.0 协议，社区参与活跃。

**4. [mendableai/firecrawl](https://github.com/mendableai/firecrawl)**
  ⭐ 130,000+ &nbsp;·&nbsp; 🍴 10,200 &nbsp;·&nbsp; `TypeScript`
  大规模网页搜索与抓取框架，将任意页面转换为干净 Markdown、结构化 JSON 或截图，是 AI Agent 工具链的核心基础设施之一。支持 JavaScript 渲染、反爬绕过和分布式爬取，已成为 RAG 数据管道的标配组件。

**5. [comfyanonymous/ComfyUI](https://github.com/comfyanonymous/ComfyUI)**
  ⭐ 107,000+ &nbsp;·&nbsp; 🍴 11,500 &nbsp;·&nbsp; `Python`
  基于节点的图像生成可视化工作流系统，为 Stable Diffusion / FLUX 等模型提供细粒度流程编排，支持视频、3D 生成扩展节点，已成为创意工作者和研究者首选的图像生成工具。

**6. [vllm-project/vllm](https://github.com/vllm-project/vllm)**
  ⭐ 83,000 &nbsp;·&nbsp; 🍴 12,000 &nbsp;·&nbsp; `Python`
  生产级高性能 LLM 推理框架，PagedAttention 算法大幅提升 GPU 内存利用率，提供 OpenAI 兼容 API，在高并发场景下吞吐量约为 Ollama 的 19 倍。2026 年扩展至 AMD、Intel Arc 及 TPU，是企业侧 LLM 部署首选。

---

*本文由 [AI Daily News](https://github.com/yf-sz/ai-daily-news) 使用 web_search 自动收集生成，每日定时发布。*
