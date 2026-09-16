import numpy as np
import pandas as pd
import yfinance as yf


def fetch_stock_data(symbol, period="1mo", interval="1h"):
    try:
        ticker = yf.Ticker(symbol)
        df = ticker.history(period=period, interval=interval, auto_adjust=False)

        if df.empty:
            raise ValueError("No market data returned.")

        df = df.reset_index()

        time_column = "Datetime" if "Datetime" in df.columns else "Date"

        df = df.rename(columns={
            time_column: "timestamp",
            "Open": "open",
            "High": "high",
            "Low": "low",
            "Close": "close",
            "Volume": "volume"
        })

        df["symbol"] = symbol

        return df[
            ["symbol", "timestamp", "open", "high", "low", "close", "volume"]
        ]

    except Exception as exc:
        print(f"Live data unavailable for {symbol}: {exc}")
        print("Generating sample data for demonstration.")
        return generate_sample_data(symbol)


def generate_sample_data(symbol, periods=180):
    rng = np.random.default_rng(abs(hash(symbol)) % (2**32))
    timestamps = pd.date_range(
        end=pd.Timestamp.now().floor("h"),
        periods=periods,
        freq="h"
    )

    starting_price = 100 + (abs(hash(symbol)) % 300)
    changes = rng.normal(0, 1.2, periods)
    close = starting_price + np.cumsum(changes)
    close = np.maximum(close, 1)

    open_price = close + rng.normal(0, 0.6, periods)
    high = np.maximum(open_price, close) + rng.uniform(0.1, 1.5, periods)
    low = np.minimum(open_price, close) - rng.uniform(0.1, 1.5, periods)
    volume = rng.integers(500_000, 5_000_000, periods)

    return pd.DataFrame({
        "symbol": symbol,
        "timestamp": timestamps,
        "open": open_price.round(2),
        "high": high.round(2),
        "low": low.round(2),
        "close": close.round(2),
        "volume": volume
    })
