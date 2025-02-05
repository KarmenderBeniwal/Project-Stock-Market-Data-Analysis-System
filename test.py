# run.py (place this in your PROJECT ROOT folder)
import sys
import os

# Add project root to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)

# Now import modules
from src.fetcher import fetch_all_stocks
from src.api.main import app
import uvicorn

if __name__ == "__main__":
    # 1. Fetch initial data
    print("⏳ Fetching stock data...")
    fetch_all_stocks()

    # 2. Start API server
    print("\n🚀 Starting API server at http://localhost:8000")
    print("📚 API Docs: http://localhost:8000/docs\n")
    uvicorn.run("src.api.main:app", host="0.0.0.0", port=8000, reload=True)
