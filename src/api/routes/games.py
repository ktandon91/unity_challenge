from typing import List
from fastapi import APIRouter, Depends, Response, status, HTTPException

from api.repository import Repository, get_database
from api.schemas.base import OID
from api.schemas.game import GameIn, GameOut
# from api.models import GameIn, GameOut, OID

router = APIRouter()


@router.get('/', response_model=List[GameOut])
async def all_games(db: Repository = Depends(get_database)):
    games = await db.get_games()
    return games


@router.get('/{game_id}', response_model=GameOut)
async def one_game(game_id: OID, db: Repository = Depends(get_database)):
    game = await db.get_game(game_id=game_id)
    if not game:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                    details="Game not found")
    return game


@router.put('/{game_id}')
async def update_game(game_id: OID, game: GameIn, db: Repository = Depends(get_database)):
    game = await db.update_game(game=game, game_id=game_id)
    if not game:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                    details="Game not found")
    return game


@router.post('/', status_code=status.HTTP_201_CREATED)
async def add_game(game_response: GameIn, db: Repository = Depends(get_database)):
    game = await db.add_game(game_response)
    return game


@router.delete('/{game_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_game(game_id: OID, db: Repository = Depends(get_database)):
    await db.delete_game(game_id=game_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
