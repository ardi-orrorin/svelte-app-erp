from pydantic import BaseModel, validator, EmailStr
import datetime


class UserCreate(BaseModel):
    user_id: str
    password1: str
    password2: str
    name: str
    email: EmailStr
    phonenumber: str
    authority: int
    create_date: datetime.datetime

    @validator('user_id', 'password1', 'password2', 'email', 'phonenumber')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v

    @validator('password2')
    def passwords_match(cls, v, values):
        if 'password1' in values and v != values['password1']:
            raise ValueError('비밀법호가 일치하지 않습니다.')
        return v


class Token(BaseModel):
    access_token: str
    token_type: str
    user_id: str


class User(BaseModel):
    id: int
    user_id: str
    name: str
    email: str
    authority: int

    class Config:
        orm_mode = True
