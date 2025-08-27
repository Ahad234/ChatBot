import os
from dotenv import load_dotenv

load_dotenv()

# Telegram API
API_ID = int(os.getenv("API_ID", "22657083"))  
API_HASH = os.getenv("API_HASH", "d6186691704bd901bdab275ceaab88f3")

# Bot Token / String Session
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
STRING1 = os.getenv("STRING_SESSION", None)

# Database
MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://ahaan:ahaad@ahaan.hgkeruq.mongodb.net/?retryWrites=true&w=majority&appName=ahaan")

# Owner / Admin
OWNER_ID = int(os.getenv("OWNER_ID", " 8195241636"))
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "x9Ahad")

# Support / Updates
SUPPORT_GRP = os.getenv("SUPPORT_GRP", "IvanxNish ")
UPDATE_CHNL = os.getenv("UPDATE_CHNL", "Botsxupdate")