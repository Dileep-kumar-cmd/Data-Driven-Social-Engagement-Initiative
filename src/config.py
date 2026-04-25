"""
Configuration file - All paths and constants in one place
"""

from pathlib import Path

# Project root
PROJECT_ROOT = Path(__file__).parent.parent

# Data paths
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"
COMMENTS_DIR = PROJECT_ROOT / "data" / "comments"

# File paths
RAW_DATA_FILE = RAW_DATA_DIR / "instagram_performance_raw.csv"
PROCESSED_DATA_FILE = PROCESSED_DATA_DIR / "instagram_performance_processed.csv"
FINAL_DATA_FILE = PROCESSED_DATA_DIR / "instagram_with_sentiment.csv"

# Reports
REPORTS_DIR = PROJECT_ROOT / "reports"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

# Models
MODELS_DIR = PROJECT_ROOT / "models"
MODELS_DIR.mkdir(parents=True, exist_ok=True)

# Dashboard
DASHBOARD_FILE = PROJECT_ROOT / "dashboard" / "app.py"

# Constants
SAMPLE_SIZE_FOR_NLP = 5000
VIRAL_QUANTILE_THRESHOLD = 0.75