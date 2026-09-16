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

# 📌 Important Design Decisions

### Why SQLite?

SQLite was selected because it is:

- Lightweight
- Serverless
- Easy to configure
- SQL-compatible
- Suitable for a portfolio project
- Useful for demonstrating relational database concepts

For a production-scale system, the database could be replaced with PostgreSQL, MySQL, or a cloud data warehouse.

---

### Why Pandas?

Pandas provides convenient tools for:

- Data cleaning
- Data transformation
- Missing-value handling
- Time-series operations
- Feature engineering
- Aggregation

---

### Why Streamlit?

Streamlit makes it possible to turn the Python analytics pipeline into an interactive web dashboard without building a separate frontend application.

---

# 🔮 Future Improvements

Possible extensions include:

- Replace SQLite with PostgreSQL.
- Add Apache Kafka for streaming ingestion.
- Add Apache Spark/PySpark for large-scale processing.
- Deploy the pipeline to AWS.
- Store raw files in Amazon S3.
- Add scheduled ingestion jobs.
- Add automated data-quality checks.
- Add authentication to the dashboard.
- Add more technical indicators.
- Add portfolio-level analytics.
- Add automated testing with `pytest`.
- Containerize the application using Docker.
- Add CI/CD using GitHub Actions.

---

# 💼 Data Engineering Concepts Demonstrated

This project demonstrates a complete small-scale data workflow:

```text
                    DATA ENGINEERING WORKFLOW

       ┌──────────────┐
       │ Data Source  │
       └──────┬───────┘
              ↓
       ┌──────────────┐
       │  Ingestion   │
       └──────┬───────┘
              ↓
       ┌──────────────┐
       │  Validation  │
       └──────┬───────┘
              ↓
       ┌──────────────┐
       │Transformation│
       └──────┬───────┘
              ↓
       ┌──────────────┐
       │   Storage    │
       └──────┬───────┘
              ↓
       ┌──────────────┐
       │   Analytics  │
       └──────┬───────┘
              ↓
       ┌──────────────┐
       │Visualization │
       └──────────────┘
```

The project therefore connects several concepts that are commonly encountered in data engineering:

**Ingestion → Processing → Storage → SQL → Analytics → Visualization**

---

# 📄 Resume Entry

You can use the following version on your resume:

### Real-Time Stock Market Analytics
**Python | Pandas | SQL | SQLite | Streamlit | yfinance**

- Built a Python-based market data pipeline to ingest, clean, transform, and store time-series stock data in SQLite, implementing validation and duplicate handling for reliable processing.
- Developed analytical features including percentage returns, moving averages, rolling volatility, and volume statistics, with SQL queries for historical market analysis.
- Created an interactive Streamlit dashboard using Plotly to visualize stock price trends, moving averages, trading volume, and key performance metrics.

---

# 🎤 Interview Explanation

If the interviewer asks:

> **"Explain your Real-Time Stock Market Analytics project."**

You can explain it like this:

> "I built a Python-based stock market analytics pipeline. The system first ingests stock data using yfinance. I then clean and validate the incoming time-series data using Pandas, remove duplicates and invalid records, and create features such as percentage returns, moving averages, and rolling volatility. The processed data is stored in a SQLite relational database, where I use SQL queries for analytical operations. Finally, I built a Streamlit dashboard with Plotly to visualize the stock price, moving averages, trading volume, and other metrics. I also added error handling with sample-data fallback so that the application can still be demonstrated if the external market-data source is temporarily unavailable."

---

# ❓ Questions You Should Be Ready For

### Python

1. Why did you use Pandas?
2. How did you handle missing values?
3. How did you remove duplicates?
4. Why did you convert the timestamp before inserting it into SQLite?
5. How does your error-handling mechanism work?

### SQL

1. Why did you use SQLite?
2. How would you find the latest record for every stock?
3. How would you calculate average volume?
4. What is the difference between `WHERE` and `HAVING`?
5. What are primary keys and unique constraints?

### Data Engineering

1. Explain your data pipeline.
2. What is ETL?
3. What is data validation?
4. How would you scale this pipeline?
5. How would you process millions of records?
6. How would you handle an API failure?
7. How would you schedule the pipeline?
8. How would you move this architecture to AWS?
9. How would you implement real-time streaming?
10. How would you monitor data quality?

### Dashboard

1. Why did you use Streamlit?
2. Why did you use Plotly?
3. How does the dashboard get its data?
4. How would you deploy the dashboard?

---

# 🌟 Learning Outcome

After completing this project, you should be able to explain and demonstrate:

```text
Python
  ↓
Pandas
  ↓
Data Cleaning
  ↓
Data Transformation
  ↓
SQL / SQLite
  ↓
Analytics
  ↓
Visualization
```

This makes the project useful as a practical demonstration of **Python, SQL, data processing, database concepts, and introductory data engineering**.

---

## 👩‍💻 Author

**Fiza Naz Shaik**

Computer Science & Engineering — AI/ML  
VIT-AP University

---

⭐ If you found this project useful, consider giving the repository a star!
