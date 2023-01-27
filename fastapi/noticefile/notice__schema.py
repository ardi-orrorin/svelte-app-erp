import datetime
from pydantic import BaseModel, validator
from user.user_schema import User


class Notice(BaseModel):
    id: int
    title: str
    body: str
    pin: int
    important: int
    create_date: datetime.datetime
    user: User | None

    class Config:
        orm_mode = True


class NoticeCreate(BaseModel):
    title: str
    body: str
    pin: int
    important: int
    create_date: datetime.datetime


class NoticeUpdate(Notice):
    id: int


class NoticeTemp(BaseModel):
    id: int
    title: str
    body: str
    pin: int
    important: int
    create_date: datetime.datetime
    user: User | None

    class Config:
        orm_mode = True


class NoticeList(BaseModel):
    total: int = 0
    notice_list: list[NoticeTemp] = []

    class Config:
        orm_mode = True


class NoticeDelete(BaseModel):
    id: int


class NoticeDeleteList(BaseModel):
    notice_idlist: list[NoticeDelete]
