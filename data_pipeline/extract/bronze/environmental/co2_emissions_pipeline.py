import sys
import os
from data_pipeline.utils.world_bank_api_utils import fetch_world_bank_data, save_raw_data_to_parquet

# CO2 Emissions Pipeline

def ingest_co2_emissions_data(country_code, start_year, end_year):
    indicator = "EN.ATM.CO2E.KT"  # CO2 emissions (kt)
    raw_data = fetch_world_bank_data(country_code, indicator, start_year, end_year)
    save_raw_data_to_parquet(
        raw_data,
        catalog="bronze",
        schema="environmental",
        table=f"co2_emissions_{country_code.lower()}"
    )

