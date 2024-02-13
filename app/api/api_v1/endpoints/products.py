from fastapi import APIRouter, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

router = APIRouter()

# @router.get('/products')
# def hello():
#     return 'hello products'

@router.get("/products", response_description="List all products")
def list_courses(request: Request):
    courses = list(request.app.products_list())
    return { 'count': len(courses),'products': courses}
