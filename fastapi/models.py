from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

from database import Base


class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True)
    create_date = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey(
        "user.id", ondelete='CASCADE'), nullable=True)
    user = relationship("User", backref=backref(
        "question_user", cascade='all,delete'))


class CustomerDetail(Base):
    __tablename__ = 'customerdetail'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    body = Column(Text, nullable=False)
    phonenumber = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    addressdetail = Column(String(255), nullable=True)
    create_date = Column(DateTime, nullable=False)

    customer_id = Column(Integer, ForeignKey(
        "customer.id"))
    customer = relationship(
        "Customer", backref="customerdetail_customers")
    user_id = Column(Integer, ForeignKey(
        "user.id"), nullable=True)
    user = relationship("User", backref="customerdetail_users")


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    phonenumber = Column(String(50), unique=True, nullable=False)
    authority = Column(Integer, nullable=False)
    create_date = Column(DateTime, nullable=False)
