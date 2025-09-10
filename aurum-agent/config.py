import os

class Settings:
    client_id = os.getenv("SCHWAB_CLIENT_ID")
    client_secret = os.getenv("SCHWAB_CLIENT_SECRET") 
    redirect_uri = "https://abc123.ngrok.io/callback"
    auth_base_url = "https://api.schwab.com/oauth2/authorize"
    token_url = "https://api.schwab.com/oauth2/token"
    api_base = "https://api.schwab.com/v1"
    account_id = os.getenv("SCHWAB_ACCOUNT_ID")
    target_gain = 1800

settings = Settings()
