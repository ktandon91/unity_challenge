from typing import List
from fastapi import status, HTTPException, APIRouter
from pydantic import EmailStr

from api.schemas.user import UserIn, UserOut
from api.services import users as users_service
from api.repository import db

router = APIRouter(
    tags=['Users']
)


@router.get('/{email}', response_model=UserOut)
async def get_user(email: EmailStr):
    user = await users_service.get_user(email, db.db)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                    details="User not found")
    return user

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserOut)
async def create_user(user: UserIn):
    new_user = await users_service.create_user(user, db.db)
    return new_user

@router.get("/", response_model=List[UserOut])
async def get_users():
    users = await users_service.get_users(db.db)
    return users
