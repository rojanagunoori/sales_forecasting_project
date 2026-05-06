from sklearn.metrics import mean_squared_error
import numpy as np
import pickle
import os

from xgboost import XGBRegressor
from statsmodels.tsa.arima.model import ARIMA
from prophet import Prophet


def rmse(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_true, y_pred))


# ------------------ XGBOOST ------------------
def train_xgb(train_df):

    features = [
        'lag_1','lag_7','lag_30',
        'rolling_mean','rolling_std',
        'day_of_week','month'
    ]

    X = train_df[features]
    y = train_df['sales']

    model = XGBRegressor()
    model.fit(X, y)

    preds = model.predict(X)

    return model, rmse(y, preds)


# ------------------ ARIMA ------------------
def train_arima(train_df):

    train_df = train_df.copy()
    train_df = train_df.asfreq('D')

    model = ARIMA(train_df['sales'], order=(5,1,0))
    model_fit = model.fit()

    preds = model_fit.predict(start=0, end=len(train_df)-1)

    # ✅ FINAL FIX: align + remove NaN properly
    df_compare = train_df[['sales']].copy()
    df_compare['pred'] = preds

    df_compare = df_compare.dropna()

    y_true = df_compare['sales']
    y_pred = df_compare['pred']

    return model_fit, rmse(y_true, y_pred)





# ------------------ PROPHET ------------------
def train_prophet(train_df):

    df = train_df.copy()

    # ✅ FIX: bring index back as column
    df = df.reset_index()

    df = df[['date','sales']].rename(columns={
        'date':'ds',
        'sales':'y'
    })

    model = Prophet()
    model.fit(df)

    future = model.make_future_dataframe(periods=0)
    forecast = model.predict(future)

    return model, rmse(df['y'], forecast['yhat'])


# ------------------ MODEL SELECTOR ------------------
def train_best_model(df, state):

    print(f"Training models for {state}")

    xgb_model, xgb_rmse = train_xgb(df)
    arima_model, arima_rmse = train_arima(df)
    prophet_model, prophet_rmse = train_prophet(df)

    scores = {
        "xgb": xgb_rmse,
        "arima": arima_rmse,
        "prophet": prophet_rmse
    }

    best = min(scores, key=scores.get)

    print(f"Best model for {state}: {best}")

    model_map = {
        "xgb": xgb_model,
        "arima": arima_model,
        "prophet": prophet_model
    }

    os.makedirs("models", exist_ok=True)

    with open(f"models/{state}_model.pkl", "wb") as f:
        pickle.dump((best, model_map[best]), f)