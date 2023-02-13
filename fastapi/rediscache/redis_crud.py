from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime
from pytz import timezone
import redis
import json

asiatimezone = timezone('Asia/Seoul')


def get_notice_list(db: Session, skip: int = 0, limit: int = 10, keyword: str = '', order: str = 'id-desc',
                    startdate: datetime = datetime.now(asiatimezone), enddate: datetime = datetime.now(asiatimezone)):

    return


if __name__ == "__main__":
    rd_pool = redis.ConnectionPool(host='192.168.0.49', port=6379, db=0)
    rdDB = redis.Redis(connection_pool=rd_pool)

    result = json.loads(
        rdDB.get('customerdetail').decode('utf-8'))

    result1 = len(rdDB.get('customerdetail'))

    print(result1)
