import requests
import pandas as pd

API_KEY = "Tb0xW0kjGYar0KwlPmSVSELGOzUZUz4qX"  #  API de Polygon.io

def fetch_stock_data(ticker, start_date, end_date):
    url = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/{start_date}/{end_date}?apiKey={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json().get("results", [])
        if not data:
            print(f"No se encontraron datos para {ticker}.")
            return None
        df = pd.DataFrame(data)
        df["date"] = pd.to_datetime(df["t"], unit="ms").dt.date
        return df[["date", "o", "h", "l", "c", "v"]]
    else:
        print(f"Error al obtener datos de la API: {response.status_code}")
        return None
