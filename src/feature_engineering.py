def create_features(df):
    df = df.copy()

    df['lag_1'] = df['sales'].shift(1)
    df['lag_7'] = df['sales'].shift(7)
    df['lag_30'] = df['sales'].shift(30)

    df['rolling_mean'] = df['sales'].rolling(7).mean()
    df['rolling_std'] = df['sales'].rolling(7).std()

    # ✅ FIXED HERE
    df['day_of_week'] = df.index.dayofweek
    df['month'] = df.index.month

    df = df.dropna()

    return df