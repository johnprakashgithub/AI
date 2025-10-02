import requests
from config import settings
from tools.auth import get_token

token = get_token()
headers = {"Authorization": f"Bearer {token['access_token']}"}

def check_deposit():
    url = f"{settings.api_base}/accounts/{settings.account_id}/balances"
    res = requests.get(url, headers=headers).json()
    return res["availableCash"]

def execute_trade(ticker, quantity, order_type="Market"):
    url = f"{settings.api_base}/accounts/{settings.account_id}/orders"
    payload = {
        "symbol": ticker,
        "quantity": quantity,
        "orderType": order_type,
        "action": "BUY"
    }
    res = requests.post(url, headers=headers, json=payload)
    return res.json()

def get_account_details(access_token: str):
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    url = f"{settings.api_base}/accounts/{settings.account_id}"
    response = requests.get(url, headers=headers)
    return response.json()
