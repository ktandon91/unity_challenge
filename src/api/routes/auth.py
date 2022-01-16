from fastapi import APIRouter, Depends

from api.repository import Repository, get_database
from api.schemas.token import Token
from api.schemas.user import UserIn
from api.services import auth as auth_service

router = APIRouter(tags=['Authentication'])


@router.post('/login', response_model=Token)
async def login(user_credentials: UserIn, db: Repository = Depends(get_database)):
    token = await auth_service.login(user_credentials, db)
    return token

