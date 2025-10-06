from langgraph.graph import StateNode
from tools.schwab_api import place_trade

@StateNode
def execute_traders(state):
    tickers = state.get("selected_tickers", [])
    access_token = state.get("access_token")
    results = []

    for ticker in tickers:
        trade_result = place_trade(access_token, ticker, quantity=10)  # or dynamic quantity
        results.append({ticker: trade_result})

    state["trade_results"] = results
    return state
