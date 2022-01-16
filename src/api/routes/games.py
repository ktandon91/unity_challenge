from typing import List
from fastapi import APIRouter, Depends, status, Request, Response, HTTPException

from api import oauth2
from api.schemas.base import OID
from api.schemas.game import GameIn, GameOut, GamesListing

from api.services import games as games_service

router = APIRouter(tags=['Games'])

async def check_authorization_header(req: Request) -> bool:
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail=f"Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    if "authorization" in req.headers:
        token = req.headers['authorization'].replace("Bearer", "").strip()
        user = oauth2.verify_access_token(token, credentials_exception)
        if user:
            return True
    return False    

@router.get('/', response_model=GamesListing)
async def get_games(is_premium_user = Depends(check_authorization_header)):
    games_listing = await games_service.all_games(is_premium_user)
    return games_listing


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
    await games_service.update_game(game_id=game_id, game=game)
    return Response("Successfully Updated!")


@router.delete('/{game_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_game(game_id: OID):
    await games_service.delete_game(game_id=game_id)
