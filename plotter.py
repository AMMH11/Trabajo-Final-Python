import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

DB_NAME = "stocks.db"

def plot_ticker_data(ticker):
    conn = sqlite3.connect(DB_NAME)
    query = '''
        SELECT date, close
        FROM stocks
        WHERE ticker = ?
        ORDER BY date
    '''
    data = pd.read_sql_query(query, conn, params=(ticker,))
    conn.close()

    if data.empty:
        print(f"No hay datos guardados para el ticker {ticker}.")
        return

    data["date"] = pd.to_datetime(data["date"])
    plt.figure(figsize=(10, 6))
    plt.plot(data["date"], data["close"], label="Precio de cierre", linewidth=2)
    plt.title(f"Precio de cierre para {ticker}")
    plt.xlabel("Fecha")
    plt.ylabel("Precio")
    plt.legend()
    plt.grid()
    plt.show()
