# 📊 DataViz AI — Sales Analytics Dashboard

> A production-grade, AI-powered business intelligence dashboard built with Python, Flask, pandas, scikit-learn, and Chart.js.

![Dashboard Preview](frontend/preview.png)

---

## 🎯 Project Overview

DataViz AI is a full-stack data analytics application that ingests raw retail sales data (Superstore dataset), processes it through a pandas data pipeline, generates machine learning forecasts, and presents everything through an interactive dark-mode glassmorphism dashboard.

**This is a real, working product — not a static mockup.**

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────┐
│                   FRONTEND                       │
│  HTML + Vanilla CSS + Chart.js + Vanilla JS      │
│                                                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────────┐  │
│  │ KPI Cards│  │  Charts  │  │ AI Insights  │  │
│  └──────────┘  └──────────┘  └──────────────┘  │
│  ┌──────────────────────────────────────────┐   │
│  │     Filter Bar (Region/Category/Date)    │   │
│  └──────────────────────────────────────────┘   │
└───────────────────┬─────────────────────────────┘
                    │ HTTP REST API (JSON)
┌───────────────────▼─────────────────────────────┐
│                   BACKEND                        │
│              Python / Flask                      │
│                                                  │
│  ┌─────────────┐  ┌───────────────────────────┐ │
│  │  app.py     │  │     data_engine.py         │ │
│  │  (Routes)   │  │   (pandas aggregations)    │ │
│  └─────────────┘  └───────────────────────────┘ │
│                   ┌───────────────────────────┐  │
│                   │    ml_predictor.py         │  │
│                   │  (scikit-learn LR model)   │  │
│                   └───────────────────────────┘  │
└─────────────────────────────────────────────────┘
                    │
┌───────────────────▼─────────────────────────────┐
│                    DATA                          │
│            data.csv / uploaded.csv               │
│         (Superstore retail dataset)              │
└─────────────────────────────────────────────────┘
```

---

## 🔬 Data Pipeline

### Stage 1 — Ingestion & Cleaning (`data_engine.py`)

```python
# Multi-encoding support (utf-8, latin1, windows-1252)
df = pd.read_csv(filepath, encoding=enc)

# Auto date column detection & normalization
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date'])

# Numeric coercion with safe fallback
df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
```

### Stage 2 — Aggregations

```python
# KPIs
total_sales   = df['Sales'].sum()          # → $2,322,048
total_profit  = df['Profit'].sum()         # → $291,550
total_orders  = len(df)                    # → 10,172
profit_margin = (total_profit / total_sales) * 100  # → 12.6%

# Category performance
category_sales = df.groupby('Category')['Sales'].sum()
# → {'Technology': 839550, 'Furniture': 741999, 'Office Supplies': 719498}

# Regional distribution
region_sales = df.groupby('Region')['Sales'].sum()
# → {'West': 725458, 'East': 678781, 'Central': 501240, 'South': 391570}

# Time series (monthly resampling)
monthly_sales = df.groupby(df['Date'].dt.to_period('M'))['Sales'].sum()
```

### Stage 3 — Smart Insights (rule-based AI)

Each insight is **computed from the data**, not hardcoded:

```python
# Insight 1: Top category with real % and $ amounts
top_cat = category_sales.idxmax()
top_pct = round((category_sales.max() / total_sales) * 100)
# → "Technology leads with ~36% of total sales ($839,550 of $2,322,048)"

# Insight 2: Month-over-month trend with direction
pct_change = ((last_month - prev_month) / prev_month) * 100
# → "Sales decreased 📉 by 28% from November to December"

# Insight 3: Regional margin comparison
reg['Margin'] = (reg['Profit'] / reg['Sales'] * 100).round(1)
# → "West leads in profitability (15.2% margin) vs Central at 8.9%"

# Insight 4: Profit mismatch detection
if high_sales_cat['Margin'] < cat['Margin'].mean():
    # → "Furniture has high sales but below-average margin of 7.0%"

# Insight 5: Peak revenue month
peak = monthly_sales.idxmax().strftime('%B %Y')
# → "Peak revenue recorded in November 2026 with $118,455"
```

### Stage 4 — Machine Learning (`ml_predictor.py`)

| Attribute | Value |
|---|---|
| **Model** | `sklearn.linear_model.LinearRegression` |
| **Input** | Monthly aggregated sales, ordinal-encoded dates |
| **Output** | Next N months of predicted revenue |
| **Training data** | 48 monthly data points |
| **Evaluation** | R² Score, Mean Absolute Error |

```python
# Training
monthly = df.groupby(df['Date'].dt.to_period('M'))['Sales'].sum()
monthly['ordinal'] = monthly['Date'].apply(lambda x: x.toordinal())

model = LinearRegression()
model.fit(X=monthly[['ordinal']], y=monthly['Sales'])

