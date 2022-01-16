from api.schemas.base import BaseDBModel

from pydantic import EmailStr


class UserIn(BaseDBModel):
    email: EmailStr
    password: str

class UserOut(BaseDBModel):
    email: EmailStr

