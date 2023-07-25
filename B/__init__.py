from pyrogram import Client
from telethon.sessions import StringSession
from telethon.sync import TelegramClient
from os import getenv
from dotenv import load_dotenv
import logging, time, sys

# Load environment variables from .env file
load_dotenv(".env")

# Configure logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Variables
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
SESSION = getenv("SESSION")
FORCESUB = getenv("FORCESUB")
OWNER = int(getenv("OWNER"))

# Start Telegram bot client
bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# Start userbot client
userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error! Have you added SESSION while deploying?")
    sys.exit(1)

# Start another client named Bot
Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
