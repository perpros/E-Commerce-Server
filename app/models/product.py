import uuid
from pydantic import BaseModel, Field
from datetime import datetime


class Product(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    price: float = Field(...)
    color: str = Field(...)
    size: int = Field(...)
    image: str = Field(...)
    created_at:  datetime = Field(default_factory=datetime.now)
    updated_at:  datetime = Field(default_factory=datetime.now)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "name": "name",
                "price": "price",
                "color": "color",
                "size": "size",
                "image": "image url",
            }
        }

class Productisplay(BaseModel):
    _id: str
    name: str
    price: float
    color: str
    size: int
    image: str
    created_at:  datetime
    updated_at:  datetime