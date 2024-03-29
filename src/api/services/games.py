from typing import List

from bson import ObjectId
from pymongo import ReturnDocument

from api.repository import Repository
from api.schemas.base import OID 
from api.schemas.game import GameIn, GameOut, GamesListing
from api.schemas.image import ImageOut

async def all_games(db:Repository, is_subscriber:bool = False) -> List[GameOut]:
    games_list = []
    if is_subscriber:
        games_q = db.games.find()
    else:
        games_q = db.games.find({"isPremium": { "$ne": True}})
    async for game in games_q:
        games_list.append(GameOut(**game, id=game['_id']))
    games_listing = GamesListing(listings=games_list)
    return games_listing


async def get_game(db:Repository, game_id: OID) -> GameOut:
    game_q = await db.games.find_one({'_id': ObjectId(game_id)})
    if game_q:
        return GameOut(**game_q, id=game_q['_id'])


async def insert_game(db:Repository, game: GameIn) -> None:
    images = []
    for img in game.images:
        images.append(ImageOut(**img.dict(), id=ObjectId()))
    game.images=images
    await db.games.insert_one(game.dict(exclude={'id'}))


async def update_game(db:Repository, game_id: OID, game: GameIn) -> None:
    images = []
    for img in game.images:
        images.append(ImageOut(**img.dict(), id=ObjectId()))
    game.images = images
    result = await db.games.find_one_and_update({'_id': ObjectId(game_id)},
                                       {'$set': game.dict(exclude={'id'})},
                                       return_document= True, 
                                       upsert=True)
    return result

async def delete_game(db:Repository, game_id: OID) -> None:
    await db.games.delete_one({'_id': ObjectId(game_id)})
