import datetime
from pydantic import BaseModel, validator

from customerdetail.customerdetail_schema import CustomerDetail
from user.user_schema import User


class Customer(BaseModel):
    id: int
    create_date: datetime.datetime
    user: User | None

    class Config:
        orm_mode = True


class CustomerCreate(BaseModel):
    name: str
    body: str
    phonenumber: str
    address: str
    addressdetail: str
    create_date: datetime.datetime


class CustomerUpdate(CustomerCreate):
    customer_id: int


class CustomterTemp(BaseModel):
    id: int
    body: str
    name: str
    phonenumber: str
    create_date: datetime.datetime


class CustomerList(BaseModel):
    total: int = 0
    customer_list: list[CustomterTemp] = []

    class Config:
        orm_mode = True


class CustomerDelete(BaseModel):
    customer_id: int


class CustomerDeleteList(BaseModel):
    customer_idlist: list[CustomerDelete]
