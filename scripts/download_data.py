import yfinance as yf
import pandas as pd
import os

# Set up
stocks = {
    "AAPL": "Apple Inc.",
    "NVDA": "NVIDIA Corporation",
    "TSLA": "Tesla, Inc.",
}
start_date = "2015-01-01"
end_date = "2024-12-31"
output_dir = os.path.join("..", "data")

os.makedirs(output_dir, exist_ok=True)

# Download, clean, and save
for ticker, name in stocks.items():
    print(f"Downloading {ticker} - {name}")
    data = yf.download(ticker, start=start_date, end=end_date)
    data = data.reset_index() # makes the date column as a normal column
    data.dropna(inplace=True)
    data.sort_values("Date", inplace=True)

    filename = f"{ticker}.csv"
    data.to_csv(os.path.join(output_dir, filename), index=False)

    print(f"Saved {ticker} data to {output_dir}/{filename}")

print("All datasets ready.")