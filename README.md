# 📈 Real-Time Stock Market Analytics

<p align="center">
  <strong>A Python-based market data pipeline and interactive analytics dashboard</strong>
</p>

<p align="center">
  Python • Pandas • SQL • SQLite • Streamlit • Plotly • yfinance
</p>

---

## 📌 Project Overview

**Real-Time Stock Market Analytics** is a data-driven application that collects stock market data, cleans and transforms the incoming records, stores them in a relational SQLite database, performs analytical calculations using Python and SQL, and presents the results through an interactive Streamlit dashboard.

The project was designed to demonstrate practical **Data Engineering and Data Analytics concepts**, including:

- Data ingestion
- Data validation
- Data cleaning
- Data transformation
- Time-series processing
- Relational database storage
- SQL analytics
- Feature engineering
- Data visualization
- Error handling
- Dashboard development

---

## 🖥️ Dashboard Preview

> **📷 INSERT YOUR PROJECT SCREENSHOT HERE**
>
> Replace this section with your own screenshot after uploading the image to GitHub.
>
> Example:
>
> `![Real-Time Stock Market Analytics Dashboard](images/dashboard.png)`

**Suggested GitHub structure for the screenshot:**

```text
real-time-stock-market-analytics/
│
├── images/
│   └── dashboard.png
│
└── README.md
```

After uploading the screenshot to the `images` folder, replace the placeholder above with:

```markdown
![Real-Time Stock Market Analytics Dashboard](images/dashboard.png)
```

---

## 🎯 Objectives

The main objectives of this project are to:

1. Collect stock market data programmatically.
2. Build a reusable data ingestion process.
3. Clean and validate raw market data.
4. Transform time-series data into useful analytical features.
5. Store structured data in a relational database.
6. Execute SQL queries for business-style analysis.
7. Calculate stock performance indicators.
8. Build an interactive dashboard for data exploration.
9. Handle external API/data-provider failures gracefully.

---

# 🏗️ System Architecture

```text
                   ┌─────────────────────┐
                   │   Market Data Source │
                   │     Yahoo Finance   │
                   └──────────┬──────────┘
                              │
                              ▼
                   ┌─────────────────────┐
                   │   Data Ingestion     │
                   │      Python         │
                   └──────────┬──────────┘
                              │
                              ▼
                   ┌─────────────────────┐
                   │ Data Cleaning &      │
                   │ Transformation       │
                   │       Pandas         │
                   └──────────┬──────────┘
                              │
                              ▼
                   ┌─────────────────────┐
                   │   SQLite Database   │
                   │   Structured Data    │
                   └──────────┬──────────┘
                              │
                 ┌────────────┴────────────┐
                 ▼                         ▼
       ┌─────────────────┐       ┌──────────────────┐
       │   SQL Analytics │       │ Python Analytics │
       └────────┬────────┘       └────────┬─────────┘
                │                         │
                └────────────┬────────────┘
                             ▼
                  ┌──────────────────────┐
                  │ Streamlit Dashboard  │
                  │      + Plotly        │
                  └──────────────────────┘
```

---

# ✨ Key Features

### 1. 📥 Market Data Ingestion

The application retrieves stock market information using `yfinance`.

Supported example symbols include:

```text
AAPL
MSFT
GOOGL
AMZN
NVDA
TSLA
```

The ingestion layer collects fields such as:

- Open price
- High price
- Low price
- Closing price
- Trading volume
- Timestamp
- Stock symbol

---

### 2. 🧹 Data Cleaning

Before storing the data, the application validates and cleans the incoming records.

The cleaning process:

- Converts timestamps into a consistent datetime format.
- Converts numeric columns into numeric data types.
- Removes invalid or missing critical records.
- Removes duplicate timestamp records.
- Sorts records chronologically.
- Validates that price values are positive.
- Handles missing volume values.

This creates a cleaner dataset for downstream analytics.

---

### 3. ⚙️ Feature Engineering

The processed dataset contains additional analytical features.

#### Daily Return

Measures percentage movement between consecutive observations.

```text
Daily Return (%) =
(Current Close - Previous Close)
-------------------------------- × 100
        Previous Close
```

#### Moving Average

The project calculates:

- 10-period moving average
- 30-period moving average

Moving averages help visualize the underlying price trend.

#### Rolling Volatility

A rolling standard deviation of returns is calculated to provide a simple measure of short-term price variability.

---

### 4. 🗄️ SQLite Database

Processed market records are stored in a SQLite relational database.

The primary table is:

```text
stock_prices
```

with fields including:

