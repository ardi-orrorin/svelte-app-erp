from fastapi import APIRouter
from starlette import status
import os
from pydantic import BaseModel


class test(BaseModel):
    result: str


router = APIRouter(prefix='/api')


@router.get('/check', status_code=status.HTTP_200_OK)
def check():
    pass


""" @router.get('/sql', response_model=test)
def sql():
    env = os.environ['SQL']
    return {'result': env} """
