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

# 收集今日资讯并自动发布到博客
python -m src.main --publish-blog

# 收集过去 3 天的内容
python -m src.main --days 3

# 只收集论文和 GitHub 热点
python -m src.main --skip-news --skip-influencers

# 指定输出目录
python -m src.main --output ./my-reports

# 详细日志模式
python -m src.main --verbose
```

## 博客自动发布

### 工作原理

```
GitHub Actions (每天 08:00 CST)
    ↓ 运行 python -m src.main --publish-blog
    ↓ 生成 Jekyll 格式文章（含 YAML front matter）
    ↓ git clone yf-sz/coco.github.io
    ↓ 写入 _posts/YYYY-MM-DD-ai-daily-news.md
    ↓ git commit + git push
    ↓ GitHub Pages 自动重新构建
```

### 一次性配置

**步骤 1：创建 GitHub PAT**

1. 打开 GitHub → Settings → Developer settings → Personal access tokens → **Fine-grained tokens**
2. 点击 **Generate new token**，设置：
   - Token name：`ai-daily-news-bot`
   - Expiration：建议 1 年
   - Repository access：**Only select repositories** → 选择 `coco.github.io`
   - Permissions → Repository permissions → **Contents**：`Read and write`
3. 复制生成的 token

**步骤 2：在 `ai-daily-news` 仓库添加 Secret**

1. 打开 `yf-sz/ai-daily-news` → Settings → Secrets and variables → **Actions**
2. 点击 **New repository secret**，添加：
   - Name：`BLOG_DEPLOY_TOKEN`
   - Value：粘贴上一步的 PAT

**步骤 3：推送本仓库代码**（触发 Workflow）

```bash
git push origin main
```

GitHub Actions 将从第二天 UTC 00:00（北京时间 08:00）开始每日自动运行。
也可以在 **Actions → Daily AI News → Run workflow** 手动触发。

### 本地一键发布

```bash
# 配置 .env
echo "BLOG_DEPLOY_TOKEN=ghp_xxxx" >> .env
echo "BLOG_REPO_URL=https://github.com/yf-sz/coco.github.io.git" >> .env

# 运行并发布
python -m src.main --publish-blog
```

## 项目结构

```
ai-daily-news/
├── .github/
│   └── workflows/
│       └── daily-ai-news.yml           # GitHub Actions 定时发布
├── src/
│   ├── main.py                         # 主入口（CLI）
│   ├── config.py                       # 配置加载
│   ├── report_generator.py             # Markdown 本地报告生成
│   ├── blog_publisher.py               # Jekyll 博客文章生成 + Git 推送
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

### 环境变量

| 变量 | 必填 | 说明 |
|------|:----:|------|
| `BLOG_DEPLOY_TOKEN` | ✅（发布用） | GitHub PAT，需 `contents:write` 权限 |
| `BLOG_REPO_URL` | ✅（发布用） | 博客仓库地址，如 `https://github.com/yf-sz/coco.github.io.git` |
| `TWITTER_BEARER_TOKEN` | 可选 | 启用 Twitter/X 动态收集 |
| `NEWS_API_KEY` | 可选 | 增强新闻收集 |
| `SEMANTIC_SCHOLAR_API_KEY` | 可选 | 提升论文 API 限制 |

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

### 本地报告（`reports/ai-daily-YYYY-MM-DD.md`）

原始 Markdown 报告，包含完整数据，用于存档。

### 博客文章（`_posts/YYYY-MM-DD-ai-daily-news.md`）

Jekyll 格式，自动推送到 `yf-sz/coco.github.io`：

```markdown
---
layout: post
title: "AI 日报 · 2026年03月23日"
date: 2026-03-23 00:00:00 +0000
categories:
  - "AI日报"
tags:
  - "AI日报"
  - "人工智能"
  - "每日新闻"
description: "今日 AI 速报：18 条资讯 · 15 篇论文 · 8 个热门项目"
toc: true
---

> **今日 AI 速报：18 条资讯 · 15 篇论文 · 8 个热门项目**

## 📰 今日 AI 资讯

### 🏭 产业动态

- **[GPT-5 正式发布](https://openai.com/...)**
  `OpenAI` · 03-23 08:00 UTC
  OpenAI 今日发布 GPT-5，在推理能力上取得重大突破…

## 📄 最新论文速览

**1. [Scaling Laws for Reasoning Models](https://arxiv.org/abs/...)**
  👤 John Doe, Jane Smith 等 12 人 &nbsp;|&nbsp; 📂 `cs.LG` &nbsp;|&nbsp; 🗓 2026-03-23
  [PDF](...) · [Code](...) ⭐1.2k

  > 本文研究了推理模型的规模化规律，发现…

## 🔥 GitHub 热门 AI 项目

**1. [owner/awesome-llm](https://github.com/...)**
  ⭐ 12,345 &nbsp;·&nbsp; 🍴 1,234 &nbsp;·&nbsp; `Python` · 今日 **+234** ⭐
```

## Claude Code Skill

安装后可通过 `/ai-daily-news` 命令在 Claude Code 中直接调用：

```
/ai-daily-news
/ai-daily-news --days 3
```
