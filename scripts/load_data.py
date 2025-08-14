import pandas as pd
import os

# Define data directory and tickers
data_dir = "../data"
tickers = ["AAPL", "ARKK"]

# Dictionary to hold the DataFrames
datasets = {}

# Read and preprocess
for ticker in tickers:
    file_path = os.path.join(data_dir, f"{ticker}.csv")
    
    # Read CSV
    df = pd.read_csv(file_path, parse_dates=["Date"])
    
    # Preprocessing
    df.dropna(inplace=True)                          # Remove missing rows
    df.sort_values("Date", inplace=True)             # Sort by date
    df.reset_index(drop=True, inplace=True)          # Clean index
    
    # Store in dictionary
    datasets[ticker] = df

    print(f"Loaded {ticker}: {df.shape[0]} rows")

# Access with datasets["AAPL"] or datasets["ARKK"]

datasets["ARKK"]