import sys
import os
import pandas as pd
pd.set_option("display.max_columns", None)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from extract import extract
from transform import transform, quality_report
from load import load

def run_pipeline():
    raw = extract("data/business_partners_raw.csv")
    processed = transform(raw)
    quality_report(raw, processed)
    load(processed, "output/business_partners_processed.csv")
    print(f"Pipeline complete. {len(processed)} records processed.")
    print(processed)

if __name__ == "__main__":
    run_pipeline()
