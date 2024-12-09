from http.client import HTTPException
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from models.models import Master
from models.schemas.master_schemas import MasterResponse, MasterCreate, MasterWithOrders
from routers.db_session import get_db

router = APIRouter()

@router.get("/masters", response_model=MasterWithOrders)
async def get_all_masters(db: Session = Depends(get_db)):
    return db.query(Master).all()

@router.post("/masters", response_model=MasterResponse, status_code=status.HTTP_201_CREATED)
async def create_master(master: MasterCreate, db: Session = Depends(get_db)):
    existing_master = db.query(Master).filter(master.name == Master.name).first()
    if existing_master:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Master with this name already exists",
        )

    new_master = Master(
        name = master.name
    )

    db.add(new_master)
    db.commit()
    db.refresh(new_master)
    return new_master