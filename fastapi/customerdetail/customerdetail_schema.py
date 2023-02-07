from pydantic import BaseModel, validator
import datetime
from user.user_schema import User


class CustomerDetailCreate(BaseModel):
    id: int
    customer_id: int
    name: str
    phonenumber: str
    body: str
    address: str
    addressdetail: str
    user: User | None

    @validator('body')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v


class CustomerDetail(BaseModel):
    id: int
    name: str
    phonenumber: str
    body: str
    address: str
    addressdetail: str
    create_date: datetime.datetime
    customer_id: int
    """ user: User | None """

    class Config:
        orm_mode = True


class CustomerDetailList(BaseModel):
    customer_list: list[CustomerDetail] = []


class CustomerDetailUpdate(CustomerDetailCreate):
    customerdetail_id: int


class CustomerDetailDelete(BaseModel):
    id: int
