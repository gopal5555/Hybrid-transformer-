from fastapi import FastAPI
from datetime import datetime
import os

app = FastAPI(title="Hybrid Trading Backend")

# ===== GLOBAL FLAGS (ye already load ke time set ho chuke honge) =====
ANN_MODEL_LOADED = True          # jab ann_model load ho
TRANSFORMER_LOADED = True        # jab transformer load ho
DATA_FILE = "data/stocks_daily.csv"

STOP_LOSS = -0.01     # -1%
TARGET   = 0.06       # +6%
UNIVERSE = "NIFTY 50"


@app.get("/health")
def health_check():
    # data updated date
    if os.path.exists(DATA_FILE):
        updated_at = datetime.fromtimestamp(
            os.path.getmtime(DATA_FILE)
        ).strftime("%Y-%m-%d %H:%M:%S")
    else:
        updated_at = "data not found"

    return {
        "status": "OK",
        "backend": "running",
        "ann_model_loaded": ANN_MODEL_LOADED,
        "transformer_loaded": TRANSFORMER_LOADED,
        "data_last_updated": updated_at,
        "universe": UNIVERSE,
        "risk_params": {
            "stop_loss": STOP_LOSS,
            "target": TARGET
        },
        "server_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
