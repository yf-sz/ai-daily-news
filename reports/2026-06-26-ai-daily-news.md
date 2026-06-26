---
layout: post
title: "AI 日报 · 2026年06月26日"
date: 2026-06-26 00:00:00 +0000
categories:
  - "AI日报"
tags:
  - "AI日报"
  - "人工智能"
  - "每日新闻"
  - "LLM"
  - "AI Agent"
  - "Google DeepMind"
  - "Anthropic"
  - "Claude"
description: "今日 AI 速报：6 条资讯 · 5 篇论文 · 3 条大牛动态 · 6 个热门项目。Google 单周四位顶级 AI 科学家出走；Gemini 3.5 Pro 延期至 7 月；Karpathy Loop 自动研究技术细节披露"
toc: true
---

> **今日 AI 速报：6 条资讯 · 5 篇论文 · 3 条大牛动态 · 6 个热门项目**
> 数据来源：Web Search · arXiv · GitHub Trending
> 生成时间：2026-06-26 00:00 UTC

---

## 📰 今日 AI 资讯

### 🏭 产业动态

- **[Google 单周痛失四位顶尖 AI 科学家，Alphabet 股价累跌逾 5%](https://fortune.com/2026/06/23/google-deepmind-ai-researcher-departures-raise-doubts-about-ability-to-win-the-ai-race-shazeer-jumper-eye-on-ai/)**
  `Fortune / Bloomberg` · 06-24
  一周之内，Google 接连失去四位核心 AI 研究员：Gemini 联合主导者、《Attention Is All You Need》共同作者 Noam Shazeer 赴 OpenAI（6-18 宣布）；AlphaFold 诺奖得主 John Jumper 赴 Anthropic（6-20 宣布）；AI 编程负责人 Jonas Adler 与训练核心成员 Alexander Pritzel 亦被 Bloomberg 于 6-24 爆出即将加入 Anthropic。Alphabet 股价因此累计下跌超 5%，分析师警告"前沿 AI 实验室依赖少数人做最难的工作，一周内同时失去四人是无法忽视的信号"。

- **[Gemini 3.5 Pro 发布正式延期至 7 月 2026](https://cryptobriefing.com/google-delays-gemini-35-pro-launch-to-july-2026/)**
  `Crypto Briefing / Analytics Insight` · 06-24
  原计划 6 月发布的 Gemini 3.5 Pro 正式延期至 7 月，官方未说明具体原因，分析人士认为与复杂任务性能优化及内部测试延长有关。该模型目标包括 200 万 token 上下文窗口、"Deep Think" 深度推理模式，定价预计约为 $15/百万输入 token、$60/百万输出 token（约为 Flash 的 10 倍）。与此同时，Gemini 3.5 Flash 在多数基准上已落后于 Anthropic 和 OpenAI 最新模型，市场对 Pro 版的期待与怀疑并存，预测平台给出年内发布概率约 50—55%。

- **[Anthropic Claude Code 领跑 AI 编程市场，微软 Google 奋力追赶](https://www.cnbc.com/2026/06/01/microsoft-and-google-take-on-anthropic-and-openai-in-ai-coding-models.html)**
  `CNBC` · 06-24
  AI 编程工具市场预计以年均 26% 的速度扩张，从当前 93 亿美元增至 2031 年约 300 亿美元。Anthropic Claude Code 目前处于明显领先地位，微软依托 GitHub Copilot 生态、Google 则以 Antigravity + Gemini Code Assist Enterprise 迎战。分析师指出，多位顶尖研究员的离开或进一步扩大 Anthropic 在 AI 编程方向的人才与技术积累优势。

### 🔬 研究前沿

- **["Karpathy Loop" 自动研究细节正式披露：700 实验 · 2 天 · 11% 训练提速](https://fortune.com/2026/03/17/andrej-karpathy-loop-autonomous-ai-agents-future/)**
  `Fortune / NextBigFuture` · 06-25
  Karpathy 领导的 Anthropic 预训练研究团队正式披露"自动研究循环"技术路径：使用单个 markdown 提示词和约 630 行训练代码，AI 编程 agent 在单 GPU 上自主运行 700 次小规模训练实验，历时两天自我发现 20 项优化，将模型训练时间压缩 11%。Karpathy 称其为"自动研究"（autoresearch），目标是将该循环嵌入 Claude 下一代预训练流程，让 AI 加速自身训练研究，压缩人工研究周期。

- **[IBM Think 2026：下一代 watsonx Orchestrate 与 OpenRAG 亮相](https://llm-stats.com/llm-updates)**
  `IBM` · 06-24
  IBM Think 2026 大会推出下一代 watsonx Orchestrate（企业级多 Agent 编排平台）、OpenRAG（基于 watsonx.data 的开放检索增强生成框架）、Engineering AI Hub 1.3 及 Guardium AI 监控套件，聚焦企业 AI 工作流的安全、合规与可观测性，是当前企业 AI 平台生态的重要扩充。

### 💰 市场观察

- **[OpenAI IPO 最新进展：拟 9 月上市，估值区间 7300—8500 亿美元](https://aiweekly.co/alerts/openai-files-confidential-ipo-targeting-850b-valuation)**
  `AI Weekly / CNBC` · 06-24
  OpenAI 与 Anthropic 将共同构成 2026 年规模最大的 AI 公司 IPO 集群，与 SpaceX IPO 路演同期进行。OpenAI 目标估值 7300—8500 亿美元，高盛和摩根士丹利承销；Anthropic 目标万亿美元估值。预测市场对两家公司年内正式上市的概率判断均超 60%，业界预计此次 AI 上市潮将是科技史上最受关注的集中 IPO 窗口之一。

---

## 📄 最新论文速览

**1. [Claudini: Autoresearch Discovers State-of-the-Art Adversarial Attack Algorithms for LLMs](https://arxiv.org/pdf/2603.24511)**
  👤 Anthropic Research Team &nbsp;|&nbsp; 📂 `cs.CR` · `cs.AI` &nbsp;|&nbsp; 🗓 2026-03-31
  [PDF](https://arxiv.org/pdf/2603.24511)

  > 利用自动研究范式（Autoresearch），Claude agent 自主探索并发现了针对 LLM 的先进对抗性攻击算法，在红队测试准确率上超越现有人工设计基线。研究展示了 AI 辅助安全研究的可行路径，同时也引发了关于 AI 自动化安全研究伦理边界的广泛讨论。

**2. [MasHost Builds It All: Autonomous Multi-Agent System Directed by Reinforcement Learning](https://arxiv.org/pdf/2506.08507)**
  👤 Multiple Authors &nbsp;|&nbsp; 📂 `cs.AI` · `cs.MA` &nbsp;|&nbsp; 🗓 2026-06-10
  [PDF](https://arxiv.org/pdf/2506.08507)

  > MasHost 提出基于强化学习的自主多 Agent 系统，通过统一调度框架指挥异构 Agent 协同完成复杂任务，在代码生成、文档处理和数据分析等多项基准上取得突破性成绩，为 Multi-Agent 编排领域提供了新的技术路径。

**3. [OpenVLThinkerV2: A Generalist Multimodal Reasoning Model for Multi-domain Visual Tasks](https://arxiv.org/pdf/2604.08539)**
  👤 Multiple Authors &nbsp;|&nbsp; 📂 `cs.CV` · `cs.AI` &nbsp;|&nbsp; 🗓 2026-04-11
  [PDF](https://arxiv.org/pdf/2604.08539)

  > OpenVLThinkerV2 通过引入视觉链式思考（VCoT）机制和跨域迁移训练策略，在数学推理、图表理解、空间感知等多类视觉任务上显著超越前作，无需任务特定微调即可适配多种视觉场景，是通用多模态推理的重要进展。

**4. [Retrieval-Augmented LLM Agents: Learning to Learn from Experience](https://arxiv.org/pdf/2603.18272)**
  👤 Multiple Authors &nbsp;|&nbsp; 📂 `cs.CL` · `cs.AI` &nbsp;|&nbsp; 🗓 2026-03-23
  [PDF](https://arxiv.org/pdf/2603.18272)

  > 提出基于经验检索增强的 LLM Agent 训练框架，Agent 能够存储并检索历史交互轨迹中的成功经验，实现"从经验中学习"的自适应推理，在复杂多步任务上相比标准 RAG 基线提升显著。

**5. [Agent-Omit: Training Efficient LLM Agents for Adaptive Thought and Observation Omission via Agentic Reinforcement Learning](https://arxiv.org/pdf/2602.04284)**
  👤 Multiple Authors &nbsp;|&nbsp; 📂 `cs.AI` · `cs.LG` &nbsp;|&nbsp; 🗓 2026-02-07
  [PDF](https://arxiv.org/pdf/2602.04284)

  > 提出通过 Agentic RL 训练的高效 LLM Agent 框架，Agent 能够自适应省略冗余思维链步骤和无关工具观察，相比标准 CoT-ReAct Agent 大幅降低 token 消耗，同时任务完成率基本持平，推进了 Agent 推理效率研究。

---

## 🧑‍🔬 大牛动态

### Research

**[Andrej Karpathy @ Anthropic](https://www.revolutioninai.com/2026/05/how-ai-automates-its-own-training-karpathy-anthropic.html)** · 06-25

> 披露"Karpathy Loop"自动研究项目进展：他所领导的 Anthropic 预训练研究团队正将 AI Agent 自主实验循环集成进 Claude 下一代预训练流程。他表示这是"将 AI 加速 AI 研究"从实验推向生产的关键一步，并预计类似的自动研究范式将在未来 12 个月内成为主要前沿实验室的标配工具。

### Newsletter

**[Sebastian Raschka](https://magazine.sebastianraschka.com/p/llm-research-papers-2026-part1)** · 06-2026

> 在 Ahead of AI newsletter 发布 2026 年 1–5 月 LLM 研究论文年度汇编，总结今年四大前沿主题：效率优化（量化、稀疏化、低秩适配）、AI 对齐（RLHF 迭代、宪法 AI 延伸研究）、长上下文推理（超百万 token 处理）与多模态理解（视觉-语言统一推理）。文章已成为社区公认的 2026 上半年论文导航地图。

### Twitter/X

**[Simon Willison](https://simonwillison.net)** · 06-24

> 在博客及 X 上发长文深度分析 Google 人才大规模流失现象，重点指出：顶级 AI 研究者的流向往往是判断各实验室技术影响力的"先行指标"。当前 Anthropic 预训练和科学研究团队在短期内集中获得 John Jumper、Jonas Adler、Alexander Pritzel 和 Andrej Karpathy 四位重量级人物，Claude 下一代模型的竞争力值得密切关注。

---

## 🔥 GitHub 热门 AI 项目

**1. [openclaw/openclaw](https://github.com/openclaw/openclaw)**
  ⭐ 247,000+ &nbsp;·&nbsp; 🍴 35,000 &nbsp;·&nbsp; `TypeScript`
  2026 年增长最快的开源 AI 项目。本地运行的个人 AI 助手，通过网关连接 WhatsApp、Telegram、Slack、Discord、Signal 等 50+ 平台，无需云端即可使用任意 AI 模型，被誉为"史上增长最快的开源 AI 仓库"。

**2. [ollama/ollama](https://github.com/ollama/ollama)**
  ⭐ 174,000 &nbsp;·&nbsp; 🍴 14,600 &nbsp;·&nbsp; `Go`
  本地运行大模型的首选工具，支持 Llama、Mistral、Gemma 等主流模型，一行命令启动本地 LLM 推理服务。2026 年大幅扩展硬件支持至 AMD、Intel Arc 及 TPU。

**3. [mendableai/firecrawl](https://github.com/mendableai/firecrawl)**
  ⭐ 130,000+ &nbsp;·&nbsp; 🍴 N/A &nbsp;·&nbsp; `TypeScript`
  大规模网页搜索与抓取框架，将任意页面转换为干净 Markdown、结构化 JSON、截图或 Agent 可直接消费的数据，是 AI Agent 工具链的核心基础设施之一。

**4. [open-webui/open-webui](https://github.com/open-webui/open-webui)**
  ⭐ 124,000 &nbsp;·&nbsp; 🍴 14,500 &nbsp;·&nbsp; `Python`
  自托管 AI 界面，支持 Ollama 和 OpenAI 兼容 API，累计下载量超 2.82 亿次，可完全离线运行，是最主流的自托管 ChatGPT 替代方案。

**5. [comfyanonymous/ComfyUI](https://github.com/comfyanonymous/ComfyUI)**
  ⭐ 106,000+ &nbsp;·&nbsp; 🍴 N/A &nbsp;·&nbsp; `Python`
  基于节点的图像生成可视化工作流系统，为 Stable Diffusion 等模型提供细粒度流程控制，已成为创意工作者和研究者的首选图像生成工具。

**6. [vllm-project/vllm](https://github.com/vllm-project/vllm)**
  ⭐ 83,000 &nbsp;·&nbsp; 🍴 N/A &nbsp;·&nbsp; `Python`
  生产级高性能 LLM 推理框架，PagedAttention 算法显著提升 GPU 内存利用率，2026 年扩展至 AMD、Intel Arc 及 TPU，提供 OpenAI 兼容 API，是企业侧 LLM 部署首选，吞吐量较 Ollama 高出约 19 倍（高并发场景）。

---

*本文由 [AI Daily News](https://github.com/yf-sz/ai-daily-news) 使用 web_search 自动收集生成，每日定时发布。*
