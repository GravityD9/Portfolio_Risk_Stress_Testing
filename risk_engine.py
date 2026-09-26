import numpy as np
import pandas as pd

def calculate_historical_var(returns: pd.Series, confidence_level: float = 0.95) -> float:
    """Calculates Historical Value at Risk (VaR)."""
    return np.percentile(returns, 100 * (1 - confidence_level))

def calculate_cvar(returns: pd.Series, confidence_level: float = 0.95) -> float:
    """Calculates Conditional VaR (Expected Shortfall)."""
    var_threshold = calculate_historical_var(returns, confidence_level)
    tail_losses = returns[returns <= var_threshold]
    return tail_losses.mean() if len(tail_losses) > 0 else var_threshold

def calculate_max_drawdown(cumulative_returns: pd.Series) -> float:
    """Calculates Maximum Drawdown from peak."""
    rolling_max = cumulative_returns.cummax()
    drawdown = (cumulative_returns - rolling_max) / rolling_max
    return drawdown.min()