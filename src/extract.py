import pandas as pd

def extract(filepath):
    df = pd.read_csv(filepath)
    #print(df["active"].unique())
    df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce")
    #df["active"] = df["active"].map({"True": True, "False": False})
    return df