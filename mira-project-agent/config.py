from dotenv import load_dotenv
import os

load_dotenv()

CONFIG = {
    "trello_api_key": os.getenv("TRELLO_API_KEY"),
    "trello_token": os.getenv("TRELLO_TOKEN"),
    "trello_board_id": os.getenv("TRELLO_BOARD_ID"),
    "openai_api_key": os.getenv("OPENAI_API_KEY"),
    "smtp_host": os.getenv("SMTP_HOST"),
    "smtp_port": int(os.getenv("SMTP_PORT")),
    "smtp_user": os.getenv("SMTP_USER"),
    "smtp_password": os.getenv("SMTP_PASSWORD"),
    "email_from": os.getenv("EMAIL_FROM"),
    "email_to": os.getenv("EMAIL_TO"),
}
