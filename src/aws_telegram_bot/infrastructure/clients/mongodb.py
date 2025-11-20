from pymongo import MongoClient
from functools import lru_cache

from aws_telegram_bot.config import settings

@lru_cache(maxsize=1)
def get_mongodb_client() -> MongoClient:
    """
    Get or create the Mongodb client.
    The client is created once and cached for subsequent calls.
    """
    return MongoClient(settings.MONGODB_CONNECTION_STRING)