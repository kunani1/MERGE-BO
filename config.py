import os


class Config(object):
    API_HASH = "3ef17a8cdb938335bd8ba292e6d816aa"
    BOT_TOKEN = "6931430553:AAELwnQueYr6BEUQ8NTNU2z18VNEsaqKNtQ"
    TELEGRAM_API = "9976721"
    OWNER = "1956698956"
    OWNER_USERNAME = "@SatoruGojo830"
    PASSWORD = "my"
    DATABASE_URL = "mongodb+srv://gojomerge:gojomerge@cluster0.xyxlyph.mongodb.net/?retryWrites=true&w=majority"
    LOGCHANNEL = "-1001923959682" # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID","root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]
