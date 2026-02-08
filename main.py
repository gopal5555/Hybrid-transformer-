# main.py (top)
import torch

ann_model = None
transformer_model = None

@app.on_event("startup")
def load_models():
    global ann_model, transformer_model

    ann_model = torch.load(
        "models/ann_model.pt",
        map_location="cpu"
    )
    transformer_model = torch.load(
        "models/transformer_model.pth",
        map_location="cpu"
    )

    ann_model.eval()
    transformer_model.eval()

    print("✅ Models loaded successfully")
