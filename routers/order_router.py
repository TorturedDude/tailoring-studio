from http.client import HTTPException
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from models.models import Order
from models.schemas.order_schemas import OrderResponse, OrderCreate
from routers.db_session import get_db

router = APIRouter()

@router.get("/orders", response_model=OrderResponse)
async def get_all_orders(db: Session = Depends(get_db)):
    return db.query(Order).all()

@router.post("/orders", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
async def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    new_order = Order(
        user_id = order.user_id,
        master_name = order.master_name,
        cloth_name = order.cloth_name,
        status = order.status,
        delivery = order.delivery
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return new_order