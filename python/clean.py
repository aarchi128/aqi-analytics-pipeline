import pandas as pd

def clean_records(records):
    """Convert raw API records into a cleaned, typed pandas DataFrame."""
    df = pd.DataFrame(records)

    # Convert text columns to real numbers
    df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
    df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")
    df["min_value"] = pd.to_numeric(df["min_value"], errors="coerce")
    df["max_value"] = pd.to_numeric(df["max_value"], errors="coerce")
    df["avg_value"] = pd.to_numeric(df["avg_value"], errors="coerce")

    # Convert date format (DD-MM-YYYY) to proper datetime
    df["last_update"] = pd.to_datetime(df["last_update"], format="%d-%m-%Y %H:%M:%S", errors="coerce")

    # Drop rows with missing/invalid values
    df = df.dropna(subset=["latitude", "longitude", "min_value", "max_value", "avg_value", "last_update"])

    # Drop non-positive readings (sensor errors)
    df = df[df["avg_value"] > 0]

    # Drop duplicates within this pull
    df = df.drop_duplicates(subset=["station", "pollutant_id", "last_update"])

    print("Rows remaining after cleaning:", len(df))
    return df