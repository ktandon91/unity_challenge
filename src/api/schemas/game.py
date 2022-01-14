from pydantic import validator, Field
from typing import Optional, List

from api.schemas.base import BaseDBModel, OID
from api.schemas.image import Image, ImageOut

class Game(BaseDBModel):
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
    version: float

class GameIn(Game):
    images: Optional[List[Image]]

class GameOut(Game):
    id: OID = Field(default_factory=OID)
    images: Optional[List[ImageOut]]

    @validator("id")
    def validate_id(cls, v):
        if not isinstance(v, str):
            return str(v)
        return v
