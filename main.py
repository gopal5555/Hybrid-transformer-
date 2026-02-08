from fastapi import FastAPI
import pandas as pd
from datetime import datetime

app = FastAPI()

HISTORY_FILE = "data/signals_history.csv"

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/history")
def history(days: int = 5):
    df = pd.read_csv(HISTORY_FILE)
    df["date"] = pd.to_datetime(df["date"])
    cutoff = pd.Timestamp.today() - pd.Timedelta(days=days)
    df = df[df["date"] >= cutoff]
    return df.sort_values("date", ascending=False).to_dict("records")
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "status": "running",
        "message": "Hybrid ANN + Transformer API live",
        "endpoints": [
            "/health",
            "/predict",
            "/history/{symbol}"
        ]
    }
