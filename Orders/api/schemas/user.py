from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class Login(BaseModel):
    email: EmailStr
    password: str


class UserRequest(Login):
    role: Optional[str] = 'user'


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    role: str
    created_dttm: datetime

    class Config:
        orm_mode = True


class Token(BaseModel):
    token_type: str
    access_token: str


class TokenData(BaseModel):
    user_id: int
    role: Optional[str]

