from pydantic import BaseModel,EmailStr,Field
from enum import Enum
from typing import Optional



class UserReadSchema(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True