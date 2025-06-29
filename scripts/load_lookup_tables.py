import os

import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from utils.db_utils import connect_db, get_engine

load_dotenv()

# connect to PostgreSQL database
connect_db()

engine = get_engine()

genre = pd.read_csv('../data/processed/genre.csv')
publisher = pd.read_csv('../data/processed/publisher.csv')
platform = pd.read_csv('../data/processed/platform.csv')

try:
    genre.to_sql('genre', engine, schema='games', if_exists='append', index=False)
    publisher.to_sql('publisher', engine, schema='games', if_exists='append', index=False)
    platform.to_sql('platform', engine, schema='games', if_exists='append', index=False)
except Exception as e:
    print(e)