from requests_oauthlib import OAuth2Session
from config import settings

def get_token():
    oauth = OAuth2Session(settings.client_id, redirect_uri=settings.redirect_uri)
    auth_url, state = oauth.authorization_url(settings.auth_base_url)
    print("Visit this URL to authorize:", auth_url)

    # After user authorizes, they get redirected with ?code=XYZ
    redirect_response = input("Paste full redirect URL here: ")
    token = oauth.fetch_token(
        settings.token_url,
        authorization_response=redirect_response,
        client_secret=settings.client_secret
    )
    return token
