
from extract.world_bank_api import fetch_data_by_country_and_year
from transform.clean_data import clean_gdp_data
from load.save_to_parquet import save_to_parquet

def run_etl_pipeline(country_code, indicator,start_year, end_year, output_path):
    """
    Run the ETL pipeline to extract, transform, and load GDP data.

    :param country_code: ISO 3166-1 alpha-2 country code (e.g., 'US').
    :param start_year: Start year for the data (e.g., 2000).
    :param end_year: End year for the data (e.g., 2020).
    :param output_path: Path to save the transformed data in Parquet format.
    """
    # Step 1: Extract
    print("Extracting data...")
    raw_data = fetch_data_by_country_and_year(country_code,indicator, start_year, end_year)

    # Step 2: Transform
    print("Transforming data...")
    cleaned_data = clean_gdp_data(raw_data)

    # Step 3: Load
    print("Loading data...")
    save_to_parquet(cleaned_data, output_path)
    print(f"Data successfully saved to {output_path}")

# Example usage:
if __name__ == "__main__":
    run_etl_pipeline(
        country_code="USA",
        start_year=2000,
        end_year=2020,
        output_path="../data/parquet/gdp_data.parquet"
    )