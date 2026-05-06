import pandas as pd

def load_data(path):
    df = pd.read_excel(path)
    df.columns = ['state', 'date', 'sales', 'category']

    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values(['state', 'date'])

    # clean numbers (remove commas)
    df['sales'] = df['sales'].astype(str).str.replace(',', '')
    df['sales'] = df['sales'].astype(float)

    return df

def preprocess(df):
    df = df.copy()

    df['date'] = pd.to_datetime(df['date'])

    # sort
    df = df.sort_values(['state', 'date'])

    # set index properly
    df = df.set_index('date')

    # fill missing dates per state
    df = df.groupby('state').apply(
        lambda x: x.asfreq('D')
    ).reset_index()

    # fill missing sales
    df['sales'] = df['sales'].ffill()

    # 🔥 IMPORTANT: set index again
    df = df.set_index('date')

    return df