from fastapi import status, Depends, HTTPException, APIRouter
from pydantic import EmailStr

from api.schemas.user import UserIn, UserOut
from api.services import users as users_service
from api.repository import Repository, get_database

router = APIRouter(
    tags=['Users']
)


@router.get('/{email}', response_model=UserOut)
async def get_user(email: EmailStr, db: Repository = Depends(get_database)):
    user = await users_service.get_user(email, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                    details="User not found")
    return user

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserOut)
async def create_user(user: UserIn, db: Repository = Depends(get_database)):
    new_user = await users_service.create_user(user, db)
    return new_user
