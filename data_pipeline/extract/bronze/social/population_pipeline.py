import sys
import os
from data_pipeline.utils.world_bank_api_utils import fetch_world_bank_data, save_raw_data_to_parquet

# Population Pipeline

def ingest_population_data(country_code, start_year, end_year):
    indicator = "SP.POP.TOTL"  # Total Population
    raw_data = fetch_world_bank_data(country_code, indicator, start_year, end_year)
    save_raw_data_to_parquet(
        raw_data,
        catalog="bronze",
        schema="social",
        table=f"population_{country_code.lower()}"
    )

