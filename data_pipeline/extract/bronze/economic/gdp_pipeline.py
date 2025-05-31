import sys
import os
from data_pipeline.utils.world_bank_api_utils import fetch_world_bank_data, save_raw_data_to_parquet

# GDP Pipeline
def ingest_gdp_data(country_code, start_year, end_year):
    indicator = "NY.GDP.MKTP.CD"  # GDP (current US$)
    raw_data = fetch_world_bank_data(country_code, indicator, start_year, end_year)
    bronze_dir = os.path.join("data", "bronze", "economic")
    os.makedirs(bronze_dir, exist_ok=True)
    bronze_path = os.path.join(bronze_dir, f"gdp_{country_code.lower()}.parquet")
    save_raw_data_to_parquet(raw_data, bronze_path)

if __name__ == "__main__":
    ingest_gdp_data("USA", 2000, 2020)
