import logging

from motor.motor_asyncio import AsyncIOMotorClient
from ..core.config import MONGODB_URL, MAX_CONNECTIONS_COUNT, MIN_CONNECTIONS_COUNT
from .mongodb import db


async def connect_to_mongo():
    logging.info("در حال اتصال به پایگاه داده...")
    db.client = AsyncIOMotorClient(str(MONGODB_URL),
                                   maxPoolSize=MAX_CONNECTIONS_COUNT,
                                   minPoolSize=MIN_CONNECTIONS_COUNT)
    logging.info("اتصال به پایگاه داده با موفقیت انجام شد")


async def close_mongo_connection():
    logging.info("در حال قطع اتصال پایگاه داده...")
    db.client.close()
    logging.info("اتصال به پایگاه داده با موفقیت قطع شد")
