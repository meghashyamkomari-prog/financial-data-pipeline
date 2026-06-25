import pandas as pd
from sqlalchemy import create_engine

DB_URL = "postgresql://postgres:Mad%4012345@localhost:5432/financial_db"

print("Loading aggregated data to PostgreSQL...")

# Load aggregated data
state_agg = pd.read_csv("data/aggregated/by_state.csv")
specialty_agg = pd.read_csv("data/aggregated/by_specialty.csv")

# Connect to database
engine = create_engine(DB_URL)

# Load tables
state_agg.to_sql('healthcare_by_state', engine, if_exists='replace', index=False)
specialty_agg.to_sql('healthcare_by_specialty', engine, if_exists='replace', index=False)

print(f"Loaded {len(state_agg)} state records")
print(f"Loaded {len(specialty_agg)} specialty records")
print("Done!")
