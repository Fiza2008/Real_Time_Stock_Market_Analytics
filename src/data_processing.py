import pandas as pd


def clean_data(df):
    if df.empty:
        return df

    result = df.copy()

    result["timestamp"] = pd.to_datetime(result["timestamp"], errors="coerce")

    numeric_columns = [
        "open", "high", "low", "close", "volume"
    ]

    for column in numeric_columns:
        result[column] = pd.to_numeric(result[column], errors="coerce")

    result = result.dropna(
        subset=["symbol", "timestamp", "open", "high", "low", "close"]
    )

    result = result[
        (result["open"] > 0) &
        (result["high"] > 0) &
        (result["low"] > 0) &
        (result["close"] > 0)
    ]

    result = result.sort_values(["symbol", "timestamp"])
    result = result.drop_duplicates(["symbol", "timestamp"])

    result["volume"] = result["volume"].fillna(0).astype("int64")

    return result


def add_features(df):
    if df.empty:
        return df

    result = df.copy()
    result["daily_return_pct"] = (
        result.groupby("symbol")["close"]
        .pct_change()
        .mul(100)
    )

    result["moving_average_10"] = (
        result.groupby("symbol")["close"]
        .transform(lambda x: x.rolling(10, min_periods=1).mean())
    )

    result["moving_average_30"] = (
        result.groupby("symbol")["close"]
        .transform(lambda x: x.rolling(30, min_periods=1).mean())
    )

    result["rolling_volatility"] = (
        result.groupby("symbol")["daily_return_pct"]
        .transform(lambda x: x.rolling(20, min_periods=5).std())
    )

    return result
