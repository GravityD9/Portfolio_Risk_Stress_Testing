import pandas as pd
from datetime import datetime

class RiskGovernanceEngine:
    def __init__(self, portfolio_value: float):
        self.portfolio_value = portfolio_value
        self.incident_log = []

    def check_concentration_limit(self, weights: dict, max_allowable: float = 0.20):
        """Flags assets exceeding maximum concentration limits."""
        for asset, weight in weights.items():
            if weight > max_allowable:
                self._log_breach("Critical", f"{asset} concentration ({weight:.1%}) exceeds {max_allowable:.1%} limit.")

    def check_var_limit(self, current_var: float, max_loss_threshold: float):
        """Flags if the 1-day VaR exceeds the acceptable dollar loss."""
        var_dollar = abs(current_var) * self.portfolio_value
        if var_dollar > max_loss_threshold:
            self._log_breach("Warning", f"1-Day VaR (${var_dollar:,.2f}) exceeds threshold (${max_loss_threshold:,.2f}).")

    def _log_breach(self, severity: str, message: str):
        self.incident_log.append({
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Severity": severity,
            "Exception": message
        })

    def export_audit_log(self) -> pd.DataFrame:
        """Returns the incident log as a structured DataFrame for reporting."""
        return pd.DataFrame(self.incident_log)