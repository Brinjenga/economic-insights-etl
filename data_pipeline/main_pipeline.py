
from extract.world_bank_api import fetch_gdp_data
from transform.clean_data import clean_gdp_data
from load.save_to_parquet import save_to_parquet

def main():
    """
    Main pipeline to extract, transform, and load GDP data.
    """
    # Step 1: Extract
    country_code = "USA"
    start_year = 2000
    end_year = 2020
    raw_data = fetch_gdp_data(country_code, start_year, end_year)

    # Step 2: Transform
    cleaned_data = clean_gdp_data(raw_data)

    # Step 3: Load
    output_path = "../data/parquet/gdp_data.parquet"
    save_to_parquet(cleaned_data, output_path)

if __name__ == "__main__":
    main()