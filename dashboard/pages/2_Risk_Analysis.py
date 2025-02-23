import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Risk Analysis - DisasterIQ",
    page_icon="🔍",
    layout="wide"
)

st.title("Risk Analysis")

# Risk Score Overview
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Risk Score Breakdown")
    # Example data for risk breakdown
    risk_types = ['Natural Disasters', 'Economic', 'Geographic', 'Market Volatility']
    risk_scores = [85, 62, 71, 93]
    
    fig_breakdown = go.Figure(data=[
        go.Bar(x=risk_types, y=risk_scores, marker_color=['#FF9999', '#66B2FF', '#99FF99', '#FFCC99'])
    ])
    fig_breakdown.update_layout(yaxis_title="Risk Score")
    st.plotly_chart(fig_breakdown, use_container_width=True)

with col2:
    st.markdown("### Geographic Risk Distribution")
    # Example data for geographic distribution
    df_geo = pd.DataFrame({
        'Latitude': np.random.uniform(25, 50, 20),
        'Longitude': np.random.uniform(-130, -70, 20),
        'Risk_Level': np.random.randint(1, 100, 20)
    })
    
    fig_geo = px.scatter_mapbox(df_geo, 
                               lat='Latitude', 
                               lon='Longitude', 
                               size='Risk_Level',
                               color='Risk_Level',
                               zoom=3,
                               mapbox_style="carto-positron")
    st.plotly_chart(fig_geo, use_container_width=True)

# Risk Matrix
st.markdown("### Risk Assessment Matrix")
impact_levels = ['Minor', 'Moderate', 'Major', 'Severe', 'Catastrophic']
likelihood_levels = ['Rare', 'Unlikely', 'Possible', 'Likely', 'Almost Certain']

# Generate sample risk data
risk_data = np.random.randint(1, 10, size=(5, 5))
fig_matrix = go.Figure(data=go.Heatmap(
    z=risk_data,
    x=impact_levels,
    y=likelihood_levels,
    colorscale='RdYlGn_r'
))
fig_matrix.update_layout(
    title='Risk Matrix: Impact vs Likelihood',
    xaxis_title="Impact",
    yaxis_title="Likelihood"
)
st.plotly_chart(fig_matrix, use_container_width=True)

# Risk Factors Analysis
st.markdown("### Risk Factors Analysis")
risk_factors = st.multiselect(
    "Select Risk Factors to Analyze",
    ["Natural Disasters", "Economic Indicators", "Market Volatility", "Geographic Location"],
    default=["Natural Disasters", "Economic Indicators"]
)

# Time series for selected risk factors
dates = pd.date_range(start='2024-01-01', periods=100, freq='D')
df_risks = pd.DataFrame({
    'Date': dates,
    'Natural Disasters': np.random.normal(70, 15, 100),
    'Economic Indicators': np.random.normal(60, 10, 100),
    'Market Volatility': np.random.normal(50, 20, 100),
    'Geographic Location': np.random.normal(45, 5, 100)
})

if risk_factors:
    fig_trends = px.line(df_risks, x='Date', y=risk_factors)
    fig_trends.update_layout(title='Risk Factors Trends Over Time')
    st.plotly_chart(fig_trends, use_container_width=True)