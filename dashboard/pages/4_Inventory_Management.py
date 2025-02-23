import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Inventory Management - DisasterIQ",
    page_icon="🔍",
    layout="wide"
)

st.title("Inventory Management")

# Inventory Overview
# Dummy data for now
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Stock Items", "1,234", "12")
with col2:
    st.metric("Stock Value", "$543,210", "+2.3%")
with col3:
    st.metric("Stockout Risk", "Low", "stable")
with col4:
    st.metric("Turnover Rate", "4.5x", "+0.2")

# Inventory Controls
st.markdown("### Inventory Control Settings")
col1, col2 = st.columns(2)

with col1:
    reorder_point = st.slider(
        "Reorder Point",
        min_value=0,
        max_value=1000,
        value=500,
        help="Set the inventory level that triggers a reorder"
    )
    
with col2:
    safety_stock = st.slider(
        "Safety Stock Level",
        min_value=0,
        max_value=500,
        value=200,
        help="Minimum stock level to maintain"
    )

# Inventory Levels Chart
st.markdown("### Current Inventory Levels")
# Generate sample inventory data
categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
inventory_levels = np.random.randint(50, 500, size=len(categories))
reorder_levels = np.random.randint(100, 200, size=len(categories))

fig_levels = go.Figure(data=[
    go.Bar(name='Current Stock', x=categories, y=inventory_levels),
    go.Bar(name='Reorder Level', x=categories, y=reorder_levels)
])
fig_levels.update_layout(barmode='group')
st.plotly_chart(fig_levels, use_container_width=True)

# Demand Forecast
st.markdown("### Demand Forecast")
dates = pd.date_range(start='2024-01-01', periods=90, freq='D')
forecast_data = pd.DataFrame({
    'Date': dates,
    'Actual': np.random.normal(100, 15, 90),
    'Forecast': np.random.normal(100, 10, 90),
    'Upper Bound': np.random.normal(120, 10, 90),
    'Lower Bound': np.random.normal(80, 10, 90)
})

fig_forecast = go.Figure([
    go.Scatter(
        name='Actual',
        x=forecast_data['Date'],
        y=forecast_data['Actual'],
        mode='lines',
        line=dict(color='blue')
    ),
    go.Scatter(
        name='Forecast',
        x=forecast_data['Date'],
        y=forecast_data['Forecast'],
        mode='lines',
        line=dict(color='red', dash='dash')
    ),
    go.Scatter(
        name='Upper Bound',
        x=forecast_data['Date'],
        y=forecast_data['Upper Bound'],
        mode='lines',
        line=dict(width=0),
        showlegend=False
    ),
    go.Scatter(
        name='Lower Bound',
        x=forecast_data['Date'],
        y=forecast_data['Lower Bound'],
        mode='lines',
        line=dict(width=0),
        fillcolor='rgba(68, 68, 68, 0.3)',
        fill='tonexty',
        showlegend=False
    )
])
st.plotly_chart(fig_forecast, use_container_width=True)

# Inventory Optimization Recommendations
# Dummy data for now
st.markdown("### Optimization Recommendations")
recommendations = pd.DataFrame({
    'Item': ['Item A', 'Item B', 'Item C', 'Item D'],
    'Current Stock': [150, 80, 200, 120],
    'Recommended Action': ['Reorder', 'Urgent Reorder', 'Reduce Stock', 'Optimal'],
    'Potential Savings': ['$1,200', '$800', '$500', '$0']
})
st.dataframe(recommendations, hide_index=True)