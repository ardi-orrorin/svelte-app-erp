from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from datetime import datetime, timedelta
from database import get_db
from models import User
from . import payment_crud, payment_schema
from user.user_router import get_current_user
from pytz import timezone


router = APIRouter(prefix='/api/payment')


@router.get('/list', response_model=payment_schema.PaymentList)
def payment_list(db: Session = Depends(get_db), page: int = 0, size: int = 10,
                 keyword: str = '', authority: int = 0, userid: int = 0, order: str = 'create_date-desc',
                 startdate: datetime = datetime.now(
        timezone('Asia/Seoul'))-timedelta(weeks=10),
        enddate: datetime = datetime.now(timezone('Asia/Seoul'))):
    total, _payment_list = payment_crud.get_payment_list(
        db, skip=page*size, limit=size, keyword=keyword, authority=authority, order=order, startdate=startdate, enddate=enddate, userid=userid)

    return {'total': total, 'list': _payment_list}


@router.get("/list/detail/{payment_id}", response_model=payment_schema.PaymentDetail)
def payment_detail(payment_id: int, db: Session = Depends(get_db)):
    payment = payment_crud.get_payment(db, payment_id=payment_id)
    return payment


@router.post("/create", response_model=payment_schema.Payment)
def payment_create(_payment_create: payment_schema.PaymentCreate, db: Session = Depends(get_db),  current_user: User = Depends(get_current_user)):
    payment = payment_crud.create_payment(
        db=db, paymentcreate=_payment_create,  user=current_user)
    return payment


@ router.put('/update', status_code=status.HTTP_204_NO_CONTENT)
def payment_update(_payment_update: payment_schema.PaymentUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_payment = payment_crud.get_payment(
        db, payment_id=_payment_update.payment_id)
    if not db_payment:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='데이터를 찾을 수 없습니다.')
    if current_user.id != db_payment.user_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='수정 권한이 없습니다')

    result = payment_crud.update_payment(
        db=db, db_question=db_payment, payment_update=_payment_update)


@ router.delete("/delete", status_code=status.HTTP_204_NO_CONTENT)
def payment_delete(_payment_delete: payment_schema.PaymentDeleteList,
                   db: Session = Depends(get_db),
                   current_user: User = Depends(get_current_user)):
    db_payment = payment_crud.del_get_payment_list(
        db, payment_idlist=_payment_delete.payment_idlist)

    if not db_payment:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을수 없습니다.")
    del_db = [i for i in db_payment if current_user.id == i.user.id]

    payment_crud.delete_payment(db=db, db_payment=del_db)
