from fastapi import APIRouter
from database import get_db
from models import User
from . import redis_crud, redis_schema
from database import rdDB
import json
from datetime import datetime
import re


router = APIRouter(prefix='/api/sqlcache')


@router.get('/cache_customerdetail', response_model=redis_schema.CustomerDetailList)
def cache_customerdetail(skip: int = 0, page: int = 10):
    start = datetime.now()
    print(start)
    result = json.loads(
        rdDB.get('customerdetail').decode('utf-8'))

    end = datetime.now()
    print(end)
    print(end-start)

    return {'result': result[skip:skip+page]}


@router.get('/cache_name', response_model=redis_schema.NameList)
def cache_name(name: str = ''):
    result = rdDB.get('name').decode('utf-8').split(",")
    """ filter_result = [i for i in result if "test" in result] """
    filter_result = []
    if (len(name) >= 2):
        search = re.compile(rf'.*{name.lower()}.*')
        filter_result += list(
            filter(lambda item: search.search(item.lower()), result))

    else:
        filter_result = []
    return {'result': filter_result[0:10]}
