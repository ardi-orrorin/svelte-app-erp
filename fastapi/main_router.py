from fastapi import APIRouter
from starlette import status


router = APIRouter(prefix='/api')


@router.get('/check', status_code=status.HTTP_200_OK)
def check():
    pass
