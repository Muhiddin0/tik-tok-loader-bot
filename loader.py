
from pyrogram import Client

import dotenv
import os

dotenv.load_dotenv()

API_HASH = os.getenv('API_HASH') 
API_ID = os.getenv('API_ID') 
BOT_TOKEN = os.getenv('BOT_TOKEN') 

app = Client(api_id=API_ID, api_hash=API_HASH, name='mySession', bot_token=BOT_TOKEN)