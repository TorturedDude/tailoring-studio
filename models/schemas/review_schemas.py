from pydantic import BaseModel, Field
from typing import Optional

class ReviewBase(BaseModel):
    user_id: int = Field(..., example=1)
    cloth_name: str = Field(..., example="T-Shirt")
    rate: int = Field(..., ge=1, le=5, example=5)
    description: str = Field(..., example="Very comfortable and fits perfectly!")
    img: Optional[str] = Field(None, example="url_to_image")

    class Config:
        from_attributes = True


class ReviewCreate(ReviewBase):
    """Схема для создания отзыва."""
    pass


class ReviewResponse(ReviewBase):
    """Схема для возврата данных отзыва."""
    id: int
