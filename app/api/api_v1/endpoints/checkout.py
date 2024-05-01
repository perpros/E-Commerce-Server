from fastapi import APIRouter, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

router = APIRouter()


@router.get("/checkout", response_description="Do checkout")
def checkout(request: Request):
    
    # Logic to remove item from card using the ID
    try:
        # Replace with your actual removal logic
        removed = request.app.checkout()  # Example database interaction

        return {
            "success": True,
            "message": "Checkout successfully",
            # "error": {"code": "UNKNOWN_ERROR", "message": "unknown error"},
            "data": {},
        }
    except Exception as e:
        # Handle other exceptions gracefully
        raise HTTPException(status_code=500, detail="Internal server errorrr")