```text
id
symbol
timestamp
open
high
low
close
volume
```

The database provides persistent structured storage for the collected market records.

---

### 5. 🔎 SQL Analytics

The project includes SQL queries for:

- Latest stock price
- Average closing price
- Highest and lowest prices
- Average trading volume
- Number of collected records

SQL queries are available in:

```text
sql/analysis_queries.sql
```

---

### 6. 📊 Interactive Dashboard

The Streamlit dashboard provides:

- Stock selection
- Latest price
- Price change
- Highest price
- Average trading volume
- Price trend chart
- Moving-average visualization
- Trading-volume chart
- Recent market records
- Manual data refresh

---

### 7. 🛡️ Error Handling

External market-data services can sometimes be unavailable.

To keep the project demonstrable, the ingestion module includes a fallback mechanism that generates realistic sample time-series data when live data cannot be retrieved.

This allows the application to continue running during:

- Temporary API failures
- Network problems
- Provider availability issues
- Development/testing without live data

---

# 📁 Project Structure

```text
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
```

---

# 🔄 Data Pipeline

The complete pipeline follows these stages:

## Step 1 — Extract

The application requests stock market data using `yfinance`.

```python
raw_data = fetch_stock_data("AAPL")
```

The result contains raw time-series market information.

---

## Step 2 — Transform

The raw dataset is passed through the cleaning layer.

```python
clean_data = clean_data(raw_data)
```

The application then creates analytical features:

```python
featured_data = add_features(clean_data)
```

This produces a structured dataset ready for storage and analysis.

---

## Step 3 — Load

The transformed records are inserted into SQLite.

```python
load_to_database(featured_data)
```

The timestamp is converted into a SQLite-compatible format before insertion.

---

## Step 4 — Analyze

Python analytics calculate summary statistics such as:

- Latest price
- Period return
- Average volume
- Maximum price
- Minimum price

SQL queries provide additional database-level analysis.

---

## Step 5 — Visualize

The Streamlit application reads the stored data and creates interactive visualizations using Plotly.

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Core programming and pipeline logic |
| **Pandas** | Data cleaning and transformation |
| **NumPy** | Numerical calculations and sample data generation |
| **yfinance** | Market data ingestion |
| **SQLite** | Relational data storage |
| **SQL** | Database analytics |
| **Streamlit** | Interactive dashboard |
| **Plotly** | Interactive charts |
| **Git/GitHub** | Version control and project hosting |

---

# 🚀 Installation & Setup

## Prerequisites

Make sure you have:

- Python 3.9+
- Git
- Internet connection for live market data

Check Python:

```bash
python --version
```

Check Git:

```bash
git --version
```

---

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/real-time-stock-market-analytics.git
```

Move into the project:

```bash
cd real-time-stock-market-analytics
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

The main dependencies are:

```text
pandas
numpy
yfinance
streamlit
plotly
```

---

# ▶️ Running the Project

## Option 1 — Run the Data Pipeline

Execute:

```bash
python -m src.pipeline
```

The pipeline will:

```text
Fetch data
    ↓
Clean data
    ↓
Create analytical features
    ↓
Store records in SQLite
    ↓
Generate analytics
    ↓
Print results
```

---

## Option 2 — Run the Dashboard

Start Streamlit:

```bash
streamlit run dashboard.py
```

The terminal will provide a local URL.

Open that URL in your browser.

You can then:

1. Select a stock.
2. Refresh market data.
3. View the latest price.
4. Inspect price movement.
5. Compare moving averages.
6. Analyze trading volume.
7. Inspect recent records.

---

# 📊 Example Analysis

The project can answer questions such as:

### What is the latest price?

The dashboard displays the latest stored market price for the selected symbol.

### What was the highest observed price?

The application calculates the maximum value from the available high-price records.

### What is the average trading volume?

The dashboard calculates the mean trading volume for the selected dataset.

### How is the stock trending?

The price chart can be compared with the 10-period and 30-period moving averages.

### Which stock has the highest average volume?

The Python analytics module can compare average volume across all loaded symbols.

---

# 🧪 Testing the Pipeline

A basic test workflow is:

```bash
python -m src.pipeline
```

Then check that:

- Data is fetched successfully.
- Invalid rows are removed.
- Features are generated.
- SQLite records are created.
- Summary statistics are printed.

After that:

```bash
streamlit run dashboard.py
```

Verify that:

- The dashboard loads.
- Stock symbols appear.
- Price metrics are displayed.
- Charts render correctly.
- Recent records are visible.

---

⭐ If you found this project useful, consider giving the repository a star!
