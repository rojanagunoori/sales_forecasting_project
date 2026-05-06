from fastapi import FastAPI
import pickle
import os
import pandas as pd

from src.forecast import forecast_xgb, forecast_arima, forecast_prophet

app = FastAPI()

# base project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@app.get("/")
def home():
    return {"message": "Forecast API running successfully 🚀"}


@app.get("/forecast/{state}")
def forecast(state: str):

    # model path
    model_path = os.path.join(BASE_DIR, "models", f"{state}_model.pkl")

    # check model exists
    if not os.path.exists(model_path):
        return {"error": f"Model for {state} not found"}

    # load model
    model_type, model = pickle.load(open(model_path, "rb"))

    # ---------------- XGBOOST FORECAST ----------------
    if model_type == "xgb":

        last = pd.DataFrame([{
            'lag_1': 100,
            'lag_7': 120,
            'lag_30': 90,
            'rolling_mean': 110,
            'rolling_std': 5,
            'day_of_week': 2,
            'month': 5
        }])

        preds = forecast_xgb(model, last)

    # ---------------- ARIMA FORECAST ----------------
    elif model_type == "arima":
        preds = forecast_arima(model)

    # ---------------- PROPHET FORECAST ----------------
    elif model_type == "prophet":
        preds = forecast_prophet(model, None)

    else:
        return {"error": "Unknown model type"}

    # ---------------- FINAL FIX (IMPORTANT) ----------------
    if hasattr(preds, "tolist"):
        preds = preds.tolist()

    preds = [float(p) for p in preds]

    return {
        "state": state,
        "model_used": model_type,
        "forecast_8_weeks": preds
    }