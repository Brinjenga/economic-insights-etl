# This file is now deprecated. The ETL orchestration is handled by Airflow.
# See airflow/dags/economic_insights_etl_dag.py for the Airflow DAG implementation.

# To run the ETL pipeline, start your Airflow scheduler and webserver, then trigger the 'economic_insights_etl' DAG from the Airflow UI or CLI.

# Example Airflow commands:
# airflow dags list
# airflow dags trigger economic_insights_etl

# For more details, see the README and airflow/dags/economic_insights_etl_dag.py

import pandas as pd
from extract.bronze.economic.gdp_pipeline import ingest_gdp_data
from extract.bronze.social.population_pipeline import ingest_population_data
from extract.bronze.environmental.co2_emissions_pipeline import ingest_co2_emissions_data
from extract.bronze.infrastructure.electricity_access_pipeline import ingest_electricity_access_data

COUNTRIES_PARQUET_PATH = 'data/bronze/utils/countries.parquet'
START_YEAR = 2010
END_YEAR = 2011

def main():
    # Read country codes from countries.parquet
    df = pd.read_parquet(COUNTRIES_PARQUET_PATH)
    if 'country_code' not in df.columns:
        raise ValueError("'country_code' column not found in countries.parquet")
    country_codes = df['country_code'].dropna().unique()

    for code in country_codes:
        # Economic: GDP
        ingest_gdp_data(code, START_YEAR, END_YEAR)
        # Social: Population
        ingest_population_data(code, START_YEAR, END_YEAR)
        # Environmental: CO2 Emissions
        ingest_co2_emissions_data(code, START_YEAR, END_YEAR)
        # Infrastructure: Electricity Access
        ingest_electricity_access_data(code, START_YEAR, END_YEAR)

if __name__ == "__main__":
    main()
