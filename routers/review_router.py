from http.client import HTTPException
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, defer
from starlette import status

from models.models import Review
from models.schemas.review_schemas import ReviewResponse, ReviewCreate
from routers.db_session import get_db

router = APIRouter()

@router.get("/review", response_model=list[ReviewResponse])
async def get_all_review(db: Session = Depends(get_db)):
    return db.query(Review).all()

@router.post("/review", response_model=ReviewResponse, status_code=status.HTTP_201_CREATED)
async def create_review(review: ReviewCreate, db: Session = Depends(get_db)):
    new_review = Review(
        user_id = review.user_id,
        cloth_name = review.cloth_name,
        rate = review.rate,
        description = review.description
    )

    db.add(new_review)
    db.commit()
    db.refresh()

    return new_review