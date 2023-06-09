from os import getenv

from dotenv import load_dotenv


load_dotenv()


def get_data_database() -> dict:
    return {
        "DB_USER": getenv("DB_USER"),
        "DB_PASS": getenv("DB_PASS"),
        "DB_HOST": getenv("DB_HOST"),
        "DB_PORT": getenv("DB_PORT"),
        "DB_NAME": getenv("DB_NAME")
    }