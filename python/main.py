from fetch import fetch_all_records
from clean import clean_records
from load import insert_data

def run_pipeline():
    print("Starting AQI data pipeline...")

    records = fetch_all_records()
    if records is None:
        print("Pipeline stopped: fetch failed.")
        return

    df = clean_records(records)
    if len(df) == 0:
        print("Pipeline stopped: no valid rows after cleaning.")
        return

    insert_data(df)
    print("Pipeline completed successfully.")

if __name__ == "__main__":
    run_pipeline()