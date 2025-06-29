import psycopg2
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

def connect_db():
    return psycopg2.connect(
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

def run_query(sql, values=None):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(sql, values)
    conn.commit()
    cur.close()
    conn.close()

def get_engine():
    return create_engine(
        f'postgresql+psycopg2://'
        f'{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}'
        f'@localhost:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}'
    )