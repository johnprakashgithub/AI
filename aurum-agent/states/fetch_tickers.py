# states/fetch_tickers.py

from langgraph.graph import StateNode
import logging
from utils.ticker_sources import get_tickers
from utils.filters import apply_filters

logger = logging.getLogger(__name__)

@StateNode
def fetch_tickers(state):
    source = state.get("ticker_source", "yahoo")  # default to Yahoo
    filters = state.get("ticker_filters", {})     # e.g., {"min_volume": 1000000}

    try:
        tickers = get_tickers(source)

        logger.info(f"Fetched {len(tickers)} tickers from {source}")

        filtered = apply_filters(tickers, filters)
        logger.info(f"{len(tickers)} tickers after filtering")

        # Update state
        state["tickers"] = filtered
        return state

    except Exception as e:
        logger.error(f"Ticker fetch failed: {e}")
        state["tickers"] = []
        state["error"] = f"Ticker fetch failed: {str(e)}"
        return state

