from api.repository.repository import Repository 
from api.repository.mongo import MongoRepository

db = MongoRepository()


async def get_database() -> Repository:
    return db
