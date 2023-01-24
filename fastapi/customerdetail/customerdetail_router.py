from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from customerdetail import customerdetail_schema, customerdetail_crud
from customer import customer_crud, customer_schema
from user.user_router import get_current_user
from models import User

router = APIRouter(
    prefix='/api/customerdetail',
)


@router.post("/customerdetail_create/{customer_id}", response_model=customerdetail_schema.CustomerDetail)
def customerdetail(customer_id: int, _customerdetail_create: customerdetail_schema.CustomerDetailCreate,
                   db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    customer = customer_crud.get_customer(db, customer_id=customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Question not found")
    customerdetail = customerdetail_crud.create_customerdetail(db, customer=customer,
                                                               customerdetail=_customerdetail_create, user=current_user)
    return customerdetail


@router.get("/detail/{customerdetail_id}", response_model=customerdetail_schema.CustomerDetail)
def customerdetail(customerdetail_id: int, db: Session = Depends(get_db)):
    customerdetail = customerdetail_crud.get_customerdetail(
        db, customerdetail_id=customerdetail_id)
    return customerdetail


@router.get("/customer/customerdetail/{customer_id}", response_model=customerdetail_schema.CustomerDetailList)
def customerdetail(customer_id: int, db: Session = Depends(get_db)):
    total, customerdetails = customerdetail_crud.customer_customerdetail(
        db, customer_id=customer_id)
    return {'total': total, 'customer_list': customerdetails}


@router.put("/update", status_code=status.HTTP_204_NO_CONTENT)
def customerdetail_update(_customerdetail_update: customerdetail_schema.CustomerDetailUpdate,
                          db: Session = Depends(get_db),
                          current_user: User = Depends(get_current_user)):
    db_customerdetail = customerdetail_crud.get_customerdetail(
        db, customerdetail_id=_customerdetail_update.customerdetail_id)
    if not db_customerdetail:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을수 없습니다.")
    if current_user.id != db_customerdetail.user.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="삭제 권한이 없습니다.")
    customerdetail_crud.update_customerdetail(db=db, db_customerdetail=db_customerdetail,
                                              customerdetail_update=_customerdetail_update)


@router.delete("/delete", status_code=status.HTTP_204_NO_CONTENT)
def customerdetail_delete(_customerdetail_delete: customerdetail_schema.CustomerDetailDelete, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_customerdetail = customerdetail_crud.get_customerdetail(
        db, customerdetail_id=_customerdetail_delete.id)
    if not db_customerdetail:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="데이터를 찾을수 없습니다.")
    if current_user.id != db_customerdetail.user.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="삭제 권한이 없습니다.")
    customerdetail_crud.delete_customerdetail(
        db=db, db_answer=db_customerdetail)
