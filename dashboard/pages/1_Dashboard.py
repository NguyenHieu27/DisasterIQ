import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import requests

st.set_page_config(
    page_title="Dashboard",
    page_icon=":bar_chart:",
    layout="wide"
)

st.title("Dashboard")

# Fetch data from FastAPI backend
def fetch_data(endpoint):
    API_URL = "http://localhost:8501"
    try:
        response = requests.get(f"{API_URL}/{endpoint}")
        return response.json()
    except Exception as e:
        return None

col1, col2, col3, col4 = st.column(4)
with col1:
    st.metric(label="Active Risks", value="127", delta="5")
with col2:
    st.metric(label="Anomalies Detected", value="3", delta="-2")
with col3:
    st.metric(label="Risk Score", value="82%", delta="3%")
with col4:
    st.metric(label="Inventory Status", value="Optimal", delta="↑")

# Real-time monitoring section
st.subheader("Real-Time Monitoring")

chart_data = pd.DataFrame({
    'timestamp': pd.date_range(start = '2025-01-01', periods = 100, freq = "H"),
    'risk_score': np.random.randint(50, 90, size = 100) # Will be replaced with actual risk score
})

fig = px.line(chart_data, x='timestamp', y='risk_score')
st.plotly_chart(fig, use_container_width=True)
