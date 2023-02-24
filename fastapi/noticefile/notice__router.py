from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from datetime import datetime, timedelta
from database import get_db
from models import User
from . import notice__crud, notice__schema
from user.user_router import get_current_user
from pytz import timezone


router = APIRouter(prefix='/api/notice')


@router.get('/list', response_model=notice__schema.NoticeList)
def notice_list(db: Session = Depends(get_db), page: int = 0, size: int = 10,
                keyword: str = '', order: str = 'id-desc',
                startdate: datetime = datetime.now(
        timezone('Asia/Seoul'))-timedelta(weeks=10),
        enddate: datetime = datetime.now(timezone('Asia/Seoul'))):
    total, _notice_list = notice__crud.get_notice_list(
        db, skip=page*size, limit=size, keyword=keyword, order=order, startdate=startdate, enddate=enddate)

    return {'total': total, 'list': _notice_list}


@router.get("/list/detail/{notice_id}", response_model=notice__schema.Notice)
def notice_detail(notice_id: int, db: Session = Depends(get_db)):
    notice = notice__crud.get_notice(db, notice_id=notice_id)
    return notice


@router.post("/create", response_model=notice__schema.Notice)
def notice_create(_notice_create: notice__schema.NoticeCreate, db: Session = Depends(get_db),  current_user: User = Depends(get_current_user)):
    result = notice__crud.create_notice(
        db=db, noticecreate=_notice_create,  user=current_user)
    return result


@ router.put('/update', status_code=status.HTTP_204_NO_CONTENT)
def notice_update(_notice_update: notice__schema.NoticeUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_notice = notice__crud.get_notice(
        db, notice_id=_notice_update.id)
    if not db_notice:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='데이터를 찾을 수 없습니다.')
    if current_user.id != db_notice.user_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='수정 권한이 없습니다')

    result = notice__crud.update_notice(
        db=db, db_notice=db_notice, notice_update=_notice_update)


@ router.delete("/delete", status_code=status.HTTP_204_NO_CONTENT)
def notice_delete(_notice_delete: notice__schema.NoticeDeleteList,
                  db: Session = Depends(get_db),
                  current_user: User = Depends(get_current_user)):
    db_notice = notice__crud.del_get_notice_list(
        db, notice_idlist=_notice_delete.notice_idlist)

    if not db_notice:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을수 없습니다.")
    del_db = [i for i in db_notice if current_user.id == i.user.id]

    notice__crud.delete_notice(db=db, db_notice=del_db)
