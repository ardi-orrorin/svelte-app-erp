from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime
from pytz import timezone

asiatimezone = timezone('Asia/Seoul')


def get_notice_list(db: Session, skip: int = 0, limit: int = 10, keyword: str = '', order: str = 'id-desc',
                    startdate: datetime = datetime.now(asiatimezone), enddate: datetime = datetime.now(asiatimezone)):

    return
