# Add at TOP
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.append(project_root)

# Then imports
from src.database import StockData, get_db
import yfinance as yf
from datetime import datetime, timedelta

STOCKS = {
    "RELIANCE": "RELIANCE.NS",
    "TCS": "TCS.NS",
    "ACC": "ACC.NS",
    "HDFCBANK": "HDFCBANK.NS",
    "COALINDIA": "COALINDIA.NS",
}


def fetch_stock_data(symbol, yf_symbol, days=30):
    try:
        print(f"\n=== Fetching {symbol} ===")
        end_date = datetime.today()
        start_date = end_date - timedelta(days=days)
        print(f"Date Range: {start_date} to {end_date}")

        # Fetch data
        ticker = yf.Ticker(yf_symbol)
        hist = ticker.history(start=start_date, end=end_date)

        # Debug: Show data
        print(f"Fetched {len(hist)} records")
        if not hist.empty:
            print(hist[["Open", "Close"]].tail(3))  # Last 3 rows

        # Store in database
        session = get_db()
        for date, row in hist.iterrows():
            existing = (
                session.query(StockData)
                .filter_by(symbol=symbol, date=date.date())
                .first()
            )

            if not existing:
                session.add(
                    StockData(
                        symbol=symbol,
                        date=date.date(),
                        open=row["Open"],
                        high=row["High"],
                        low=row["Low"],
                        close=row["Close"],
                        volume=row["Volume"],
                    )
                )
        session.commit()
        print(f"✅ {symbol} data stored successfully!")

        # Return latest price
        return ticker.info.get("regularMarketPreviousClose", None)

    except Exception as e:
        print(f"❌ Error fetching {symbol}: {str(e)}")
        return None
    finally:
        session.close()


def fetch_all_stocks():
    results = {}
    for symbol, yf_code in STOCKS.items():
        results[symbol] = fetch_stock_data(symbol, yf_code)
    return results


# Verification Test
if __name__ == "__main__":
    fetch_all_stocks()
