---
layout: post
title: "AI 日报 · 2026年07月07日"
date: 2026-07-07 08:00:00 +0000
categories:
  - "AI日报"
tags:
  - "AI"
  - "AI日报"
  - "每日新闻"
  - "人工智能"
  - "LLM"
  - "Agent"
  - "Anthropic"
  - "Claude"
  - "Multimodal"
description: "今日 AI 速报：7 条资讯 · 5 篇论文 · 3 条大牛动态 · 7 个热门项目"
toc: true
---

> **今日 AI 速报：7 条资讯 · 5 篇论文 · 3 条大牛动态 · 7 个热门项目**
> 数据来源：RSS · arXiv · GitHub Trending · Web Search
> 生成时间：2026-07-07 08:00 UTC

---

## 📰 今日 AI 资讯

### 🏭 产业动态

- **[Claude Fable 5 今日起结束免费订阅权益，全面转为按量计费](https://www.anthropic.com/news)**  
  `Anthropic` · 07-07 UTC  
  7 月 7 日是 Claude Fable 5 纳入 Pro、Max、Team 及部分 Enterprise 订阅计划免费使用的最后一天。从 7 月 8 日起，Fable 5 的使用将扣除订阅套餐以外的额外用量积分，API 定价维持 $10/$50（每百万 input/output tokens）不变。此次调整标志着 Anthropic 旗舰模型从"订阅捆绑"转向"按量收费"新阶段。

- **[联合国首届全球 AI 治理对话在日内瓦召开，169 国代表出席](https://news.un.org/en/story/2026/07/1167848)**  
  `UN News` · 07-06 UTC  
  联合国首届全球 AI 治理对话于 7 月 6–7 日在日内瓦举行，169 个国家代表参与多边磋商。对话结束后即举办 ITU AI for Good 全球峰会（7 月 7–10 日）。这是国际社会在 AI 监管框架上迄今规模最大的政府级协商，主要议题涵盖 AI 安全基准、算法透明度标准和跨境数据流动规则。

- **[OpenAI GPT-5.6 三款子模型定价出炉，Sol/Terra/Luna 差异化布局](https://llm-stats.com/llm-updates)**  
  `LLM Stats` · 07-06 UTC  
  OpenAI 确认 GPT-5.6 系列定价：旗舰款 Sol 为 $5/$30、中档款 Terra 为 $2.50/$15、轻量款 Luna 为 $1/$6（每百万 input/output tokens）。Sam Altman 表示将在 7 月 7–14 日窗口期扩大公众访问权限，白宫自愿 AI 标准框架公告也将于近日发布。三档定价策略标志着 OpenAI 从"单一旗舰"转向梯度化产品组合。

- **[Anthropic 发布 Claude Science Beta：接入 60+ 科学数据库的多 Agent 科研工作台](https://www.anthropic.com/news/claude-science-ai-workbench)**  
  `Anthropic` · 07-04 UTC  
  Claude Science 正式进入公开 Beta，面向所有付费订阅用户开放。该平台连接 Opus 4.8 与超过 60 个精选科学数据库，涵盖基因组学、单细胞测序、蛋白质组学、结构生物学和化学信息学，并集成 NVIDIA BioNeMo Agent Toolkit。用户通过单一对话界面即可完成文献检索、数据分析、可视化和论文初稿撰写，全程可复现、有代码溯源。AI for Science 资助计划申请截止 7 月 15 日，最高提供 3 万美元 credits。

- **[小米 MiMo-V2.5-Pro 跻身 OpenRouter 周流量榜首，中国 AI 模型占平台 45% 流量](https://openrouter.ai/xiaomi/mimo-v2.5-pro)**  
  `OpenRouter` · 07-05 UTC  
  小米 MiMo-V2.5-Pro 以每周 4.21 万亿 tokens 的处理量成为 OpenRouter 平台流量最大的单一模型，占平台总量 21.1%，超过 OpenAI 的 7.5%。中国 AI 服务商合计占 OpenRouter 流量约 45%，较一年前不足 2% 急剧攀升。MiMo-V2.5-Pro 拥有超过 1 万亿参数和 100 万 token 上下文，在 ClawEval、SWE-bench Pro 等基准上排名领先，且价格仅为同级别西方模型的 1/5 至 1/25。

- **[Google Gemini 3.5 Pro 进入企业预览，2M token 上下文窗口全面开放](https://llm-stats.com/ai-news)**  
  `LLM Stats` · 07-06 UTC  
  Gemini 3.5 Pro 在 Vertex AI 企业预览扩大后，正式开始向开发者平台渐进推送。该模型提供 200 万 token 上下文窗口，标准档定价约 $1.25/$10（每百万 tokens），内置深度思考推理模式，在 GPQA Diamond 上达到 82.4%，MMLU-Pro 达到 89.8%。此前因安全审查推迟至 7 月的正式 GA 版本预计本月内落地。

- **[Meta Watermelon 内测：据称性能匹配 GPT-5.5，训练算力为上代十倍](https://siliconangle.com/2026/07/03/openai-offers-feds-stake-anthropic-gets-ai-model-jail-meta-wants-neocloud/)**  
  `SiliconANGLE` · 07-03 UTC  
  Meta 代号 Watermelon 的新一代旗舰模型在内部评测中据称达到 GPT-5.5 同级别性能，训练算力为前代的十倍量级。与此同时，Meta 宣布约 8000 名员工（约 10% 人力）裁员，另有 7000 人被调配至 AI 专项团队，标志着 Meta 在组织层面全面向 AI 优先转型。Watermelon 暂无公开发布时间表。

---

## 📄 最新论文速览

**1. [Perception-Aware Policy Optimization for Multimodal Reasoning](https://arxiv.org/abs/2507.06448)**
  👤 多位作者 &nbsp;|&nbsp; 📂 `cs.LG · cs.CV` &nbsp;|&nbsp; 🗓 2026-07-07
  [PDF](https://arxiv.org/pdf/2507.06448)

  > 现有 RLVR（Reinforcement Learning with Verifiable Rewards）方法在训练多模态推理模型时，主要优化语言推理链，而忽略视觉感知错误这一主要失败来源。本文提出 PAPO（感知感知策略优化），在策略梯度目标中引入视觉感知校准损失，使模型在"学会推理"的同时"学会感知"。在多个多模态基准上，PAPO 相比标准 RLVR 方法提升 4–9 个百分点。

**2. [World Models: A Comprehensive Survey of Architectures, Methodologies, Reasoning Paradigms, and Applications](https://arxiv.org/abs/2507.00000)**
  👤 多位作者 &nbsp;|&nbsp; 📂 `cs.AI · cs.LG` &nbsp;|&nbsp; 🗓 2026-07-05
  [PDF](https://arxiv.org/pdf/2507.00000)

  > 本综述系统梳理"世界模型"领域的主流架构（基于 Transformer、扩散模型、状态空间模型）、训练范式（预测性、生成性、混合式）和应用场景（机器人规划、游戏 AI、自动驾驶、科学发现）。作者提出统一的世界模型能力评估框架，并梳理了当前在时序一致性、泛化能力和样本效率方面的主要挑战与未来方向。

**3. [Tool-Call Dependency Structure is Linearly Decodable in LLM Agent Residual Streams](https://arxiv.org/abs/2605.25310)**
  👤 多位作者 &nbsp;|&nbsp; 📂 `cs.AI · cs.LG` &nbsp;|&nbsp; 🗓 2026-05-30
  [PDF](https://arxiv.org/pdf/2605.25310)

  > 本文通过机理可解释性方法发现：LLM Agent 在规划工具调用序列时，其残差流中的中间表征已线性编码了工具之间的依赖关系（如"需先调用 A 才能调用 B"）。利用这一线性结构，作者设计了一种轻量级探针可实时预测工具调用顺序错误，为 Agent 系统的运行时监控和调试提供了新思路。

**4. [Skill Reuse as Compression in Agentic RL](https://arxiv.org/abs/2605.31509)**
  👤 多位作者 &nbsp;|&nbsp; 📂 `cs.LG · cs.AI` &nbsp;|&nbsp; 🗓 2026-06-01
  [PDF](https://arxiv.org/pdf/2605.31509)

  > 本文将强化学习中的技能复用理解为"策略压缩"：Agent 习得的可复用技能本质上是对高频行为模式的有损压缩表示。作者在多任务 Agentic RL 环境中验证：显式技能压缩目标可让 Agent 在新任务上的样本效率提升 30–50%，同时保持跨任务泛化能力。该工作为分层强化学习和终身学习提供了新的理论视角。

**5. [Beyond Next-Token Prediction: An RLVR Proof of Concept for Tool-Use Agents on Atlassian Workflows](https://arxiv.org/abs/2507.03100)**
  👤 Karthikeya Aditya Vissa 等 &nbsp;|&nbsp; 📂 `cs.AI · cs.LG` &nbsp;|&nbsp; 🗓 2026-07-04
  [PDF](https://arxiv.org/pdf/2507.03100)

  > 本文在 Atlassian 工作流（Jira、Confluence 等）上，将 RLVR 方法应用于工具使用 Agent 训练，以"任务最终结果"作为奖励信号取代传统的 next-token 监督。结果显示，经 RLVR 微调的 7B 模型在多步工具调用任务上超越未经过对齐的 70B 基线，为生产级 Agentic 系统的轻量化提供了实证依据。

---

## 🧑‍🔬 大牛动态

### Blog

**[Simon Willison](https://simonwillison.net/)** · 07-03 UTC

在最新博文中，Simon Willison 分享了一个实用的编码 Agent 模式："对所有编码任务，应自行判断并在子 Agent 中运行合适的低功耗模型。"其核心逻辑是：实现类工作很少需要顶级模型，判断、审查和综合才需要主循环保留旗舰模型。他同时记录了使用 Claude Fable 5 与 GPT-5.5 组合处理 sqlite-utils 4.0 积压 issue 的实际体验，主张在多模型协作中精细匹配任务复杂度与模型层级以控制成本。

**[Demis Hassabis](https://www.fastcompany.com/91563254/google-deepmind-ceo-says-these-are-the-skills-that-will-set-humans-apart-from-ai)** · 07-02 UTC

在接受 Fast Company 专访时，Demis Hassabis 指出将使人类区别于 AI 的核心能力是"元认知"（对自身思维过程的理解与调控）、"意义构建"和"跨领域直觉"。他坚持 AGI 到来时间约在 2030 年左右（±1年），并强调即将到来的 AGI 并不意味着人类无用，而是需要人类掌握与 AI 协作的新型技能。他将 AI 的潜在影响力比作"工业革命的十倍速度和十倍规模"。

### Twitter/X

**[Sam Altman](https://openai.com/news/)** · 07-06 UTC

Sam Altman 在社交平台表示，GPT-5.6 的公众访问扩展窗口为 7 月 7–14 日，白宫的自愿 AI 标准框架公告亦将在此期间发布。他同时回应外界对 OpenAI 向美国政府提议 5% 股权换取合作方案的质疑，强调这是"探索 AI 与民主政府深度合作的新模式"，而非出售公司控制权。OpenAI 当前估值约 8512 亿美元，5% 股权约折合 426 亿美元。

---

## 🔥 GitHub 热门 AI 项目

**1. [usestrix/strix](https://github.com/usestrix/strix)**
  ⭐ 37,971 &nbsp;·&nbsp; 🍴 — &nbsp;·&nbsp; `Python` · 今日 **+10,759** ⭐
  Open-source AI penetration testing tool to find and fix your app's vulnerabilities.

**2. [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)**
  ⭐ 34,317 &nbsp;·&nbsp; 🍴 — &nbsp;·&nbsp; `Python` · 今日 **+6,039** ⭐
  World's first open-source, agentic video production system. 12 pipelines, 52 tools, 500+ agent skills.

**3. [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire)**
  ⭐ 11,121 &nbsp;·&nbsp; 🍴 — &nbsp;·&nbsp; `Python` · 今日 **+4,616** ⭐
  AI-era Berkshire: a value investing research framework built for Claude Code / Codex. 4 masters' methodologies + multi-agent adversarial analysis.

**4. [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)**
  ⭐ 55,119 &nbsp;·&nbsp; 🍴 — &nbsp;·&nbsp; `Python` · 今日 **+3,432** ⭐
  LLM-driven multi-market stock analysis with real-time news, decision dashboards, and automated notifications for zero-cost scheduled operations.

**5. [browser-use/video-use](https://github.com/browser-use/video-use)**
  ⭐ 15,448 &nbsp;·&nbsp; 🍴 — &nbsp;·&nbsp; `Python` · 今日 **+3,706** ⭐
  Edit videos with coding agents.

**6. [browser-use/browser-use](https://github.com/browser-use/browser-use)**
  ⭐ 103,138 &nbsp;·&nbsp; 🍴 — &nbsp;·&nbsp; `Python` · 今日 **+1,788** ⭐
  Make websites accessible for AI agents. Automate tasks online with ease.

**7. [topoteretes/cognee](https://github.com/topoteretes/cognee)**
  ⭐ 27,255 &nbsp;·&nbsp; 🍴 — &nbsp;·&nbsp; `Python` · 今日 **+1,825** ⭐
  Open-source AI memory platform providing persistent long-term memory for agents via self-hosted knowledge graphs.

---

*本文由 [AI Daily News](https://github.com/yf-sz/ai-daily-news) 自动收集生成，每日定时发布。*
