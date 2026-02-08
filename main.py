@app.on_event("startup")
def load_models():
    global ann_model, transformer_model, ann_scaler

    # ANN
    ann_model = SimpleANN(input_dim=6)
    ann_model.load_state_dict(
        torch.load("ann_model.pt", map_location="cpu")
    )
    ann_model.eval()

    # Transformer
    transformer_model = TransformerModel(input_dim=6)
    transformer_model.load_state_dict(
        torch.load("transformer_model.pth", map_location="cpu")
    )
    transformer_model.eval()

    # Scaler
    with open("ann_scaler.pkl", "rb") as f:
        ann_scaler = pickle.load(f)

    print("✅ Models loaded correctly")# -------------------------
# Test API (safe)
# -------------------------
@app.get("/")
def root():
    return {"message": "API running"}
