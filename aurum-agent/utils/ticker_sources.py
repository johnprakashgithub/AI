# aurum-agent/utils/ticker_sources.py

def get_tickers(source):
    if source == "yahoo":
        return ["AAPL", "MSFT", "GOOG", "TSLA"]
    elif source == "alpha":
        return ["AMZN", "NVDA", "META", "NFLX"]
    return ["DEMO1", "DEMO2"]
