from bson import ObjectId
from pydantic import BaseModel

class OID(str):
    """
        Bson ObjectId is not json serializable by default,
        this will convert bson ObjectId to str
    """
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)
    
    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class BaseDBModel(BaseModel):
    """
        Base model, properties will be inherited by children. 
        
        :Config 
            orm_mode Model can be used with MongoDB/ORMs
            allow_population_by_field_name, JSON output can use the alias names               
    """
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
