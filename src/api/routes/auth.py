from fastapi import APIRouter, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from api.repository import db
from api.schemas.token import Token
from api.services import auth as auth_service

router = APIRouter(tags=['Authentication'])


@router.post('/login', response_model=Token)
async def login(user_credentials: OAuth2PasswordRequestForm = Depends()):
    token = await auth_service.login(user_credentials, db.db)
    return token

