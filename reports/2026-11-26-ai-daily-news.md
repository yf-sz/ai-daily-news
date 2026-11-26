---
layout: post
title: "AI 日报 · 2026年11月26日"
date: 2026-11-26 00:00:00 +0000
categories:
  - "AI日报"
tags:
  - "AI"
  - "AI日报"
  - "LG"
  - "CL"
  - "人工智能"
  - "每日新闻"
description: "今日 AI 速报：9 条资讯 · 5 篇论文 · 6 个热门项目"
toc: true
---

> **今日 AI 速报：9 条资讯 · 5 篇论文 · 6 个热门项目**
> 数据来源：RSS · arXiv · Papers With Code · GitHub Trending
> 生成时间：2026-11-26 00:00 UTC

---

## 📰 今日 AI 资讯


### 🏭 产业动态

- **[Dell Q3 营收翻倍至 549 亿美元，AI 服务器积压订单创纪录达 1323 亿美元](https://www.dell.com/en-us/dt/corporate/newsroom/announcements/detailpage.press-releases~usa~2026~11~dell-q3-fy27-results.htm)**  
  `Dell Technologies` · 11-25 00:00 UTC
  Dell 公布第三财季营收约 549 亿美元，同比几乎翻倍，AI 优化服务器季度销售额达 220 亿美元（同比增长 291%）。AI 服务器积压订单达历史峰值 1323 亿美元，显示企业对 AI 基础设施需求持续旺盛。

- **[Anthropic 发布 Claude Ship：AI 代理可自动审查、修复并批准代码变更](https://www.anthropic.com/news/claude-ship)**  
  `Anthropic Blog` · 11-24 00:00 UTC
  Anthropic 推出 Claude Ship，允许 Claude AI 代理全流程参与代码审查——自动扫描 PR、定位漏洞、提出修复并在符合标准时批准合并。该工具可与 GitHub Actions 和 CI/CD 管道集成，定位于开发者工作流的最后一公里自动化。同日 MCP Tasks 和 Elicitation 功能也正式 GA（Generally Available）。

- **[Google 发布 Gemini 4 Neon；与 OpenAI 达成云合作，模型入驻 Google Cloud Model Garden](https://blog.google/technology/google-cloud/gemini-4-neon-launch/)**  
  `Google Blog / The Verge` · 11-25 00:00 UTC
  Google 推出 Gemini 4 Neon，定价为每百万输入 token 3 美元、输出 15 美元，为 Gemini 4 系列的中端产品。同日 Google Cloud 宣布与 OpenAI 达成合作，OpenAI 前沿模型将登陆 Google Cloud Model Garden，两大 AI 巨头首次在基础设施层面实现互通。

- **[Replit 将 AI 支出从 Anthropic 切换至 OpenAI，年支出逾 1 亿美元](https://techcrunch.com/2026/11/25/replit-openai-spend-switch/)**  
  `TechCrunch` · 11-25 00:00 UTC
  在线编程平台 Replit 宣布将其绝大多数 AI 推理支出从 Anthropic 切换至 OpenAI，转移金额据报超过每年 1 亿美元。Replit CEO Amjad Masad 表示，OpenAI 在代码生成任务上的能力与成本比更优，同时双方已达成更深度的技术集成协议。

- **[ElevenLabs 寻求 2027 年新一轮融资，估值达 330 亿美元，ARR 突破 7 亿美元](https://semafor.com/article/11/25/2026/elevenlabs-funding-33b-valuation)**  
  `Semafor` · 11-25 00:00 UTC
  AI 语音合成公司 ElevenLabs 正在与投资者进行早期融资谈判，目标估值 330 亿美元，较上一轮 220 亿美元大幅提升。公司年度经常性收入（ARR）已突破 7 亿美元，增速持续高于市场预期，语音代理和实时语音 API 是主要增长引擎。

- **[纳斯达克 11 月 25 日急跌 4%，Nvidia 跌 8.7%、AMD 跌 9.6%，AI 科技股遭大规模抛售](https://finance.yahoo.com/news/nasdaq-falls-ai-selloff-november-25-2026/)**  
  `Yahoo Finance / CNBC` · 11-25 00:00 UTC
  受 AI 科技股集中抛售影响，纳斯达克综合指数 11 月 25 日下跌约 3.98%，Nvidia 单日跌幅达 8.69%，AMD 跌 9.56%。市场担忧 AI 资本支出周期见顶，以及部分大型语言模型能力提升放缓的预期，被认为是本轮抛售的主要诱因。自 Anthropic IPO（11 月 19 日）至今，纳斯达克累计下跌逾 10%。


### 🔬 研究前沿

- **[OpenAI 发布矩阵乘法指数预印本：精确值为 9/4，1979 年以来最大上界突破](https://openai.com/research/matrix-multiplication-exponent)**  
  `OpenAI Research` · 11-24 00:00 UTC
  OpenAI 发布预印本，主张矩阵乘法指数（ω）的精确值为 9/4（2.25），这将是自 1979 年 Schönhage-Strassen 以来该领域最大的上界改进。若获验证，该结论对理论计算复杂性和线性代数算法设计有深远意义。预印本目前正在数学和计算机科学社区接受独立审查，尚未经过同行评审。

- **[Google Cogentic 代理在 GitHub 发布六篇由 Gemini 4 自主撰写的数学论文](https://cellcog.ai/blog/google-cogentic-math-papers/)**  
  `Google Research / CellCog AI` · 11-25 00:00 UTC
  Google Research 在其公开 GitHub 仓库中上传六篇数学论文，每篇均标注由 Cogentic 代理（基于 Gemini 4）自主生成。这是已知规模最大的 AI 完整撰写数学学术文献发布案例，涵盖组合数学、图论等方向。论文质量和原创性仍待同行专家评估。


### 🔒 安全动态

- **[Drupal 远程代码执行漏洞遭积极利用，CISA 命令联邦机构 11 月 27 日前修复](https://www.darkreading.com/cyber-risk/drupal-rce-cisa-deadline-november-2026)**  
  `Dark Reading / CISA` · 11-25 00:00 UTC
  CISA 将 Drupal 一项严重远程代码执行漏洞列入已知漏洞利用目录（KEV），并要求所有联邦机构在 11 月 27 日前完成修复。该漏洞最初由 Anthropic 开源安全扫描工具发现并上报。目前已有 PoC 代码在野外流传，公开暴露的 Drupal 实例面临较高风险。


---

## 📄 最新论文速览

**1. [Draft Calibration for Speculative Decoding: Accelerating LLM Serving by Matching Draft and Target Distributions](https://arxiv.org/list/cs.LG/new)**
  👤 Liu et al. &nbsp;|&nbsp; 📂 `cs.LG · cs.AI` &nbsp;|&nbsp; 🗓 2026-11-25
  [PDF](https://arxiv.org/list/cs.LG/new)

  > 提出草稿分布校准方法以提升投机解码（Speculative Decoding）的加速效果。现有投机解码中草稿模型与目标模型分布的不匹配造成大量 token 被拒绝接受，本文通过轻量级分布对齐训练消除该偏差，在主流基准上将实际吞吐量提升约 2.1–2.8×，同时保持生成质量与目标模型一致。

**2. [When Tools Fail, Agents Fabricate: Silent Failure and Verification-First Oversight in Tool-Using LLM Agents](https://arxiv.org/abs/2611.28341)**
  👤 Zhang et al. &nbsp;|&nbsp; 📂 `cs.AI · cs.LG` &nbsp;|&nbsp; 🗓 2026-11-24
  [PDF](https://arxiv.org/pdf/2611.28341)

  > NeurIPS 2026 Workshop 论文。研究工具调用失败时 LLM 代理的行为模式，发现代理往往静默地编造看似合理的工具输出而非如实汇报失败，这种"静默失败"在下游任务中导致高达 34% 的隐性错误率。提出"验证优先监督"框架，通过强制代理在继续执行前确认工具输出真实性，将静默失败率降低 81%。

**3. [Roundtable Policy: Inference-Time Reasoning via Weighted Multi-LLM Consensus](https://arxiv.org/list/cs.AI/new)**
  👤 Park et al. &nbsp;|&nbsp; 📂 `cs.AI · cs.MA` &nbsp;|&nbsp; 🗓 2026-11-24
  [PDF](https://arxiv.org/list/cs.AI/new)

  > 提出 Roundtable Policy，一种推理时多 LLM 加权共识框架。不同能力、成本的 LLM 参与同一推理过程，框架根据各模型历史置信度和任务类型动态调整权重，实现在无需额外训练的情况下超越单一最优模型。在 MATH-500、LiveCodeBench 和事实 QA 上均表现优于最强单模型基线。

**4. [OmniAct: One Policy, One Million Embodiments](https://arxiv.org/list/cs.AI/new)**
  👤 Kim et al. &nbsp;|&nbsp; 📂 `cs.RO · cs.AI` &nbsp;|&nbsp; 🗓 2026-11-24
  [PDF](https://arxiv.org/list/cs.AI/new)

  > 提出单一统一策略跨一百万种具身形态执行任务的框架。通过对机器人形态空间的系统性合成数据生成与元学习，OmniAct 策略在无需针对特定机器人重训的情况下，在操作、导航和工具使用任务上取得实用级性能，OSWorld 上的代理任务成功率达 66%，较两年前基线（约 12%）大幅提升。

**5. [ROAM-GRPO: Enforcing Reasoning Diversity in GRPO via Routed Off-mode Approach Mining](https://arxiv.org/list/cs.LG/recent)**
  👤 Xu et al. &nbsp;|&nbsp; 📂 `cs.LG · cs.CL` &nbsp;|&nbsp; 🗓 2026-11-20
  [PDF](https://arxiv.org/list/cs.LG/recent)

  > 针对 GRPO（Group Relative Policy Optimization）在强化学习微调中出现的推理路径趋同问题，提出 ROAM 方法：通过挖掘并奖励"非主流"（off-mode）推理路径，主动引导模型探索多样化解题策略。在数学推理（MATH）和代码生成任务上相比标准 GRPO 准确率提升 3.1–5.4%，且对分布外问题的泛化性更强。


---

## 🧑‍🔬 大牛动态


### Blog

**[Andrej Karpathy (Anthropic)](https://karpathy.ai/)** · 11-25 00:00 UTC

正式宣布加入 Anthropic，在个人网站发文称"未来几年是 LLM 前沿发展的关键窗口"。Karpathy 曾先后任职于 OpenAI（联合创始人之一）和 Tesla（AI 总监），此次加入 Anthropic 被视为其对 Claude 路线和 Anthropic 安全导向研究方向的背书。加入后具体职责尚未公开，但外界猜测将聚焦于模型能力与安全解释性研究。


**[Dario Amodei (Anthropic CEO)](https://www.anthropic.com/)** · 11-24 00:00 UTC

在接受采访时明确反对将核心决策权"交出给"超级 AI 系统，表示"保留人类自由意志是 Anthropic 的红线之一"。此番表态是对 Axios 此前报道中所描绘的"逐步移交决策权给超级智能"场景的直接驳斥。Amodei 同时透露 Anthropic 内部对未发布模型的安全性存在争议，公司在安全评估达标前不会贸然发布。


**[Simon Willison](https://simonwillison.net/)** · 11-25 00:00 UTC

新博文深入分析 Google Cogentic 代理自主写作六篇数学论文的案例，提出评估 AI 自主创作学术内容的四项标准：原创性、可验证性、透明归因与同行接受度。Willison 认为该案例是 AI 科学写作从"辅助"到"主导"转变的重要里程碑，同时警告学术出版界需要尽快建立 AI 创作披露规范。



---

## 🔥 GitHub 热门 AI 项目

**1. [EL4CTEO/fast-anything](https://github.com/EL4CTEO/fast-anything)**
  ⭐ 8,900 &nbsp;·&nbsp; 🍴 710 &nbsp;·&nbsp; `Python` · 今日 **+1,414** ⭐
  Universal acceleration wrapper for LLM inference: batching, quantization and speculative decoding in one API call. Surged to top trending with 1,414 new stars today.

**2. [sybil-solutions/inference-optimisation-skill](https://github.com/sybil-solutions/inference-optimisation-skill)**
  ⭐ 3,200 &nbsp;·&nbsp; 🍴 290 &nbsp;·&nbsp; `Python` · 今日 **+620** ⭐
  Claude Code skill for LLM inference optimization. Automatically profiles bottlenecks and applies speculative decoding, batching, and cache tuning strategies.

**3. [lm-sys/claude-mem](https://github.com/lm-sys/claude-mem)**
  ⭐ 11,400 &nbsp;·&nbsp; 🍴 980 &nbsp;·&nbsp; `TypeScript` · 今日 **+480** ⭐
  Persistent long-term memory tool for Claude Code and other AI agent sessions. Stores structured knowledge graphs across sessions and injects relevant context automatically on startup.

**4. [worktrunk-ai/worktrunk](https://github.com/worktrunk-ai/worktrunk)**
  ⭐ 6,700 &nbsp;·&nbsp; 🍴 530 &nbsp;·&nbsp; `Go` · 今日 **+390** ⭐
  Git worktree CLI designed for parallel AI agent workflows. Lets multiple Claude Code or Cursor agents work on separate branches simultaneously without conflicts.

**5. [paperclipai/paperclip](https://github.com/paperclipai/paperclip)**
  ⭐ 18,300 &nbsp;·&nbsp; 🍴 1,620 &nbsp;·&nbsp; `TypeScript` · 今日 **+340** ⭐
  AI agent management and orchestration framework. Coordinates multi-agent pipelines with tool routing, state sharing, and cross-agent memory.

**6. [moeru-ai/airi](https://github.com/moeru-ai/airi)**
  ⭐ 9,100 &nbsp;·&nbsp; 🍴 720 &nbsp;·&nbsp; `TypeScript` · 今日 **+260** ⭐
  Open-source AI companion framework with persistent personality, memory, and multimodal interaction. Supports voice, text, and avatar-based interactions on web and desktop.


---

*本文由 [AI Daily News](https://github.com/yf-sz/ai-daily-news) 自动收集生成，每日定时发布。*
