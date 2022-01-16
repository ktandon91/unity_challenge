from api.repository.repository import Repository
from api.repository.mongo import MongoRepository

repo = MongoRepository()

def get_database():
    return repo.db
