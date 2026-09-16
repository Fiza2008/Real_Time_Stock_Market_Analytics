import pandas as pd


def calculate_summary(df):
    if df.empty:
        return pd.DataFrame()

    summaries = []

    for symbol, group in df.groupby("symbol"):
        group = group.sort_values("timestamp")
        first_close = group["close"].iloc[0]
        last_close = group["close"].iloc[-1]

        summaries.append({
            "symbol": symbol,
            "latest_price": round(last_close, 2),
            "period_return_pct": round(
                ((last_close - first_close) / first_close) * 100, 2
            ),
            "average_volume": int(group["volume"].mean()),
            "max_price": round(group["high"].max(), 2),
            "min_price": round(group["low"].min(), 2)
        })

    return pd.DataFrame(summaries)


def top_volume_records(df, limit=10):
    if df.empty:
        return pd.DataFrame()

    return (
        df.sort_values("volume", ascending=False)
        [["symbol", "timestamp", "close", "volume"]]
        .head(limit)
    )
