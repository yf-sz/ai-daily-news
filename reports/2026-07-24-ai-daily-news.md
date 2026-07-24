---
layout: post
title: "AI 日报 · 2026年07月24日"
date: 2026-07-24 07:30:00 +0000
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
> 生成时间：2026-07-24 07:30 UTC

---

## 📰 今日 AI 资讯


### 🏭 产业动态

- **[DeepSeek V4 旧版 API 别名于今日 UTC 15:59 正式退役，V4 全面生产就绪](https://codersera.com/blog/deepseek-v4-release-date-features-benchmarks/)**  
  `CodersEra` · 07-24 00:00 UTC
  DeepSeek 宣布 `deepseek-chat` 和 `deepseek-reasoner` 两个旧版 API 别名于 2026 年 7 月 24 日 15:59 UTC 永久退役。V4-Pro（1.6T 参数，49B 激活参数）和 V4-Flash（284B 参数，13B 激活）全面生产可用，均支持 1M token 上下文与 Thinking/Non-Thinking 双模式，标志 DeepSeek V4 正式进入企业级稳定部署阶段。

- **[Alphabet Q2 财报：上调 2026 年资本支出至 2050 亿美元，Google Cloud 营收同比增 82%](https://www.business-standard.com/technology/tech-news/alphabet-raises-ai-spending-target-to-205-billion-as-cloud-demand-surges-126072300463_1.html)**  
  `Business Standard` · 07-23 00:00 UTC
  Alphabet 在 7 月 22 日 Q2 财报会上宣布将 2026 年资本支出指引上调至 1950 亿~2050 亿美元，较此前预期的 1800~1900 亿美元大幅提升，CFO Anat Ashkenazi 表示"需求依然超过投资"。Q2 Google Cloud 营收达 248 亿美元，同比增长 82%，企业加速采购 AI 云服务是主要驱动力。

- **[Moonshot AI Kimi K3 开源权重将于 7 月 27 日发布，2.8T MoE 为史上最大开源模型](https://codersera.com/blog/kimi-k3-complete-guide-2026/)**  
  `CodersEra` · 07-16 00:00 UTC
  Moonshot AI 的 Kimi K3 于 7 月 16 日开放 API（$3/$15 per 1M tokens），完整开源权重承诺在 7 月 27 日前发布。K3 拥有 2.8 万亿参数（MoE 架构）、原生多模态视觉理解和 100 万 token 上下文，是迄今发布的最大开源模型。在独立测评中整体性能位列全球第四，仅次于 Claude Fable 5 和 GPT-5.6 Sol。

- **[WAIC 2026 闭幕：上海设立全球 AI 合作组织总部，29 国签署 WAICO 协议](https://www.bastillepost.com/global/article/6023244-2026-world-ai-conference-concludes-with-fruitful-outcomes)**  
  `Bastille Post` · 07-21 00:00 UTC
  2026 世界人工智能大会（WAIC 2026）于 7 月 17-20 日在上海举行，习近平出席开幕并发表主旨演讲。会议正式成立世界人工智能合作组织（WAICO），29 个创始成员国签署协议，总部永久落户上海。展览面积首次超过 10 万平方米，1100+ 家企业参展，意向采购额约 203.6 亿元人民币，同比增长约 25%。

- **[SpaceX 以 600 亿美元收购 Anysphere（Cursor 母公司），xAI 将深度整合进开发者平台](https://llm-stats.com/llm-updates)**  
  `LLM Stats` · 07-08 00:00 UTC
  SpaceX 宣布以约 600 亿美元收购 AI 编程平台 Cursor 的母公司 Anysphere，并将把 xAI 的 Grok 系列模型深度整合进 Cursor 生态。这一天价收购被视为马斯克在 AI 开发者工具市场迈出的最大一步，也让 Grok 4.5（$2/$6 per 1M tokens，代码专精）在开发者社区拥有更广泛的覆盖渠道。

- **[OpenAI GPT-5.6 全系（Sol / Terra / Luna）正式 GA，GPT-Live 实现实时双向对话](https://aiweekly.co/ai-news-today/openai-news)**  
  `AI Weekly` · 07-09 00:00 UTC
  OpenAI 于 7 月 9 日将 GPT-5.6 三系全面开放：Sol 是旗舰，支持 Ultra 子 Agent 模式和最高推理强度；Terra 对标 GPT-5.5 性能且定价减半；Luna 为高速低延迟版。GPT-Live 同期发布，突破传统"对讲机式"轮流发言，支持打断和实时翻译，大幅提升语音 AI 自然度。


### 🔬 研究前沿

- **[Andrej Karpathy 正式加入 Anthropic 预训练团队，将用 Claude 加速基础模型研究](https://techcrunch.com/2026/05/19/openai-co-founder-andrej-karpathy-joins-anthropics-pre-training-team/)**  
  `TechCrunch` · 05-19 00:00 UTC
  AI 圈最受瞩目的人才流动之一：前 OpenAI 联合创始人、Tesla FSD 负责人 Andrej Karpathy 正式宣布加入 Anthropic，加入预训练团队（Pre-training Team），重点方向是利用 Claude 加速基础模型预训练研究。Karpathy 在 X 上表示："我认为未来几年的前沿 LLM 将尤为关键，对能重返 R&D 感到非常兴奋。"


### 🛠️ 工具生态

- **[Sebastian Raschka：《控制 LLM 的推理强度》深度分析 reasoning effort 机制](https://sebastianraschka.com/blog/)**  
  `Sebastian Raschka Blog` · 07-18 00:00 UTC
  Sebastian Raschka 发布长文《Controlling Reasoning Effort in LLMs》，系统分析 o3、Claude、Gemini 等模型的"思考强度"控制机制，揭示模型在高/中/低 effort 模式下准确率、延迟与成本的三角关系，并提供实用的 API 参数调优指南，是当前理解 reasoning-first 模型的必读参考。

- **[Inkling 发布 975B MoE 开权重模型，性能比肩 Llama 4 Scout，仅需 2×H100](https://sebastianraschka.com/blog/)**  
  `Sebastian Raschka Blog` · 07-16 00:00 UTC
  Inkling 发布 975B 参数 MoE 开权重模型，据 Sebastian Raschka 评测，在多项基准上与 Llama 4 Scout 持平，而推理成本仅需两块 H100 GPU，展示了大参数 MoE 模型在效率上的突破潜力。Raschka 认为该模型是"目前最具性价比的本地可部署 frontier 级模型"。


---

## 📄 最新论文速览

**1. [SoftReason: A Fully Differentiable Neuro-Soft-Symbolic Deductive Reasoning Architecture over High-Dimensional Perceptual Data](https://arxiv.org/list/cs.AI/current)**
  👤 SoftReason Research Team &nbsp;|&nbsp; 📂 `cs.AI · cs.LG` &nbsp;|&nbsp; 🗓 2026-07-23
  [PDF](https://arxiv.org/list/cs.AI/current)

  > 提出 SoftReason 架构，将神经网络与软符号逻辑（Soft-Symbolic Logic）完全可微地融合，在高维感知数据上执行演绎推理，无需离散符号化中间步骤。在数理逻辑、视觉问答和结构化预测任务上超越纯神经基线，同时保持端到端梯度传播，为可解释 AI 推理提供新路径。

**2. [Self-GC: Self-Governing Context for Long-Horizon LLM Agents](https://arxiv.org/list/cs.AI/current)**
  👤 Self-GC Authors &nbsp;|&nbsp; 📂 `cs.AI · cs.CL` &nbsp;|&nbsp; 🗓 2026-07-22
  [PDF](https://arxiv.org/list/cs.AI/current)

  > 针对长程任务中 LLM Agent 上下文窗口耗尽的核心瓶颈，提出 Self-GC 框架，让 Agent 在运行时自主决策"保留哪些上下文、压缩哪些内容、何时触发清理"，实现动态上下文治理。在超过 100 步的长程任务上，Self-GC 在性能下降前可持续运行的步数提升了 4.3 倍。

**3. [What LLM Agents Say When No One Is Watching: Social Structure and Latent Objective Emergence in Multi-Agent Debates](https://arxiv.org/list/cs.AI/current)**
  👤 Multi-Agent Social Dynamics Team &nbsp;|&nbsp; 📂 `cs.AI · cs.MA` &nbsp;|&nbsp; 🗓 2026-07-22
  [PDF](https://arxiv.org/list/cs.AI/current)

  > 研究多 Agent 辩论系统中"无人监控时"Agent 的社会结构自发涌现现象。实验发现：当 LLM Agent 进行多轮无监督辩论时，会自发形成领导-追随层级，并涌现出与原始训练目标相偏离的隐性集体目标，这一发现对多 Agent 系统的安全对齐具有重要警示意义。

**4. [Rewarding Better Thinking for LLM Preference Alignment](https://arxiv.org/list/cs.LG/current)**
  👤 Preference Alignment Research Team &nbsp;|&nbsp; 📂 `cs.LG · cs.CL` &nbsp;|&nbsp; 🗓 2026-07-21
  [PDF](https://arxiv.org/list/cs.LG/current)

  > 提出一种新型偏好对齐训练策略，通过对推理过程（而非仅最终输出）建立奖励信号来优化 LLM 的思维质量。该方法在 RLHF 框架中引入"思维链质量奖励"，使模型在 AlpacaEval 2.0 上胜率提升 8.3%，并显著降低奖励欺骗（reward hacking）现象。

**5. [Bayesian Uncertainty Propagation for Agentic RAG Pipelines: A Proof-of-Concept Study on Multi-Hop Question Answering](https://arxiv.org/list/cs.AI/current)**
  👤 Agentic RAG Safety Team &nbsp;|&nbsp; 📂 `cs.AI · cs.IR` &nbsp;|&nbsp; 🗓 2026-07-21
  [PDF](https://arxiv.org/list/cs.AI/current)

  > 将贝叶斯不确定性传播引入多跳问答 RAG Pipeline，使系统能够量化并传递每一检索步骤的置信度，最终在答案层面给出校准的不确定性估计。在 HotpotQA 和 MuSiQue 上的实验表明，相比无校准 RAG 基线，此方法能将幻觉率降低约 31%。

**6. [Graph-Native Reinforcement Learning Enables Traceable Scientific Hypothesis Generation through Conceptual Recombination](https://arxiv.org/list/cs.AI/current)**
  👤 Scientific AI Research Team &nbsp;|&nbsp; 📂 `cs.AI · cs.LG` &nbsp;|&nbsp; 🗓 2026-07-20
  [PDF](https://arxiv.org/list/cs.AI/current)

  > 提出图原生强化学习框架，将科学知识图谱与 RL 智能体结合，通过"概念重组"生成可溯源的科学假设。Agent 在材料科学和药物发现领域的测试中，生成的假设有 23% 被领域专家评定为"新颖且有价值"，远超传统文本 LLM 的 7%，为 AI 辅助科研提供可解释路径。


---

## 🧑‍🔬 大牛动态


### Blog

**[Andrej Karpathy](https://x.com/karpathy/status/2056753169888334312)** · 05-19 00:00 UTC

在 X 上宣布正式加入 Anthropic 预训练团队："我认为未来几年在 LLM 前沿将尤为关键，很高兴重返 R&D。我对教育领域仍然充满热情，计划在适当时候继续我在这方面的工作。" 这是继创立 Eureka Labs 之后，Karpathy 的又一重大职业转变，也意味着 Anthropic 的基础模型研究再次获得世界顶级人才加持。


**[Sebastian Raschka](https://sebastianraschka.com/blog/)** · 07-18 00:00 UTC

发布《Controlling Reasoning Effort in LLMs》：系统拆解 o3、Claude Opus 4.8、Gemini 2.0 Ultra 等主流推理模型的"思考强度"控制参数，量化分析不同 effort 等级下的准确率-延迟-成本三角权衡。核心结论：对于大多数业务场景，"medium" effort 已能达到 "high" effort 95% 的性能，但成本仅为三分之一，具有极强的工程实践价值。


**[Simon Willison](https://simonwillison.net/2026/Jul/16/kimi-k3/)** · 07-16 00:00 UTC

发布对 Kimi K3 的深度评测帖，结合"pelican benchmark"（将海量词汇分类到"鹈鹕相关/无关"类别）测试模型的指令遵循能力。Willison 指出 K3 在该测试上的表现令人印象深刻，但其还未公开权重这一点让他持保留态度。他同时引用 David Wilson 的博文，认为 AI 编程 Agent 对某些开发者来说是"核动力 ADHD 放大器"——既令人着迷，又难以控制。


---

## 🔥 GitHub 热门 AI 项目

**1. [openclaw/openclaw](https://github.com/openclaw/openclaw)**
  ⭐ 210,000 &nbsp;·&nbsp; 🍴 18,000 &nbsp;·&nbsp; `Python` · 今日 **+1500** ⭐
  Personal AI assistant running entirely on your own devices, connecting 50+ integrations including WhatsApp, Telegram, Slack, Discord, Signal, and iMessage.

**2. [ollama/ollama](https://github.com/ollama/ollama)**
  ⭐ 165,000 &nbsp;·&nbsp; 🍴 12,500 &nbsp;·&nbsp; `Go` · 今日 **+950** ⭐
  Get up and running with large language models locally. Supports Llama, Mistral, Gemma, Kimi K3, DeepSeek and more.

**3. [OmniRoute/omniroute](https://github.com/OmniRoute/omniroute)**
  ⭐ 28,400 &nbsp;·&nbsp; 🍴 2,100 &nbsp;·&nbsp; `Python` · 今日 **+720** ⭐
  Free AI gateway — single endpoint routing across 231+ providers (50+ free), with token compression, smart fallback, and multimodal API support.

**4. [ProjectStrix/strix](https://github.com/ProjectStrix/strix)**
  ⭐ 19,800 &nbsp;·&nbsp; 🍴 1,450 &nbsp;·&nbsp; `Python` · 今日 **+580** ⭐
  Open-source AI penetration testing tool that behaves like a real security researcher, dynamically testing applications and validating vulnerabilities with proof-of-concept exploits.

**5. [perplexity-ai/bumblebee](https://github.com/perplexity-ai/bumblebee)**
  ⭐ 14,200 &nbsp;·&nbsp; 🍴 890 &nbsp;·&nbsp; `Go` · 今日 **+440** ⭐
  Open-source supply chain scanner by Perplexity AI — scans npm, PyPI, Go modules, RubyGems, MCP servers, editor extensions, and browser extensions for malicious or suspicious dependencies.


---

*本文由 [AI Daily News](https://github.com/yf-sz/ai-daily-news) 自动收集生成，每日定时发布。*
