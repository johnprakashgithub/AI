from tools.auth import get_auth_url, exchange_code_for_token
from tools.schwab_api import get_account_details

print("Visit this URL to authorize:", get_auth_url())

# After authorization, paste the code here
code = input("Enter the code from Schwab: ")
token_data = exchange_code_for_token(code)
print("Access Token:", token_data["access_token"])

account_info = get_account_details(token_data["access_token"])
print("Account Info:", account_info)
