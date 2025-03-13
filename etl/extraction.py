import requests
import os
import json
from datetime import datetime
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
API_KEY = os.getenv("METEOSTAT_API_KEY")
    # check if API is loaded correctly
if not API_KEY:
    raise ValueError(" ERROR: API Key not found.")

# Define location and date range 
LAT = "51.5074"  
LON = "-0.1278"
ALT = "14"  
START_DATE = "2002-01-01"
END_DATE = "2024-12-31"

# Meteostat base url
url = "https://meteostat.p.rapidapi.com/point/monthly"

# Request headers
headers = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": "meteostat.p.rapidapi.com"
}

# Request parameters
querystring = {
    "lat": LAT,
    "lon": LON,
    "alt": ALT,
    "start": START_DATE,
    "end": END_DATE
}

# Make the API call
response = requests.get(url, headers=headers, params=querystring)

# Process API response
if response.status_code == 200:
    data = response.json()

    # Ensure raw data folder exists
    os.makedirs("data/raw", exist_ok=True)

    # Save data to a JSON file
    file_name = f"data/raw/london_weather_{START_DATE}_to_{END_DATE}.json"
    with open(file_name, "w") as json_file:
        json.dump(data, json_file, indent=4)

    print(f"Data  saved to {file_name}")

else:
    print(f"ERROR: {response.status_code} - {response.text}")
