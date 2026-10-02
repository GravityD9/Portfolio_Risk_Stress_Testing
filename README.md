# RiskGuard - Portfolio Risk Stress Tessting

[Streamlit App](https://portfolioriskstresstesting-864t4pynxzds2vdnrjpdny.streamlit.app/#portfolio-risk-stress-testing)

**RiskGuard** is a Python-based quantitative risk and operational governance engine. Designed for middle-office and risk management teams, it automates the measurement of market risk (VaR, CVaR), executes portfolio stress tests, and dynamically monitors asset allocations against predefined debt covenants and concentration limits. 

By identifying structural anomalies and threshold breaches in real-time, this model replaces manual Excel exception-handling with a programmatic, zero-defect audit trail.

---

## Key Capabilities

*   **Quantitative Risk Measurement (BAU):** Computes Historical Value at Risk (VaR), Expected Shortfall (CVaR), and Maximum Drawdown across user-defined multi-asset portfolios.
*   **Automated Covenant & Limit Monitoring:** Continuously evaluates portfolio weights and risk exposures against hardcoded limits (e.g., maximum single-asset concentration of 20%, maximum allowable daily dollar-loss limits).
*   **Stress Testing & Scenario Analysis:** Simulates tail-risk market events—including instant equity shocks and extreme volatility regime shifts—to evaluate portfolio resilience and Distance-to-Liquidation metrics.
*   **Audit-Ready Exception Logging:** Automatically flags operational deviations (Warnings vs. Critical Breaches) and generates structured, timestamped CSV exception reports for internal controls and cross-functional reporting.

---

## System Architecture

The engine is built on a modular architecture to separate quantitative mathematics from operational governance logic:

1.  `risk_engine.py`: The quantitative core utilizing `numpy` and `scipy.stats` to execute array-based risk modeling.
2.  `limits_monitor.py`: The compliance rules engine. Evaluates outputs from the risk engine against strict governance thresholds to identify material deviations.
3.  `stress_tests.py`: Applies hypothetical and historical shock matrices to raw time-series data to evaluate drawdown indicators.
4.  `app.py`: A `Streamlit` frontend that ingests live market data via `yfinance`, visualizes cumulative returns, and provides an interactive dashboard for risk reporting.

---

## Tech Stack

*   **Core Logic & Analytics:** `Python 3.10+`, `pandas`, `numpy`, `scipy`
*   **Data Ingestion:** `yfinance` (Yahoo Finance API)
*   **Frontend & Visualization:** `Streamlit`, `plotly`

---

## Quick Start / Local Deployment

1. **Clone the repository:**
   ```bash
   git clone https://github.com/GravityD9/Portfolio_Risk_Stress_Testing.git
   cd Portfolio_Risk_Stress_Testing
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the dashboard:**
   ```bash
   streamlit run app.py
   ```
