# Import necessary modules
import datetime
import requests
import pandas as pd

# Existing imports
from fastapi import FastAPI
from .macro_api import get_inflation_data
from .weather_api import get_weather_data

app = FastAPI()

@app.get("/api/inflation")
async def inflation_data():
    return get_inflation_data()

@app.get("/api/weather")
async def weather_data():
    return get_weather_data()

# Fetch inflation data from FRED API
def get_inflation_data():
    API_KEY = "f738d9d4d13f3345328f8720c487fc98"
    SERIES_ID = "CPIAUCSL"
    end_date = datetime.datetime.today().strftime('%Y-%m-%d')
    start_date_36m = (datetime.datetime.today() - datetime.timedelta(days=36*30)).strftime('%Y-%m-%d')
    BASE_URL = "https://api.stlouisfed.org/fred/series/observations"
    params = {
        "series_id": SERIES_ID,
        "api_key": API_KEY,
        "file_type": "json",
        "observation_start": start_date_36m,
        "observation_end": end_date,
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    if "observations" in data:
        df = pd.DataFrame(data["observations"])
        df["date"] = pd.to_datetime(df["date"])
        df["inflation"] = pd.to_numeric(df["value"], errors="coerce")
        return df.to_dict(orient='records')
    else:
        return {"error": "API Error", "details": data}

# Fetch weather data from Open-Meteo API
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
