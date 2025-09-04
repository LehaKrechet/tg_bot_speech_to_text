from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

VOICE_DIR = os.getenv("VOICE_DIR")