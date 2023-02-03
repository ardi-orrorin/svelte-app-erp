from fastapi import APIRouter
from database import get_db
from models import User
from . import redis_crud, redis_schema
from database import rdDB
import json


router = APIRouter(prefix='/api/sqlcache')


@router.get('/cache_customerdetail', response_model=redis_schema.CustomerDetailList)
def cache_customerdetail(skip: int = 0, page: int = 10):
    result = json.loads(
        rdDB.get('customerdetail').decode('utf-8'))

    return {'result': result[skip:skip+page]}
