from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from ...database import get_db
from ..schemas.property import Property, PropertyCreate, PropertyUpdate, PropertySearchParams
from ..models.user import User
from ..utils.auth import get_current_active_user
from ..services import property as property_service

router = APIRouter()

@router.post("/", response_model=Property)
def create_property(
    property_in: PropertyCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Create a new property listing.
    """
    if current_user.role != "property_owner":
        raise HTTPException(
            status_code=403,
            detail="Only property owners can create listings"
        )
    return property_service.create_property(db, property_in, current_user.id)

@router.get("/", response_model=List[Property])
def get_properties(
    skip: int = 0,
    limit: int = 100,
    property_type: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    city: Optional[str] = None,
    district: Optional[str] = None,
    bedrooms: Optional[int] = None,
    bathrooms: Optional[int] = None,
    is_furnished: Optional[bool] = None,
    has_parking: Optional[bool] = None,
    has_security: Optional[bool] = None,
    radius: Optional[float] = None,
    latitude: Optional[float] = None,
    longitude: Optional[float] = None,
    db: Session = Depends(get_db)
):
    """
    Get all properties with optional filters.
    """
    search_params = PropertySearchParams(
        property_type=property_type,
        min_price=min_price,
        max_price=max_price,
        city=city,
        district=district,
        bedrooms=bedrooms,
        bathrooms=bathrooms,
        is_furnished=is_furnished,
        has_parking=has_parking,
        has_security=has_security,
        radius=radius,
        latitude=latitude,
        longitude=longitude
    )
    return property_service.get_properties(db, skip, limit, search_params)

@router.get("/{property_id}", response_model=Property)
def get_property(
    property_id: int,
    db: Session = Depends(get_db)
):
    """
    Get a specific property by ID.
    """
    property = property_service.get_property(db, property_id)
    if not property:
        raise HTTPException(status_code=404, detail="Property not found")
    return property

@router.put("/{property_id}", response_model=Property)
def update_property(
    property_id: int,
    property_in: PropertyUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Update a property listing.
    """
    property = property_service.update_property(db, property_id, property_in, current_user.id)
    if not property:
        raise HTTPException(status_code=404, detail="Property not found")
    return property

@router.delete("/{property_id}")
def delete_property(
    property_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Delete a property listing.
    """
    success = property_service.delete_property(db, property_id, current_user.id)
    if not success:
        raise HTTPException(status_code=404, detail="Property not found")
    return {"message": "Property deleted successfully"}

@router.get("/owner/me", response_model=List[Property])
def get_my_properties(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Get all properties owned by the current user.
    """
    if current_user.role != "property_owner":
        raise HTTPException(
            status_code=403,
            detail="Only property owners can view their listings"
        )
    return property_service.get_owner_properties(db, current_user.id, skip, limit) 