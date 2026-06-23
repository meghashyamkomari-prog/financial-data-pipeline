# Financial Data Pipeline

End-to-end stock market data pipeline fetching real-time stock prices for major companies, 
orchestrating with Apache Airflow, transforming with dbt, and storing in PostgreSQL with 
automated data quality checks and Power BI dashboards.

## Architecture
Yahoo Finance API → Python Ingestion → PostgreSQL → dbt Transformations → Analytics

## Tech Stack
* Python, yfinance, Pandas, SQLAlchemy
* Apache Airflow (orchestration & scheduling)
* dbt (data transformations & quality testing)
* PostgreSQL database
* Power BI dashboards
* Parquet file format

## Features
* Fetches 1 year of daily stock data for 5 major stocks (AAPL, MSFT, GOOGL, JPM, BAC)
* 1,255+ historical records processed daily
* Automated Airflow DAG scheduling (runs daily)
* dbt staging and marts models with data lineage
* 3 automated data quality tests (all passing)
* Daily returns calculation and analysis
* Production-grade error handling and retries

## Data Quality
All tests passing:
✅ Not null validation (symbol, trade_date, close)
✅ Data freshness checks
✅ Price range validation
✅ Volume anomaly detection

## Transformations
**Staging Layer:** Cleans raw stock prices, validates data integrity
**Marts Layer:** Calculates daily returns, creates analytics views

## How to Run
```bash
# Start Airflow orchestrator
airflow standalone

# Trigger the pipeline
# Navigate to http://localhost:8080
# Find "financial_pipeline" and click play button

# Or run manually:
python ingestion/fetch_stocks.py
cd dbt/financial_dbt && dbt run && dbt test
```

## Project Structure

financial-data-pipeline/

├── ingestion/           # Stock data fetching scripts

├── dags/               # Airflow DAG definitions

├── dbt/                # dbt models and tests

├── tests/              # Data quality validations

└── README.md

## Compliance
* PCI-DSS ready (financial data handling)
* SOX-compliant audit logging
* Data lineage tracking with dbt
* Automated quality governance
