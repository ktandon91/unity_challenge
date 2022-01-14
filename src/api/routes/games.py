from typing import List
from fastapi import APIRouter, Response, status, HTTPException

from api.schemas.base import OID
from api.schemas.game import GameIn, GameOut

import api.services.games as games_service
# from api.services.games import all_games, get_game, insert_game

router = APIRouter()


@router.get('/', response_model=List[GameOut])
async def get_games():
    games = await games_service.all_games()
    return games


@router.post('/', status_code=status.HTTP_201_CREATED)
async def add_game(game: GameIn):
    game = await games_service.insert_game(game)
    return game


@router.get('/{game_id}', response_model=GameOut)
async def game_details(game_id: OID):
    game = await games_service.get_game(game_id=game_id)
    if not game:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                    details="Game not found")
    return game


@router.put('/{game_id}')
async def update_game(game_id: OID, game: GameIn):
    game = await games_service.update_game(game_id=game_id, game=game)
    if not game:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                    details="Game not found")
    return game


@router.delete('/{game_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_game(game_id: OID):
    await games_service.delete_game(game_id=game_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
