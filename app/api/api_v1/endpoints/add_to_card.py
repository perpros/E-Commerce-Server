from fastapi import APIRouter, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

router = APIRouter()


@router.get("/addToCard", response_description="Add to card")
def list_courses(request: Request):
    return {
        "success": True,
        "message": "Add to card successfully",
        # "error": {"code": "UNKNOWN_ERROR", "message": "unknown error"},
        "data": {},
    }
