from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from customer import customer_router
from customerdetail import customerdetail_router
from user import user_router
from noticefile import notice__router
from payment import payment_router
from statistics_anal import statistics_router
from rediscache import redis_router
import check_router
from database import DWORIGIN


app = FastAPI()

origins = DWORIGIN


app.add_middleware(CORSMiddleware, allow_origins=origins,
                   allow_credentials=False, allow_methods=['*'], allow_headers=['*'])


app.include_router(customer_router.router)
app.include_router(customerdetail_router.router)
app.include_router(user_router.router)
app.include_router(notice__router.router)
app.include_router(payment_router.router)
app.include_router(statistics_router.router)
app.include_router(redis_router.router)
app.include_router(check_router.router)
