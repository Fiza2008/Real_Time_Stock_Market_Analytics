import pandas as pd
import streamlit as st
import plotly.graph_objects as go

from src.config import DEFAULT_SYMBOLS
from src.database import read_stock_data
from src.data_ingestion import fetch_stock_data
from src.data_processing import clean_data, add_features
from src.database import load_to_database


st.set_page_config(
    page_title="Stock Market Analytics",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Real-Time Stock Market Analytics")
st.caption("Python • Pandas • SQL/SQLite • Streamlit • yfinance")

symbol = st.sidebar.selectbox(
    "Select Stock",
    DEFAULT_SYMBOLS
)

if st.sidebar.button("Refresh Market Data"):
    raw = fetch_stock_data(symbol)
    processed = add_features(clean_data(raw))
    load_to_database(processed)
    st.sidebar.success("Data refreshed.")

df = read_stock_data(symbol)

if df.empty:
    raw = fetch_stock_data(symbol)
    df = add_features(clean_data(raw))
    load_to_database(df)

if df.empty:
    st.error("No data available.")
    st.stop()

df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.sort_values("timestamp")

latest_price = df["close"].iloc[-1]
previous_price = df["close"].iloc[-2] if len(df) > 1 else latest_price
change_pct = ((latest_price - previous_price) / previous_price) * 100

col1, col2, col3, col4 = st.columns(4)

col1.metric("Latest Price", f"${latest_price:,.2f}")
col2.metric("Change", f"{change_pct:.2f}%")
col3.metric("Highest Price", f"${df['high'].max():,.2f}")
col4.metric("Average Volume", f"{df['volume'].mean():,.0f}")

st.subheader(f"{symbol} Price Trend")

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df["timestamp"],
    y=df["close"],
    mode="lines",
    name="Close"
))

if "moving_average_10" in df.columns:
    fig.add_trace(go.Scatter(
        x=df["timestamp"],
        y=df["moving_average_10"],
        mode="lines",
        name="10-period MA"
    ))

if "moving_average_30" in df.columns:
    fig.add_trace(go.Scatter(
        x=df["timestamp"],
        y=df["moving_average_30"],
        mode="lines",
        name="30-period MA"
    ))

fig.update_layout(
    xaxis_title="Time",
    yaxis_title="Price",
    hovermode="x unified"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Trading Volume")

volume_fig = go.Figure()
volume_fig.add_trace(go.Bar(
    x=df["timestamp"],
    y=df["volume"],
    name="Volume"
))

volume_fig.update_layout(
    xaxis_title="Time",
    yaxis_title="Volume"
)

st.plotly_chart(volume_fig, use_container_width=True)

st.subheader("Recent Records")
st.dataframe(
    df.tail(20).sort_values("timestamp", ascending=False),
    use_container_width=True
)
