"""
Content Performance Tracker (Module 1)
- Loads raw Instagram performance data (from Kaggle)
- Cleans and standardizes it
- Computes basic engagement metrics
- Saves processed dataset for all other modules
"""

import pandas as pd
from pathlib import Path
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

class ContentPerformanceTracker:
    def __init__(self):
        self.project_root = Path(__file__).parent.parent
        self.raw_data_path = self.project_root / "data" / "raw" / "instagram_performance_raw.csv"
        self.processed_data_path = self.project_root / "data" / "processed" / "instagram_performance_processed.csv"
        
        # Create processed folder if it doesn't exist
        self.processed_data_path.parent.mkdir(parents=True, exist_ok=True)

    def load_raw_data(self) -> pd.DataFrame:
        """Load the raw Kaggle dataset"""
        if not self.raw_data_path.exists():
            raise FileNotFoundError(
                f"❌ Raw dataset not found!\n"
                f"Expected at: {self.raw_data_path}\n"
                f"Please download the Kaggle dataset and place it there."
            )
        
        logger.info("📥 Loading raw Instagram performance data...")
        df = pd.read_csv(self.raw_data_path)
        logger.info(f"✅ Loaded {len(df):,} posts with {df.shape[1]} columns")
        return df

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Clean and standardize the dataset"""
        logger.info("🧹 Cleaning and standardizing data...")
        
        # Standard column name mapping (works with most Kaggle IG datasets)
        column_map = {
            'Impressions': 'impressions',
            'Reach': 'reach',
            'Saves': 'saves',
            'Shares': 'shares',
            'Likes': 'likes',
            'Comments': 'comments',      # some datasets have 'Comment'
            'Comment': 'comments',
            'Profile Visits': 'profile_visits',
            'From Home': 'from_home',
            'From Hashtags': 'from_hashtags',
            'From Explore': 'from_explore',
        }
        
        df = df.rename(columns=lambda x: column_map.get(x, x.lower().replace(' ', '_').replace('.', '')))
        
        # Fill missing values (common in these datasets)
        numeric_cols = ['impressions', 'reach', 'saves', 'shares', 'likes', 'comments', 'profile_visits']
        for col in numeric_cols:
            if col in df.columns:
                df[col] = df[col].fillna(0)
        
        # Add derived metrics (very important for later modules)
        df['engagement_rate'] = 0.0
        if 'likes' in df.columns and 'impressions' in df.columns:
            df['engagement_rate'] = (
                (df['likes'] + df.get('comments', 0) + df.get('saves', 0) + df.get('shares', 0)) 
                / df['impressions'].replace(0, 1) * 100
            )
        
        # High-value action score (used in Virality Engine later)
        df['high_value_actions'] = (
            df.get('saves', 0) * 1.5 + 
            df.get('shares', 0) * 2.0
        )
        
        logger.info("✅ Data cleaning completed")
        return df

    def run(self):
        """Main method — run this to execute the tracker"""
        try:
            df = self.load_raw_data()
            df_clean = self.clean_data(df)
            
            # Save processed data
            df_clean.to_csv(self.processed_data_path, index=False)
            logger.info(f"💾 Saved processed dataset → {self.processed_data_path}")
            
            # Print summary report
            print("\n" + "="*60)
            print("📊 CONTENT PERFORMANCE TRACKER SUMMARY")
            print("="*60)
            print(f"Total Posts Analyzed     : {len(df_clean):,}")
            print(f"Avg Impressions          : {df_clean.get('impressions', pd.Series([0])).mean():.1f}")
            print(f"Avg Saves                : {df_clean.get('saves', pd.Series([0])).mean():.1f}")
            print(f"Avg Shares               : {df_clean.get('shares', pd.Series([0])).mean():.1f}")
            print(f"Avg Engagement Rate      : {df_clean['engagement_rate'].mean():.2f}%")
            print(f"Total High-Value Actions : {df_clean['high_value_actions'].sum():,}")
            print("="*60)
            
            return df_clean
            
        except Exception as e:
            logger.error(f"❌ Error: {e}")
            raise

# ========================= RUN THE MODULE =========================
if __name__ == "__main__":
    tracker = ContentPerformanceTracker()
    tracker.run()