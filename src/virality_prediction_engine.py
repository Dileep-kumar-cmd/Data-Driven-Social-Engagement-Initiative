"""
Virality Prediction Engine (Module 2)
- Calculates Viral Coefficient (weights Shares & Saves heavily)
- Identifies top-performing topics/categories
- Builds a simple ML model to predict viral potential
- Saves results for dashboard and strategy report
"""

import pandas as pd
from pathlib import Path
import logging
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

class ViralityPredictionEngine:
    def __init__(self):
        self.project_root = Path(__file__).parent.parent
        self.processed_data_path = self.project_root / "data" / "processed" / "instagram_performance_processed.csv"
        self.models_dir = self.project_root / "models"
        self.models_dir.mkdir(parents=True, exist_ok=True)
        
        self.model_path = self.models_dir / "virality_model.pkl"

    def load_data(self) -> pd.DataFrame:
        """Load the cleaned dataset from Module 1"""
        if not self.processed_data_path.exists():
            raise FileNotFoundError(
                f"❌ Processed dataset not found!\n"
                f"Expected at: {self.processed_data_path}\n"
                f"Make sure you ran content_performance_tracker.py first."
            )
        
        logger.info("📥 Loading processed Instagram data...")
        df = pd.read_csv(self.processed_data_path)
        logger.info(f"✅ Loaded {len(df):,} posts")
        return df

    def calculate_viral_coefficient(self, df: pd.DataFrame) -> pd.DataFrame:
        """Calculate Viral Coefficient as per project PDF"""
        logger.info("🔥 Calculating Viral Coefficient...")
        
        # Heavy weight on high-value actions (Shares & Saves) as mentioned in PDF
        df['viral_coefficient'] = (
            (df.get('shares', 0) * 2.0) + 
            (df.get('saves', 0) * 1.5) + 
            (df.get('comments', 0) * 1.0)
        ) / (df.get('likes', 0) + 1)   # +1 to avoid division by zero
        
        # Create viral label (we will use this for the ML model)
        df['is_viral'] = (df['viral_coefficient'] > df['viral_coefficient'].quantile(0.75)).astype(int)
        
        logger.info(f"Average Viral Coefficient: {df['viral_coefficient'].mean():.3f}")
        return df

    def analyze_topics(self, df: pd.DataFrame):
        """Show which content categories/topics perform best"""
        logger.info("\n📊 TOP TOPICS BY VIRAL POTENTIAL")
        logger.info("="*60)
        
        if 'content_category' in df.columns:
            topic_analysis = df.groupby('content_category').agg({
                'viral_coefficient': 'mean',
                'shares': 'mean',
                'saves': 'mean',
                'likes': 'mean',
                'is_viral': 'mean'
            }).round(3)
            
            topic_analysis = topic_analysis.sort_values('viral_coefficient', ascending=False)
            print(topic_analysis.head(10))
            
            # Save for later use (strategy report)
            topic_analysis.to_csv(self.project_root / "reports" / "top_topics_viral.csv")
        else:
            logger.warning("⚠️ No 'content_category' column found. Skipping topic analysis.")

    def train_model(self, df: pd.DataFrame):
        """Train a simple Random Forest model to predict viral posts"""
        logger.info("\n🤖 Training Virality Prediction Model...")
        
        # Features for the model
        feature_cols = ['likes', 'comments', 'shares', 'saves', 'reach', 'impressions', 
                       'engagement_rate', 'high_value_actions']
        
        # Use only columns that actually exist
        available_features = [col for col in feature_cols if col in df.columns]
        
        X = df[available_features]
        y = df['is_viral']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        # Evaluate
        y_pred = model.predict(X_test)
        print("\nModel Performance:")
        print(classification_report(y_test, y_pred))
        
        # Save model
        joblib.dump(model, self.model_path)
        logger.info(f"✅ Model saved → {self.model_path}")
        
        return model

    def run(self):
        """Run the complete Virality Prediction Engine"""
        try:
            df = self.load_data()
            df = self.calculate_viral_coefficient(df)
            self.analyze_topics(df)
            self.train_model(df)
            
            # Save final dataset with viral metrics
            output_path = self.project_root / "data" / "processed" / "instagram_with_virality.csv"
            df.to_csv(output_path, index=False)
            logger.info(f"💾 Saved dataset with Viral Coefficient → {output_path}")
            
            print("\n🎉 Virality Prediction Engine completed successfully!")
            return df
            
        except Exception as e:
            logger.error(f"❌ Error: {e}")
            raise

# ========================= RUN THE MODULE =========================
if __name__ == "__main__":
    engine = ViralityPredictionEngine()
    engine.run()