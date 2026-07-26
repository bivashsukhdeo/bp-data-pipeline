# bp-data-pipeline

# Business Partner Data Pipeline

A Python ETL pipeline that ingests, validates, and transforms Business Partner master data — modelled on SAP S/4HANA migration data structures.

## What it does

- **Extract**: Reads raw Business Partner CSV data, handles missing values and type casting
- **Transform**: Validates records, fills missing revenue with 0, classifies partners into revenue bands (High / Mid / Low)
- **Load**: Writes processed output to CSV

## Project structure

bp-data-pipeline/
├── data/ # Raw input data
├── output/ # Processed output (git-ignored)
├── src/
│ ├── extract.py # Data ingestion and type casting
│ ├── transform.py # Cleaning, validation, enrichment
│ ├── load.py # Output writer
│ └── pipeline.py # Pipeline orchestrator
└── README.md

## How to run

```bash
python src/pipeline.py
```

## Tech stack

- Python 3.12
- pandas

## Background

This project draws on hands-on experience with Business Partner master data from SAP S/4HANA migrations. The pipeline reframes that domain knowledge in a modern Python/pandas stack.