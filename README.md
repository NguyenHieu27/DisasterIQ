# Hacklytics 2025: DisasterIQ Intelligent Disaster Management Platform

## Vision & Goals
DisasterIQ aims to create an advanced disaster management platform that will combine real-time data analytics, machine learning, and predictive modeling to revolutionize disaster response and risk management. This README outlines our planned features and architectural vision.

## Proposed Architecture

### Market Insights AI Engine 
- Integration with Open-Meteo API for real-time weather data
- Integration with OpenFEMA for disaster-related data
- Sentiment analysis capabilities using GPT/BERT models (Planned)
- Data processing pipeline for multiple sources:
  - Insurance claims data
  - Disaster reports
  - Economic indicators

### Risk & Anomaly Detection System (Planned)
- Isolation Forest Model implementation for anomaly detection
- Correlation analysis between various risk factors
- Real-time alerting system design
- Risk scoring and classification framework

### Demand Forecast & Risk Optimization (Planned)
- XGBoost implementation for predictive modeling
- Monte Carlo simulations for risk assessment
- Dynamic pricing adjustment system
- Resource allocation optimization

### Stakeholder Dashboard & API Integration 
- Interactive web interface using Streamlit
- Real-time visualization system
- FastAPI backend implementation
- Secure authentication system

## Technical Architecture Design

### Data Layer
- `insurance_claims.csv`: Insurance claim data storage
- `disaster_reports.json`: Disaster event reports
- `economic_indicators.csv`: Economic impact data

### Processing Layer
- `market_insights_agent.py`: Data processing and API integration  (Planned)
- `risk_anomaly_agent.py`: Anomaly detection implementation (Planned)
- `demand_forecast_agent.py`: Predictive modeling system (Planned)

### Interface Layer
- `Home.py`: Streamlit dashboard
- `server.py`: FastAPI server implementation

## Development Roadmap

### Phase 1: Foundation
- Set up basic project structure
- Implement data ingestion framework
- Establish API connections (Open-Meteo, OpenFEMA)

### Phase 2: Core Features
- Develop anomaly detection system
- Implement basic dashboard
- Create initial API endpoints

### Phase 3: Advanced Features
- Add machine learning models
- Enhance visualization capabilities
- Implement optimization algorithms

### Phase 4: Integration & Testing
- System integration
- Performance optimization
- Security implementation

## Technical Requirements (Planned)

### Prerequisites
- Python 3.8+
- Required packages: streamlit, fastapi, pandas, numpy, scikit-learn, xgboost, plotly
- API keys for Open-Meteo and OpenFEMA

### Proposed Installation Process
```bash
git clone https://github.com/NguyenHieu27/DisasterIQ/
```

### Development Setup
```bash
# Launch the Streamlit dashboard
streamlit run app.py
```

## Planned Data Flow
1. Data Collection: Continuous ingestion from various sources
2. Processing & Analysis: Market insights AI processing
3. Risk Assessment: Pattern analysis and alert generation
4. Optimization: Resource allocation and pricing adjustments
5. Visualization: Dashboard display and API access

## Dashboard Access

Access our interactive dashboard on Streamlit: [DisasterIQ Dashboard](https://disasteriq.streamlit.app/)

## Current Project Status
This project is currently in development as part of Hacklytics 2025. The features and components described in this README represent our planned implementation and architectural vision.

## Contributing
We welcome ideas and contributions to help realize this vision. Please feel free to submit suggestions and improvements.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- Georgia Tech Hacklytics 2025 organizers and mentors
- Open-Meteo for weather data API
- OpenFEMA for disaster data resources

## Contact
For any queries about the project vision or contributing, please open an issue in the repository.
