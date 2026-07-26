import pandas as pd

def assign_band(revenue):
    if revenue >= 5000000:
        return "High"
    elif revenue >= 2000000:
        return "Mid"
    else:
        return "Low"

def transform(df):
    df = df.dropna(subset=["bp_id"])
    df["revenue"] = df["revenue"].fillna(0)
    df["revenue_band"] = df["revenue"].apply(assign_band)
    return df