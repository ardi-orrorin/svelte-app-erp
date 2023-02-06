import datetime
from pydantic import BaseModel, validator

from customerdetail.customerdetail_schema import CustomerDetail
from user.user_schema import User


class Payment(BaseModel):
    id: int
    corp_name: str
    bank_name: str
    bank_account: str
    bank_number: str
    money: str
    memo: str
    create_date: datetime.datetime
    user: User
    customerdetail: CustomerDetail

    class Config:
        orm_mode = True


class PaymentDetail(BaseModel):
    id: int
    corp_name: str
    bank_name: str
    bank_account: str
    bank_number: str
    money: str
    memo: str
    customerdetail_id: int
    customerdetail_name: str
    phonenumber: str
    body: str
    address: str
    addressdetail: str
    user_name: str
    create_date: datetime.datetime

    class Config:
        orm_mode: True


class PaymentCreate(BaseModel):
    corp_name: str
    bank_name: str
    bank_account: str
    bank_number: str
    money: int
    memo: str
    customerdetail_id: int
    create_date: datetime.datetime


class PaymentUpdate(PaymentCreate):
    payment_id: int


class PaymentTemp(BaseModel):
    id: int
    corp_name: str
    bank_name: str
    bank_account: str
    bank_number: str
    money: int
    name: str
    create_date: datetime.datetime

    class Config:
        orm_mode = True


class PaymentList(BaseModel):
    total: int = 0
    payment_list: list[PaymentTemp] = []

    class Config:
        orm_mode = True


class PaymentDelete(BaseModel):
    payment_id: int


class PaymentDeleteList(BaseModel):
    payment_idlist: list[PaymentDelete]
