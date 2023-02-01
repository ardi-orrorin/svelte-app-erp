from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from datetime import datetime, timedelta
from database import get_db
from models import User
from . import statistics_crud, statistics_schema
from user.user_router import get_current_user


router = APIRouter(prefix='/api/statistics')


@router.get('/barone', response_model=statistics_schema.StatisticsBarOneList)
def payment_list(db: Session = Depends(get_db), day: datetime = datetime.now()):
    result = statistics_crud.statistics_bar_days(
        db, day=day)

    return {'stat': result}
