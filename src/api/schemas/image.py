from pydantic import validator
from typing import Optional
from api.schemas.base import BaseDBModel, OID

class Image(BaseDBModel):
    """
        Base Image Schema
    """
    url: Optional[str]
    type: Optional[int]

class ImageOut(Image):
    """
        During input id will not be passed. At the time of saving 
        the object to Mongo id will be automatically generated and
        this be returned during get request.
    """
    id: Optional[OID]

    # Validator to validate str oid is returned
    @validator("id")
    def validate_id(cls, v):
        """validator to sanitize id"""
        if v and not isinstance(v, str):
            return str(v)
        return v
