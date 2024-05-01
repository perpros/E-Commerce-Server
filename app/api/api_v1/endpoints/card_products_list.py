from fastapi import APIRouter, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

router = APIRouter()


@router.get("/cardProductsList", response_description="List all card's products")
def card_products_list(request: Request):
    courses = list(request.app.card_products_list())

    return {
        "success": True,
        "message": "List all products successfully",
        # "error": {"code": "UNKNOWN_ERROR", "message": "unknown error"},
        "data": {"count": len(courses), "products": courses},
    }
