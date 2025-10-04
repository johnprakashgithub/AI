from langgraph.graph import StateNode
from tools.stock_data import get_performance_metrics

@StateNode
def track_performance(state):
    trades = state.get("trade_results", [])
    performance = get_performance_metrics(trades)
    state["performance"] = performance
    return state
