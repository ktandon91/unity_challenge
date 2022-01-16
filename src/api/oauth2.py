import os
from typing import Optional

from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer

from api.config import settings
from api.repository import repo
from api.schemas import token as schemas


oauth2_scheme =  OAuth2PasswordBearer(tokenUrl='login', auto_error=False)


SECRET_KEY = os.getenv("SECRET", settings.secret_key)
ALGORITHM = os.getenv("ALGORITHM", settings.algorithm)
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", settings.access_token_expire_minutes))


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def verify_access_token(token: str, credentials_exception):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("email")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
    except JWTError:
        raise credentials_exception

    return token_data


async def is_subscriber(token: Optional[str] = Depends(oauth2_scheme)):  
    print(token)      
    if not token:
        return False

    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail=f"Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})

    token = verify_access_token(token, credentials_exception)
    user = await repo.db.users.find_one({"email" : token.email})

    if not user:
        raise credentials_exception
    return True
