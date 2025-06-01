import requests
from pyspark.sql import SparkSession
import json
import os

def fetch_world_bank_data(country_code: str, indicator: str, start_year: int, end_year: int) -> dict:
    """
    Fetch World Bank data for a specific country and year range.

    Args:
        country_code (str): The country code (e.g., 'USA').
        indicator (str): The indicator code (e.g., 'NY.GDP.MKTP.CD').
        start_year (int): The start year for the query.
        end_year (int): The end year for the query.

    Returns:
        dict: The JSON response from the API.
    """
    base_url = "https://api.worldbank.org/v2"
    endpoint = f"country/{country_code}/indicator/{indicator}"
    params = {
        "date": f"{start_year}:{end_year}",
        "format": "json"
    }
    response = requests.get(f"{base_url}/{endpoint}", params=params)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def save_raw_data_to_parquet(raw_data, catalog, schema, table):
    """
    Save raw JSON data to a Parquet file and register it in the specified Spark catalog, schema, and table.
    Args:
        raw_data (dict or list): Raw data from the API.
        catalog (str): The Spark catalog/database name (e.g., 'bronze').
        schema (str): The schema/subfolder name under the catalog (e.g., 'economic').
        table (str): The table name (e.g., 'gdp_usa').
    """
    spark = SparkSession.builder.getOrCreate()
    base_dir = os.path.join("data", catalog, schema)
    os.makedirs(base_dir, exist_ok=True)
    parquet_path = os.path.join(base_dir, f"{table}.parquet")
    json_str = json.dumps(raw_data)
    df = spark.createDataFrame([(json_str,)], ["raw_json"])
    df.write.mode("overwrite").parquet(parquet_path)
    spark.sql(f"CREATE DATABASE IF NOT EXISTS {catalog} LOCATION 'data/{catalog}'")
    spark.sql(f"""
        CREATE TABLE IF NOT EXISTS {catalog}.{schema}_{table}
        (raw_json STRING)
        USING PARQUET
        LOCATION '{parquet_path}'
    """)
