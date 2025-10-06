# Aurum Agent

A LangGraph-powered autonomous trading agent designed to optimize short-term gains in a Schwab account.

## Features

- Deposit monitoring
- Dynamic ticker selection
- Trade execution
- Goal tracking
- Sell logic
- Slack reporting

## Achitecture Flow
monitor_funds → fetch_tickers → rank_tickers → execute_traders → track_performance → sell_decision → report


## Setup

1. Set environment variables:
   - `SCHWAB_API_KEY`
   - `POLYGON_API_KEY`
   - `SLACK_WEBHOOK`

2. Run the agent:
```bash
python main.py