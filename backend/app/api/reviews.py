from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.review import Review
from app.schemas.review import ReviewCreate, Review as ReviewSchema, ReviewUpdate
from app.api.auth import get_current_user
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=ReviewSchema)
async def create_review(
    review: ReviewCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Check if user has already reviewed this property
    existing_review = db.query(Review).filter(
        Review.property_id == review.property_id,
        Review.reviewer_id == current_user.id
    ).first()
    
    if existing_review:
        raise HTTPException(status_code=400, detail="You have already reviewed this property")
    
    db_review = Review(
        property_id=review.property_id,
        reviewer_id=current_user.id,
        rating=review.rating,
        comment=review.comment
    )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

@router.get("/property/{property_id}", response_model=List[ReviewSchema])
async def get_property_reviews(
    property_id: int,
    db: Session = Depends(get_db)
):
    reviews = db.query(Review).filter(Review.property_id == property_id).all()
    return reviews

@router.put("/{review_id}", response_model=ReviewSchema)
async def update_review(
    review_id: int,
    review_update: ReviewUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    db_review = db.query(Review).filter(Review.id == review_id).first()
    if not db_review:
        raise HTTPException(status_code=404, detail="Review not found")
    
    if db_review.reviewer_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this review")
    
    for field, value in review_update.dict(exclude_unset=True).items():
        setattr(db_review, field, value)
    
    db.commit()
    db.refresh(db_review)
    return db_review

@router.delete("/{review_id}")
async def delete_review(
    review_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    db_review = db.query(Review).filter(Review.id == review_id).first()
    if not db_review:
        raise HTTPException(status_code=404, detail="Review not found")
    
    if db_review.reviewer_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this review")
    
    db.delete(db_review)
    db.commit()
    return {"message": "Review deleted successfully"} 