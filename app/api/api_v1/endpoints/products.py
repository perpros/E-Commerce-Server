from fastapi import APIRouter, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

router = APIRouter()

# @router.get('/products')
# def hello():
#     return 'hello products'


@router.get("/products", response_description="List all products")
def products(request: Request):
    courses = list(request.app.products_list())

    return {
        "success": True,
        "message": "List all products successfully",
        # "error": {"code": "UNKNOWN_ERROR", "message": "unknown error"},
        "data": {"count": len(courses), "products": courses},
    }
