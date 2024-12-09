from http.client import HTTPException
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, defer
from starlette import status

from models.models import ClothingModel
from models.schemas.clothingmodel_schemas import ClothingModelWithDetails
from routers.db_session import get_db

router = APIRouter()

@router.get("/clothes", response_model=ClothingModelWithDetails)
async def get_all_clothes(db: Session = Depends(get_db)):
    return db.query(ClothingModel).all()
