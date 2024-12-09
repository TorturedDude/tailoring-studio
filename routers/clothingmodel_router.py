from http.client import HTTPException
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, defer
from starlette import status

from models.models import ClothingModel
from models.schemas.clothingmodel_schemas import ClothingModelWithDetails, ClothingModelCreate, ClothingModelResponse
from routers.db_session import get_db

router = APIRouter()


@router.get("/clothes", response_model=list[ClothingModelWithDetails])
async def get_all_clothes(db: Session = Depends(get_db)):
    return db.query(ClothingModel).all()


@router.post("/clothes", response_model=ClothingModelResponse)
async def create_cloth(cloth: ClothingModelCreate, db: Session = Depends(get_db)):
    new_cloth = ClothingModel(
        name=cloth.name,
        description=cloth.description,
        price=cloth.price,
        color=cloth.color,
        size=cloth.size
    )

    db.add(new_cloth)
    db.commit()
    db.refresh()

    return new_cloth
