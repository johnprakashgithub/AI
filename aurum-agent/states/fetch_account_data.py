from langgraph.graph import StateNode
from tools.schwab_api import get_account_details

@StateNode
def fetch_account_data(state):
    access_token = state.get("access_token")
    account_info = get_account_details(access_token)
    state["account_info"] = account_info
    return state
