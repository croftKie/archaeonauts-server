from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class PlayerSchema(BaseModel):
    username: str = Field(...)
    email: EmailStr = Field(...)
    hash: str = Field(...)
    stats: dict = Field(...)

class UpdatePlayerModel(BaseModel):
    username: Optional[str]
    email: Optional[EmailStr]
    hash: Optional[str]
    stats: Optional[object]

def ResponseModel(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message
    }

def ErrorResponseModel(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message
    }