# Add at TOP
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_root)

# Then imports
from fastapi import FastAPI, HTTPException
from datetime import date
from src.fetcher import fetch_stock_data as fetch_and_store_data
from src.analysis.calculator import (
    calculate_daily_returns,
    get_high_low,
    calculate_statistics,
)

app = FastAPI()
SYMBOLS = ["RELIANCE", "TCS", "ACC", "HDFCBANK", "COALINDIA"]

# ... rest of your API endpoints ...


@app.get("/stocks/prices/{symbol}")
async def get_latest_price(symbol: str):
    if symbol not in SYMBOLS:
        raise HTTPException(status_code=404, detail="Symbol not supported")
    fetch_and_store_data(symbol)
    return {"message": f"Latest data fetched for {symbol}. Check database."}


@app.get("/stocks/history/{symbol}")
async def get_history(symbol: str, start_date: date, end_date: date):
    if symbol not in SYMBOLS:
        raise HTTPException(status_code=404, detail="Symbol not supported")
    fetch_and_store_data(symbol, start_date, end_date)
    return {
        "message": f"Historical data fetched for {symbol} from {start_date} to {end_date}"
    }


@app.get("/stocks/analysis/returns/{symbol}")
async def get_returns(symbol: str):
    return calculate_daily_returns(symbol)


@app.get("/stocks/analysis/high_lows/{symbol}")
async def get_high_low_prices(symbol: str, target_date: date):
    return get_high_low(symbol, target_date)


@app.get("/stocks/analysis/stats/{symbol}")
async def get_stats(symbol: str):
    return calculate_statistics(symbol)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.api.main:app", host="0.0.0.0", port=8000, reload=True)
