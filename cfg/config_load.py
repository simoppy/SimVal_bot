from os import getenv
from dotenv import load_dotenv

load_dotenv()
TOKEN = getenv("BOT_TOKEN")
PROXY_URL = getenv("SOCKS5_PROXY")
FOLDER_ID = getenv("GOOGLE_FOLDER_ID")