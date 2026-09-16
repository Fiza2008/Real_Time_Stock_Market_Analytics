# 📈 Real-Time Stock Market Analytics

<p align="center">
  <strong>A Python-based market data pipeline and interactive analytics dashboard</strong>
</p>

<p align="center">
  🐍 Python • 🐼 Pandas • 🗄️ SQL/SQLite • 📊 Streamlit • 📈 Plotly • 🌐 yfinance
</p>

---

## 📌 Overview

**Real-Time Stock Market Analytics** is a Python-based data analytics project that collects stock market data, processes and validates time-series records, stores structured data in a SQLite database, performs analytical calculations using Python and SQL, and presents the results through an interactive Streamlit dashboard.

The project demonstrates a practical end-to-end data workflow:

**Data Ingestion → Data Cleaning → Data Transformation → Database Storage → Analytics → Visualization**

It was developed to demonstrate practical concepts relevant to **Data Engineering, Data Analytics, Python, SQL, databases, and cloud-ready data workflows**.



## 🎯 Objectives

The main objectives of this project are:

- Collect stock market data programmatically.
- Build a reusable data ingestion pipeline.
- Clean and validate incoming market data.
- Transform raw time-series data into analytical features.
- Store structured records in a relational database.
- Perform SQL-based analysis.
- Calculate stock performance metrics.
- Visualize market trends through an interactive dashboard.
- Handle external data-source failures gracefully.

---

# 🏗️ System Architecture

