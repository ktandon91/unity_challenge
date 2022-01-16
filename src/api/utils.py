from fastapi import Request, HTTPException, status
from passlib.context import CryptContext

from api import oauth2

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(password: str):
    return pwd_context.hash(password)


def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

async def check_authorization_header(req: Request) -> bool:
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail=f"Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    if "authorization" in req.headers:
        token = req.headers['authorization'].replace("Bearer", "").strip()
        user = oauth2.verify_access_token(token, credentials_exception)
        if user:
            return True
    return False    
