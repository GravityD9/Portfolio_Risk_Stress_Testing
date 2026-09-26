import streamlit as st
import pandas as pd
import yfinance as yf
from risk_engine import calculate_historical_var, calculate_cvar, calculate_max_drawdown
from limits_monitor import RiskGovernanceEngine

st.set_page_config(page_title="RiskGuard Engine", layout="wide")

st.title("🛡️ Portfolio Risk Stress Testing")
st.markdown("Automated risk measurement and covenant breach detection engine.")

# Sidebar Configuration
st.sidebar.header("Portfolio Configuration")
tickers_input = st.sidebar.text_input("Enter Tickers (comma separated)", "AAPL,MSFT,JPM")
tickers = [t.strip() for t in tickers_input.split(",")]
portfolio_value = st.sidebar.number_input("Total Portfolio Value ($)", value=1000000)

@st.cache_data
def load_data(tickers):
    # downloading the full dataset first without forcing 'Adj Close'
    data = yf.download(tickers, start="2023-01-01", end="2024-01-01")
    
    # fallback mechanism: use 'Adj Close' if available, otherwise use 'Close'
    if 'Adj Close' in data.columns:
        price_data = data['Adj Close']
    elif 'Close' in data.columns:
        price_data = data['Close']
    else:
        st.error("Error fetching data from Yahoo Finance. Check ticker spellings.")
        st.stop()
        
    # handling single vs multiple tickers safely
    if isinstance(price_data, pd.Series):
        price_data = price_data.to_frame(tickers[0])
        
    return price_data.pct_change().dropna()

if tickers:
    returns = load_data(tickers)
    
    # Equal weight assumption for simplicity
    weights = {ticker: 1/len(tickers) for ticker in tickers}
    portfolio_returns = (returns * list(weights.values())).sum(axis=1)
    
    # Calculate Risk Metrics
    var_95 = calculate_historical_var(portfolio_returns, 0.95)
    cvar_95 = calculate_cvar(portfolio_returns, 0.95)
    cum_returns = (1 + portfolio_returns).cumprod()
    max_dd = calculate_max_drawdown(cum_returns)

    # UI Layout: Risk Metrics
    st.subheader("Quantitative Risk Profile")
    col1, col2, col3 = st.columns(3)
    col1.metric("1-Day VaR (95%)", f"{var_95:.2%}")
    col2.metric("Expected Shortfall (CVaR)", f"{cvar_95:.2%}")
    col3.metric("Maximum Drawdown", f"{max_dd:.2%}")
    
    st.line_chart(cum_returns)

    # Execute Limit Monitoring
    st.subheader("Operational Governance & Exception Log")
    engine = RiskGovernanceEngine(portfolio_value)
    
    # Execute checks
    engine.check_concentration_limit(weights, max_allowable=0.20) 
    engine.check_var_limit(var_95, max_loss_threshold=15000)
    
    audit_log = engine.export_audit_log()
    
    if not audit_log.empty:
        st.dataframe(audit_log, use_container_width=True)
        st.download_button(
            label="📥 Export Audit Log (CSV)", 
            data=audit_log.to_csv(index=False).encode('utf-8'), 
            file_name="risk_exceptions.csv",
            mime="text/csv"
        )
    else:
        st.success("No covenant or risk limit breaches detected.")