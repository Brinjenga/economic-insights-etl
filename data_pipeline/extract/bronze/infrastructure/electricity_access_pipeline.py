import sys
import os
from data_pipeline.utils.world_bank_api_utils import fetch_world_bank_data, save_raw_data_to_parquet

def ingest_electricity_access_data(country_code, start_year, end_year):
    indicator = "EG.ELC.ACCS.ZS"  # Access to electricity (% of population)
    raw_data = fetch_world_bank_data(country_code, indicator, start_year, end_year)
    save_raw_data_to_parquet(
        raw_data,
        catalog="bronze",
        schema="infrastructure",
        table=f"electricity_access_{country_code.lower()}"
    )

if __name__ == "__main__":
    ingest_electricity_access_data("NGA", 2000, 2020)
