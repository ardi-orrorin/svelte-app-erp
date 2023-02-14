from datetime import datetime
from models import Notice
from .notice__schema import NoticeCreate, NoticeUpdate
from sqlalchemy.orm import Session
from sqlalchemy import func
from user import user_schema
from datetime import datetime
from pytz import timezone
import re

asiatimezone = timezone('Asia/Seoul')


def get_notice_list(db: Session, skip: int = 0, limit: int = 10, keyword: str = '', order: str = 'id-desc',
                    startdate: datetime = datetime.now(asiatimezone), enddate: datetime = datetime.now(asiatimezone)):

    notice_list = db.query(Notice).filter(Notice.create_date >= startdate.astimezone(
        asiatimezone), Notice.create_date <= enddate.astimezone(asiatimezone))

    if (keyword):
        important = re.compile(r'.*important.*')
        pin = re.compile(r'.*pin.*')

        if important.match(keyword):
            notice_list = notice_list.filter(
                Notice.important == 1)
        if pin.match(keyword):
            notice_list = notice_list.filter(
                Notice.pin == 1)
        keyword = keyword.split(' ')
        print(keyword)
        for keyword in keyword:
            if important.match(keyword) or pin.match(keyword):
                continue
            search = f'%%{keyword}%%'
            notice_list = notice_list.filter(
                Notice.body.like(search) | Notice.title.like(search))

    order_dict = {'id-asc': Notice.id, 'id-desc': Notice.id.desc(),
                  'create_date-asc': Notice.create_date, 'create_date-desc': Notice.create_date.desc()}
    result = notice_list.order_by(
        order_dict[order]).offset(skip).limit(limit).all()
    total = notice_list.count()

    return total, result


def get_notice(db: Session, notice_id: int):
    notice = db.query(Notice).get(notice_id)
    return notice


def del_get_notice_list(db: Session, notice_idlist: list):
    notice_list = []
    for i in notice_idlist:
        notice_list.append(db.query(Notice).get(i.id))
    return notice_list


def create_notice(db: Session, noticecreate: NoticeCreate, user: user_schema.User):
    create_date = datetime.now()
    db_notice = Notice(title=noticecreate.title, body=noticecreate.body, pin=noticecreate.pin,
                       important=noticecreate.important, create_date=create_date, user=user)
    db.add(db_notice)
    db.commit()
    result = db.query(Notice).filter(
        Notice.title == noticecreate.title, Notice.body == noticecreate.body).order_by(Notice.id.desc()).first()

    return result


def update_notice(db: Session, db_notice: Notice, notice_update: NoticeUpdate):
    db_notice.title = notice_update.title
    db_notice.body = notice_update.body
    db_notice.pin = notice_update.pin
    db_notice.important = notice_update.important
    db.add(db_notice)
    db.commit()


def delete_notice(db: Session, db_notice: list[Notice]):
    for i in db_notice:
        db.delete(i)
    db.commit()
