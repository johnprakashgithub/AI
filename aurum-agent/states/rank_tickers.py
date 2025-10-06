from langgraph.graph import StateNode
from tools.stock_data import score_tickers

@StateNode
def rank_tickers(state):
    tickers = state.get("selected_tickers", [])
    ranked = score_tickers(tickers)
    state["ranked_tickers"] = ranked
    return state
