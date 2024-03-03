from fastapi import APIRouter, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

router = APIRouter()


@router.post("/removeFromCard/{id}", response_description="Remove from card")
def list_courses(id: str, request: Request):
    
    # Validate ID
    if not isinstance(id, str):
        raise HTTPException(status_code=400, detail="Invalid ID format")

    # Logic to remove item from card using the ID
    try:
        # Replace with your actual removal logic
        removed = request.app.remove_from_cards(id)  # Example database interaction
        if not removed:
            raise HTTPException(status_code=404, detail="Item not found")

        return {"success": True, "message": "Item removed successfully"}
    except Exception as e:
        # Handle other exceptions gracefully
        raise HTTPException(status_code=500, detail="Internal server errorrr")