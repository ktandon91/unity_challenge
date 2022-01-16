import logging

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from api.repository.repository import Repository


class MongoRepository(Repository):
    client: AsyncIOMotorClient = None
    db: AsyncIOMotorDatabase = None

    async def connect(self, url: str):
        logging.info("Connecting to MongoDB.")
        self.client = AsyncIOMotorClient(
            url,
            maxPoolSize=10,
            minPoolSize=10)
        self.db = self.client.unity_db
        await self.add_constraints()
        logging.info("Connected to MongoDB.")

    
    async def add_constraints(self):
        await self.db.users.create_index("email", unique=True)
    
    
    async def close(self):
        logging.info("Closing connection with MongoDB.")
        self.client.close()
        logging.info("Closed connection with MongoDB.")
