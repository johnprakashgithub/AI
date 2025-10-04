from langgraph.graph import StateNode
from tools import schwab_api
from config import settings

@StateNode
def monitor_funds(state):
    deposit = schwab_api.check_deposit()
    state["funds_checked"] = True
    state["deposit"] = deposit
    state["funds_ok"] = deposit >= settings.min_deposit_threshold
    return state
