# from typing import List, Optional
# from bson import ObjectId
# from pydantic import BaseModel, Field, validator

# class OID(str):
#     @classmethod
#     def __get_validators__(cls):
#         yield cls.validate

#     @classmethod
#     def validate(cls, v):
#         if not ObjectId.is_valid(v):
#             raise ValueError("Invalid objectid")
#         return ObjectId(v)
    
#     @classmethod
#     def __modify_schema__(cls, field_schema):
#         field_schema.update(type="string")

# class BaseDBModel(BaseModel):
#     class Config:
#         # By default pydantic only works with dict
#         # setting orm_mode = True will allow it to work with Mongo
#         orm_mode = True
#         allow_population_by_field_name = True

#         # @classmethod
#         # def alias_generator(cls, string: str) -> str:
#         #     """ Camel case generator """
#         #     temp = string.split('_')
#         #     return temp[0] + ''.join(ele.title() for ele in temp[1:])

# class Image(BaseDBModel):
#     url: Optional[str]
#     type: Optional[int]

# class ImageOut(Image):
#     id: Optional[OID]

#     @validator("id")
#     def validate_id(cls, v):
#         if v and not isinstance(v, str):
#             return str(v)
#         return v

# class Game(BaseDBModel):
#     category: Optional[str]
#     title: Optional[str]
#     subtitle: Optional[str]
#     description: Optional[str]
#     type: Optional[int]
#     tags: Optional[List[str]]
#     author: Optional[str]
#     replayBundleUrlJson: Optional[str]
#     isDownloadable: Optional[bool] = False
#     isStreamable: Optional[bool] = False
#     version: float

# class GameIn(Game):
#     images: Optional[List[Image]]

# class GameOut(Game):
#     id: OID = Field(default_factory=OID)
#     images: Optional[List[ImageOut]]

#     @validator("id")
#     def validate_id(cls, v):
#         if not isinstance(v, str):
#             return str(v)
#         return v
