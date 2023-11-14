import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    # Bot token can be obtained via https://t.me/BotFather
    TOKEN = os.getenv("BOT_TOKEN")

    def __init__(self, host, port, path, url, secret=None):
        self.WEB_SERVER_HOST = host
        self.WEB_SERVER_PORT = port

        self.WEBHOOK_PATH = path

        self.WEBHOOK_SECRET = secret
        self.BASE_WEBHOOK_URL = url


WEB_SERVER_HOST = os.getenv("WEB_SERVER_HOST")
WEB_SERVER_PORT = os.getenv("WEB_SERVER_PORT")
WEBHOOK_PATH = os.getenv("WEBHOOK_PATH")
# get var without error if it's not exist
WEBHOOK_SECRET = os.environ.get("WEBHOOK_SECRET", None)
BASE_WEBHOOK_URL = os.getenv("BASE_WEBHOOK_URL")

CONFIG = Config(
    host=WEB_SERVER_HOST,
    port=WEB_SERVER_PORT,
    path=WEBHOOK_PATH,
    secret=WEBHOOK_SECRET,
    url=BASE_WEBHOOK_URL
)


if __name__ == '__main__':
    print(CONFIG)
