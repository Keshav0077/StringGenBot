from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("26954495"))
API_HASH = getenv("2061c55207cfee4f106ff0dc331fe3d9")

BOT_TOKEN = getenv("BOT_TOKEN")
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

OWNER_ID = int(getenv("OWNER_ID", 7045947967))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/moviesbazaarsupp")
