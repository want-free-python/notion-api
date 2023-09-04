from os import getenv

from dotenv import load_dotenv

load_dotenv(verbose=True)

DB = getenv("DB_NAME")
USER = getenv("DB_USER")
PASSWORD = getenv("DB_PASSWORD")
HOST = getenv("DB_HOST")
PORT = int(getenv("DB_PORT"))
