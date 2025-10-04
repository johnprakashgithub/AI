from langgraph.graph import StateNode
from tools.stock_data import get_balanced_portfolio

@StateNode
def balanced_strategy(state):
    tickers = get_balanced_portfolio()
    state["selected_tickers"] = tickers
    state["strategy"] = "balanced"
    return state
