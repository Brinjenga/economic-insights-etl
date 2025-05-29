# 🌍 World Bank ETL Pipeline

A lightweight ETL pipeline built in Python to extract, transform, and load global development indicators from the [World Bank Open Data API](https://data.worldbank.org/). 
This project demonstrates API integration, data normalization, and file-based data warehousing in Parquet format.

---

## 🚀 Features

- Connects to the World Bank API using country and indicator codes
- Extracts time-series data 
- Transforms JSON responses into a structured tabular format
- Cleans and normalizes data types
- Saves cleaned data as partitioned Parquet files

---

## 🏗️ Project Structure

worldbank-etl-pipeline/
├── config/
│ └── indicators.yaml # List of indicators and countries
├── data/
│ ├── raw/
│ ├── cleaned/
│ └── parquet/
├── logs/
│ └── etl.log
├── notebooks/
│ └── exploration.ipynb
├── src/
│ ├── extract.py # Connects to World Bank API
│ ├── transform.py # Cleans and flattens data
│ ├── load.py # Writes to Parquet
│ └── utils.py # Helpers, logging, config loader
├── tests/
│ └── test_transform.py
├── requirements.txt
├── README.md
└── main.py 

🧪 How to Run
1. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```
2. Run the pipeline:
```bash
python main.py
```
3. Outputs will appear in:
```bash
data/raw/ – Unprocessed API responses

data/cleaned/ – Normalized tabular CSVs

data/parquet/ – Partitioned Parquet files
```

License
MIT License
