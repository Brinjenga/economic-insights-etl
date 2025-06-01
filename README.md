# 🌍 Economic Insights ETL Pipeline

A robust ETL pipeline built in Python to extract, transform, and load economic, social, environmental, and infrastructure indicators from the World Bank Open Data API. This project demonstrates modular ETL design, API integration, data normalization, and file-based data warehousing in Parquet format.

---

## 🚀 Features

- Modular ETL pipelines for economic, social, environmental, and infrastructure indicators
- Connects to the World Bank API using country and indicator codes
- Extracts time-series data for multiple domains
- Transforms and cleans JSON responses into structured tabular format
- Saves cleaned data as partitioned Parquet files in bronze, silver, and gold layers
- Logging for ETL processes

---

## 🏗️ Project Structure

economic-insights-etl/
├── airflow/                  # Airflow orchestration (optional)
│   ├── dags/
│   └── docker-compose.yml
├── artifacts/                # Model artifacts or outputs
├── backend/                  # Backend API (Node.js)
├── data/
│   ├── bronze/               # Raw data (partitioned Parquet)
│   ├── silver/               # Cleaned/transformed data
│   └── gold/                 # Data for analytics/logic
├── data_pipeline/
│   ├── extract/              # Extraction scripts by domain
│   │   ├── bronze/
│   │   │   ├── economic/
│   │   │   ├── social/
│   │   │   ├── environmental/
│   │   │   ├── infrastructure/
│   │   │   └── util/
│   │   ├── silver/
│   │   └── gold/
│   ├── load/                 # Loaders (e.g., save_to_parquet.py)
│   ├── transform/            # Transformers (e.g., clean_data.py)
│   └── utils/                # Utilities (e.g., world_bank_api_utils.py)
├── frontend/                 # Frontend (React)
├── requirements.txt
├── README.md
└── main.py 

---

## 🧪 How to Run

1. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```
2. Run the pipeline:
```bash
python -m data_pipeline.main_pipeline
```
3. Outputs will appear in:
```bash
data/bronze/ – raw data

data/silver/ – transformed data

data/gold/ – data used in analytics/logic
```

---

## 📁 Data Layers
- **Bronze:** Raw data as received from the API
- **Silver:** Cleaned and normalized data
- **Gold:** Data ready for analytics and business logic

---

## 📝 Notes
- Airflow DAGs for orchestration are available in the `airflow/dags/` directory (optional)
- Backend and frontend folders are for API and UI extensions (optional)

---

📚 License
MIT License
