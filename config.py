import os


class Config(object):
    API_HASH = "2beecc3ee357e6e3f2b2e783d4159f9f"
    BOT_TOKEN = "1843277705:AAGj9xjvO9jbnC75R8USUKxKjIRmq2k1xlE"
    TELEGRAM_API = "2929027"
    OWNER = "959184369"
    OWNER_USERNAME = "@kids_movies_and_Episodes_founder"
    PASSWORD = "my"
    DATABASE_URL = "mongodb+srv://ksai:ksai@cluster0.kayzwoi.mongodb.net/cluster0?retryWrites=true&w=majority"
    LOGCHANNEL = "-1001856739396" # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID","root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]
