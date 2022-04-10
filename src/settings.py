from environs import Env
from dotenv import load_dotenv

load_dotenv()
env = Env()


class Settings:
    CLIENT_API_KEY = env.str("CLIENT_API_KEY")
    CLIENT_SECRET_KEY = env.str("CLIENT_SECRET_KEY")

    TRACK_TOPIC = env.str("TRACK_TOPIC")
    STREAM_URL = env.str("STREAM_URL")
    LOG_LEVEL = env.str("LOG_LEVEL", "INFO")
    OUTPUT_PATH = env.str("OUTPUT_PATH")
    MAX_TWEETS = env.int("MAX_TWEETS", 100)
    MAX_READ_TIME_SEC = env.int("MAX_READ_TIME_SEC", 30)
    DELIMITER = env.str("DELIMITER", "\t")

    OAUTH_TOKEN = env.str("OAUTH_TOKEN")
    OAUTH_TOKEN_SECRET = env.str("OAUTH_TOKEN_SECRET")
