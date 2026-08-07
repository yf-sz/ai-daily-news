---
layout: post
title: "AI 日报 · 2026年08月07日"
date: 2026-08-07 08:00:00 +0000
categories:
  - "AI日报"
tags:
  - "AI"
  - "AI日报"
  - "CL"
  - "LG"
  - "人工智能"
  - "每日新闻"
description: "今日 AI 速报：9 条资讯 · 6 篇论文 · 5 个热门项目"
toc: true
---

> **今日 AI 速报：9 条资讯 · 6 篇论文 · 5 个热门项目**
> 数据来源：Web Search · arXiv · GitHub Trending
> 生成时间：2026-08-07 08:00 UTC

---

## 📰 今日 AI 资讯


### 🏭 产业动态

- **[Demis Hassabis 卸任 Google DeepMind CEO，Koray Kavukcuoglu 接掌日常运营](https://dataconomy.com/2026/08/06/demis-hassabis-stepping-down-google-deepmind-ceo/)**  
  `Dataconomy` · 08-06 00:00 UTC
  Google DeepMind 宣布重大人事变动：联合创始人 Demis Hassabis 从 CEO 一职转任董事长，同时出任 Alphabet 首席科学家，继续掌舵制药子公司 Isomorphic Labs。现任 CTO Koray Kavukcuoglu 升任高级副总裁，直接向 Alphabet CEO Sundar Pichai 汇报，全面负责 Gemini 模型研发、前沿 AI 研究及 Gemini 应用与开发者团队。

- **[Jeff Dean 离开 Google 27 年后创立 Discovery Loop，目标 AI 驱动科学发现](https://techcrunch.com/2026/08/05/jeff-dean-and-other-top-ai-researchers-are-leaving-google-to-launch-their-own-startup/)**  
  `TechCrunch` · 08-05 00:00 UTC
  Alphabet 前首席科学家 Jeff Dean 携手老搭档 Sanjay Ghemawat、Oriol Vinyals 和 Quoc Le 共同创立 Discovery Loop——一家专注于 AI 自动化科学研究的初创公司。Google 作为种子投资方，将为其提供云计算资源。Discovery Loop 首期目标是自动化机器学习研究与工程，远期计划延伸至硬件设计、药物研发和清洁能源。Radical Ventures 与 Khosla Ventures 联合领投。

- **[Meta 发布 Muse Spark 1.2 与终端编程 Agent Muse Code（Beta）](https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2)**  
  `Meta AI Research` · 08-05 00:00 UTC
  Meta 超级智能实验室在 8 月 5 日发布 Muse Spark 1.2 和配套 Beta 编码 Agent Muse Code。Muse Spark 1.2 在代码能力上相比 1.1 有显著提升，GDPval-AA v2 Elo 从 1371 升至 1631，Terminal-Bench 2.1 达 80%。Muse Code 专为复杂软件工程任务设计，可跨大型代码仓库完成规划、编写与验证。API 定价 $1.25/$4.25（输入/输出，per M tokens），缓存输入仅 $0.15。

- **[MiniMax 发布全模态视频模型 H3，2K 15 秒视频带原生立体声，计划开源权重](https://www.marktechpost.com/2026/08/01/minimax-releases-minimax-h3-an-omni-modal-video-model-that-generates-15-second-2k-clips-with-native-stereo-audio/)**  
  `MarkTechPost` · 08-01 00:00 UTC
  MiniMax 于 7 月 31 日正式发布 H3，全模态（文本/图像/音频/视频输入）视频生成模型，可生成 2K 分辨率、最长 15 秒带原生立体声的视频片段，API 定价约 CNY¥0.8/秒（约 $1.95/15 秒），仅为竞品 Seedance 2.5 的 1/12。MiniMax 宣布近期将开源 H3 模型权重，支持企业私有部署。目前该模型尚未开放英美欧韩市场。

- **[Anthropic 与 Blackstone 合资 15 亿美元成立 Ode With Anthropic，100 名工程师已就位](https://aiweekly.co/ai-news-today/anthropic-news)**  
  `AI Weekly` · 08-06 00:00 UTC
  Anthropic、Blackstone 和 Hellman & Friedman 联合宣布 15 亿美元 AI 实施合资公司 Ode With Anthropic 正式启动，目前已有 100 名工程师参与项目交付，聚焦企业级 AI 能力落地。该合资计划于 5 月首次披露，现已进入执行阶段。


### 🔬 研究前沿

- **[Google 将 AI 决策中心迁回加州总部，加速追赶 Anthropic 与 OpenAI](https://www.bloomberg.com/news/articles/2026-08-06/google-shifts-ai-power-to-california-in-race-against-anthropic-openai)**  
  `Bloomberg` · 08-06 00:00 UTC
  随着此次领导层重组，Google 宣布将 AI 核心研究与模型开发决策权从英国伦敦 DeepMind 总部迁回加州山景城，与 Gemini 产品和开发者团队更紧密协同。此举被视为 Google 加速整合研究与产品、应对 Anthropic 和 OpenAI 竞争压力的战略布局。


### 🛠️ 工具生态

- **[Simon Willison 发布 LLM CLI 0.32：推理追踪、OpenAI Responses 支持、服务端工具](https://simonwillison.net/)**  
  `Simon Willison's Weblog` · 08-05 00:00 UTC
  Simon Willison 发布 LLM CLI 与 Python 库的重大新版本 0.32，这是该项目发布以来功能更新最多的一次。新增功能包括：完整的推理过程追踪（reasoning traces）、对 OpenAI Responses API 的原生支持、服务端工具集成、更智能的日志记录，以及对数百个不同 LLM 提供商的兼容支持。

- **[Simon Willison 博客：MiniMax H3 发布，"意外网络攻击"新标签追踪 AI 安全事故](https://simonwillison.net/)**  
  `Simon Willison's Weblog` · 08-04 00:00 UTC
  Willison 在其博客详细分析了 MiniMax H3 的技术特性，并创建 "accidental-cyberattacks" 分类标签，专门追踪 AI 实验室在测试网络攻击潜力时意外触发真实攻击的安全事故案例，呼吁业界重视 AI 安全测试中的潜在风险。


---

## 📄 最新论文速览

**1. [Robotouille: An Asynchronous Planning Benchmark for LLM Agents](https://arxiv.org/pdf/2502.05227)**
  👤 Pranav Putta, Edmund Mills, Naman Garg 等 &nbsp;|&nbsp; 📂 `cs.AI · cs.LG` &nbsp;|&nbsp; 🗓 2026-08-06
  [PDF](https://arxiv.org/pdf/2502.05227)

  > 提出 Robotouille 基准，专门评估 LLM Agent 在异步多任务规划场景下的能力。不同于单步推理任务，Robotouille 要求 Agent 在并行子任务间进行动态调度，模拟真实厨房环境中的多任务协同，揭示现有 LLM 在长程任务规划上的瓶颈。

**2. [Real-Time Reasoning Agents in Evolving Environments](https://arxiv.org/pdf/2511.04898)**
  👤 Mohamed Amine Ferrag, Norbert Tihanyi, Merouane Debbah &nbsp;|&nbsp; 📂 `cs.AI · cs.MA` &nbsp;|&nbsp; 🗓 2026-08-05
  [PDF](https://arxiv.org/pdf/2511.04898)

  > 研究大型语言模型 Agent 在动态变化环境中的实时推理能力。提出一种自适应框架，使 Agent 能持续感知环境变化并更新推理链，在动态决策任务中比静态 ReAct 基线提升显著。

**3. [KLong: Training LLM Agent for Extremely Long-horizon Tasks](https://arxiv.org/pdf/2602.17547)**
  👤 Pan Lu, Bowen Chen 等 &nbsp;|&nbsp; 📂 `cs.LG · cs.AI` &nbsp;|&nbsp; 🗓 2026-08-04
  [PDF](https://arxiv.org/pdf/2602.17547)

  > 提出 KLong 框架，通过课程学习和长程奖励塑形训练 LLM Agent 完成极长时间跨度任务（最长 1000+ 步），在软件工程、科学实验规划等复杂 Agent 基准上取得新最佳结果。

**4. [Agentic Code Reasoning: Can LLM Agents Reason About Code Semantics Without Executing It?](https://arxiv.org/abs/2603.01896)**
  👤 Shubham Ugare, Satish Chandra &nbsp;|&nbsp; 📂 `cs.SE · cs.AI` &nbsp;|&nbsp; 🗓 2026-08-03
  [PDF](https://arxiv.org/abs/2603.01896)

  > 系统评估 LLM Agent 在无需实际执行代码的情况下对代码语义的静态推理能力。实验表明当前 frontier 模型在代码数据流、别名分析和副作用推理上仍存在明显缺陷，为 AI 辅助编程工具提供了明确的改进方向。

**5. [OpenVLThinkerV2: A Generalist Multimodal Reasoning Model for Multi-domain Visual Tasks](https://arxiv.org/pdf/2604.08539)**
  👤 OpenVLThinker Team &nbsp;|&nbsp; 📂 `cs.CV · cs.LG` &nbsp;|&nbsp; 🗓 2026-07-31
  [PDF](https://arxiv.org/pdf/2604.08539)

  > 提出 OpenVLThinkerV2 多模态通用推理模型，在数学、科学、图表理解等多领域视觉任务上统一建模。通过慢思考（slow thinking）机制和跨域训练策略，在多项多模态基准上超越同规模模型。

**6. [Multi-level Value Alignment in Agentic AI Systems: Survey and Perspectives](https://arxiv.org/pdf/2506.09656)**
  👤 多机构合作团队 &nbsp;|&nbsp; 📂 `cs.AI · cs.MA` &nbsp;|&nbsp; 🗓 2026-07-30
  [PDF](https://arxiv.org/pdf/2506.09656)

  > 系统综述 Agentic AI 系统中的多层次价值对齐问题，从个体 Agent 到多 Agent 系统再到社会层面，分析当前对齐方法的局限性，提出跨层次对齐的研究框架，为 AAAI/NeurIPS 2026 相关研究提供理论基础。


---

## 🧑‍🔬 大牛动态


### 博客 / 社交

**[Simon Willison](https://simonwillison.net/)** · 08-05 00:00 UTC

发布 LLM CLI v0.32 重大更新，这是其 Python 库项目成立以来规模最大的功能版本。新版原生支持 OpenAI Responses API，新增推理追踪（reasoning traces）和服务端工具调用，并大幅提升日志智能化程度。Willison 同步发布 MiniMax H3 技术分析文章，并在博客开设 accidental-cyberattacks 专栏追踪 AI 安全实验意外事故。

**[Andrej Karpathy](https://karpathy.github.io/)** · 近期动态

据 TechCrunch 报道，Karpathy 已于 5 月正式加入 Anthropic 预训练团队，专注利用 Claude 加速基础模型研究。其 nanochat 项目（轻量 LLM 训练教程框架）持续受到开发者社区关注，被列为 2026 年 GitHub 年度优秀教育性项目之一。

**[Yann LeCun](https://x.com/ylecun)** · 近期动态

在卸任 Meta FAIR 主任后，LeCun 已创立新 AI 初创公司，目标是构建超越 LLM 范式的高级机器智能架构（World Models）。其持续在 X/LinkedIn 上发表对 AGI 路径的深度见解，并坚持反对"纯 LLM 路线能达成 AGI"的主流观点。


---

## 🔥 GitHub 热门 AI 项目

**1. [open-claw/openclaw](https://github.com/open-claw/openclaw)**
  ⭐ 210,000+ &nbsp;·&nbsp; 🍴 18,000+ &nbsp;·&nbsp; `TypeScript` · 持续热门
  本地优先 AI 个人助手，作为本地网关连接各类 AI 模型与 50+ 应用集成，数据完全不离开本机。从 2 万 star 猛涨到 21 万，是 2026 年 GitHub 增速最快的 AI 项目。

**2. [comfyanonymous/ComfyUI](https://github.com/comfyanonymous/ComfyUI)**
  ⭐ 106,000+ &nbsp;·&nbsp; 🍴 11,000+ &nbsp;·&nbsp; `Python` · 持续热门
  节点式图像生成工作流系统，提供对 Stable Diffusion 及各类扩散模型的精细化流程控制，社区插件生态极其丰富，已成为本地图像生成的事实标准工具。

**3. [ollama/ollama](https://github.com/ollama/ollama)**
  ⭐ 165,000+ &nbsp;·&nbsp; 🍴 13,000+ &nbsp;·&nbsp; `Go` · 持续热门
  一行命令在本地运行 Llama、Mistral、Qwen 等主流大模型的平台，隐私友好、无需云依赖，持续领跑本地 LLM 赛道，近期增加对 Kimi K3 权重的原生支持。

**4. [VoltAgent/awesome-ai-agent-papers](https://github.com/VoltAgent/awesome-ai-agent-papers)**
  ⭐ 8,500+ &nbsp;·&nbsp; 🍴 620+ &nbsp;·&nbsp; `Markdown` · 近期热门
  2026 年 AI Agent 领域研究论文精选合集，涵盖 Agent 工程、记忆机制、评估方法、工作流编排和自主系统设计，同步收录 ICML/NeurIPS 2026 相关论文，是 Agent 研究者的必备索引。

**5. [karpathy/nanochat](https://github.com/karpathy/nanochat)**
  ⭐ 42,000+ &nbsp;·&nbsp; 🍴 4,200+ &nbsp;·&nbsp; `Python` · 持续热门
  Andrej Karpathy 开源的极简 LLM 训练与推理教学框架，从零实现 Transformer 核心组件，代码清晰易读，深受 AI 初学者和研究者追捧，被社区誉为"最适合理解 LLM 本质的项目"。


---

*本文由 [AI Daily News](https://github.com/yf-sz/ai-daily-news) 自动收集生成，每日定时发布。*
