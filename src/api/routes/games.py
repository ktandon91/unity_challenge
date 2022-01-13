from fastapi import APIRouter, Depends

from api.repository import Repository, get_database
from api.models import Game, OID

router = APIRouter()


@router.get('/')
async def all_games(db: Repository = Depends(get_database)):
    games = await db.get_games()
    return games


@router.get('/{game_id}')
async def one_game(game_id: OID, db: Repository = Depends(get_database)):
    game = await db.get_game(game_id=game_id)
    return game


@router.put('/{game_id}')
async def update_game(game_id: OID, game: Game, db: Repository = Depends(get_database)):
    game = await db.update_game(game=game, game_id=game_id)
    return game


@router.post('/', status_code=201)
async def add_game(game_response: Game, db: Repository = Depends(get_database)):
    game = await db.add_game(game_response)
    return game


@router.delete('/{game_id}')
async def delete_game(game_id: OID, db: Repository = Depends(get_database)):
    await db.delete_game(game_id=game_id)
