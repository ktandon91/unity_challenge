from api.schemas.base import OID

from pydantic import BaseModel, EmailStr, Field, validator


class UserIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True

class UserOut(BaseModel):
    id: OID = Field(default_factory=OID)
    email: EmailStr

    @validator("id")
    def validate_id(cls, v):
        """validator to sanitize id"""
        if not isinstance(v, str):
            return str(v)
        return v
