# AI Daily News 🤖

每日自动收集 AI 相关新闻、最新论文和知名研究者动态，生成结构化 Markdown 报告。

## 功能特性

- **📰 AI 资讯**：聚合 15+ 主流 AI 媒体 RSS，包括 VentureBeat、MIT Tech Review、OpenAI Blog、Hugging Face Blog 等
- **📄 最新论文**：实时抓取 arXiv（cs.AI/LG/CL/CV）和 Papers With Code，支持关键词过滤
- **🧑‍🔬 大牛动态**：收集 Karpathy、Yann LeCun、Lilian Weng 等知名研究者的博客和 Twitter 动态
- **🔥 GitHub 热点**：每日最热 AI 开源项目
- **📊 Markdown 报告**：自动生成结构化日报，保存至 `reports/` 目录

## 快速开始

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 配置（可选，不配置也可运行基础功能）
cp .env.example .env
# 编辑 .env 填入 API 密钥

# 3. 运行
python -m src.main
```

## 使用方法

```bash
# 收集今日资讯（默认）
python -m src.main

# 收集过去 3 天的内容
python -m src.main --days 3

# 只收集论文和 GitHub 热点
python -m src.main --skip-news --skip-influencers

# 指定输出目录
python -m src.main --output ./my-reports

# 详细日志模式
python -m src.main --verbose
```

## 项目结构

```
ai-daily-news/
├── src/
│   ├── main.py                         # 主入口（CLI）
│   ├── config.py                       # 配置加载
│   ├── report_generator.py             # Markdown 报告生成
│   └── collectors/
│       ├── news_collector.py           # RSS 新闻收集
│       ├── paper_collector.py          # arXiv / Papers With Code
│       └── influencer_collector.py     # Twitter/X + 博客 + GitHub
├── config/
│   └── sources.yaml                    # 资讯来源配置
├── .claude/
│   └── skills/
│       └── ai-daily-news.md            # Claude Code Skill 定义
├── reports/                            # 生成的报告（自动创建）
├── requirements.txt
├── .env.example
└── README.md
```

## 配置说明

### API 密钥（均为可选）

| 变量 | 说明 | 获取方式 |
|------|------|--------|
| `TWITTER_BEARER_TOKEN` | 启用 Twitter/X 动态收集 | [Twitter Developer Portal](https://developer.twitter.com) |
| `NEWS_API_KEY` | 增强新闻收集 | [newsapi.org](https://newsapi.org) |
| `SEMANTIC_SCHOLAR_API_KEY` | 提升论文 API 限制 | [Semantic Scholar](https://www.semanticscholar.org/product/api) |

### 自定义来源

编辑 `config/sources.yaml` 添加自定义 RSS Feed 或 Twitter 账号：

```yaml
news_feeds:
  - name: "我的自定义源"
    url: "https://example.com/feed.xml"
    category: "research"  # industry / research / newsletter / tools / tutorial / influencer

twitter_accounts:
  - username: "new_researcher"
    name: "新增研究者"
```

## 输出示例

报告保存在 `reports/ai-daily-YYYY-MM-DD.md`，格式如下：

```markdown
# 🤖 AI 日报 - 2026年03月23日

## 📰 AI 资讯
### 产业动态
- **[GPT-5 正式发布](https://openai.com/...)** - OpenAI | 2026-03-23
  - OpenAI 今日发布 GPT-5，在推理能力上取得重大突破...

## 📄 最新论文
#### 1. [Scaling Laws for Reasoning Models](https://arxiv.org/abs/...)
**作者：** John Doe, Jane Smith 等 12 人
**分类：** `cs.LG / cs.AI`
> 本文研究了推理模型的规模化规律...

## 🧑‍🔬 大牛动态
#### [Andrej Karpathy](https://karpathy.github.io/...)
新的博客文章：深度解析 Transformer 注意力机制...

## 🔥 GitHub 热门 AI 项目
#### 1. [owner/awesome-llm](https://github.com/...)
⭐ 12,345 | `Python`（今日 +234⭐）
```

## Claude Code Skill

安装后可通过 `/ai-daily-news` 命令在 Claude Code 中直接调用：

```
/ai-daily-news
/ai-daily-news --days 3
```
