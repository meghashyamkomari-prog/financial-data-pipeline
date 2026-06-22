import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

# Stock symbols to track
STOCKS = ['AAPL', 'MSFT', 'GOOGL', 'JPM', 'BAC']

# PostgreSQL connection
DB_URL = DB_URL = DB_URL = "postgresql://postgres:Mad%4012345@localhost:5432/financial_db"

def fetch_stock_data():
    all_data = []
    
    for symbol in STOCKS:
        print(f"Fetching data for {symbol}...")
        ticker = yf.Ticker(symbol)
        df = ticker.history(period="1y")
        df['symbol'] = symbol
        df['ingested_at'] = datetime.now()
        df = df.reset_index()
        df.columns = [c.lower().replace(' ', '_') for c in df.columns]
        all_data.append(df)
    
    return pd.concat(all_data, ignore_index=True)

def load_to_postgres(df):
    engine = create_engine(DB_URL)
    df.to_sql(
        'raw_stock_prices',
        engine,
        if_exists='replace',
        index=False
    )
    print(f"Loaded {len(df)} rows to raw_stock_prices")

if __name__ == "__main__":
    print("Starting stock data ingestion...")
    df = fetch_stock_data()
    print(f"Fetched {len(df)} total rows")
    load_to_postgres(df)
    print("Done!")