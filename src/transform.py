import pandas as pd

def assign_band(revenue):
    if revenue >= 5000000:
        return "High"
    elif revenue >= 2000000:
        return "Mid"
    else:
        return "Low"

def transform(df):
    df = df.dropna(subset=["bp_id", "name"])
    df["revenue"] = df["revenue"].fillna(0)
    df["revenue_band"] = df["revenue"].apply(assign_band)
    df["is_high_value"] = df["revenue"] >= 5000000
    return df

def quality_report(raw_df, processed_df):
    print(f"=== Data Quality Report ===")
    print(f"Records received: {len(raw_df)}")
    print(f"Records dropped: {len(raw_df) - len(processed_df)}")
    print(f"Null names: {raw_df['name'].isnull().sum()}")
    print(f"Null revenue: {raw_df['revenue'].isnull().sum()}")
    print(f"Invalid revenue: {raw_df['revenue'].isnull().sum()}")
    print(f"High value BPs: {processed_df['is_high_value'].sum()}")