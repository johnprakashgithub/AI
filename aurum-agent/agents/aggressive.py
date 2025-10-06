from langgraph.graph import StateNode
from tools.stock_data import get_high_volatility_tickers

@StateNode
def aggressive_strategy(state):
    tickers = get_high_volatility_tickers()
    state["selected_tickers"] = tickers[:5]  # top 5 risky picks
    state["strategy"] = "aggressive"
    return state
