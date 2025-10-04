from langgraph.graph import StateNode
from tools.stock_data import evaluate_sell_conditions

@StateNode
def sell_decision(state):
    positions = state.get("current_positions", [])
    to_sell = evaluate_sell_conditions(positions)
    state["sell_list"] = to_sell
    return state
