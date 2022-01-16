from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from api.repository import Repository, get_database
from api.schemas.token import Token
from api.services import auth as auth_service

router = APIRouter(tags=['Authentication'])


@router.post('/login', response_model=Token)
async def login(user_credentials: OAuth2PasswordRequestForm = Depends(), 
                db: Repository = Depends(get_database)):
    token = await auth_service.login(user_credentials, db)
    return token

