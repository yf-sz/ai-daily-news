---
layout: post
title: "AI 日报 · 2026年07月13日"
date: 2026-07-13 00:10:00 +0000
categories:
  - "AI日报"
tags:
  - "AI"
  - "AI日报"
  - "人工智能"
  - "每日新闻"
description: "今日 AI 速报：6 条资讯 · 5 篇论文 · 6 个热门项目"
toc: true
---

> **今日 AI 速报：6 条资讯 · 5 篇论文 · 6 个热门项目**
> 数据来源：RSS · arXiv · Papers With Code · GitHub Trending
> 生成时间：2026-07-13 00:10 UTC

---

## 📰 今日 AI 资讯


### 🏭 产业动态

- **[Microsoft 开始以自研 MAI 模型替换 Excel/Outlook 中的 OpenAI 和 Anthropic API](https://www.bloomberg.com/news/articles/2026-07-07/microsoft-replaces-openai-anthropic-with-own-ai-in-some-apps)**  
  `Bloomberg` · 07-07 00:00 UTC
  微软已开始用内部构建的 MAI 系列模型处理旗下 Excel 和 Outlook 等核心产品中的 AI 请求，每周已有数万条提示由 MAI 完成，不再依赖 OpenAI 或 Anthropic 的 API。此举旨在控制日益增长的第三方 AI 成本，是微软 AI 战略自主化的关键一步。微软同期宣布 2026 年全年资本支出预期将达 1900 亿美元，其中 250 亿美元增量源于 AI 基础设施对内存和存储器需求的激增。

- **[Google Gemini 3.5 Pro 确认 7 月 17 日 GA，架构全面重建，携 200 万 token 上下文与 Deep Think 推理](https://www.techtimes.com/articles/319877/20260708/gemini-35-pro-targets-july-17-deepseeks-july-24-deadline-hits-developers-now.htm)**  
  `TechTimes` · 07-08 00:00 UTC
  Google 将 Gemini 3.5 Pro 正式发布日期确定为 7 月 17 日，此前因决定对模型进行全面架构重建而从 6 月延期至今。新模型将具备 200 万 token 上下文窗口、Deep Think 深度推理层和自主工作流能力，同时支持更强的 SVG 渲染和通过 Fable 集成的音效生成功能，目标直指 Claude Sonnet 5 和 GPT-5.6 Terra 在企业代理场景的竞争。

- **[Meta 推出 Muse Spark 1.1，开放首款带 API 的 Spark 模型，主打代理工具调用与计算机操控](https://dentro.de/ai/news/)**  
  `dentro.de/AI` · 07-09 00:00 UTC
  Meta 发布 Muse Spark 1.1，这是 Spark 系列首款提供 API 接入的模型，支持 100 万 token 上下文窗口，并针对代理任务中的工具调用（tool calling）和计算机操控（computer use）进行了显著强化。Simon Willison 在其博客中评测了该模型，称 Meta 宣传在代理场景上实现了重大性能跃升，直接参与 Claude 和 GPT-5.6 Terra 在代理赛道的正面竞争。


### 🔬 研究前沿

- **[OpenAI GPT-5.6 Sol Ultra 用 64 个并行子代理在一小时内证明了困扰数学界 50 年的"环双覆盖猜想"](https://cryptobriefing.com/openai-gpt-5-6-sol-ultra-math-proof/)**  
  `CryptoBriefing` · 07-10 00:00 UTC
  OpenAI 宣布 GPT-5.6 Sol Ultra 生成了"环双覆盖猜想"（Cycle Double Cover Conjecture）的机器验证证明，该猜想由 George Szekeres（1973）和 Paul Seymour（1979）各自独立提出，在图论领域悬而未决长达 50 年。整个证明流程由 64 个子代理并行运作完成，仅耗时不足一小时。OpenAI 同步公布了完整的 700 词提示词，揭示多代理编排的核心技术手法。需注意该证明目前正处于学界同行评审阶段，历史上曾有多份类似"证明"被发现存在漏洞。


### 🛠️ 工具生态

- **[Simon Willison 发布 llm-coding-agent 0.1a0，并深度解读 GPT-Live 实时对话与 llm-meta-ai 插件](https://simonwillison.net/2026/Jul/8/introducing-gptlive/)**  
  `simonwillison.net` · 07-08 00:00 UTC
  知名开发者 Simon Willison 近日密集产出：7 月 2 日发布基于 LLM 工具库的编程代理 llm-coding-agent 0.1a0；7 月 8 日发表对 GPT-Live 实时对话功能的深度介绍；同期发布 llm-meta-ai 插件，为 LLM 生态提供访问 Meta AI 模型的 CLI 和 Python 接口。他同时倡导在子代理任务中优先使用 Sonnet/Haiku 等轻量模型以大幅降低推理成本，主循环保留高算力模型用于判断与审查。

- **[Karpathy 发布 Sequoia Ascent 2026 总结：AI 基础设施迎来"组合式爆炸"，Jevons 悖论重塑软件需求](https://karpathy.bearblog.dev/sequoia-ascent-2026/)**  
  `karpathy.bearblog.dev` · 07-12 00:00 UTC
  Andrej Karpathy 在其博客发布了 Sequoia Ascent 2026 参会总结，重点分享了对 AI 基础设施、代理应用和 LLM 能力前沿的观察。他指出随着 AI 按需生成可运行软件的能力持续提升，杰文斯悖论（Jevons' Paradox）正在推动对定制化软件工具需求的大幅增加而非减少，预计未来 12 个月内软件形态将发生根本性重构。


---

## 📄 最新论文速览

**1. [Self-GC: Self-Governing Context for Long-Horizon LLM Agents](https://arxiv.org/abs/2607.00692)**
  👤 Xubin Hao, Hongjin Meng, Xin Yin, Jiawei Zhu, Chenpeng Cao &nbsp;|&nbsp; 📂 `cs.AI · cs.LG` &nbsp;|&nbsp; 🗓 2026-07-01
  [PDF](https://arxiv.org/pdf/2607.00692)

  > 长 horizon 代理在运行过程中积累大量工具输出、文件、计划及用户约束，现有系统多依赖按时序截断或最终自我摘要等启发式手段。Self-GC 将用户请求、工具调用结果、技能状态等建模为可索引的上下文"对象"，通过侧通道规划器提议 fold、mask、prune 操作并由 harness 强制执行，实现对代理上下文生命周期的主动治理，而非被动的 token 回收。

**2. [Seed2.0 Model Card: Towards Intelligence Frontier for Real-World Complexity](https://arxiv.org/abs/2607.00248)**
  👤 ByteDance Seed Team &nbsp;|&nbsp; 📂 `cs.AI · cs.CL` &nbsp;|&nbsp; 🗓 2026-07-01
  [PDF](https://arxiv.org/pdf/2607.00248)

  > ByteDance Seed 团队发布 Seed2.0 模型报告，该系列以应对复杂真实世界任务为核心目标，重点突破长尾知识覆盖与复杂指令跟随两大挑战。报告详述了模型在代码生成、多步推理等任务上的技术突破，以及大规模预训练与后训练对齐的工程实践，是字节跳动 AI 研究团队迄今最为系统的模型能力披露。

**3. [Autonomous Information Seeking: A Roadmap for Agentic Recommender Systems](https://arxiv.org/abs/2607.04433)**
  👤 arXiv 2607.04433 Authors &nbsp;|&nbsp; 📂 `cs.AI · cs.IR` &nbsp;|&nbsp; 🗓 2026-07-05
  [PDF](https://arxiv.org/pdf/2607.04433)

  > 提出代理推荐系统（Agentic Recommender Systems）的系统性路线图，将传统被动推荐范式升级为以自主信息搜寻为核心的主动代理架构。梳理了评估方法论并提出多模态对齐、可控性、可信性、隐私保护、可扩展性和效率等六大开放挑战，为下一代个性化 AI 系统的研究提供参考框架。

**4. [From Signals to Structure: How Memory Architecture Drives Language Emergence in LLM Agents](https://arxiv.org/abs/2607.00233)**
  👤 Yashar Talebirad, Eden Redman, Ali Parsaee, Osmar R. Zaiane &nbsp;|&nbsp; 📂 `cs.AI · cs.CL · cs.MA` &nbsp;|&nbsp; 🗓 2026-07-01
  [PDF](https://arxiv.org/pdf/2607.00233)

  > 研究 LLM 代理中记忆架构对语言涌现行为的驱动作用。作者发现结构化记忆对代理在多轮交互中形成稳定语言模式至关重要，不同记忆设计方案会导致显著差异的涌现行为，为代理记忆系统的工程设计提供了实验性理论基础，涵盖 AI、计算语言学与多代理系统三个研究方向。

**5. [An Experimental Design Approach to Evaluating Agentic AI's Autonomous Model Discovery](https://arxiv.org/abs/2607.06413)**
  👤 arXiv 2607.06413 Authors &nbsp;|&nbsp; 📂 `cs.AI · cs.LG` &nbsp;|&nbsp; 🗓 2026-07-08
  [PDF](https://arxiv.org/pdf/2607.06413)

  > 提出使用实验设计方法系统评估代理 AI 在自主模型发现任务中的能力。通过受控实验比较了不同代理框架在假设生成、数据采集和结论验证三个阶段的表现，为代理 AI 在科学发现场景中的部署提供了可复现的评估基准，对 AI for Science 方向具有方法论参考价值。


---

## 🧑‍🔬 大牛动态


### Twitter/X

**[Sam Altman](https://www.techblit.com/sam-altman-compares-child-milestone-to-gpt-56-math-discovery)** · 07-05 00:00 UTC

发推将长子说出第一个双字句与 GPT-5.6 Sol Ultra 自主发现新数学证明并列类比，感叹 AI 正在经历"里程碑时刻"。该推文在 GPT-5.6 系列发布 9 天后发出，获得 9,646 点赞、256 次转推，在 AI 社区引发广泛讨论，也被部分观察者视为 OpenAI 对此次环双覆盖猜想突破重要性的非正式背书，并隐晦传递了其对 AGI 进程的乐观判断。

❤️ 9,646 · 🔁 256

**[Andrej Karpathy](https://karpathy.bearblog.dev/sequoia-ascent-2026/)** · 07-12 00:00 UTC

在 Sequoia Ascent 2026 总结博文中深度分享了他加入 Anthropic 后的视角：AI 模型正迅速成为软件生产的基础设施，Jevons 悖论在软件领域正在重演——按需生成软件的能力越强，反而会激发出更大的定制化软件需求。Karpathy 还在 Twitter 分享了对 Claude Fable 5 的使用体验，认为其在代码推理和长文档理解上较前代有质的飞跃，并表示 AI 驱动的个性化教育将是下一个十年最重要的社会变革之一。


### Blog

**[Simon Willison](https://simonwillison.net/2026/Jul/8/introducing-gptlive/)** · 07-08 00:00 UTC

近期在博客密集产出：发表对 GPT-Live 实时对话功能的深度评测，指出其在低延迟语音交互和实时工具调用方面表现超出预期；同期记录了 llm-coding-agent 0.1a0 在真实编程任务中的实践心得，并发布 llm-meta-ai 插件扩展 Meta AI 的访问能力。Willison 持续倡导在子代理任务中使用 Sonnet/Haiku 等轻量模型降本提效，主循环保留高算力模型负责判断与协调，为社区提供了切实可行的多代理成本优化方案。


---

## 🔥 GitHub 热门 AI 项目

**1. [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search)**
  ⭐ 21,159 &nbsp;·&nbsp; 🍴 5,620 &nbsp;·&nbsp; `Python` · 今日 **+1,350** ⭐
  AI-powered job application framework built on Claude Code. Fork it, fill in your profile, and let Claude evaluate jobs, tailor CVs, write cover letters, and prepare you for interviews.

**2. [openclaw/openclaw](https://github.com/openclaw)**
  ⭐ 210,200 &nbsp;·&nbsp; 🍴 18,400 &nbsp;·&nbsp; `TypeScript` · 今日 **+1,100** ⭐
  Personal AI assistant running entirely on your own devices — connects to 50+ integrations (WhatsApp, Telegram, Slack, Discord, Signal, iMessage) with data never leaving your machine.

**3. [ollama/ollama](https://github.com/ollama/ollama)**
  ⭐ 165,500 &nbsp;·&nbsp; 🍴 12,700 &nbsp;·&nbsp; `Go` · 今日 **+980** ⭐
  Get up and running with large language models locally. Run Llama, DeepSeek, Mistral, Gemma and more — the Docker equivalent for local LLMs.

**4. [open-webui/open-webui](https://github.com/open-webui/open-webui)**
  ⭐ 124,500 &nbsp;·&nbsp; 🍴 14,600 &nbsp;·&nbsp; `Svelte` · 今日 **+870** ⭐
  User-friendly AI Interface (Supports Ollama, OpenAI API, ...) — self-hosted, works offline, extensible with plugins and model integrations.

**5. [ai-boost/awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering)**
  ⭐ 2,900 &nbsp;·&nbsp; 🍴 285 &nbsp;·&nbsp; 今日 **+420** ⭐
  Awesome list for AI agent harness engineering: tools, patterns, evals, memory, MCP, permissions, observability, and orchestration.

**6. [VoltAgent/awesome-ai-agent-papers](https://github.com/VoltAgent/awesome-ai-agent-papers)**
  ⭐ 3,250 &nbsp;·&nbsp; 🍴 195 &nbsp;·&nbsp; 今日 **+310** ⭐
  A curated collection of AI agent research papers released in 2026, covering agent engineering, memory, evaluation, workflows, and autonomous systems.


---

*本文由 [AI Daily News](https://github.com/yf-sz/ai-daily-news) 自动收集生成，每日定时发布。*
