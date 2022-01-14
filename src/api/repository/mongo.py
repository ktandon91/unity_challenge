import logging
from typing import List

from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from api.repository.repository import Repository
from api.schemas.base import OID
from api.schemas.game import GameIn, GameOut
from api.schemas.image import ImageOut

# from api.models import GameIn, GameOut, OID, ImageOut


class MongoRepository(Repository):
    client: AsyncIOMotorClient = None
    db: AsyncIOMotorDatabase = None

    async def connect(self, path: str):
        logging.info("Connecting to MongoDB.")
        self.client = AsyncIOMotorClient(
            path,
            maxPoolSize=10,
            minPoolSize=10)
        self.db = self.client.main_db
        logging.info("Connected to MongoDB.")

    async def close(self):
        logging.info("Closing connection with MongoDB.")
        self.client.close()
        logging.info("Closed connection with MongoDB.")

    async def get_games(self) -> List[GameOut]:
        games_list = []
        games_q = self.db.games.find()
        async for game in games_q:
            games_list.append(GameOut(**game, id=game['_id']))
        return games_list

    async def get_game(self, game_id: OID) -> GameOut:
        game_q = await self.db.games.find_one({'_id': ObjectId(game_id)})
        if game_q:
            return GameOut(**game_q, id=game_q['_id'])

    async def delete_game(self, game_id: OID):
        await self.db.games.delete_one({'_id': ObjectId(game_id)})

    async def update_game(self, game_id: OID, game: GameIn):
        await self.db.games.update_one({'_id': ObjectId(game_id)},
                                       {'$set': game.dict(exclude={'id'})})

    async def add_game(self, game: GameOut):
        images = []
        for img in game.images:
            images.append(ImageOut(**img.dict(), id=ObjectId()))
        game.images=images
        await self.db.games.insert_one(game.dict(exclude={'id'}))