```text
                 ┌────────────────────────┐
                 │    Yahoo Finance       │
                 │    Market Data Source  │
                 └────────────┬───────────┘
                              │
                              ▼
                 ┌────────────────────────┐
                 │    Data Ingestion      │
                 │        Python          │
                 └────────────┬───────────┘
                              │
                              ▼
                 ┌────────────────────────┐
                 │ Data Cleaning &         │
                 │ Transformation          │
                 │       Pandas            │
                 └────────────┬───────────┘
                              │
                              ▼
                 ┌────────────────────────┐
                 │    SQLite Database     │
                 │   Structured Storage   │
                 └────────────┬───────────┘
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
          ┌──────────────────┐  ┌──────────────────┐
          │   SQL Analytics  │  │ Python Analytics │
          └────────┬─────────┘  └────────┬─────────┘
                   │                     │
                   └──────────┬──────────┘
                              ▼
                 ┌────────────────────────┐
                 │   Streamlit Dashboard  │
                 │       + Plotly         │
                 └────────────────────────┘







✨ Features
📥 1. Market Data Ingestion
The project retrieves stock market data programmatically using the yfinance Python library.

Example supported symbols:
AAPL
MSFT
GOOGL
AMZN
NVDA
TSLA

The ingestion process collects:
Stock symbol
Timestamp
Open price
High price
Low price
Closing price
Trading volume


🧹 2. Data Cleaning & Validation
Raw market data is processed before being stored in the database.

The cleaning process:
Converts timestamps into a consistent datetime format.
Converts price and volume fields into numeric data types.
Removes records with invalid critical values.
Removes duplicate timestamp records.
Sorts records chronologically.
Validates positive price values.
Handles missing volume values.

This ensures that downstream analytics operate on structured and validated data.


⚙️ 3. Feature Engineering
The project generates additional features from the raw market data.

📊 Percentage Return
The percentage return is calculated using:
Return (%) =
(Current Close - Previous Close)
-------------------------------- × 100
        Previous Close

This helps measure price movement between consecutive observations.

📈 Moving Averages
The application calculates:
10-period moving average
30-period moving average

These values are displayed alongside the stock price to help visualize price trends.

📉 Rolling Volatility
A rolling standard deviation of percentage returns is calculated to provide a simple measure of short-term price variability.


🗄️ 4. Database Storage
Processed records are stored in a SQLite relational database.

The main table is:

stock_prices
Table Structure
Column	Description
id	Unique record identifier
symbol	Stock ticker symbol
timestamp	Market observation timestamp
open	Opening price
high	Highest price
low	Lowest price
close	Closing price
volume	Trading volume

The database uses a uniqueness constraint on the combination of:
symbol + timestamp
to prevent duplicate market observations.


🔎 5. SQL Analytics
The project contains SQL queries for performing database-level analysis.

SQL queries are available in:
sql/analysis_queries.sql

The included queries can determine:
Latest price for each stock
Average closing price
Highest recorded price
Lowest recorded price
Average trading volume
Number of records collected

Example:
SELECT
    symbol,
    ROUND(AVG(close), 2) AS average_close
FROM stock_prices
GROUP BY symbol
ORDER BY average_close DESC;


📊 6. Interactive Dashboard
The Streamlit dashboard provides an interactive interface for exploring the collected market data.

Dashboard capabilities
🔽 Select a stock
🔄 Refresh market data
💰 View latest price
📈 View price change
🔝 View highest price
📊 View average trading volume
📈 Analyze price trends
📉 Compare moving averages
📊 Analyze trading volume
🗃️ View recent records

The charts are generated using Plotly.


🛡️ 7. Error Handling
The application depends on an external market-data provider, so network or provider issues can occur.
To make the project more reliable for development and demonstration, the ingestion module includes a fallback mechanism.
If live market data cannot be retrieved, the application generates sample time-series data so that the rest of the pipeline can still be demonstrated.

This allows the project to continue working during:
Temporary network failures
Data-provider availability issues
Development/testing
Temporary API errors


📁 Project Structure
real-time-stock-market-analytics/
│
├── data/
│   └── .gitkeep
│
├── database/
│   └── .gitkeep
│
├── sql/
│   └── analysis_queries.sql
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   ├── data_ingestion.py
│   ├── data_processing.py
│   ├── analytics.py
│   └── pipeline.py
│
├── dashboard.py
├── requirements.txt
├── .gitignore
└── README.md


🔄 Data Pipeline Workflow
The complete project follows an end-to-end data workflow.

Step 1 — Extract
Stock data is requested using the yfinance library.
raw_data = fetch_stock_data("AAPL")
The returned data contains raw time-series market information.

Step 2 — Transform
The raw data is passed through the data-cleaning layer.
clean = clean_data(raw_data)
The project then generates analytical features:
featured = add_features(clean)
This produces a structured dataset suitable for storage and analysis.

Step 3 — Load
The processed data is loaded into SQLite:
load_to_database(featured)
Before insertion, timestamps are converted into a SQLite-compatible format.

Step 4 — Analyze
The project performs analytics using both Python and SQL.
Python calculates:
Returns
Moving averages
Volatility
Average volume
Maximum price
Minimum price

SQL performs database-level aggregation and historical analysis.

Step 5 — Visualize
The Streamlit application reads the processed data and generates interactive Plotly visualizations.

🛠️ Technologies Used
Technology	Purpose
🐍 Python	Core programming and pipeline development
🐼 Pandas	Data cleaning and transformation
🔢 NumPy	Numerical processing
🌐 yfinance	Market data ingestion
🗄️ SQLite	Relational data storage
🔎 SQL	Database analytics
📊 Streamlit	Interactive dashboard
📈 Plotly	Data visualization
🔧 Git	Version control
🐙 GitHub	Repository hosting
🚀 Installation
Prerequisites
Make sure you have the following installed:
Python 3.9 or higher
Git
Internet connection for live market data

Check Python:
python --version

Check Git:
git --version
1️⃣ Clone the Repository
git clone https://github.com/Fiza2008/Real-Time-Stock-Market-Analytics.git

Navigate to the project:
cd Real-Time-Stock-Market-Analytics
2️⃣ Create a Virtual Environment
Windows
python -m venv venv

Activate:
venv\Scripts\activate
Linux/macOS
python3 -m venv venv

Activate:
source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
▶️ Running the Project
Run the Data Pipeline

Execute:
python -m src.pipeline

The pipeline performs:

Market Data
     ↓
Data Cleaning
     ↓
Data Transformation
     ↓
Database Storage
     ↓
Analytics
     ↓
Results
Run the Dashboard

Start Streamlit:

streamlit run dashboard.py

The application will open in your browser.

From the dashboard, you can:

Select a stock.
Refresh market data.
View the latest price.
Analyze price movement.
Compare moving averages.
Analyze trading volume.
Inspect recent records.
🧪 Testing the Project

First run:
python -m src.pipeline

Verify that:
Market data is retrieved.
Data cleaning completes successfully.
Analytical features are generated.
SQLite records are created.
Summary statistics are displayed.

Then run:
streamlit run dashboard.py

Verify that:
The dashboard loads successfully.
Stock symbols appear.
Price metrics are displayed.
Charts render correctly.
Recent records are visible.


