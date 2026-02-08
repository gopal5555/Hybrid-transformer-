from fastapi import FastAPI
import torch

app = FastAPI()   # ← yeh line missing thi

# -------------------------
# Startup: model load
# -------------------------
ann_model = None
transformer_model = None

@app.on_event("startup")
def load_models():
    global ann_model, transformer_model

    ann_model = torch.load(
        "ann_model.pt",
        map_location="cpu"
    )
    transformer_model = torch.load(
        "transformer_model.pth",
        map_location="cpu"
    )

    ann_model.eval()
    transformer_model.eval()

    print("✅ Models loaded")

# -------------------------
# Health check
# -------------------------
@app.get("/health")
def health():
    return {"status": "ok"}

# -------------------------
# Test API (safe)
# -------------------------
@app.get("/")
def root():
    return {"message": "API running"}
