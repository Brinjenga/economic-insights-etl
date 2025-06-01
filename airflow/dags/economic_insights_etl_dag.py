from airflow import DAG
from airflow.operators import PythonOperator
from datetime import datetime
import pandas as pd
from data_pipeline.extract.bronze.economic.gdp_pipeline import ingest_gdp_data
from data_pipeline.extract.bronze.social.population_pipeline import ingest_population_data
from data_pipeline.extract.bronze.environmental.co2_emissions_pipeline import ingest_co2_emissions_data
from data_pipeline.extract.bronze.infrastructure.electricity_access_pipeline import ingest_electricity_access_data

COUNTRIES_PARQUET_PATH = '/opt/airflow/data/bronze/utils/countries.parquet'  # Adjust path as needed for Airflow
START_YEAR = 2010
END_YEAR = 2011

def get_country_codes():
    df = pd.read_parquet(COUNTRIES_PARQUET_PATH)
    if 'country_code' not in df.columns:
        raise ValueError("'country_code' column not found in countries.parquet")
    return df['country_code'].dropna().unique().tolist()

def ingest_gdp(**kwargs):
    for code in get_country_codes():
        ingest_gdp_data(code, START_YEAR, END_YEAR)

def ingest_population(**kwargs):
    for code in get_country_codes():
        ingest_population_data(code, START_YEAR, END_YEAR)

def ingest_co2_emissions(**kwargs):
    for code in get_country_codes():
        ingest_co2_emissions_data(code, START_YEAR, END_YEAR)

def ingest_electricity_access(**kwargs):
    for code in get_country_codes():
        ingest_electricity_access_data(code, START_YEAR, END_YEAR)

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

dag = DAG(
    'economic_insights_etl',
    default_args=default_args,
    description='ETL pipeline for World Bank indicators using Airflow',
    schedule_interval=None,
    catchup=False,
)

gdp_task = PythonOperator(
    task_id='ingest_gdp',
    python_callable=ingest_gdp,
    dag=dag,
)
population_task = PythonOperator(
    task_id='ingest_population',
    python_callable=ingest_population,
    dag=dag,
)
co2_task = PythonOperator(
    task_id='ingest_co2_emissions',
    python_callable=ingest_co2_emissions,
    dag=dag,
)
electricity_task = PythonOperator(
    task_id='ingest_electricity_access',
    python_callable=ingest_electricity_access,
    dag=dag,
)

[gdp_task, population_task, co2_task, electricity_task]
