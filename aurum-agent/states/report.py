from langgraph.graph import StateNode

@StateNode
def report(state):
    summary = {
        "strategy": state.get("strategy"),
        "tickers": state.get("selected_tickers"),
        "trades": state.get("trade_results"),
        "balance": state.get("account_balance"),
        "goal": state.get("goal"),
    }
    state["report"] = summary
    return state
