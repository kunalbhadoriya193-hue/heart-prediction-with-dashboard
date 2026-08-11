import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model = joblib.load(os.path.join(BASE_DIR, "model", "heart_model.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "model", "scaler.pkl"))