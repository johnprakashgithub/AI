from tools.schwab_api import get_account_details

access_token = input("Enter your access token: ")
response = get_account_details(access_token)

print("Account Info:")
print(response)
