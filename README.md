# Data-Driven Social Engagement Initiative

**Major Data Science Project**  
Advanced Statistical Modeling | Virality Prediction | Sentiment Analysis | A/B Testing | Trend Forecasting

---

## 📋 Project Overview

This project builds a complete data-driven analytics ecosystem to measure, predict, and optimize "relatability" in social media content. It replaces creative guesswork with evidence-based insights using statistical modeling, NLP, A/B testing, and visualization.

**Dataset Used**: 29,999 Instagram posts (Kaggle)

---

## 🛠️ Core Modules

| Module | Name | Status |
|--------|------|--------|
| 1 | Content Performance Tracker | ✅ Completed |
| 2 | Virality Prediction Engine | ✅ Completed |
| 3 | Audience Sentiment Analyzer (NLP) | ✅ Completed |
| 4 | A/B Testing Framework | ✅ Completed |
| 5 | Engagement Optimization Recommender | ✅ Completed |
| 6 | Growth Visualization Dashboard | ✅ Completed |
| 7 | Trend Forecasting Module | ✅ Completed |

---
## 🗄️ Database & Visualization (As per Project PDF)

- **Database**: MySQL (`social_engagement_db.instagram_posts`)
- **Visualization Dashboard**: PowerBI (`powerbi/Growth_Visualization_Dashboard.pbix`)
- **Interactive Frontend Dashboard**: Streamlit (`dashboard/app.py`)
---

## 🚀 How to Run the Project

1. Activate the virtual environment:
   ```bash
   venv\Scripts\activate
2. Run the Interactive Dashboard (Main Deliverable):
   ```bash
   streamlit run dashboard/app.py
3. (Optional) Run individual modules:
   ```bash
   python -m src.virality_prediction_engine
   python -m src.audience_sentiment_analyzer
   python -m src.ab_testing_framework
   python -m src.engagement_recommender
   python -m src.trend_forecasting_module
4. Open PowerBI Dashboard:
    Open powerbi/Growth_Visualization_Dashboard.pbix in PowerBI Desktop
---
## 📁 Project Structure

```bash
Data_Driven_Social_Engagement_Initiative/
├── data/
│   └── processed/                  ← Cleaned & enriched datasets (with virality & sentiment)
├── src/                            ← All 7 Core Modules
│   ├── content_performance_tracker.py
│   ├── virality_prediction_engine.py
│   ├── audience_sentiment_analyzer.py
│   ├── ab_testing_framework.py
│   ├── engagement_recommender.py
│   ├── growth_visualization.py
│   └── trend_forecasting_module.py
├── dashboard/
│   └── app.py                      ← Interactive Streamlit Dashboard (Main Deliverable)
├── powerbi/
│   └── Growth_Visualization_Dashboard.pbix   ← PowerBI Dashboard
├── reports/                        ← All deliverables & insights
│   ├── Strategy_Report.docx
│   ├── ab_test_results.csv
│   ├── weekly_optimization_recommendations.csv
│   └── trend_forecast_next_week.csv
├── models/                         ← Saved ML Models
├── requirements.txt
├── README.md
└── Strategy_Report.docx
---
## 📦 Deliverables (All Completed)
 1. Fully functional Analytics Dashboard → dashboard/app.py
 2. Structured Dataset → data/processed/instagram_with_sentiment.csv
 3. NLP Sentiment Model → src/audience_sentiment_analyzer.py
 4. Strategy Report → Strategy_Report.docx
 5. Content Series → Kaggle Instagram dataset used for analysis
---
## 🛠️ Tech Stack
 * Data Processing: Python, Pandas, NumPy
 * NLP: NLTK, TextBlob, VADER
 * Database: MySQL
 * Statistical Modeling: Scikit-learn, SciPy
 * Visualization:PowerBI + Streamlit + Matplotlib/   Seaborn
 * Forntend Dashboard: Streamlit
 ---
Built as Major Data Science Project
April 2026
