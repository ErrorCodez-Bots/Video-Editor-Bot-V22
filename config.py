"""
Configuration module for the Video Editor Bot
"""
import os
from dotenv import load_dotenv

load_dotenv()  # This line loads the .env file

class Config:
    """Bot configuration class"""
    
    # Telegram Bot Configuration
    BOT_TOKEN = os.getenv("8966841579:AAHx25ZPwvubxhwWigqCka5xuWf0T6G_Axo")
    API_ID = int(os.getenv("API_ID", "20293219"))
    API_HASH = os.getenv("4aef7d9e065d92f4a95736eaeb93d3ac")
    
    # MongoDB Configuration
    MONGODB_URI = os.getenv("MONGODB_URI", "mongodb+srv://nshubh345:1FmseyW0TKaWNMNo@cluster0.pgewb.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = os.getenv("DATABASE_NAME", "video_editor_bot")
    
    # Channel Configuration
    LOG_CHANNEL_ID = os.getenv("-1004461255503")
    BROADCAST_AS_COPY = os.getenv("BROADCAST_AS_COPY", "True") == "True"
    
    # Admin Configuration
    ADMIN_IDS = [int(x) for x in os.getenv("ADMIN_IDS", "").split(",") if x.strip()]
    
    # File Settings
    MAX_FILE_SIZE = int(os.getenv("MAX_FILE_SIZE", "4000"))  # in MB
    DOWNLOAD_PATH = os.getenv("DOWNLOAD_PATH", "./downloads")
    UPLOAD_PATH = os.getenv("UPLOAD_PATH", "./uploads")
    
    # Feature Toggles
    ENABLE_BROADCAST = os.getenv("ENABLE_BROADCAST", "True") == "True"
    ENABLE_URL_UPLOAD = os.getenv("ENABLE_URL_UPLOAD", "True") == "True"
    ENABLE_WATERMARK = os.getenv("ENABLE_WATERMARK", "True") == "False"
    
    # Ensure directories exist
    os.makedirs(DOWNLOAD_PATH, exist_ok=True)
    os.makedirs(UPLOAD_PATH, exist_ok=True)
    os.makedirs("logs", exist_ok=True)
