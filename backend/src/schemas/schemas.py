from pydantic import BaseModel,EmailStr,Field
from enum import Enum
from typing import Optional
from datetime import datetime   



class UserReadSchema(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True

class UserReadStat(UserReadSchema):

    count_find_cancer: int


class HistoryCancerInfo(BaseModel):
    id: int
    user_id : int
    created_date: datetime