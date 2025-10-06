from langgraph.graph import StateNode
from tools.stock_data import get_low_risk_tickers

@StateNode
def conservative_strategy(state):
    tickers = get_low_risk_tickers()
    state["selected_tickers"] = tickers[:3]  # top 3 safest picks
    state["strategy"] = "conservative"
    return state