# Evaluation
r2  = r2_score(y, model.predict(X))   # e.g. 0.412
mae = mean_absolute_error(y, ...)      # e.g. $18,240

# Prediction
future_dates = [last_date + DateOffset(months=i) for i in range(1, periods+1)]
predictions  = model.predict(future_ordinals)
```

---

## 🌐 REST API Reference

All endpoints return JSON. Chart endpoints support filters via query params.

| Endpoint | Method | Description | Params |
|---|---|---|---|
| `/api/status` | GET | Health check + row count | — |
| `/api/kpi` | GET | Total sales, profit, orders, margin, growth% | `region`, `category`, `date_from`, `date_to` |
| `/api/filters` | GET | Available filter options (regions, categories, date range) | — |
| `/api/sales-trend` | GET | Monthly sales time series | ✅ filterable |
| `/api/category-sales` | GET | Sales + profit per category | ✅ filterable |
| `/api/region-sales` | GET | Sales per region | ✅ filterable |
| `/api/insights` | GET | 5 AI-generated insights with real figures | ✅ filterable |
| `/api/prediction` | GET | ML forecast (actual + predicted + model metrics) | `days` |
| `/api/table` | GET | Raw records (paginated) | ✅ filterable + `limit` |
| `/api/upload` | POST | Upload and process new CSV file | multipart/form-data |

### Example Response — `/api/kpi`

```json
{
  "total_sales":    2322048.33,
  "total_profit":   291550.90,
  "total_orders":   10172,
  "profit_margin":  12.6,
  "growth_percent": -5.03,
  "avg_order_value": 228.28,
  "highest_category": "Technology"
}
```

### Example Response — `/api/prediction`

```json
{
  "dates":     ["2023-01", "2023-02", "...", "2027-03"],
  "actual":    [45231, 62100, "...", null],
  "predicted": [null, null, "...", 95420.50],
  "r2":        0.412,
  "mae":       18240.33,
  "model_info": {
    "type":       "Linear Regression",
    "library":    "scikit-learn",
    "input":      "Monthly aggregated sales (ordinal-encoded dates)",
    "output":     "Next 3 months of predicted revenue",
    "trained_on": "48 monthly data points",
    "r2_score":   0.412,
    "mae":        "$18,240.33",
    "coefficient": 2.4531,
    "intercept":  -312450.12
  }
}
```

---

## 🚀 Running the Project

### Prerequisites

```bash
pip install flask flask-cors pandas numpy scikit-learn
```

### Start

```bash
cd backend
python app.py
```

Open **http://127.0.0.1:5000**

---

## 📁 Project Structure

```
AI Data Visualization/
├── backend/
│   ├── app.py           # Flask routes & API layer
│   ├── data_engine.py   # Pandas cleaning, aggregation, insights
│   ├── ml_predictor.py  # Scikit-learn Linear Regression model
│   └── data.csv         # Default Superstore dataset (4 years)
├── frontend/
│   ├── index.html       # Dashboard UI structure
│   ├── script.js        # API calls, Chart.js rendering, filters
│   └── css/style.css    # Dark glassmorphism theme
└── README.md
```

---

## 💡 Key Technical Decisions

**Why Linear Regression for forecasting?**
Linear regression was chosen as the baseline model because the Superstore dataset shows a discernible long-term upward sales trend across 4 years. It's interpretable, fast to train on small data (48 monthly points), and provides a clean explanation for interviews. The model is evaluated with R² and MAE to quantify accuracy.

**Why pandas over SQL?**
The dataset (10K rows) fits comfortably in memory. Pandas allows fast prototyping of complex aggregations (groupby, resample, rolling) without a database setup, making the project portable and self-contained.

**Why rule-based insights instead of NLP?**
Business insights from structured data are most reliable when derived from deterministic calculations. Each insight is a computed fact (e.g., exact % contribution, real $ figures) rather than a language model hallucination — which is what real BI tools do.

---

## 🎓 Interview Q&A

**Q: What model did you use for prediction?**
A: Linear Regression from scikit-learn. Trained on 48 monthly aggregated data points with ordinal-encoded dates as the feature. Evaluated with R² score and MAE.

**Q: Are insights hardcoded?**
A: No. Every insight is computed at request time from the filtered DataFrame using pandas groupby/aggregation logic. They update dynamically when filters are applied.

**Q: What happens when a new CSV is uploaded?**
A: The file is validated (CSV check, Sales column check, date column detection), loaded into pandas, the ML model is retrained, and all API endpoints immediately return data from the new dataset.

**Q: How do filters work?**
A: The frontend sends `?region=West&category=Technology` query params. The backend applies `df[df['Region'] == region]` before any aggregation. The ML prediction always uses the full dataset for better trend accuracy.
