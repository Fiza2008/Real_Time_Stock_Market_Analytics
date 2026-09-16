import sqlite3
import pandas as pd
from .config import DATABASE_PATH


def get_connection():
    return sqlite3.connect(DATABASE_PATH)


def create_tables():
    query = '''
    CREATE TABLE IF NOT EXISTS stock_prices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        symbol TEXT NOT NULL,
        timestamp TEXT NOT NULL,
        open REAL,
        high REAL,
        low REAL,
        close REAL,
        volume INTEGER,
        UNIQUE(symbol, timestamp)
    )
    '''
    with get_connection() as conn:
        conn.execute(query)
        conn.commit()


def load_to_database(df):
    if df.empty:
        return

    create_tables()

    columns = [
        "symbol", "timestamp", "open",
        "high", "low", "close", "volume"
    ]

    data = df[columns].copy()

    # SQLite does not natively bind pandas.Timestamp objects.
    # Convert timestamps to ISO-8601 strings before insertion.
    data["timestamp"] = pd.to_datetime(
        data["timestamp"], errors="coerce"
    ).map(lambda value: value.isoformat() if pd.notna(value) else None)

    data = data.dropna(subset=["timestamp"])

    rows = list(data.itertuples(index=False, name=None))

    with get_connection() as conn:
        conn.executemany(
            '''
            INSERT OR REPLACE INTO stock_prices
            (symbol, timestamp, open, high, low, close, volume)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ''',
            rows
        )
        conn.commit()


def read_stock_data(symbol=None):
    create_tables()

    query = "SELECT * FROM stock_prices"
    params = ()

    if symbol:
        query += " WHERE symbol = ?"
        params = (symbol,)

    query += " ORDER BY timestamp"

    with get_connection() as conn:
        return pd.read_sql_query(query, conn, params=params)
