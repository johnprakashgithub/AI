from langgraph.graph import StateGraph
from states import (
    monitor_funds, fetch_tickers, rank_tickers,
    execute_traders, track_performance, sell_decision, report, fetch_account_data, 
    select_strategy
)
from agents.aggressive import aggressive_strategy
from agents.balanced import balanced_strategy
from agents.conservative import conservative_strategy


def build_graph():
    builder = StateGraph()
    builder.add_node("monitor_funds", monitor_funds.run)
    builder.add_node("fetch_tickers", fetch_tickers.run)
    builder.add_node("rank_tickers", rank_tickers.run)
    builder.add_node("execute_traders", execute_traders.run)
    builder.add_node("track_performance", track_performance.run)
    builder.add_node("sell_decision", sell_decision.run)
    builder.add_node("report", report.run)
    builder.add_node("fetch_account_data", fetch_account_data)
    builder.add_node("aggressive", aggressive_strategy)
    builder.add_node("balanced", balanced_strategy)
    builder.add_node("conservative", conservative_strategy)

    builder.set_entry_point("monitor_funds")
    builder.add_edge("monitor_funds", "fetch_tickers")
    builder.add_edge("fetch_tickers", "rank_tickers")
    builder.add_edge("rank_tickers", "execute_traders")
    builder.add_edge("execute_traders", "track_performance")
    builder.add_edge("track_performance", "sell_decision")
    builder.add_edge("sell_decision", "report")

    return builder.compile()
