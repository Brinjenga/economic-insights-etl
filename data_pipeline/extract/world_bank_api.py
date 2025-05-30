import requests


def fetch_data_by_country_and_year(country_code: str, indicator: str, start_year: int, end_year: int) -> dict:
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



# Example usage:
# data = fetch_data_by_country_and_year("USA", "NY.GDP.MKTP.CD", 2000, 2020)
# print(data)
