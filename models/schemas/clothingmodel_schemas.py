from pydantic import BaseModel, Field
from typing import Optional, List

from models.schemas.order_schemas import OrderResponse
from models.schemas.review_schemas import ReviewResponse


class ClothingModelBase(BaseModel):
    name: str = Field(..., example="T-Shirt")
    description: str = Field(..., example="A comfortable cotton t-shirt")
    price: int = Field(..., example=500)
    color: str = Field(..., example="white")
    average_rating: Optional[int] = Field(None, example=4)
    size: str = Field(..., example="M")
    img: Optional[str] = Field(None, example="url_to_image")

    class Config:
        from_attributes = True


class ClothingModelCreate(ClothingModelBase):
    """Схема для создания одежды."""
    pass


class ClothingModelResponse(ClothingModelBase):
    """Схема для возврата данных одежды."""
    pass

class ClothingModelWithDetails(ClothingModelResponse):
    reviews: List[ReviewResponse]
    orders: List[OrderResponse]