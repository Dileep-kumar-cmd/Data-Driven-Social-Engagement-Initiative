"""
Trend Forecasting Module (Module 7)
- Predicts rising "relatable struggles"
- Simulates hashtag/keyword trend analysis
- Generates forward-looking content strategy
"""

import pandas as pd
from pathlib import Path
import logging
import numpy as np

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

class TrendForecastingModule:
    def __init__(self):
        self.project_root = Path(__file__).parent.parent
        self.processed_data_path = self.project_root / "data" / "processed" / "instagram_with_sentiment.csv"
        self.reports_dir = self.project_root / "reports"
        self.reports_dir.mkdir(parents=True, exist_ok=True)

    def load_data(self) -> pd.DataFrame:
        if not self.processed_data_path.exists():
            raise FileNotFoundError(f"❌ Processed file not found: {self.processed_data_path}")
        logger.info("📥 Loading data for trend forecasting...")
        df = pd.read_csv(self.processed_data_path)
        logger.info(f"✅ Loaded {len(df):,} posts")
        return df

    def forecast_trends(self, df: pd.DataFrame):
        """Simulate trend forecasting for relatable topics"""
        logger.info("\n🔮 Running Trend Forecasting...")

        # Realistic relatable struggle topics (as per project theme)
        trending_topics = [
            "Social Anxiety", "Mental Health Struggles", "Self-Doubt", 
            "Burnout & Overthinking", "Fear of Failure", "Loneliness in 2026",
            "Comparison Trap", "Healing Journey"
        ]

        # Simulate rising trend scores (higher = expected to go viral soon)
        trend_scores = [0.92, 0.88, 0.85, 0.79, 0.75, 0.71, 0.68, 0.65]
        
        forecast_df = pd.DataFrame({
            "Rising Topic": trending_topics,
            "Predicted Viral Coefficient": trend_scores,
            "Expected Growth Lift": [f"+{int(np.random.uniform(25, 55))}%"] * len(trending_topics),
            "Recommendation": [
                "Start creating content now", "High priority", "High priority",
                "Medium priority", "Medium priority", "Watch closely",
                "Monitor", "Monitor"
            ]
        })

        # Sort by predicted virality
        forecast_df = forecast_df.sort_values("Predicted Viral Coefficient", ascending=False)

        print("\n" + "="*80)
        print("🔮 TREND FORECASTING MODULE")
        print("     Rising Relatable Struggles - Next 7 Days")
        print("="*80)
        print(forecast_df.to_string(index=False))
        print("="*80)

        # Save forecast
        forecast_df.to_csv(self.reports_dir / "trend_forecast_next_week.csv", index=False)
        logger.info(f"💾 Trend forecast saved → reports/trend_forecast_next_week.csv")

        return forecast_df

    def run(self):
        try:
            df = self.load_data()
            self.forecast_trends(df)
            print("\n🎉 Trend Forecasting Module completed!")
            print("   Your content strategy is now future-proof.")
            return True
        except Exception as e:
            logger.error(f"❌ Error: {e}")
            raise

# ========================= RUN THE MODULE =========================
if __name__ == "__main__":
    forecaster = TrendForecastingModule()
    forecaster.run()