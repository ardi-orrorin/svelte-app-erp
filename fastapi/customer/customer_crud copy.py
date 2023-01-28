from datetime import datetime
from models import Customer, CustomerDetail as CD, User
from customer.customer_schema import CustomerCreate, CustomerUpdate
from sqlalchemy.orm import Session
from sqlalchemy import func
from user import user_schema
from datetime import datetime
from pytz import timezone


def get_customer_list(db: Session, skip: int = 0, limit: int = 10, keyword: str = '', userid: int = 0, order: str = 'create_date-desc',
                      startdate: datetime = datetime.now(timezone('Asia/Seoul')), enddate: datetime = datetime.now(timezone('Asia/Seoul'))):

    if (userid > 0):
        subquery = db.query(Customer.id).filter(
            Customer.user_id == userid).subquery()
    else:
        subquery = db.query(Customer.id).subquery()

    customer_list = db.query(func.max(CD.id).label(
        'id')).filter(CD.customer_id == subquery.c.id).group_by(CD.customer_id).subquery()

    sub = db.query(subquery.c.id, CD.id.label('customerid'),
                   CD.phonenumber,
                   CD.create_date, CD.body, CD.user_id,
                   ).outerjoin(CD).join(customer_list, CD.id == customer_list.c.id).subquery()

    order_dict = {'id-asc': sub.c.id, 'id-desc': sub.c.id.desc(),
                  'create_date-asc': sub.c.create_date, 'create_date-desc': sub.c.create_date.desc()}

    customer_list = db.query(sub.c.id, sub.c.customerid,
                             sub.c.body, sub.c.phonenumber,
                             sub.c.create_date, User.name
                             ).join(User, sub.c.user_id == User.id).filter(sub.c.create_date >= startdate.astimezone(timezone('Asia/Seoul')),
                                                                           sub.c.create_date <= enddate.astimezone(timezone('Asia/Seoul'))).order_by(order_dict[order])

    if (keyword):
        keyword = keyword.split(' ')
        for keyword in keyword:
            search = f'%%{keyword}%%'
            customer_list = customer_list.filter(
                sub.c.phonenumber.ilike(search) | User.name.ilike(search))

    result = customer_list.offset(skip).limit(limit).all()
    total = customer_list.count()

    return total, result


def get_customer(db: Session, customer_id: int):
    customer = db.query(Customer).get(customer_id)
    return customer


def del_get_customer_list(db: Session, customer_idlist: list):
    customer_list = []
    for i in customer_idlist:
        customer_list.append(db.query(Customer).get(i.customer_id))
    return customer_list


def create_customer(db: Session, customercreate: CustomerCreate, user: user_schema.User):
    create_date = datetime.now()
    db_customer = Customer(
        create_date=create_date, user=user)
    db.add(db_customer)
    db.commit()
    customer = db.query(Customer).filter(
        Customer.user_id == user.id).order_by(Customer.id.desc()).first()
    db_customerdetail = CD(
        name=customercreate.name, body=customercreate.body,
        phonenumber=customercreate.phonenumber, address=customercreate.address,
        addressdetail=customercreate.addressdetail, create_date=create_date, customer_id=customer.id, user=user)
    db.add(db_customerdetail)
    db.commit()

    return customer


def update_customer(db: Session, db_customer: Customer, customer_update: CustomerUpdate):
    db_customer.subject = customer_update.subject
    db_customer.content = customer_update.content
    db_customer.modify_date = datetime.now()
    db.add(db_customer)
    db.commit()


def delete_customer(db: Session, db_customer: list[Customer]):
    for i in db_customer:
        db.delete(i)
    db.commit()
