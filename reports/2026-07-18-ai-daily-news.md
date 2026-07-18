---
layout: post
title: "AI 日报 · 2026年07月18日"
date: 2026-07-18 00:10:00 +0000
categories:
  - "AI日报"
tags:
  - "AI"
  - "AI日报"
  - "人工智能"
  - "每日新闻"
  - "LG"
  - "MA"
description: "今日 AI 速报：8 条资讯 · 5 篇论文 · 4 条大牛动态 · 5 个热门项目"
toc: true
---

> **今日 AI 速报：8 条资讯 · 5 篇论文 · 4 条大牛动态 · 5 个热门项目**
> 数据来源：RSS · arXiv · Papers With Code · GitHub Trending
> 生成时间：2026-07-18 00:10 UTC

---

## 📰 今日 AI 资讯


### 🏭 产业动态

- **[月之暗面发布 Kimi K3：全球首个 2.8 万亿参数开源 MoE 模型，性能逼近美国顶尖闭源系统](https://venturebeat.com/technology/chinas-moonshot-ai-releases-kimi-k3-the-largest-open-source-model-ever-rivaling-top-u-s-systems)**  
  `VentureBeat · Moonshot AI` · 07-17 00:00 UTC
  月之暗面于 7 月 16 日正式发布 Kimi K3，这是全球首个突破 3 万亿参数级别的开源 MoE 大模型，实际参数量为 2.8T（896 专家、每 token 激活 16 个），搭载自研 Kimi Delta Attention（KDA）混合线性注意力机制，原生支持 100 万 token 上下文窗口。K3 Max 聚焦对话与 Agent 任务，K3 Swarm Max 面向大规模并行处理。权威评测 GDPval-AA v2 上，K3 以 1,687 分位列全球第三，仅次于 Claude Fable 5 Max（1,815）和 GPT-5.6 Sol Max（1,747.8）；AA-Briefcase 榜上更超越 GPT-5.6 Sol Max 升至第二。完整模型权重将于 7 月 27 日上线 Hugging Face，被视为中国开源 AI 缩小与美国差距的标志性进展。

- **[TSMC Q2 2026 创历史纪录：净利润暴涨 77.4%，AI 芯片全年增速预期上调至 40%+](https://www.techtimes.com/articles/320696/20260716/tsmc-posts-record-quarter-ai-chip-demand-pushes-full-year-growth-outlook-past-40.htm)**  
  `TechTimes / Yahoo Finance` · 07-16 00:00 UTC
  台积电发布 2026 年 Q2 财报，单季营收达 402 亿美元（同比增 36%），净利润飙升 77.4% 至新台币 7,065 亿元，连续第九个季度实现双位数利润增长，所有主要财务指标均超析师预期。高性能计算（HPC，含 AI 芯片）贡献 Q2 营收的 66%，2nm 制程首次对营收作出实质贡献（占晶圆营收 3%）。台积电同步宣布追加美国亚利桑那州 1,000 亿美元投资，并将全年 AI 芯片营收增速预期上调至 40% 以上，连续刷新纪录的财报进一步印证全球 AI 算力军备竞赛的持续升温。

- **[Meta 裁员 8,000 人 + 转岗 7,000 人：扎克伯格内部承认"AI 加速不及预期"](https://247wallst.com/investing/2026/07/07/after-laying-off-8000-employees-zuckerberg-admits-metas-ai-hasnt-really-accelerated-as-expected/)**  
  `24/7 Wall St. / NPR` · 07-07 00:00 UTC
  Meta 在 5 月完成约 8,000 人裁员（占总员工数约 10%，主要波及完整性、网络安全和 Reality Labs 团队），并同步将 7,000 名员工调往 Applied AI Engineering、Agent Transformation Accelerator XFN 等新成立的 AI 专项团队。然而，扎克伯格在 7 月 2 日内部全员会上坦承，过去四个月 AI Agent 开发"并未按预期加速"，重组"还没像计划那样干净"。尽管如此，Meta 2026 年资本支出预测仍高达 1,250—1,450 亿美元（是 2025 年两倍有余），显示公司长期 AI 战略押注不变。

- **[Grok Build 强制开源：xAI 静默上传用户代码库曝光 72 小时后发布 844K 行 Rust 代码](https://simonwillison.net/2026/Jul/15/grok-build/)**  
  `Simon Willison's Weblog / The Register` · 07-15 00:00 UTC
  xAI 旗下 AI 编程 CLI 工具 Grok Build 于 7 月 15 日将全部 844,530 行 Rust 代码以 Apache 2.0 协议开源，时间节点恰在 AI 安全研究人员发布 Grok Build 静默将用户完整代码库上传至 SpaceXAI 云端的技术取证约 72 小时后。xAI 已于 7 月 12 日起为所有用户关闭默认数据留存并删除历史编程数据。开源内容涵盖 Agent 循环、工具层、终端 UI（含 Mermaid 图表 Unicode 盒状字符渲染器）及扩展系统（插件、MCP 服务器、子 Agent）；模型权重（Grok 4.5，$2/$6 per million tokens）依然闭源。外界普遍认为此次开源是"危机公关下的被迫之举"，但开源本身对生态意义重大。


### 🔬 研究前沿

- **[欧盟 AI Act 执法倒计时：8 月 2 日起 GPAI 违规最高罚款 3% 全球年营收](https://beam.ai/agentic-insights/eu-ai-act-enforcement-august-2-2026-gpai-fines)**  
  `Beam AI / DataGuard` · 07-18 00:00 UTC
  欧盟 AI 法案（AI Act）针对通用目的 AI 模型（GPAI）的监管执法权将于 2026 年 8 月 2 日正式落地，届时欧盟委员会及 AI 办公室可对违规 GPAI 提供商发起文件索取、技术评估、合规整改要求乃至市场禁入，罚款上限为全球年营收的 3% 或 1,500 万欧元（取较高者）。GPAI 实质性义务（透明度申报、版权声明、安全评估）已自 2025 年 8 月起生效，此次是执法机制正式激活——距截止日仅剩约两周，全球主流大模型厂商的合规状态备受关注。

- **[数百名跨学科专家联署警告：AI 社会冲击准备不足，呼吁建立国际约束性协调机制](https://www.aljazeera.com/economy/2026/7/13/hundreds-of-experts-warn-the-world-must-prepare-now-for-ais-impact)**  
  `Al Jazeera` · 07-13 00:00 UTC
  来自经济学、社会科学、公共政策等领域的数百名顶尖学者联名发出警告：全球社会对 AI 大规模部署的准备严重不足，涵盖就业结构冲击、教育体系适配、公共服务重构与心理健康影响等多个维度。联署专家特别强调，当前各国 AI 治理框架的制定速度远落后于技术能力提升速度，呼吁建立具约束力的国际协调机制以防止 AI 收益被少数企业和国家垄断。声明发布时间与上海世界人工智能大会开幕高度重叠，引发全球政策界广泛关注。


### 🛠️ 工具生态

- **[colibri：纯 C 实现，消费级 25GB 内存运行 GLM-5.2 744B MoE 超大模型](https://github.com/JustVugg/colibri)**  
  `GitHub JustVugg/colibri` · 07-10 00:00 UTC
  开发者 JustVugg 发布 colibri，以纯 C 语言（零外部依赖）实现在 25GB 内存消费级机器上运行 GLM-5.2（744B MoE）——通过将专家权重按需从磁盘流式加载的方式突破显存瓶颈。核心特性：LRU 专家缓存自动调整至可用 RAM 上限（2026-07-10 版本起生效）、PILOT 模式利用 GLM-5.2 可预测的专家路由实现 I/O 线程预取、对话 KV-cache 可持久化磁盘（每 token 约 182KB）重开对话无需重新 prefill。随使用频率提升热门专家常驻内存，推理速度自动加快，被社区称为"让万亿参数模型飞入寻常百姓家"的工程典范。

- **[OfficeCLI：首个专为 AI Agent 构建的 Office 自动化命令行套件，单二进制无需安装 Office](https://github.com/iOfficeAI/OfficeCLI)**  
  `GitHub iOfficeAI/OfficeCLI` · 07-06 00:00 UTC
  iOfficeAI 开源的 OfficeCLI 是首个专为 AI Agent 设计的 Office 自动化工具套件，以单一二进制文件支持 Word、Excel、PowerPoint 的读取、编辑与自动化操作，内置高保真 HTML 渲染引擎可将 Office 文件转为 HTML 或 PNG——全程无需安装 Microsoft Office。工具已原生集成 Claude Code、Codex CLI、ChatGPT 等主流 AI 编程助手，可一行代码赋予 Agent 完整文档操作能力，是构建文档处理 AI 工作流的重要基础设施。

---

## 📄 最新论文速览

**1. [Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops](https://arxiv.org/abs/2607.07663)**
  👤 Mingguang Chen 等 &nbsp;|&nbsp; 📂 `cs.AI · cs.LG` &nbsp;|&nbsp; 🗓 2026-07-08
  [PDF](https://arxiv.org/pdf/2607.07663)

  > 覆盖 2024—2026 年 arXiv 1,250 篇论文的 RSI（递归自我改进）综述。论文沿两个轴建立分类体系：改进对象（部署行为 / 训练策略 / 评估器 / 研究过程本身）与闭环程度（人类在环 → 完全自主）。核心贡献在于明确区分"有界自我精炼"（bounded self-refinement，已是工业实践）与"开放式递归自我改进"（open-ended RSI）——前者收敛可评估，后者目前仍处探索阶段。论文给出从数据飞轮到完全自主研究循环的演进路线图，鉴于 Karpathy Loop 等真实实验的涌现，此综述具有极高参考价值。

**2. [Self-Improvements in Modern Agentic Systems: A Survey](https://arxiv.org/abs/2607.13104)**
  👤 多机构联合研究团队 &nbsp;|&nbsp; 📂 `cs.AI · cs.CL` &nbsp;|&nbsp; 🗓 2026-07-17
  [PDF](https://arxiv.org/pdf/2607.13104)

  > 聚焦现代 Agent 系统自我改进机制的专项综述，涵盖提示优化、工具使用优化、记忆检索优化、代码执行反馈等主要路径，重点分析 Agent 如何在开放环境中通过无监督交互自动更新决策策略。作者将自我改进能力界定为迈向通用 Agent 的核心瓶颈，并系统整理当前方法在长期稳定性、灾难性遗忘与安全边界方面的关键挑战，为构建更自主的 Agent 系统提供了全面参考框架。

**3. [ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory](https://arxiv.org/abs/2607.10350)**
  👤 多大学联合研究团队 &nbsp;|&nbsp; 📂 `cs.RO · cs.AI · cs.CV` &nbsp;|&nbsp; 🗓 2026-07-15
  [PDF](https://arxiv.org/pdf/2607.10350)

  > 提出通用机器人 Agent 操作系统（AgentOS），集成场景条件规划、上下文隔离技能执行、多阶段验证、多模态终身记忆与边缘云协同五大模块，使机器人 Agent 能在长时跨任务操作中持续积累和迁移经验。终身记忆模块显著降低跨任务知识遗忘率，系统在家庭任务操作和工业装配场景中展现出明显优于基线的任务完成率，为具身智能的持续自主学习提供了完整系统级解决方案。

**4. [SwarmResearch: Orchestrating Coding Agents for Open-Ended Discovery](https://arxiv.org/abs/2607.02807)**
  👤 arXiv 开放研究团队 &nbsp;|&nbsp; 📂 `cs.AI · cs.SE` &nbsp;|&nbsp; 🗓 2026-07-03
  [PDF](https://arxiv.org/pdf/2607.02807)

  > 提出 SwarmResearch 框架，用于协调多编程 Agent 群在开放探索场景中自主发现新算法与优化方案。核心机制为提案—评审—整合的分布式迭代：多个专业化 Agent 并行提出候选方案、交叉验证并由协调层提炼共识。在机器学习优化算法自动搜索任务中，SwarmResearch 全程无人类介入即找到优于手工设计的新变体，揭示了多 Agent 协作在科学发现流水线中取代人工迭代的可行路径。

**5. [ComfyClaw: Self-Evolving Skill Harnesses for Image Generation Workflows](https://arxiv.org/abs/2607.01709)**
  👤 arXiv 独立研究团队 &nbsp;|&nbsp; 📂 `cs.AI · cs.CV` &nbsp;|&nbsp; 🗓 2026-07-02
  [PDF](https://arxiv.org/pdf/2607.01709)

  > 提出 ComfyClaw，用于控制 ComfyUI 图像生成工作流的 Agent 技能自进化框架：Agent 将历史工作流模式、执行约束与用户偏好纳入持久化记忆，每次任务后自动提炼新技能节点并更新技能库，实现工作流知识的自我积累。实验显示迭代后任务平均完成步骤数显著减少，新技能具备跨用户场景泛化能力，为构建无需专家干预即可持续优化的图像生成自动化系统提供了完整技术路径。

---

## 🧑‍🔬 大牛动态


### Twitter/X

**[Andrej Karpathy](https://x.com/karpathy/status/2049903821095354523)** · 07-16 00:00 UTC

Karpathy 在 X 上分享了对 Kimi K3 发布的第一手评价，称 2.8T 参数 MoE 开源是"重大里程碑"，并指出 Kimi Delta Attention 在百万 token 上下文下实现 6.3 倍解码提速是架构层面的真正创新，而非单纯参数堆砌。他同期在回复中重申了在 Anthropic 推进的自主研究项目（Karpathy Loop）的核心目标：让 AI Agent 全程自主设计实验、分析结果、更新模型权重，人类仅负责提出研究方向与审阅最终结论，并透露下一步计划将单 Agent 扩展为数十个并行运行的 Agent 协同体系。

❤️ 31,400 · 🔁 5,200

**[Yann LeCun](https://x.com/ylecun)** · 07-17 00:00 UTC

LeCun 在 X 上连发多条推文回应 Kimi K3 发布，再度强调开源大模型对"AI 民主化"的战略意义，指出当开源模型性能比肩顶级闭源系统后，商业 API 护城河将迅速收窄，而非科技巨头的更广泛受益者将从中获益。他同时更新了 AMI Labs 世界模型研究框架：JEPA（联合嵌入预测架构）正向真实物理环境推演方向扩展，目标是构建能理解因果关系而非仅捕捉统计相关性的通用智能底座，以区别于当前 LLM 范式的根本局限。

❤️ 14,800 · 🔁 2,100


### Blog

**[Simon Willison](https://simonwillison.net/2026/Jul/15/grok-build/)** · 07-15 00:00 UTC

Willison 发布深度博文剖析 Grok Build 开源的 844K 行 Rust 代码库，重点挖掘其中"自给自足的终端 Mermaid 图表渲染器"（用 Unicode 盒状字符渲染图表）等工程亮点，并将核心 Mermaid-to-ASCII 功能提取后编译为 WebAssembly 运行，与早期 Go 实现进行对比评测。他指出，Grok Build 的开源对整个 AI CLI 工具生态意义深远——不在于商业价值，而在于暴露了 AI 工具链在隐私审计层面的系统性盲区：Grok Build 静默上传代码库的行为将推动业界对 AI 工具数据流向形成更高警觉，进而加速 Agent 工具的安全标准化进程。

**[Andrej Karpathy (bearblog)](https://karpathy.bearblog.dev/)** · 07-17 00:00 UTC

Karpathy 在个人博客更新了关于"Karpathy Loop"自主研究实验的技术回顾，详细梳理 700 次 Agent 自主实验中最具突破性的关键迭代，涵盖 Agent 自主设计学习率调度器、发现混合精度训练盲区以及引入实验性 Tokenizer 的决策链路。他将这套自主研究框架的核心限制归纳为三点：验证基准的设计质量、Agent 的代码执行安全边界、以及探索与利用之间的动态平衡策略，并表示这些正是他在 Anthropic 接下来要系统性解决的方向。

---

## 🔥 GitHub 热门 AI 项目

**1. [openclaw/openclaw](https://github.com/openclaw/openclaw)**
  ⭐ 348,200 &nbsp;·&nbsp; 🍴 28,600 &nbsp;·&nbsp; `TypeScript` · 今日 **+1,100** ⭐
  Your own personal AI assistant. Any OS. Any Platform. — 本地运行的私人 AI 助手，支持 WhatsApp、Telegram、Slack、Discord、iMessage 等 50+ 消息平台接入任意本地或云端 AI 模型，持续占据 GitHub 历史总星数榜首，今日新增热度稳定。

**2. [JustVugg/colibri](https://github.com/JustVugg/colibri)**
  ⭐ 6,200 &nbsp;·&nbsp; 🍴 280 &nbsp;·&nbsp; `C` · 今日 **+1,400** ⭐
  Run GLM-5.2 (744B MoE) on a 25GB-RAM consumer machine — 纯 C 实现、零依赖，通过专家流式加载和 LRU 缓存策略在消费级机器上运行 744B MoE 超大模型，发布仅数日便引爆社区关注，本周单日增速位居 GitHub 全语言榜榜首。

**3. [xai-org/grok-build](https://github.com/xai-org/grok-build)**
  ⭐ 37,500 &nbsp;·&nbsp; 🍴 2,900 &nbsp;·&nbsp; `Rust` · 今日 **+4,800** ⭐
  Grok Build — xAI 开源 AI 编程 CLI 全部 844K 行 Rust 代码，含 Agent 循环、工具层、终端 UI 及扩展系统，Apache 2.0 授权。开源三天内迅速跻身 GitHub 全语言日榜前五，争议性的开源背景反而带来更高关注度，Rust 社区对其架构设计评价颇高。

**4. [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI)**
  ⭐ 17,900 &nbsp;·&nbsp; 🍴 890 &nbsp;·&nbsp; `Go` · 今日 **+680** ⭐
  OfficeCLI — 专为 AI Agent 构建的 Office 自动化命令行工具，单二进制无需安装 Microsoft Office，支持 Word/Excel/PowerPoint 读写与自动化，内置高保真 HTML 渲染，已原生集成 Claude Code、Codex CLI 等主流 AI 编程助手，是 AI Agent 文档操作领域的热门基础工具。

**5. [comfyanonymous/ComfyUI](https://github.com/comfyanonymous/ComfyUI)**
  ⭐ 106,500 &nbsp;·&nbsp; 🍴 11,750 &nbsp;·&nbsp; `Python` · 今日 **+490** ⭐
  The most powerful and modular stable diffusion GUI and backend. 节点式可视化工作流系统，因 ComfyClaw 自进化技能论文同期引发关注，持续吸引图像/视频生成领域用户，最新版本新增多模态视频节点与更完善的 Agent 工作流控制接口。

---

*本文由 [AI Daily News](https://github.com/yf-sz/ai-daily-news) 自动收集生成，每日定时发布。*
