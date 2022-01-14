from pydantic import validator
from typing import Optional
from api.schemas.base import BaseDBModel, OID

class Image(BaseDBModel):
    url: Optional[str]
    type: Optional[int]

class ImageOut(Image):
    id: Optional[OID]

    @validator("id")
    def validate_id(cls, v):
        if v and not isinstance(v, str):
            return str(v)
        return v
