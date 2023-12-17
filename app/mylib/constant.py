import os
from dotenv import load_dotenv

load_dotenv()
EXTENTIONS = [
    # extentions here
    "cogs.ping",
    "cogs.spotify",
    #"cogs.reminder",
]
TOKEN = os.environ["TOKEN"]
REMINDER_CHANNEL_ID = int(os.environ["REMINDER_CHANNEL_ID"])
