from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional

class OrderBase(BaseModel):
    user_id: int = Field(..., example=1)
    master_name: str = Field(..., example="Tailor John")
    cloth_name: str = Field(..., example="T-Shirt")
    status: str = Field(..., example="Создан")
    delivery: str = Field(..., example="Почта")

    class Config:
        orm_mode = True


class OrderCreate(OrderBase):
    """Схема для создания заказа."""
    pass


class OrderResponse(OrderBase):
    """Схема для возврата данных заказа."""
    id: int
    start_date: datetime
    update_date: datetime
