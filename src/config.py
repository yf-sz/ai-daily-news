"""配置加载模块"""
import os
from pathlib import Path

import yaml
from dotenv import load_dotenv

load_dotenv()

ROOT_DIR = Path(__file__).parent.parent
CONFIG_DIR = ROOT_DIR / "config"


def load_sources() -> dict:
    """加载资讯来源配置"""
    config_path = CONFIG_DIR / "sources.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


class Settings:
    # API Keys
    twitter_bearer_token: str = os.getenv("TWITTER_BEARER_TOKEN", "")
    news_api_key: str = os.getenv("NEWS_API_KEY", "")
    semantic_scholar_api_key: str = os.getenv("SEMANTIC_SCHOLAR_API_KEY", "")

    # Output
    output_dir: Path = Path(os.getenv("OUTPUT_DIR", str(ROOT_DIR / "reports")))

    # Limits
    max_items_per_source: int = int(os.getenv("MAX_ITEMS_PER_SOURCE", "10"))
    days_back: int = int(os.getenv("DAYS_BACK", "1"))

    # Request timeout（单个请求超时，并发拉取时总耗时约等于此值）
    request_timeout: int = 8


settings = Settings()
sources = load_sources()
