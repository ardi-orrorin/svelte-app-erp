
from pydantic import BaseModel, validator


class CustomerDetail(BaseModel):
    id: int
    customer_id: int
    phonenumber: str
    body: str
    create_date: str
    name: str


class CustomerDetailList(BaseModel):
    result: list[CustomerDetail]
