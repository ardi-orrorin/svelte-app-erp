from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from datetime import datetime, timedelta
from database import get_db
from models import User
from . import customer_crud, customer_schema
from user.user_router import get_current_user
from pytz import timezone


router = APIRouter(prefix='/api/customer')


@router.get('/list', response_model=customer_schema.CustomerList)
def customer_list(db: Session = Depends(get_db), page: int = 0, size: int = 10,
                  keyword: str = '', userid: int = 0, order: str = 'create_date-desc',
                  startdate: datetime = datetime.now(
        timezone('Asia/Seoul'))-timedelta(weeks=10),
        enddate: datetime = datetime.now(timezone('Asia/Seoul'))):
    total, _customer_list = customer_crud.get_customer_list(
        db, skip=page*size, limit=size, keyword=keyword, order=order, startdate=startdate, enddate=enddate, userid=userid)

    return {'total': total, 'customer_list': _customer_list}


@router.get("/list/detail/{customer_id}", response_model=customer_schema.Customer)
def customer_detail(customer_id: int, db: Session = Depends(get_db)):
    customer = customer_crud.get_customer(db, customer_id=customer_id)
    return customer


@router.post("/create", response_model=customer_schema.Customer)
def customer_create(_customer_create: customer_schema.CustomerCreate, db: Session = Depends(get_db),  current_user: User = Depends(get_current_user)):
    customer = customer_crud.create_customer(
        db=db, customercreate=_customer_create,  user=current_user)
    return customer


@ router.put('/update', status_code=status.HTTP_204_NO_CONTENT)
def customer_update(_customer_update: customer_schema.CustomerUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_customer = customer_crud.get_customer(
        db, customer_id=_customer_update.customer_id)
    if not db_customer:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='데이터를 찾을 수 없습니다.')
    if current_user.id != db_customer.user_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='수정 권한이 없습니다')

    result = customer_crud.update_customer(
        db=db, db_question=db_customer, customer_update=_customer_update)


@ router.delete("/delete", status_code=status.HTTP_204_NO_CONTENT)
def customer_delete(_customer_delete: customer_schema.CustomerDeleteList,
                    db: Session = Depends(get_db),
                    current_user: User = Depends(get_current_user)):
    db_customer = customer_crud.del_get_customer_list(
        db, customer_idlist=_customer_delete.customer_idlist)

    if not db_customer:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을수 없습니다.")
    del_db = [i for i in db_customer if current_user.id == i.user.id]

    customer_crud.delete_customer(db=db, db_customer=del_db)
