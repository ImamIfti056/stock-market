# 1. Strip whitespace from column names
df.columns = df.columns.str.strip()

# 2. Convert Date column to datetime
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# 3. Convert all other columns to numeric (safely)
for col in df.columns:
    if col != "Date":
        df[col] = pd.to_numeric(df[col], errors="coerce")

# 4. Drop rows where Date or Close is missing
df.dropna(subset=["Date", "Close"], inplace=True)

# 5. Sort and reset index
df.sort_values("Date", inplace=True)
df.reset_index(drop=True, inplace=True)
df