from typing import Optional

from fastapi import APIRouter, Depends, status, Response, HTTPException

from api import oauth2
from api.repository import Repository, get_database
from api.schemas.base import OID
from api.schemas.game import GameIn, GameOut, GamesListing
from api.services import games as games_service


router = APIRouter(tags=['Games'])


@router.get('/', response_model=GamesListing)
async def get_game_listings(is_subscriber: Optional[bool] = Depends(oauth2.is_subscriber), 
                db: Repository = Depends(get_database)):
    games_listing = await games_service.all_games(db, is_subscriber)
    return games_listing


@router.post('/', status_code=status.HTTP_201_CREATED)
async def add_game(game: GameIn, db: Repository = Depends(get_database)):
    game = await games_service.insert_game(db, game)
    return game


@router.get('/{game_id}', response_model=GameOut)
async def game_details(game_id: OID, db: Repository = Depends(get_database)):
    game = await games_service.get_game(db, game_id)
    if not game:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                    detail="Game not found")
    return game


@router.put('/{game_id}')
async def update_game(game_id: OID, game: GameIn, db: Repository = Depends(get_database)):
    result = await games_service.update_game(db=db, game_id=game_id, game=game)
    if result is None:
        return HTTPException(detail="Not able to update the document!", 
                        status_code=status.HTTP_400_BAD_REQUEST)
    return Response("Successfully Updated!")


@router.delete('/{game_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_game(game_id: OID, db: Repository = Depends(get_database)):
    await games_service.delete_game(db=db, game_id=game_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
