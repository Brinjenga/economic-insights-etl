import sys
import os
import requests
from data_pipeline.utils.world_bank_api_utils import save_raw_data_to_parquet
import pandas as pd
from pyspark.sql import SparkSession

def fetch_all_countries():
    """
    Fetch a list of all countries and their country codes from the World Bank API.
    Returns:
        dict: The JSON response containing country data.
    """
    url = "https://api.worldbank.org/v2/country?format=json&per_page=400"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def transform_countries_to_tabular(raw_data):
    """
    Transform the raw JSON country data to a tabular format (list of dicts).
    Returns a pandas DataFrame.
    """
    # The country data is in raw_data[1]
    countries = raw_data[1] if isinstance(raw_data, list) and len(raw_data) > 1 else []
    records = []
    for entry in countries:
        records.append({
            'id': entry.get('id'),
            'name': entry.get('name'),
            'region': entry.get('region', {}).get('value'),
            'incomeLevel': entry.get('incomeLevel', {}).get('value'),
            'iso2Code': entry.get('iso2Code'),
            'capitalCity': entry.get('capitalCity'),
            'longitude': entry.get('longitude'),
            'latitude': entry.get('latitude')
        })
    return pd.DataFrame(records)

def ingest_countries():
    raw_data = fetch_all_countries()
    df = transform_countries_to_tabular(raw_data)
    spark = SparkSession.builder.getOrCreate()
    spark_df = spark.createDataFrame(df)
    base_dir = os.path.join("data", "bronze", "utils")
    os.makedirs(base_dir, exist_ok=True)
    parquet_path = os.path.join(base_dir, "countries.parquet")
    spark_df.write.mode("overwrite").parquet(parquet_path)
    # Optionally, register as a table
    spark.sql("CREATE DATABASE IF NOT EXISTS bronze LOCATION 'data/bronze'")
    spark.sql(f"""
        CREATE TABLE IF NOT EXISTS bronze.utils_countries
        USING PARQUET
        LOCATION '{parquet_path}'
    """)

if __name__ == "__main__":
    ingest_countries()
