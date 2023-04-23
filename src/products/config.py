from typing import TypedDict, TypeVar
import os

from dotenv import load_dotenv


T = TypeVar("T")


class Data(TypedDict):

    DB_USER: T
    DB_PASS: T
    DB_HOST: T
    DB_PORT: T
    DB_NAME: T


def get_data_database() -> Data:
    return Data(**{
        "DB_USER": os.getenv("DB_USER"),
        "DB_PASS": os.getenv("DB_PASS"),
        "DB_HOST": os.getenv("DB_HOST"),
        "DB_PORT": os.getenv("DB_PORT"),
        "DB_NAME": os.getenv("DB_NAME")
    })