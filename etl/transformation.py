import json
import pandas as pd
import os

# Define file paths
RAW_DATA_FILE = "data/raw/london_weather_2002-01-01_to_2024-12-31.json"
TRANSFORMED_DATA_FILE = "data/transformed/london_weather_cleaned.csv"

# Ensure processed data folder exists
os.makedirs("data/transformed", exist_ok=True)

# Load raw JSON data
with open(RAW_DATA_FILE, "r") as file:
    raw_data = json.load(file)

# Extract weather data
weather_records = raw_data.get("data", [])

# Convert to pandas DataFrame
df = pd.DataFrame(weather_records)

# Convert 'date' to datetime
df["date"] = pd.to_datetime(df["date"])

# Create 'month' and 'year' columns
df["month"] = df["date"].dt.month
df["year"] = df["date"].dt.year

# Convert 'wspd' to numeric
df["wspd"] = pd.to_numeric(df["wspd"], errors="coerce")

# Interpolate linearly
df["wspd"] = df["wspd"].interpolate(method="linear")

# Fill starting NaNs using backward fill
df["wspd"].fillna(method="bfill", inplace=True)


# Save the cleaned data
df.to_csv(TRANSFORMED_DATA_FILE, index=False)

print(f" Data successfully transformed and saved to {TRANSFORMED_DATA_FILE}")
