from tools import schwab_api
from config import settings

def run(state):
    deposit = schwab_api.check_deposit()
    if deposit >= settings.min_deposit_threshold:
        state["funds"] = deposit
    return state
