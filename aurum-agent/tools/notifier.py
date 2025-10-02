import requests
from config import settings

def notify(message):
    requests.post(settings.slack_webhook, json={"text": message})
