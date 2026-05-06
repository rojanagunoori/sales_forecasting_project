import pandas as pd

# def forecast_xgb(model, last_row, steps=56):
#     preds = []

#     current = last_row.copy()

#     for i in range(steps):
#         X = current[['lag_1','lag_7','lag_30',
#                      'rolling_mean','rolling_std',
#                      'day_of_week','month']]

#         pred = model.predict(X.values.reshape(1,-1))[0]
#         pred = max(0, pred)

#         preds.append(pred)

#         current['lag_1'] = pred

#     return preds


import numpy as np

def forecast_xgb(model, last_row, steps=56):

    preds = []
    current = last_row.copy()

    history = list(current['lag_30'] * 30 if isinstance(current['lag_30'], (int, float)) else [0]*30)

    for _ in range(steps):

        X = current[['lag_1','lag_7','lag_30',
                     'rolling_mean','rolling_std',
                     'day_of_week','month']]

        pred = model.predict(X.values.reshape(1, -1))[0]
        pred = max(0, float(pred))

        preds.append(pred)

        # ---------------- FIX: update history properly ----------------
        history.append(pred)

        # rebuild lag features from real sequence
        current['lag_1'] = history[-1]
        current['lag_7'] = history[-7] if len(history) >= 7 else history[0]
        current['lag_30'] = history[-30] if len(history) >= 30 else history[0]

        # rolling features based on real history
        window = history[-7:]
        current['rolling_mean'] = np.mean(window)
        current['rolling_std'] = np.std(window)

    return preds


    

def forecast_arima(model, steps=56):
    forecast = model.forecast(steps=steps)
    return [max(0, float(x)) for x in forecast]


def forecast_prophet(model, last_date, steps=56):
    future = model.make_future_dataframe(periods=steps)
    forecast = model.predict(future)
    return forecast['yhat'].tail(steps).clip(lower=0).tolist()