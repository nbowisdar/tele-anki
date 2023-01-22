from aiogram import Dispatcher, Bot, Router
from dotenv import load_dotenv
import os
from pathlib import Path


load_dotenv()
TOKEN = os.getenv("TG_TOKEN")


admins_id = [286365412, ]
ngrok_url = ""


bot = Bot(TOKEN)
dp = Dispatcher()

# create routes

admin_router = Router()
user_router = Router()
# common_router = Router()

ROOT_DIR = Path(__file__).parent





