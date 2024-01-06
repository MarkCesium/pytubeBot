from dotenv import load_dotenv
from os import getenv


def get_token() -> str:
    if load_dotenv():
        return getenv("BOT_TOKEN")
    else:
        raise Exception("file .env not find")
