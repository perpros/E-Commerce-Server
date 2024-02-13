import uuid
from pydantic import BaseModel, Field
from datetime import datetime


class Cart(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    products: list[str] = Field(default=None)
    created_at:  datetime = Field(default_factory=datetime.now)
    updated_at:  datetime = Field(default_factory=datetime.now)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "products": "products",
            }
        }

class Productisplay(BaseModel):
    _id: str
    products: list[str]