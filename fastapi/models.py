from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from database import Base


class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True, index=True)
    create_date = Column(DateTime, nullable=False, index=True)
    user_id = Column(Integer, ForeignKey(
        "user.id", ondelete='CASCADE'), nullable=True,)
    user = relationship("User", backref=backref(
        "question_user", cascade='all,delete'))


class CustomerDetail(Base):
    __tablename__ = 'customerdetail'
    __table_args__ = {
        'postgresql_partition_by': 'RANGE (create_date)'
    }

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    body = Column(Text, nullable=False)
    phonenumber = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    addressdetail = Column(String(255), nullable=True)
    create_date = Column(DateTime, nullable=False, index=True)
    customer_id = Column(Integer, index=True)
    user_id = Column(Integer,  nullable=False, index=True)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(100), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    phonenumber = Column(String(50), unique=True, nullable=False)
    confirm_notice = Column(Text, nullable=True)
    authority = Column(Integer, nullable=False, index=True)
    create_date = Column(DateTime, nullable=False)


class Notice(Base):
    __tablename__ = 'notice'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    body = Column(Text, nullable=True)
    create_date = Column(DateTime, nullable=False, index=True)
    pin = Column(Integer, nullable=False)
    important = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey(
        "user.id", ondelete="CASCADE"), nullable=True, index=True)
    user = relationship("User", backref=backref(
        "notice_users", cascade='all,delete'))


class Payment(Base):
    __tablename__ = 'payment'
    id = Column(Integer, primary_key=True, index=True)
    corp_name = Column(String(100), nullable=False)
    bank_name = Column(String(100), nullable=False)
    bank_account = Column(String(100), nullable=False)
    bank_number = Column(String(100), nullable=False)
    money = Column(Integer, nullable=False)
    memo = Column(Text, nullable=True)
    create_date = Column(DateTime, nullable=False, index=True)
    user_id = Column(Integer, ForeignKey(
        "user.id", ondelete="CASCADE"), nullable=True, index=True)
    user = relationship("User", backref=backref(
        "payment_users", cascade='all,delete'))
    customerdetail_id = Column(Integer, ForeignKey(
        "customerdetail.id", ondelete="CASCADE"), nullable=True, index=True)
    customerdetail = relationship("CustomerDetail", backref=backref(
        "payment_customerdetails", cascade='all,delete'))


class NoticeConfirm(Base):
    __tablename__ = 'noticeconfirm'
    __table_args__ = {
        'postgresql_partition_by': 'RANGE (confirm_date)'
    }
    id = Column(Integer, primary_key=True, index=True)
    notice_id = Column(Integer, index=True, nullable=False)
    user_id = Column(Integer, index=True, nullable=False)
    confirm_date = Column(DateTime, index=True, nullable=False)


class Notification(Base):
    __tablename__ = 'notification'
    id = Column(Integer, primary_key=True, index=True)
    channel = Column(String(255), nullable=False)
    message = Column(String(255), nullable=False)
    user_id = Column(Integer, index=True, nullable=False)
    authority = Column(Integer, index=True, nullable=False)
    create_date = Column(DateTime, index=True, nullable=False)


""" class CustomerDetail(Base):
    __tablename__ = 'customerdetail'
    __table_args__ = {
        'postgresql_partition_by': 'RANGE (create_date)'
    }

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    body = Column(Text, nullable=False)
    phonenumber = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    addressdetail = Column(String(255), nullable=True)
    create_date = Column(DateTime, nullable=False, index=True)

    customer_id = Column(Integer, ForeignKey(
        "customer.id", ondelete='CASCADE'), index=True)
    customer = relationship(
        "Customer", backref=backref("customerdetail_customers", cascade='all,delete'))
    user_id = Column(Integer, ForeignKey(
        "user.id", ondelete="CASCADE"), nullable=True, index=True)
    user = relationship("User", backref=backref(
        "customerdetail_users", cascade='all,delete')) """
