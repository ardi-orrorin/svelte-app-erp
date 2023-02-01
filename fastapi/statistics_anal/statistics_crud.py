from datetime import datetime
from models import Payment, User, CustomerDetail as CD

from sqlalchemy.orm import Session
from sqlalchemy import func
from user import user_schema
from datetime import datetime
from pytz import timezone


def statistics_bar_days(db: Session, day: datetime):

    result = db.query(CD.user_id, func.count(CD.user_id).label('usercount'), func.date(CD.create_date).label('date')).filter(
        func.date(CD.create_date) == func.date(day), CD.user_id <= 20).group_by(CD.user_id, func.date(CD.create_date)).limit(20).all()

    return result
