import numpy as np
import pandas as pd

def annualized_return(returns: pd.Series, trading_days: int = 252) -> float:
    cum = (1 + returns).prod()
    n = len(returns)
    if n == 0:
        return np.nan
    return cum**(trading_days / n) - 1

def annualized_volatility(returns: pd.Series, trading_days: int = 252) -> float:
    return returns.std(ddof=1) * np.sqrt(trading_days)

def cvar(returns: pd.Series, alpha: float = 0.95) -> float:
    if len(returns) == 0:
        return np.nan
    losses = -returns.dropna()
    var = np.quantile(losses, alpha)
    tail_losses = losses[losses >= var]
    if len(tail_losses) == 0:
        return 0.0
    return float(tail_losses.mean())

def max_drawdown(cum_returns: pd.Series) -> float:
    rolling_max = cum_returns.cummax()
    drawdowns = cum_returns / rolling_max - 1.0
    return float(drawdowns.min())