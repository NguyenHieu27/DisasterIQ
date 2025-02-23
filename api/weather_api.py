import requests
import pandas as pd

def get_weather_data():
    LAT = 40.7128
    LON = -74.0060
    START_DATE = "2024-01-01"
    END_DATE = "2025-02-20"
    URL = f"https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": LAT,
        "longitude": LON,
        "start_date": START_DATE,
        "end_date": END_DATE,
        "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_sum", "windspeed_10m_max"],
        "timezone": "America/New_York"
    }
    response = requests.get(URL, params=params)
    data = response.json()
    if "daily" in data:
        df_weather = pd.DataFrame(data["daily"])
        df_weather["date"] = pd.to_datetime(df_weather["time"])
        df_weather.drop(columns=["time"], inplace=True)
        return df_weather.to_dict(orient='records')
    else:
        return {"error": "API Error", "details": data}

# Define location (Latitude & Longitude for New York City)
LAT = 40.7128
LON = -74.0060

# Define time range for historical data
START_DATE = "2024-01-01"  # Change to your desired start date
END_DATE = "2025-02-20"    # Change to your desired end date

# Open-Meteo API Endpoint
URL = f"https://archive-api.open-meteo.com/v1/archive"

# API Request Parameters
params = {
    "latitude": LAT,
    "longitude": LON,
    "start_date": START_DATE,
    "end_date": END_DATE,
    "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_sum", "windspeed_10m_max"],
    "timezone": "America/New_York"
}

# Fetch Data
response = requests.get(URL, params=params)
data = response.json()

# Check response
if "daily" in data:
    df_weather = pd.DataFrame(data["daily"])
    df_weather["date"] = pd.to_datetime(df_weather["time"])  # Convert time to datetime
    df_weather.drop(columns=["time"], inplace=True)  # Drop unnecessary time column

    # Display first few rows
    print(df_weather.head())

    # Save to CSV (optional)
    df_weather.to_csv("data/historical_weather.csv", index=False)
else:
    print("❌ API Error:", data)