# 🔷 Veritas Pro — Fake News Detection Dashboard

An AI-powered system that detects fake news, explains *why* it's fake, and tracks analysis through a professional dashboard.

---

## ✨ Features

| Feature | Description |
|---|---|
| **Fake/Real Classification** | ML-powered text classification using Logistic Regression + TF-IDF |
| **Explainability** | Keyword importance + Sentiment analysis (VADER) |
| **Confidence Score** | Probability-based confidence for every prediction |
| **Dashboard** | Real-time metrics, donut chart, recent activity feed |
| **Scan History** | Searchable history with CSV export |
| **Demo Mode** | Works out-of-the-box without needing to train a model |

---

## 🏗️ Architecture

```
User Input → Frontend (HTML/CSS/JS SPA)
                ↓
           FastAPI Backend (/api/predict)
                ↓
           ML Module (TF-IDF + Logistic Regression)
                ↓
           Explainability (VADER + Keyword Weights)
                ↓
           SQLite (Persist results)
                ↓
           Dashboard UI Update
```

---

## 📁 Project Structure

```
├── ml/
│   ├── predict.py          # Prediction + explainability module
│   └── train.py            # Model training script
├── backend/
│   ├── main.py             # FastAPI app + API endpoints
│   └── database.py         # SQLite data layer
├── frontend/
│   ├── index.html           # SPA shell
│   ├── css/styles.css       # Dark-mode design system
│   └── js/
│       ├── api.js           # Backend API wrappers
│       ├── router.js        # SPA view router
│       ├── app.js           # State management + init
│       ├── components/      # Reusable UI components
│       │   ├── sidebar.js
│       │   ├── card.js
│       │   └── table.js
│       └── views/           # Page views
│           ├── dashboard.js
│           ├── analyzer.js
│           └── history.js
├── run.py                   # One-command launcher
├── requirements.txt
└── README.md
```

---

## 🚀 Quick Start

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the application

```bash
python run.py
```

The dashboard opens at **http://localhost:8000**

---

## 🧠 Train Your Own Model (Optional)

For higher accuracy, train on the [WELFake Dataset](https://www.kaggle.com/datasets/saurabhshahane/fake-news-classification):

```bash
# Download the dataset and place CSV in data/ folder
python -m ml.train --data data/WELFake_Dataset.csv
```

This generates `ml/model.pkl` and `ml/vectorizer.pkl` for production-grade predictions.

Without a trained model, the system runs in **Demo Mode** using keyword heuristics + VADER sentiment.

---

## 📡 API Reference

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/predict` | Classify text → { label, confidence, keywords, sentiment } |
| `GET` | `/api/stats` | Aggregate statistics |
| `GET` | `/api/history` | Scan history (supports `?search=` and `?limit=`) |
| `DELETE` | `/api/history` | Clear all history |

---

## 🛠️ Technology Stack

- **Frontend:** HTML, CSS, JavaScript (Vanilla SPA)
- **Backend:** Python, FastAPI, Uvicorn
- **ML:** Scikit-learn, TF-IDF, Logistic Regression
- **NLP:** NLTK (VADER Sentiment)
- **Database:** SQLite
- **Charts:** Chart.js

---

## 📌 Future Improvements

- BERT-based deep learning model for higher accuracy
- Real-time news API integration
- Multi-language support
- Browser extension for live detection

---

## 📝 License

MIT License — Built for academic & educational purposes.
