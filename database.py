import sqlite3

DB_NAME = "stocks.db"

def initialize_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stocks (
            ticker TEXT,
            date TEXT,
            open REAL,
            high REAL,
            low REAL,
            close REAL,
            volume INTEGER,
            PRIMARY KEY (ticker, date)
        )
    ''')
    conn.commit()
    conn.close()

def save_stock_data(ticker, data):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    for _, row in data.iterrows():
        cursor.execute('''
            INSERT OR IGNORE INTO stocks (ticker, date, open, high, low, close, volume)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (ticker, row["date"], row["o"], row["h"], row["l"], row["c"], row["v"]))
    conn.commit()
    conn.close()

def get_saved_tickers():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT ticker, MIN(date) AS start_date, MAX(date) AS end_date
        FROM stocks
        GROUP BY ticker
    ''')
    tickers = cursor.fetchall()
    conn.close()
    return tickers
