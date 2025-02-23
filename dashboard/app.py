import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import requests
import numpy as np

# Configure the page
st.set_page_config(
    page_title="DisasterIQ",
    page_icon="🔍",
    layout="wide"
)

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select a Page",
    ["Dashboard", "Risk Analysis", "Anomaly Detection", "Inventory Management"]
)

# Main title
st.title("DisasterIQ")

# Add subtitle
st.markdown("### Real-Time Anomaly Detection & Risk Optimization")

# Function to fetch data from FastAPI backend
def fetch_data(endpoint):
    API_URL = "http://localhost:8000"  # Replace with your FastAPI backend URL
    try:
        response = requests.get(f"{API_URL}/{endpoint}")
        return response.json()
    except:
        return None

if page == "Dashboard":
    # Overview metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Active Risks", value="127", delta="5")
    with col2:
        st.metric(label="Anomalies Detected", value="3", delta="-2")
    with col3:
        st.metric(label="Risk Score", value="82%", delta="3%")
    with col4:
        st.metric(label="Inventory Status", value="Optimal", delta="↑")

    # Real-time monitoring section
    st.subheader("Real-Time Risk Monitoring")
    
    # Example time series plot
    chart_data = pd.DataFrame({
        'timestamp': pd.date_range(start='2024-01-01', periods=100, freq='H'),
        'risk_score': np.random.randn(100).cumsum()
    })
    fig = px.line(chart_data, x='timestamp', y='risk_score')
    st.plotly_chart(fig, use_container_width=True)

elif page == "Risk Analysis":
    st.header("Risk Analysis Dashboard")
    
    # Risk factors selection
    risk_factors = st.multiselect(
        "Select Risk Factors",
        ["Natural Disasters", "Economic Indicators", "Market Volatility", "Geographic Location"]
    )
    
    # Risk matrix
    st.subheader("Risk Assessment Matrix")
    # Add your risk matrix visualization here

elif page == "Anomaly Detection":
    st.header("Anomaly Detection System")
    
    # Time range selector
    time_range = st.select_slider(
        "Select Time Range",
        options=["Last Hour", "Last Day", "Last Week", "Last Month"]
    )
    
    # Anomaly detection parameters
    st.sidebar.subheader("Detection Parameters")
    sensitivity = st.sidebar.slider("Detection Sensitivity", 0.0, 1.0, 0.5)
    
    # Placeholder for anomaly visualization
    st.subheader("Detected Anomalies")
    # Add your anomaly visualization here

elif page == "Inventory Management":
    st.header("Dynamic Inventory Management")
    
    # Inventory metrics
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Current Stock Levels")
        # Add inventory level visualization
    
    with col2:
        st.subheader("Predicted Demand")
        # Add demand prediction visualization
    
    # Optimization controls
    st.subheader("Optimization Settings")
    reorder_point = st.slider("Reorder Point", 0, 1000, 500)
    safety_stock = st.slider("Safety Stock Level", 0, 500, 200)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>Real-Time Anomaly Detection & Risk Optimization System</p>
        <p>Powered by Multi-Agent AI</p>
    </div>
    """,
    unsafe_allow_html=True
)