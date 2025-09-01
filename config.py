import os
from dotenv import load_dotenv

load_dotenv()

# Telegram API
API_ID = int(os.getenv("API_ID", "22657083"))  
API_HASH = os.getenv("API_HASH", "d6186691704bd901bdab275ceaab88f3")

# Bot Token / String Session
BOT_TOKEN = os.getenv("BOT_TOKEN", "8319779558:AAGzwWPdZOylLjRRHUlmU9-AZZAeWhLDm9A")
STRING1 = os.getenv("STRING_SESSION", "AgCOaU4AmN-Ic-0SCPaou_eWQIQxG06WVlq3yTvbUFCE2JsVSI2OQgXlZnVI79_YRV3dNUGBijMJDhFHTec6NccYvmFHFR3BgYxfbLaneC4hRIx1VvOAHJpT7KsnUbKWFuRTFaDhRQwTO1_15MaDgYVJUBi9lWUhe22YDIu-CkVEa_GswpDS0lWyD-g0LommxBncq4-EmUyzKElGWzZVlWnlI8o3Pl-a6qF_P6vGalwD5RWSwXrbuld4Ippc6A38NoHDeHlBS6P4t1n141f62_RpMuAZ8OMKeW0U_5ZG25LU-PD2qGO7hebEpMA1OYWMTztRcdj14gqF1Aoz7_ncesebLRKY2wAAAAHR4jcZAA")

# Database
MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://ahaan:ahaad@ahaan.hgkeruq.mongodb.net/?retryWrites=true&w=majority&appName=ahaan")

# Owner / Admin
OWNER_ID = int(os.getenv("OWNER_ID", " 8195241636"))
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "x9Ahad")

# Support / Updates
SUPPORT_GRP = os.getenv("SUPPORT_GRP", "preetixmusic")
UPDATE_CHNL = os.getenv("UPDATE_CHNL", "Botsxupdate")