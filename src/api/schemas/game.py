
from typing import Optional, List

from pydantic import validator, Field

from api.schemas.base import BaseDBModel, OID
from api.schemas.image import Image, ImageOut

class Game(BaseDBModel):
    """
        Base Game Model
    """
    category: Optional[str]
    title: Optional[str]
    subtitle: Optional[str]
    description: Optional[str]
    type: Optional[int]
    tags: Optional[List[str]]
    author: Optional[str]
    replayBundleUrlJson: Optional[str]
    isDownloadable: Optional[bool] = False
    isStreamable: Optional[bool] = False
    isPremium: Optional[bool] = False
    version: float

class GameIn(Game):
    """
        Input Game Request Schema, Game object and 
        image array will be passed without ids.
    """
    images: Optional[List[Image]]

class GameOut(Game):
    """
        Output Game Response Schema
        Game object will be return with auto generated Mongo ObjectId.
        Image array will also be return with unique ids.
    """
    id: OID = Field(default_factory=OID)
    images: Optional[List[ImageOut]]

    # Validator to validate oid is converted to str
    @validator("id")
    def validate_id(cls, v):
        """validator to sanitize id"""
        if not isinstance(v, str):
            return str(v)
        return v


# Games Listing Model
class GamesListing(BaseDBModel):
    listings: List[GameOut]
