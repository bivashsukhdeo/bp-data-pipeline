import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from extract import extract
from transform import transform
from load import load

def run_pipeline():
    raw = extract("data/business_partners.csv")
    processed = transform(raw)
    load(processed, "output/business_partners_processed.csv")
    print(f"Pipeline complete. {len(processed)} records processed.")
    print(processed)

if __name__ == "__main__":
    run_pipeline()
