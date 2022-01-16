from fastapi import APIRouter, Depends, status, Request, Response, HTTPException

from api.repository import Repository, get_database
from api.schemas.base import OID
from api.schemas.game import GameIn, GameOut, GamesListing
from api.services import games as games_service
from api.utils import check_authorization_header

router = APIRouter(tags=['Games'])


@router.get('/', response_model=GamesListing)
async def get_game_listings(is_premium_user: bool = Depends(check_authorization_header), 
                db: Repository = Depends(get_database)):
    games_listing = await games_service.all_games(db, is_premium_user)
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
                    details="Game not found")
    return game


@router.put('/{game_id}')
async def update_game(game_id: OID, game: GameIn, db: Repository = Depends(get_database)):
    await games_service.update_game(db=db, game_id=game_id, game=game)
    return Response("Successfully Updated!")


@router.delete('/{game_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_game(game_id: OID, db: Repository = Depends(get_database)):
    await games_service.delete_game(db=db, game_id=game_id)
