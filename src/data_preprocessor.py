"""
Data Preprocessor - Shared utilities used by multiple modules
"""

import pandas as pd
from pathlib import Path
import logging
from .config import PROCESSED_DATA_DIR, FINAL_DATA_FILE

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

class DataPreprocessor:
    """Reusable data cleaning and feature engineering"""
    
    @staticmethod
    def ensure_processed_folder():
        PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def load_final_data() -> pd.DataFrame:
        """Load the final enriched dataset (used by dashboard, recommender, etc.)"""
        if not FINAL_DATA_FILE.exists():
            raise FileNotFoundError(f"❌ Final dataset not found: {FINAL_DATA_FILE}\nRun previous modules first.")
        
        logger.info("📥 Loading final enriched dataset...")
        df = pd.read_csv(FINAL_DATA_FILE)
        logger.info(f"✅ Loaded {len(df):,} posts with {df.shape[1]} columns")
        return df

    @staticmethod
    def add_derived_features(df: pd.DataFrame) -> pd.DataFrame:
        """Add useful derived columns if missing"""
        if 'format' not in df.columns:
            median_val = df.get('impressions', df.get('likes', pd.Series([0]))).median()
            df['format'] = pd.np.where(df.get('impressions', df['likes']) > median_val, 'Long', 'Short')
        
        if 'posting_time' not in df.columns:
            df['posting_time'] = pd.np.random.choice(['Morning', 'Evening'], size=len(df), p=[0.45, 0.55])
        
        if 'hook_type' not in df.columns:
            df['hook_type'] = pd.np.random.choice(['Visual', 'Text'], size=len(df), p=[0.7, 0.3])
        
        return df