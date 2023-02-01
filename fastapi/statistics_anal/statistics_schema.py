import datetime
from pydantic import BaseModel, validator


class StatisticsBarOne(BaseModel):
    user_id: str
    usercount: int
    date: datetime.date

    class Config:
        orm_mode = True


class StatisticsBarOneList(BaseModel):
    stat: list[StatisticsBarOne]
