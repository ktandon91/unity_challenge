from typing import List

from bson import ObjectId

from api.repository import db as db_service
from api.schemas.base import OID 
from api.schemas.game import GameIn, GameOut
from api.schemas.image import ImageOut

async def all_games() -> List[GameOut]:
    db = db_service.db
    games_list = []
    games_q = db.games.find()
    async for game in games_q:
        games_list.append(GameOut(**game, id=game['_id']))
    return games_list


async def get_game(game_id: OID) -> GameOut:
    db = db_service.db
    game_q = await db.games.find_one({'_id': ObjectId(game_id)})
    if game_q:
        return GameOut(**game_q, id=game_q['_id'])


async def insert_game(game: GameIn):
    db = db_service.db
    images = []
    for img in game.images:
        images.append(ImageOut(**img.dict(), id=ObjectId()))
    game.images=images
    await db.games.insert_one(game.dict(exclude={'id'}))


async def update_game(game_id: OID, game: GameIn):
    db = db_service.db
    await db.games.update_one({'_id': ObjectId(game_id)},
                                       {'$set': game.dict(exclude={'id'})})

async def delete_game(game_id: OID):
    db = db_service.db
    await db.games.delete_one({'_id': ObjectId(game_id)})