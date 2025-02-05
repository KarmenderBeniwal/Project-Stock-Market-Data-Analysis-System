# Project-Stock-Market-Data-Analysis-System

# Stock Market Data Analysis System

A Python-based system for fetching, storing, and analyzing stock market data from Yahoo Finance using yfinance, FastAPI, and SQLAlchemy.

# 📁 Project Structure
stock_analysis/
├── src/
│   ├── __init__.py       # Marks src as a module
│   ├── database.py       # SQLite database setup
│   ├── fetcher.py        # Fetches stock data from Yahoo Finance
│   ├── analysis/
│   │   ├── __init__.py   # Marks analysis as a module
│   │   └── calculator.py # Computes returns, high/low, statistics
│   └── api/
│       ├── __init__.py   # Marks api as a module
│       └── main.py       # FastAPI endpoints
├── data/                # Auto-created directory for SQLite database
├── requirements.txt      # Python dependencies
├── test.py               # Runs API & fetches stock data
└── README.md             # Documentation


## Features

- 📈 Fetch historical daily data for 5 major Indian stocks
- 💾 Store data in SQLite database
- 📊 Perform financial analysis (returns, high/low prices, statistics)
- 🚀 REST API endpoints for data access
- 🧪 Unit testing support

## Supported Stocks
- RELIANCE
- TCS
- ACC
- HDFCBANK
- COALINDIA

# Install Dependencies
pip install -r requirements.txt


🚀 Setup Instructions

1️⃣ Install Dependencies

Ensure you have Python 3.8+, then run:

pip install -r requirements.txt

2️⃣ Initialize Database

python src/database.py

✅ Expected Output: "Database and tables created successfully!"

3️⃣ Fetch Stock Data

python src/fetcher.py

✅ Expected Output: "✅ RELIANCE data stored successfully!"


# API Endpoints
Endpoint	Method	Description
/stocks/prices/{symbol}	GET	Get latest price for a stock
/stocks/history/{symbol}	GET	Get historical data (specify start_date and end_date)
/stocks/analysis/returns/{symbol}	GET	Get daily returns analysis
/stocks/analysis/high_lows/{symbol}	GET	Get daily high/low prices
/stocks/analysis/stats/{symbol}	GET	Get statistical analysis
Access API Documentation:
http://localhost:8000/docs

Key Features
✅ Automatic data fetching and storage

✅ SQLite database integration

✅ Error handling for API calls

✅ Parameterized SQL queries

✅ Interactive API documentation

# Future Improvements
Add authentication for API endpoints

Implement bulk data insert operations

Add more technical indicators (RSI, MACD)

Implement caching mechanism

Add frontend dashboard

# Dependencies-
* Python 3.8+
* yfinance
* FastAPI
* SQLAlchemy
* pandas
* uvicorn

# Testing
- Run unit tests:
fetcher.py
test.py


  📡 Deployment (Optional)

Deploy using Docker:
docker build -t stock-api 
docker run -p 8000:8000 stock-api

# Evaluation Criteria

✔ Code organization ✔ Error handling ✔ Documentation ✔ Testing approach
