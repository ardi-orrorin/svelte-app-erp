from datetime import datetime
from models import Payment, User
from payment.payment_schema import PaymentCreate, PaymentUpdate
from sqlalchemy.orm import Session
from sqlalchemy import func
from user import user_schema
from datetime import datetime
from pytz import timezone


def get_payment_list(db: Session, skip: int = 0, limit: int = 10, keyword: str = '', userid: int = 0, order: str = 'create_date-desc',
                     startdate: datetime = datetime.now(timezone('Asia/Seoul')), enddate: datetime = datetime.now(timezone('Asia/Seoul'))):

    payment_list = db.query(Payment.id, Payment.corp_name, Payment.bank_name, Payment.bank_account, Payment.bank_number, Payment.money, Payment.create_date, User.name).filter(Payment.create_date >= startdate.astimezone(
        timezone('Asia/Seoul')), Payment.create_date <= enddate.astimezone(timezone('Asia/Seoul'))).outerjoin(User, User.id == Payment.user_id)

    if userid > 0:
        payment_list = payment_list.filter(Payment.user_id == userid)

    if keyword:
        keyword = keyword.split(' ')
        for keyword in keyword:
            search = f'%%{keyword}%%'
            payment_list = payment_list.filter(Payment.bank_account.ilike(search) | Payment.bank_name.ilike(
                search) | Payment.corp_name.ilike(search) | User.name.ilike(search) | Payment.bank_number.ilike(search))

    order_dict = {'id-asc': Payment.id, 'id-desc': Payment.id.desc(),
                  'create_date-asc': Payment.create_date, 'create_date-desc': Payment.create_date.desc()}

    result = payment_list.order_by(
        order_dict[order]).offset(skip).limit(limit).all()
    total = payment_list.count()

    return total, result


def get_payment(db: Session, payment_id: int):
    payment = db.query(Payment).get(payment_id)
    return payment


def del_get_payment_list(db: Session, payment_idlist: list):
    payment_list = []
    for i in payment_idlist:
        payment_list.append(db.query(Payment).get(i.payment_id))
    return payment_list


def create_payment(db: Session, paymentcreate: PaymentCreate, user: user_schema.User):
    create_date = datetime.now()
    db_payment = Payment(
        create_date=create_date, user=user)
    db.add(db_payment)
    db.commit()
    payment = db.query(Payment).filter(
        Payment.user_id == user.id).order_by(Payment.id.desc()).first()
    db_customerdetail = Payment(
        corp_name=paymentcreate.corp_name, bank_name=paymentcreate.bank_name,
        bank_account=paymentcreate.bank_account, bank_number=paymentcreate.bank_number,
        money=paymentcreate.money, memo=paymentcreate.memo, create_date=create_date, customerdetail_id=paymentcreate.customerdetail_id, user=user)
    db.add(db_customerdetail)
    db.commit()

    return payment


def update_payment(db: Session, db_payment: Payment, payment_update: PaymentUpdate):

    db_payment.create_date = datetime.now()
    db.add(db_payment)
    db.commit()


def delete_payment(db: Session, db_payment: list[Payment]):
    for i in db_payment:
        db.delete(i)
    db.commit()
