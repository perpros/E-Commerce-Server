from fastapi import APIRouter, Depends

router = APIRouter()

@router.get('/')
def hello():
    return 'hello world'