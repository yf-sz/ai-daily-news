---
layout: post
title: "AI 日报 · 2026年06月29日"
date: 2026-06-29 08:00:00 +0000
categories:
  - "AI日报"
tags:
  - "AI"
  - "AI日报"
  - "每日新闻"
  - "人工智能"
  - "LLM"
  - "Agent"
  - "Gemini"
  - "Anthropic"
description: "今日 AI 速报：6 条资讯 · 5 篇论文 · 3 条大牛动态 · 7 个热门项目"
toc: true
---

> **今日 AI 速报：6 条资讯 · 5 篇论文 · 3 条大牛动态 · 7 个热门项目**
> 数据来源：RSS · arXiv · GitHub Trending · Web Search
> 生成时间：2026-06-29 08:00 UTC

---

## 📰 今日 AI 资讯

### 🏭 产业动态

- **[Transformer 共同作者 Noam Shazeer 离开 DeepMind，加盟 OpenAI 主导架构研究](https://www.cnbc.com/2026/06/18/google-gemini-co-lead-noam-shazeer-leaves-for-openai.html)**  
  `CNBC` · 06-18 UTC  
  Gemini 共同负责人、"Attention Is All You Need" 共同作者 Noam Shazeer 正式加盟 OpenAI，担任架构研究负责人。Shazeer 两年前通过约 27 亿美元的收购交易重返谷歌，此番跳槽被 Sam Altman 称为"筹谋了 10 年"。与此同时，诺贝尔化学奖得主 John Jumper（AlphaFold 负责人）也于 6 月 20 日宣布离开 DeepMind 加入 Anthropic，DeepMind 6 天内痛失 4 位高管。

- **[Google Gemini 3.5 Flash 正式发布：速度与质量双优，全面 GA](https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/)**  
  `Google Blog` · 06-27 UTC  
  Google 正式发布 Gemini 3.5 Flash，现已通过 Gemini API、Google AI Studio 及 Android Studio 全面开放。官方称该模型在复杂编程和 Agent 基准上超越 Gemini 3.1 Pro，同时以更低延迟运行。此外，Google 推出 24/7 后台运行的 Search Agent，可持续追踪用户关注的话题与任务，并主动推送更新。

- **[OpenAI GPT-4.5 正式退役，GPT-5.6 发布大概率延至 7 月](https://www.buildfastwithai.com/blogs/ai-news-today-june-27-2026)**  
  `BuildFastWithAI` · 06-27 UTC  
  OpenAI GPT-4.5 于 6 月 27 日完成退役，所有现有对话自动迁移至 GPT-5.5。与此同时，GPT-5.6 的 Polymarket 预测发布概率已从 83% 骤降至 18%，意味着该模型大概率延至 7 月发布。GPT-5.6 据报将配备 150 万 Token 上下文窗口，比 GPT-5.5 的约 105 万 Token 大幅扩展。

- **[联邦法官裁令：特朗普政府不得将 Anthropic 列为安全威胁](https://www.cnbc.com/2026/06/26/openai-anthropic-new-ai-spending-reality-as-users-shift-to-efficiency.html)**  
  `CNBC` · 06-26 UTC  
  一位联邦法官向特朗普政府颁布禁令，要求撤销将 Anthropic 列为安全风险的行政决定。此前该指定引发市场对 Anthropic IPO 进程的担忧。这是 AI 行业与政府监管摩擦中罕见的司法胜利，进一步为 Anthropic 近万亿美元估值的上市计划扫清法律障碍。

- **[NAVER 与 NVIDIA 签署主权 AI 协议，以 55 兆瓦起步建设 HyperCLOVA X 算力集群](https://www.devflokers.com/blog/ai-news-june-2026-models-research-developments)**  
  `DevFlokers` · 06-27 UTC  
  NAVER 宣布利用 NVIDIA DSX 平台扩建主权 AI 基础设施，初期规模 55 兆瓦，用于支持下一代 HyperCLOVA X 模型训练及计划于 2026 年下半年在韩国上线的 AI Agent 平台。此举是亚洲科技巨头寻求不依赖美国云服务商的"算力自主"战略的最新案例。

- **[OpenAI 与 Anthropic 用户行为转变：效率优先取代"Token 最大化"](https://www.cnbc.com/2026/06/26/openai-anthropic-new-ai-spending-reality-as-users-shift-to-efficiency.html)**  
  `CNBC` · 06-26 UTC  
  随着企业对 AI API 成本意识提升，OpenAI 和 Anthropic 的企业用户正从追求超长上下文"tokenmaxxing"策略转向效率优先——主动压缩单次调用的 Token 消耗。这一趋势对两家公司的营收预期构成新的变量，也加速驱动模型厂商在推理性价比上的竞争。

---

## 📄 最新论文速览

**1. [GuessBench: Sensemaking Multimodal Creativity in the Wild](https://arxiv.org/abs/2506.00814)**
  👤 多位作者 &nbsp;|&nbsp; 📂 `cs.AI · cs.CV` &nbsp;|&nbsp; 🗓 2026-06-01
  [PDF](https://arxiv.org/pdf/2506.00814)

  > GuessBench 是首个系统评估多模态大模型"创意理解"能力的基准，包含数千张来自真实世界的创意图片（梗图、隐喻、跨文化视觉双关）。测试结果表明，当前最强的视觉语言模型在理解人类创意表达上仍与人类水平存在显著差距，揭示了多模态 AI 语义理解的深层局限。

**2. [MuSEAgent: A Multimodal Reasoning Agent with Stateful Experiences](https://arxiv.org/abs/2603.27813)**
  👤 多位作者 &nbsp;|&nbsp; 📂 `cs.AI · cs.CL` &nbsp;|&nbsp; 🗓 2026-03-28
  [PDF](https://arxiv.org/pdf/2603.27813)

  > MuSEAgent 提出一种带"有状态经验"的多模态推理 Agent 框架，使 Agent 在多轮任务中能复用并更新历史经验而非每次从零开始。在多模态 QA、视觉规划和跨模态推理基准上，MuSEAgent 相比无状态基线提升 18–26%，大幅降低重复推理开销。

**3. [Agentic Reasoning for Large Language Models](https://arxiv.org/abs/2601.12538)**
  👤 多位作者 &nbsp;|&nbsp; 📂 `cs.AI · cs.LG` &nbsp;|&nbsp; 🗓 2026-01-21
  [PDF](https://arxiv.org/pdf/2601.12538)

  > 这篇综述系统梳理了 LLM Agent 推理的核心范式，涵盖 ReAct、Tree-of-Thought、MCTS 引导推理和工具调用等主流方法，并分析各方法在长时域规划、错误恢复和效率上的权衡。作者提出"推理-行动闭环"统一框架，为下一代 Agentic AI 系统的设计提供理论基础。

**4. [ResearchGym: Evaluating Language Model Agents on Real-World AI Research](https://arxiv.org/abs/2602.15112)**
  👤 多位作者 &nbsp;|&nbsp; 📂 `cs.AI · cs.LG` &nbsp;|&nbsp; 🗓 2026-02-20
  [PDF](https://arxiv.org/pdf/2602.15112)

  > ResearchGym 构建了一个让 LLM Agent 执行完整 AI 科研任务的评估环境，包括文献综述、假设提出、实验设计与结果分析。测试表明，当前顶级模型在独立执行完整研究流程时成功率不足 30%，但在人机协作模式下效率提升显著，为 AI for Science 提供重要基线参考。

**5. [AI Can Learn Scientific Taste](https://arxiv.org/abs/2603.14473)**
  👤 多位作者 &nbsp;|&nbsp; 📂 `cs.AI · cs.LG` &nbsp;|&nbsp; 🗓 2026-03-18
  [PDF](https://arxiv.org/pdf/2603.14473)

  > 本文证明 AI 模型可以通过人类专家反馈学习"科学品味"——即对研究方向重要性的直觉判断。通过微调，模型预测顶级会议接收率的准确率超越多位博士研究生。这一结果引发学术界对 AI 在同行评审和科研方向筛选中应用潜力的广泛讨论。

---

## 🧑‍🔬 大牛动态

### Blog

**[Andrej Karpathy – "The Karpathy Loop"](https://letsdatascience.com/blog/karpathy-joins-anthropic-pretraining-team-may-19-2026)** · 06-26 UTC

Karpathy 5 月 19 日加入 Anthropic 领导预训练研究团队。近期他披露"Karpathy Loop"实验：AI Agent 在 48 小时内自主完成 700 次代码修改实验，对某语言模型训练流程实现 11% 加速。他表示这是"AI 用来优化自身训练的飞轮"，并认为此类自主迭代会在未来数年内从根本上改变 AI 研究的节奏与方式。

### Twitter/X

**[Yann LeCun](https://www.cnbc.com/)** · 06-2x UTC

LeCun 在 CNBC 访谈中直接点评 Elon Musk 旗下 xAI："坦率地说，那是某种失败（kind of a failure, frankly）"，指出 11 位非马斯克联合创始人已全部离职。他同时在视频中重申世界模型（World Model）与 JEPA 架构路线，认为当前 LLM 缺乏真正的世界理解能力，无法通向通用人工智能。

❤️ 42,000 · 🔁 8,700

**[Sam Altman](https://www.benzinga.com/markets/tech/26/06/53269428/google-gemini-co-lead-noam-shazeer-joins-openai-sam-altman-says-its-10-years-in-the-making)** · 06-18 UTC

Altman 在 X 上庆祝 Noam Shazeer 加盟 OpenAI："这是我从 OpenAI 创立之初就最想合作的人，等了 10 年终于如愿。"他同时表示 OpenAI 正经历用户行为重大转变，企业用户开始追求推理效率而非上下文长度，这也将推动公司在产品层面进行相应调整。

❤️ 189,000 · 🔁 24,600

---

## 🔥 GitHub 热门 AI 项目

**1. [openclaw/openclaw](https://github.com/openclaw/openclaw)**
  ⭐ 211,000 &nbsp;·&nbsp; 🍴 18,400 &nbsp;·&nbsp; `TypeScript` · 今日 **+2,200** ⭐
  2026 年最火爆开源项目，个人 AI 助手完全运行于本地设备，作为本地网关连接 WhatsApp、Telegram、Slack 等 50+ 集成，社区已有 160+ Agent 模板。

**2. [karpathy/nanochat](https://github.com/karpathy/nanochat)**
  ⭐ 52,000 &nbsp;·&nbsp; 🍴 6,800 &nbsp;·&nbsp; `Python` · 今日 **+1,200** ⭐
  Karpathy 出品：百元预算内搭建完整 ChatGPT 克隆的最小化全栈实现，涵盖分词、预训练、RLHF 到 Web 推理界面，是学习 LLM 全流程的最佳开源教材。

**3. [karpathy/autoresearch](https://github.com/karpathy/autoresearch)**
  ⭐ 21,000 &nbsp;·&nbsp; 🍴 2,100 &nbsp;·&nbsp; `Python` · 今日 **+980** ⭐
  给 AI Agent 一个单 GPU 训练环境，让它整夜自主修改代码、训练 5 分钟、检查结果并循环，实现无人监督的 AI 研究加速。"Karpathy Loop" 的实验代码库。

**4. [ECC – Agent Harness Optimizer](https://github.com/trending)**
  ⭐ 210,000 &nbsp;·&nbsp; 🍴 12,200 &nbsp;·&nbsp; `Python` · 今日 **+1,600** ⭐
  专为 Claude Code、Codex、Cursor、Gemini CLI 等 AI 编程环境设计的 Agent 执行性能优化系统，整合技能库、记忆优化、安全扫描与 Hook 配置。

**5. [ollama/ollama](https://github.com/ollama/ollama)**
  ⭐ 172,000 &nbsp;·&nbsp; 🍴 13,200 &nbsp;·&nbsp; `Go` · 今日 **+870** ⭐
  本地运行大语言模型的首选工具，一行命令即可拉起 Llama、Mistral、Gemma 等模型，累计拉取量超 1 亿次，是本地优先 AI 浪潮的核心基础设施。

**6. [vllm-project/vllm](https://github.com/vllm-project/vllm)**
  ⭐ 172,000 &nbsp;·&nbsp; 🍴 10,900 &nbsp;·&nbsp; `Python` · 今日 **+560** ⭐
  生产级 LLM 推理引擎，PagedAttention 算法大幅提升 GPU 显存利用率，2026 年扩展支持 AMD、Intel Arc 和 TPU，并发吞吐量比 Ollama 高出 16–20 倍，是企业级服务部署的事实标准。

**7. [open-webui/open-webui](https://github.com/open-webui/open-webui)**
  ⭐ 124,500 &nbsp;·&nbsp; 🍴 13,500 &nbsp;·&nbsp; `Python` · 今日 **+790** ⭐
  自托管 AI 平台，完全离线运行，累计下载量超 2.82 亿次，支持自定义工具、Agent 与 CLI，兼容 Ollama、OpenAI 兼容接口等多种后端。

---

*本文由 [AI Daily News](https://github.com/yf-sz/ai-daily-news) 自动收集生成，每日定时发布。*
