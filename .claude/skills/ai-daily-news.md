# AI Daily News Skill

收集今日最新 AI 资讯、论文和大牛动态，生成每日简报。

## 使用方式

```
/ai-daily-news [选项]
```

## 选项

- `--days N`：收集过去 N 天的内容（默认：1）
- `--skip-news`：跳过资讯收集
- `--skip-papers`：跳过论文收集
- `--skip-influencers`：跳过大牛动态收集
- `--skip-github`：跳过 GitHub 热门项目
- `--output PATH`：指定报告输出目录

## 执行步骤

当用户调用此 skill 时，按以下步骤执行：

1. **环境检查**：确认依赖已安装（`pip install -r requirements.txt`），确认 `.env` 文件存在（参考 `.env.example`）

2. **运行收集脚本**：
   ```bash
   cd /home/user/ai-daily-news
   python -m src.main $ARGS
   ```

3. **展示结果**：读取生成的报告文件（`reports/ai-daily-YYYY-MM-DD.md`），以结构化方式呈现给用户，包括：
   - 📰 **AI 资讯摘要**：按分类展示重要新闻
   - 📄 **论文速览**：展示最受关注的新论文（附作者、摘要、代码链接）
   - 🧑‍🔬 **大牛动态**：展示知名 AI 研究者的最新博客和推文
   - 🔥 **GitHub 热门**：今日最热 AI 开源项目

4. **提供互动**：询问用户是否需要：
   - 对某篇论文进行深度解读
   - 对某条资讯展开分析
   - 调整收集范围或来源

## 数据来源

| 类型 | 来源 |
|------|------|
| AI 新闻 | VentureBeat、MIT Tech Review、Google AI Blog、OpenAI Blog、Hugging Face Blog 等 RSS |
| 论文 | arXiv (cs.AI/LG/CL/CV)、Papers With Code |
| 大牛动态 | Twitter/X API、个人博客 RSS（Karpathy、Lilian Weng 等）|
| 开源项目 | GitHub Trending（AI/ML 相关）|

## 配置

在项目根目录创建 `.env` 文件（参考 `.env.example`）：

```bash
# 可选 - 有 Token 则启用 Twitter/X 动态收集
TWITTER_BEARER_TOKEN=xxx

# 可选 - NewsAPI 增强新闻收集
NEWS_API_KEY=xxx

# 自定义设置
MAX_ITEMS_PER_SOURCE=10
DAYS_BACK=1
OUTPUT_DIR=./reports
```

自定义资讯来源：编辑 `config/sources.yaml`，添加 RSS Feed 或 Twitter 账号。
