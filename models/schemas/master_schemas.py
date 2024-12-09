from typing import List

from pydantic import BaseModel, Field

from models.schemas.order_schemas import OrderResponse


class MasterBase(BaseModel):
    name: str = Field(..., example="Tailor John")

    class Config:
        from_attributes = True

class MasterCreate(BaseModel):
    """Схема для создания мастера"""
    pass

class MasterResponse(MasterBase):
    """Схема для возврата данных мастера."""
    pass

class MasterWithOrders(MasterResponse):
    orders: List[OrderResponse]
