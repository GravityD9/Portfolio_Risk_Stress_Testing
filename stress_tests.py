import pandas as pd

def simulate_equity_crash(returns: pd.DataFrame, shock_pct: float = -0.20) -> pd.DataFrame:
    """Simulates a sudden market crash across all equities in the portfolio."""
    stressed_returns = returns.copy()
    # Apply a sudden drop to the most recent day to simulate an immediate shock
    stressed_returns.iloc[-1] = stressed_returns.iloc[-1] + shock_pct
    return stressed_returns

def simulate_volatility_spike(returns: pd.DataFrame, vol_multiplier: float = 1.5) -> pd.DataFrame:
    """Simulates a high-volatility regime by scaling historical returns."""
    mean_return = returns.mean()
    stressed_returns = mean_return + (returns - mean_return) * vol_multiplier
    return stressed_returns