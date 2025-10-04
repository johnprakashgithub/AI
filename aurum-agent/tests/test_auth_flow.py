from tools.auth import get_auth_url, exchange_code_for_token

print("Visit this URL to authorize your app:")
print(get_auth_url())

code = input("Paste the authorization code from Schwab: ")
token_data = exchange_code_for_token(code)

print("Access Token:", token_data.get("access_token"))
print("Refresh Token:", token_data.get("refresh_token"))
