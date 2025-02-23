import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Anomaly Detection - DisasterIQ",
    page_icon="🔍",
    layout="wide"
)

st.title("Anomaly Detection")

# Controls
col1, col2, col3 = st.columns(3)
with col1:
    time_range = st.selectbox(
        "Time Range",
        ["Last 24 Hours", "Last Week", "Last Month", "Last Quarter"]
    )
with col2:
    detection_sensitivity = st.slider(
        "Detection Sensitivity",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        help="Adjust the sensitivity of anomaly detection"
    )
with col3:
    update_frequency = st.selectbox(
        "Update Frequency",
        ["Real-time", "5 minutes", "15 minutes", "1 hour"]
    )

# Generate sample data with anomalies
np.random.seed(42)
dates = pd.date_range(start='2024-01-01', periods=1000, freq='5T')
normal_data = np.random.normal(100, 10, 1000)
anomalies = np.random.randint(0, 1000, 20)
normal_data[anomalies] += np.random.normal(50, 10, 20)

df_anomalies = pd.DataFrame({
    'timestamp': dates,
    'value': normal_data,
    'is_anomaly': [i in anomalies for i in range(1000)]
})

# Main anomaly plot
st.markdown("### Real-time Anomaly Detection")
fig = go.Figure()

# Add normal data
fig.add_trace(go.Scatter(
    x=df_anomalies[~df_anomalies['is_anomaly']]['timestamp'],
    y=df_anomalies[~df_anomalies['is_anomaly']]['value'],
    mode='lines',
    name='Normal'
))

# Add anomalies
fig.add_trace(go.Scatter(
    x=df_anomalies[df_anomalies['is_anomaly']]['timestamp'],
    y=df_anomalies[df_anomalies['is_anomaly']]['value'],
    mode='markers',
    name='Anomaly',
    marker=dict(color='red', size=10)
))

st.plotly_chart(fig, use_container_width=True)

# Anomaly Statistics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Anomalies", "20", "5")
with col2:
    st.metric("Average Detection Time", "45 seconds", "-10s")
with col3:
    st.metric("False Positive Rate", "2.3%", "-0.5%")

# Recent Anomalies Table
st.markdown("### Recent Anomalies")
recent_anomalies = df_anomalies[df_anomalies['is_anomaly']].tail(5)
st.dataframe(
    recent_anomalies[['timestamp', 'value']].rename(
        columns={'timestamp': 'Time', 'value': 'Anomaly Value'}
    )
)

# Anomaly Distribution
st.markdown("### Anomaly Distribution")
col1, col2 = st.columns(2)

with col1:
    # Distribution by time of day
    hours = df_anomalies[df_anomalies['is_anomaly']]['timestamp'].dt.hour
    fig_hours = px.histogram(
        x=hours,
        nbins=24,
        title="Anomalies by Hour of Day"
    )
    st.plotly_chart(fig_hours, use_container_width=True)

with col2:
    # Distribution by value range
    fig_dist = px.histogram(
        df_anomalies[df_anomalies['is_anomaly']],
        x='value',
        title="Anomaly Value Distribution"
    )
    st.plotly_chart(fig_dist, use_container_width=True)