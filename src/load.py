import pandas as pd

def load(df, filepath):
    df.to_csv(filepath, index=False)