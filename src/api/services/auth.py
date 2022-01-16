from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from api import utils, oauth2
from api.repository import Repository


async def login(user_credentials: OAuth2PasswordRequestForm, db: Repository):
    user = await db.users.find_one({"email": user_credentials.username})
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    if not utils.verify(user_credentials.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")


    access_token = oauth2.create_access_token(data={"email": user["email"]})

    return {"access_token": access_token, "token_type": "bearer"}
