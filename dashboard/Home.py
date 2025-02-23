import streamlit as st

# Configure the page
st.set_page_config(
    page_title="DisasterIQ",
    page_icon=":bar_chart:",
    layout="wide"
)

# Main title and subtitle
st.title("DisasterIQ")
st.markdown("### Real-Time Anomaly Detection & Risk Optimization")

# Introduction section
st.markdown("""
## About the Project
Our Multi-Agent AI System integrates real-time market insights, economic trends, and mathematical reasoning 
to predict disaster-driven spikes, optimize risk, and manage inventory dynamically.
            
### Key Features:
- Real-time disaster monitoring and risk assessment
- Dynamic pricing optimization
- Intelligent inventory management
- Anomaly detection and alerting
""")

# Quick access cards using columns
st.markdown("## Quick Access")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 🚀 Dashboard
    Access real-time monitoring and key metrics
    """)
    st.link_button("Go to Dashboard", "Dashboard")

with col2:
    st.markdown("""
    ### 🔍 Risk Analysis
    View detailed risk assessments and analysis
    """)
    st.link_button("Go to Risk Analysis", "Risk Analysis")

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    ### 🚨 Anomaly Detection
    Monitor and detect unusual patterns
    """)
    st.link_button("Go to Anomaly Detection", "Anomaly Detection")

with col4:
    st.markdown("""
    ### 💸 Inventory Management
    Optimize inventory levels and forecasting
    """)
    st.link_button("Go to Inventory Management", "Inventory Management")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>Real-Time Anomaly Detection & Risk Optimization System</p>
        <p>Powered by Multi-Agent AI</p>
        <p>Hacklytics 2025<p>
    </div>
    """,
    unsafe_allow_html=True
)

# Team Members Section
team_col1, team_col2, team_col3, team_col4 = st.columns(4)

with team_col1:
    st.markdown("Vishrut Goel")
with team_col2:
    st.markdown("Hieu Nguyen")
with team_col3:
    st.markdown("Laurent Vong")
with team_col4:
    st.markdown("Naga Sekhar Madala")