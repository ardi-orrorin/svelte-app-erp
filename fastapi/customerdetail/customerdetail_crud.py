from datetime import datetime

from sqlalchemy.orm import Session

from customerdetail.customerdetail_schema import CustomerDetailCreate, CustomerDetailUpdate

from models import Customer, CustomerDetail, User


def create_customerdetail(db: Session, customer: Customer, customerdetail: CustomerDetailCreate, user: User):
    db_customerdetail = CustomerDetail(
        customer_id=customer.id,
        name=customerdetail.name,
        phonenumber=customerdetail.phonenumber,
        body=customerdetail.body,
        address=customerdetail.address,
        addressdetail=customerdetail.addressdetail,
        create_date=datetime.now(), user=user)
    db.add(db_customerdetail)
    db.commit()
    _customerdetail = db.query(CustomerDetail).filter(
        CustomerDetail.name == customerdetail.name and customer.id == CustomerDetail.customer_id).order_by(CustomerDetail.id.desc()).first()
    return _customerdetail


def get_customerdetail(db: Session, customerdetail_id: int):
    customerdetail = db.query(CustomerDetail).get(customerdetail_id)
    return customerdetail


def customer_customerdetail(db: Session, customer_id: int, order: str = 'create_date-desc'):
    customerdetails = db.query(CustomerDetail).filter(
        CustomerDetail.customer_id == customer_id)

    total = customerdetails.count()

    order_list = {'id-asc': CustomerDetail.id, 'id-desc': CustomerDetail.id.desc(), 'create_date-asc':
                  CustomerDetail.create_date, 'create_date-desc': CustomerDetail.create_date.desc()}
    customerdetails = customerdetails.order_by(order_list[order]).all()

    return total, customerdetails


def update_customerdetail(db: Session, db_customerdetail: CustomerDetail,
                          customerdetail_update: CustomerDetailUpdate):
    db_customerdetail.body = customerdetail_update.body
    db_customerdetail.create_date = datetime.now()
    db.add(db_customerdetail)
    db.commit()


def delete_customerdetail(db: Session, db_customerdetail: CustomerDetail):
    db.delete(db_customerdetail)
    db.commit()
