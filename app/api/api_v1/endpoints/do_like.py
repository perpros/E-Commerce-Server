from fastapi import APIRouter, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

router = APIRouter()

@router.get("/doLike", response_description="Do like")
def list_courses(request: Request):
    return {
        "success": True,
        "message": "Like successfully",
        # "error": {"code": "UNKNOWN_ERROR", "message": "unknown error"},
        "data": {},
    }
