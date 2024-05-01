from fastapi import APIRouter, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

router = APIRouter()


@router.post("/addToCard", response_description="Add to card")
def add_to_card(id: str, request: Request):
    
    # Validate ID
    if not isinstance(id, str):
        raise HTTPException(status_code=400, detail="Invalid ID format")

    # Logic to remove item from card using the ID
    try:
        # Replace with your actual removal logic
        added = request.app.add_to_card(id)  # Example database interaction
        if not added:
            raise HTTPException(status_code=404, detail="Item not found")

        return {"success": True, "message": "Item added successfully"}
    except Exception as e:
        # Handle other exceptions gracefully
        raise HTTPException(status_code=500, detail="Internal server errorrr")