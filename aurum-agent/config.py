from pydantic import BaseSettings

class Settings(BaseSettings):
    client_id: str
    client_secret: str
    redirect_uri: str = "https://abc123.ngrok.io/callback"
    auth_base_url: str = "https://api.schwab.com/oauth2/authorize"
    token_url: str = "https://api.schwab.com/oauth2/token"
    api_base: str = "https://api.schwab.com/v1"
    account_id: str
    target_gain: int = 1800

    class Config:
        env_file = ".env"

settings = Settings()
