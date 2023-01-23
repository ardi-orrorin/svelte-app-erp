from passlib.context import CryptContext
from sqlalchemy.orm import Session
from user.user_schema import UserCreate
from models import User
from datetime import datetime

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_user(db: Session, user_create: UserCreate):
    db_user = User(user_id=user_create.user_id,
                   password=pwd_context.hash(user_create.password1),
                   name=user_create.name,
                   email=user_create.email,
                   phonenumber=user_create.phonenumber,
                   authority=user_create.authority,
                   create_date=datetime.now()
                   )
    db.add(db_user)
    db.commit()


def get_existing_user(db: Session, user_create: UserCreate):
    return db.query(User).filter(
        (User.user_id == user_create.user_id) |
        (User.email == user_create.email)
    ).first()


def get_user(db: Session, user_id: str):
    return db.query(User).filter(User.user_id == user_id).first()
