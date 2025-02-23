import datetime
import requests
import pandas as pd
import matplotlib.pyplot as plt

# API Key & Series ID for Inflation (CPI)
API_KEY = "f738d9d4d13f3345328f8720c487fc98"
SERIES_ID = "CPIAUCSL"  # Consumer Price Index (Inflation)

# Define Date Range (Last 36 Months for Visualization)
end_date = datetime.datetime.today().strftime('%Y-%m-%d')
start_date_36m = (datetime.datetime.today() - datetime.timedelta(days=36*30)).strftime('%Y-%m-%d')
start_date_6m = (datetime.datetime.today() - datetime.timedelta(days=6*30)).strftime('%Y-%m-%d')

# Fetch Inflation Data from FRED API
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

# Convert to DataFrame
if "observations" in data:
    df = pd.DataFrame(data["observations"])
    df["date"] = pd.to_datetime(df["date"])
    df["inflation"] = pd.to_numeric(df["value"], errors="coerce")

    # Sort by date
    df.sort_values("date", inplace=True)

    # Extract only last 6 months for forecasting decision
    df_6m = df[df["date"] >= start_date_6m]

    # Get first & last inflation values in 6-month period
    first_value_6m = df_6m.iloc[0]["inflation"]
    last_value_6m = df_6m.iloc[-1]["inflation"]

    # Compute Net Inflation Change Over 6 Months
    net_inflation_change = last_value_6m - first_value_6m

    # Determine Insurance Impact
    if net_inflation_change > 0:
        result = "📈 Inflation has increased → Insurance prices may rise."
    else:
        result = "📉 Inflation has decreased → Insurance prices may stabilize or drop."

    # Print Results
    print(f"First Inflation Value (6 months ago): {first_value_6m}")
    print(f"Last Inflation Value (Today): {last_value_6m}")
    print(f"Net Inflation Change: {net_inflation_change}")
    print(f"📢 {result}")

    # Plot Inflation Trend Over 36 Months
    plt.figure(figsize=(12, 6))
    plt.plot(df["date"], df["inflation"], marker="o", linestyle="-", color="b", label="Inflation Rate (Last 36 Months)")
    
    # Highlight Last 6 Months Used for Forecasting
    plt.plot(df_6m["date"], df_6m["inflation"], marker="o", linestyle="-", color="red", label="Last 6 Months (Used for Forecast)")

    # Mark First & Last Inflation Points for 6-Month Analysis
    plt.axhline(y=first_value_6m, color="gray", linestyle="--", label="Inflation 6 Months Ago")
    plt.axhline(y=last_value_6m, color="darkred", linestyle="--", label="Current Inflation")

    # Labels & Title
    plt.xlabel("Date")
    plt.ylabel("Inflation (CPI)")
    plt.title("Inflation Trend Over 36 Months (Forecasting Based on Last 6 Months)")
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)

    # Show Plot
    plt.show()

else:
    print("❌ API Error:", data)

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