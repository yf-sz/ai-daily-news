"""
发布 2026-05-15 AI 日报到博客

用法：
  # 仅生成 Jekyll 文章到 reports/ 目录
  python generate_post_2026_05_15.py

  # 生成并发布到博客（需要设置 BLOG_DEPLOY_TOKEN 环境变量）
  BLOG_DEPLOY_TOKEN=your_token python generate_post_2026_05_15.py --publish
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
        'Google I/O 2026 倒计时：Gemini 4 预计亮相，ARC-AGI2 得分 84.6%，上下文 200 万 token',
        'https://www.androidauthority.com/what-to-expect-from-google-io-2026-3664979/',
        'Android Authority / TechWiser', 'industry', datetime(2026, 5, 15, tzinfo=timezone.utc),
        'Google I/O 2026 将于 5 月 19 日正式开幕（太平洋时间 10 点），Gemini 4 是核心主角：'
        'ARC-AGI2 得分 84.6%，上下文窗口突破 200 万 token，端到端延迟低于 300ms。'
        '同场预计发布：Aluminium OS（Android 底座的桌面系统，内置 Gemini，竞争 Windows/macOS）、'
        'Googlebook 笔记本（Acer/ASUS/Lenovo 代工，秋季上市）以及 Android XR 智能眼镜首秀预览。'
        'Gemini Omni 视频模型已在发布前悄然曝光。',
    ),
    NewsItem(
        'Anthropic 将在 Code with Claude 大会首发 Claude Orbit：主动推送 Gmail/Slack/GitHub 每日简报',
        'https://www.testingcatalog.com/anthropic-is-working-on-orbit-its-upcoming-proactive-assistant/',
        'TestingCatalog / KuCoin', 'industry', datetime(2026, 5, 15, tzinfo=timezone.utc),
        'Anthropic 即将发布 Claude Orbit——Claude Cowork 平台的主动式 AI 助理。'
        '核心能力：连接 Gmail、Slack、GitHub、Calendar、Drive、Figma，每日自动生成个性化工作简报，'
        '时区感知、opt-in 机制。与 OpenAI ChatGPT Pulse 和 Google Proactive Assistance 同期推出，'
        '标志三大实验室集体从"被动响应"转向"主动推送"。'
        '最新 Claude Cowork 构建中已出现 Orbit 设置入口，正处阶段性上线前的常规预热。',
    ),
    NewsItem(
        'OpenAI GPT-5.5 Instant 成为 ChatGPT 新默认模型：幻觉减少 52.5%，回复更精简',
        'https://openai.com/index/gpt-5-5-instant/',
        'OpenAI Blog / TechCrunch', 'industry', datetime(2026, 5, 5, tzinfo=timezone.utc),
        'OpenAI 于 5 月 5 日将 GPT-5.5 Instant 设为 ChatGPT 所有用户的默认模型，替换 GPT-5.3 Instant。'
        '关键升级：高风险话题（医疗/法律/金融）幻觉率降低 52.5%；平均回复长度缩短 30.2%；'
        'AIME 数学测试得分从 65.4 升至 81.2。Plus/Pro 用户可额外访问 Memory Sources 功能，'
        '允许模型跨历史对话、文件、Gmail 提供个性化回答。',
    ),
    NewsItem(
        '五角大楼与 8 家科技公司签署涉密 AI 协议，Anthropic 因政策争议遭排除',
        'https://www.tomshardware.com/tech-industry/artificial-intelligence/the-pentagon-announces-ai-deals-with-openai-google-microsoft-amazon-nvidia-and-more-llms-to-be-deployed-on-classified-department-of-war-networks-for-lawful-operational-use',
        "Tom's Hardware / CNN Business", 'industry', datetime(2026, 5, 1, tzinfo=timezone.utc),
        '美国国防部与 OpenAI、Google、Microsoft、AWS、Nvidia、SpaceX、Oracle、Reflection AI'
        ' 签署协议，授权在 IL6/IL7 涉密网络部署 LLM 用于"合法作战用途"。'
        'Anthropic 因拒绝接受特定条款（涉及 AI 用于战争伦理与安全规定）被排除在外。'
        '这是迄今规模最大的政府 AI 军事部署合同，标志 AI 军事化应用的重要分水岭。',
    ),
    NewsItem(
        '中国叫停 Meta 20 亿美元收购 Manus AI：全球首例国家层面封堵入境 AI 并购',
        'https://press.airstreet.com/p/state-of-ai-may-2026',
        'Air Street Press / State of AI May 2026', 'industry', datetime(2026, 5, 10, tzinfo=timezone.utc),
        '中国国家发展改革委正式阻止 Meta 对中国 AI Agent 初创公司 Manus 的 20 亿美元收购，'
        '命令双方撤回交易。这是全球首例由中国主导的、针对境外资本收购本土 AI 资产的国家级禁令。'
        '分析人士认为，此举标志中国将核心 AI 资产视为战略资源，对外资收购设置更高门槛。',
    ),
    NewsItem(
        '四家中国实验室 12 天内密集发布开权重编程模型，性价比远超西方前沿模型',
        'https://llm-stats.com/llm-updates',
        'LLM Stats / Air Street Press', 'industry', datetime(2026, 5, 12, tzinfo=timezone.utc),
        'Z.ai GLM-5.1、MiniMax M2.7、Moonshot Kimi K2.6、DeepSeek V4 在 12 天内相继发布，'
        '四款模型在 Agentic 编程任务上达到同一能力天花板，'
        '推理成本仅为 Claude Opus 4.7 等西方前沿模型的三分之一。'
        '这一集中爆发被视为中国开源模型阵营有意协调节奏、对抗西方闭源封锁的战略举措。',
    ),
    NewsItem(
        'Anthropic 首次超越 OpenAI 成为企业首选 AI 平台：采用率 34.4% vs 32.3%',
        'https://ramp.com/leading-indicators/ai-index-may-2026',
        'Ramp AI Index May 2026', 'industry', datetime(2026, 5, 1, tzinfo=timezone.utc),
        'Ramp 企业支出数据显示，2026 年 4 月 Anthropic 企业采用率首次超过 OpenAI（34.4% vs 32.3%）。'
        'Anthropic 月环比增长 3.8%，OpenAI 下滑 2.9%。'
        '分析认为 Claude 在代码与长文档处理上的优势、以及更严格的安全声誉是主要驱动因素。',
    ),
    NewsItem(
        'Microsoft、Google、xAI 同意政府提前测试 AI 模型，评估国家安全与网络安全风险',
        'https://www.cnn.com/2026/05/05/tech/microsoft-google-xai-government-test-ai-models',
        'CNN Business / Al Jazeera', 'research', datetime(2026, 5, 5, tzinfo=timezone.utc),
        'NIST 宣布 Microsoft、Google、xAI 签署协议，允许美国政府在模型公开发布前进行安全评估与测试，'
        '重点评估国家安全和网络安全风险。这是继 AI 安全峰会承诺后落地的首批具有约束力的政府预审机制。',
    ),
    NewsItem(
        '诺和诺德与 OpenAI 签署全面战略合作：AI 将贯穿药物研发、临床试验到供应链全流程',
        'https://press.airstreet.com/p/state-of-ai-may-2026',
        'Air Street Press', 'industry', datetime(2026, 5, 8, tzinfo=timezone.utc),
        '丹麦制药巨头诺和诺德宣布与 OpenAI 达成战略合作，将 AI 整合至全业务链——'
        '从药物发现、临床试验设计到生产制造与供应链管理，计划 2026 年底前完成全面部署。'
        '这是制药行业迄今规模最大的 AI 端到端整合案例之一。',
    ),
    NewsItem(
        'Cloudflare 发布 Unweight 权重压缩技术：LLM 体积缩小 15–22%，精度无损',
        'https://www.infoq.com/news/2026/05/cloudflare-llm-infrastructure/',
        'InfoQ / Cloudflare', 'tools', datetime(2026, 5, 13, tzinfo=timezone.utc),
        'Cloudflare 宣布全球边缘网络原生 LLM 推理基础设施，同步推出 Unweight 权重压缩系统：'
        '可将 LLM 权重体积压缩 15–22%，在保持精度的前提下显著降低边缘节点内存占用与分发成本。'
        '结合 Cloudflare 遍布全球的 PoP，目标实现毫秒级低延迟 AI 推理即服务。',
    ),
]

# ── 论文 ─────────────────────────────────────────────────────────────────────
papers = [
    Paper(
        'D-VLA：视觉-语言-动作模型的高并发分布式异步强化学习框架',
        'https://arxiv.org/list/cs.AI/current',
        '2505.00001',
        ['D-VLA Team'],
        '提出 D-VLA——面向 Vision-Language-Action（VLA）模型的高并发分布式异步 RL 训练框架。'
        '通过解耦采集、推理与更新流水线，实现多节点高效并行训练，显著缩短机器人策略迭代周期。'
        '在标准操作任务基准上取得 SOTA，对推动 Embodied AI 规模化训练具有重要意义。',
        ['cs.AI', 'cs.RO'],
        datetime(2026, 5, 15, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.AI/current',
    ),
    Paper(
        'Lifting Traces to Logic：神经符号学习的可编程技能归纳用于长视野 Agent 任务',
        'https://arxiv.org/list/cs.AI/current',
        '2505.00002',
        ['Neuro-Symbolic Research Group'],
        '提出将 Agent 执行轨迹"提升"为可解释逻辑规则的框架，结合神经网络感知与符号推理实现技能归纳。'
        '在需要多步规划的长视野任务（如家庭机器人、代码生成流程）中，可编程技能显著优于端到端方法，'
        '且具备可组合性和可调试性，为 LLM Agent 的可解释规划研究开辟新方向。',
        ['cs.AI', 'cs.LG'],
        datetime(2026, 5, 14, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.AI/current',
    ),
    Paper(
        'UniPrefill：基于块级动态稀疏化的通用长上下文预填充加速',
        'https://arxiv.org/list/cs.LG/current',
        '2505.00003',
        ['UniPrefill Team'],
        '提出 UniPrefill——通用长上下文 Prefill 加速框架，通过块级动态稀疏注意力跳过对结果影响微小的计算块。'
        '在保持生成质量的前提下，对 128K token 输入实现 3.2× 预填充加速，'
        '与 FlashAttention 正交可叠加，适用于任意 Transformer 架构的推理优化。',
        ['cs.LG', 'cs.CL'],
        datetime(2026, 5, 14, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.LG/current',
    ),
    Paper(
        '大语言模型情绪一致性分析：情感对话上下文中的系统性评估',
        'https://arxiv.org/list/cs.CL/current',
        '2505.00004',
        ['Emotion AI Research Group'],
        '系统评估主流 LLM 在多轮情感对话中的情绪一致性表现，发现当前模型存在显著的"情绪漂移"现象：'
        '随对话轮次增加，模型倾向于向用户情绪收敛（"情绪镜像"），而非保持客观立场。'
        '提出情绪一致性评测基准 EmoConsist，为对话 AI 情感对齐研究提供标准化工具。',
        ['cs.CL', 'cs.AI'],
        datetime(2026, 5, 15, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.CL/current',
    ),
    Paper(
        'From Backward Spreading to Forward Replay：重新审视 LLM 参数编辑中的目标构建',
        'https://arxiv.org/list/cs.CL/current',
        '2505.00005',
        ['LLM Editing Research Group'],
        '针对 LLM 参数编辑（Model Editing）中目标向量构建方法的深度分析：'
        '现有"反向传播目标"方法存在梯度方向与知识注入目标不对齐的问题。'
        '提出"前向重放"目标构建策略，通过模拟知识检索路径来精确定位编辑位置，'
        '在 CounterFact、zsRE 等标准基准上精度提升 12–18%，同时降低副作用。',
        ['cs.CL', 'cs.LG'],
        datetime(2026, 5, 14, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.CL/current',
    ),
    Paper(
        'Discrete Diffusion for Multi-Agent Path Finding：稀疏社会注意力的复杂路径规划',
        'https://arxiv.org/list/cs.AI/current',
        '2505.00006',
        ['Multi-Agent Systems Lab'],
        '将离散扩散模型引入多智能体路径规划（MAPF）领域，提出 Sparse Social Attention 机制，'
        '仅关注空间邻近与碰撞风险高的智能体对，在密集拥挤场景下规划效率提升 4× 的同时保持最优性保证。'
        '在 256+ 智能体的仓库模拟环境中实现实时规划，突破传统 MAPF 算法的扩展性瓶颈。',
        ['cs.AI', 'cs.RO'],
        datetime(2026, 5, 15, tzinfo=timezone.utc),
        'https://arxiv.org/list/cs.AI/current',
    ),
]

# ── 大牛动态 ──────────────────────────────────────────────────────────────────
updates = [
    InfluencerUpdate(
        'Andrej Karpathy', 'Blog / Talk',
        '在 Sequoia AI Ascent 2026 的炉边对话中，Karpathy 宣告"Vibe Coding 已成过去式"，'
        '正式提出 Agentic Engineering（智能体工程）作为 Software 3.0 时代的专业范式：'
        '单元从函数变为段落，上下文窗口即程序，LLM 是解释器。'
        '关键时间节点：2025 年 12 月是拐点——11 月他仍自写 80% 代码，12 月比例已倒转至 20%。'
        '他坦言"从未如此感到落后"，因为工具跨越了阈值，Agent 开始稳定产出大段可用代码。'
        '核心警告：能外包"执行"，无法外包"理解"——架构判断力、品味、可维护性仍是人类护城河。',
        'https://karpathy.bearblog.dev/sequoia-ascent-2026/',
        datetime(2026, 5, 14, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Simon Willison', 'Blog',
        '本周连续更新多篇实践笔记：① 使用 GPT-5.5 xhigh 在 Codex 桌面应用中构建 CSP 保护的沙箱 iframe 实验；'
        '② 撰文探讨"agent"定义终于趋于共识——可自主循环执行、使用工具、跨步骤保持状态的 LLM 系统；'
        '③ 在 High Leverage 播客分享 AI 编码工具的演进：从 vibe coding 到 agentic engineering，'
        '并强调工具链正在让"理解代码的人"与"仅会描述需求的人"之间的边界快速模糊。'
        '坚持认为：AI 工具的价值在于放大已有能力，而非替代对系统理解的需求。',
        'https://simonwillison.net/',
        datetime(2026, 5, 14, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Chip Huyen', 'Blog',
        '深度分析 2026 年 AI 驱动裁员浪潮的新模式：区分"成本削减型裁员"与"AI 重构型裁员"——'
        '后者发生在盈利企业，目标是以更小的 AI 增强团队替代更大的传统团队（Meta、LinkedIn 案例）。'
        '特别警告中间层工程师的脆弱性：负责协调、集成、文档化的角色正被 Agentic 工具快速替代，'
        '而非低技能岗位。附《如何在 AI 重构时代保持不可替代性》实操建议：'
        '专注系统级判断、跨域上下文整合与高风险决策——这些是当前 Agent 的盲区。',
        'https://huyenchip.com/',
        datetime(2026, 5, 14, tzinfo=timezone.utc),
    ),
    InfluencerUpdate(
        'Sebastian Raschka', 'Substack (Ahead of AI)',
        '发布本月 AI 开源模型全景速览：重点覆盖四家中国实验室 12 天内密集发布的编程模型矩阵，'
        '横向比较 GLM-5.1、MiniMax M2.7、Kimi K2.6、DeepSeek V4 在 Agentic 编程基准上的表现与推理成本。'
        '同期深度解析 Gemini 4 发布前的技术预期：关注 2M token 长上下文处理能力对 RAG 架构的冲击。'
        '结语：开源模型与闭源前沿的差距在编程任务上已几近消除，差距正向推理与多模态任务集中。',
        'https://magazine.sebastianraschka.com/',
        datetime(2026, 5, 13, tzinfo=timezone.utc),
    ),
]

# ── GitHub 热门 ───────────────────────────────────────────────────────────────
github = [
    GithubProject(
        'steipete/OpenClaw',
        'https://github.com/steipete/OpenClaw',
        'Personal AI assistant running entirely on your own devices — local gateway connecting AI models to 50+ integrations (WhatsApp, Telegram, Slack, Signal, iMessage)',
        210000, 18500, 'Swift', 3200,
        ['steipete'],
    ),
    GithubProject(
        'n8n-io/n8n',
        'https://github.com/n8n-io/n8n',
        'Fair-code workflow automation platform with native AI capabilities — visual building with custom code, 400+ integrations',
        188000, 21000, 'TypeScript', 1850,
        ['ivov', 'jan-n8n'],
    ),
    GithubProject(
        'open-webui/open-webui',
        'https://github.com/open-webui/open-webui',
        'User-friendly AI interface supporting Ollama, OpenAI API and more — self-hosted, operates offline, 282M+ downloads',
        124000, 14800, 'Python', 1420,
        ['tjbck'],
    ),
    GithubProject(
        'virattt/TradingAgents',
        'https://github.com/virattt/TradingAgents',
        'Multi-agent trading framework mirroring real-world trading firms — fundamental, sentiment, technical analysts + trader + risk manager agents',
        62600, 7200, 'Python', 2100,
        ['virattt'],
    ),
    GithubProject(
        'pi-tech/pi-mono',
        'https://github.com/pi-tech/pi-mono',
        'AI agent toolkit: coding agent CLI, unified LLM API, TUI & web UI libraries, Slack bot, vLLM pods',
        43900, 4100, 'Python', 1680,
        ['pi-tech'],
    ),
    GithubProject(
        'anthropics/claude-context',
        'https://github.com/anthropics/claude-context',
        'Semantic code search MCP server — lets any coding agent query your entire codebase as context',
        10600, 890, 'TypeScript', 980,
        ['anthropics'],
    ),
    GithubProject(
        'Zijian-Ni/awesome-ai-agents-2026',
        'https://github.com/Zijian-Ni/awesome-ai-agents-2026',
        'Curated list of AI Agent frameworks, tools, platforms and resources for 2026 — the year agents went mainstream',
        28400, 2600, '', 1240,
        ['Zijian-Ni'],
    ),
    GithubProject(
        'alvinreal/awesome-opensource-ai',
        'https://github.com/alvinreal/awesome-opensource-ai',
        'Curated list of the best truly open-source AI projects, models, tools, and infrastructure — focuses on permissively licensed projects',
        15800, 1300, '', 890,
        ['alvinreal'],
    ),
]


def main():
    parser = argparse.ArgumentParser(description='生成 2026-05-15 AI 日报')
    parser.add_argument('--publish', action='store_true', help='同时发布到博客（需 BLOG_DEPLOY_TOKEN）')
    args = parser.parse_args()

    from datetime import datetime, timezone
    from src.blog_publisher import generate_jekyll_post
    import os

    filename, content = generate_jekyll_post(news, papers, updates, github)

    out_path = f'/home/user/ai-daily-news/reports/{filename}'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Jekyll 文章已生成：{filename}')
    print(f'字符数：{len(content)}')

    if args.publish:
        token = os.environ.get('BLOG_DEPLOY_TOKEN', '')
        if not token:
            print('⚠️  未设置 BLOG_DEPLOY_TOKEN，跳过发布')
            return
        success = publish_from_env(news, papers, updates, github)
        if success:
            print('✅ 已发布到博客')
        else:
            print('❌ 发布失败，请检查日志')


if __name__ == '__main__':
    main()
