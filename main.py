from src.preprocessing import load_data, preprocess
from src.feature_engineering import create_features
from src.train import train_best_model

DATA_PATH = "data/sales.xlsx"

def main():
    df = load_data(DATA_PATH)
    df = preprocess(df)
    df = create_features(df)

    for state in df['state'].unique():
        state_df = df[df['state'] == state]
        train_best_model(state_df, state)

    print("Training complete!")

if __name__ == "__main__":
    main()