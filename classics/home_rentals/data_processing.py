import numpy as np
import pandas as pd


def main():
    df = pd.read_csv('raw_data/all_rentals.csv')

    np.random.seed(555)
    split_maks = np.random.rand(len(df)) < 0.8
    train_df = df[split_maks]
    test_df = df[~split_maks]

    train_df.to_csv('dataset/train.csv', index=False)
    test_df.to_csv('dataset/test.csv', index=False)

main()