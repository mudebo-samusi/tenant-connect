from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from .user import User
from ..models.property import PropertyType, PropertyStatus

class PropertyBase(BaseModel):
    title: str
    description: Optional[str] = None
    property_type: PropertyType
    address: str
    city: str
    district: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    bedrooms: Optional[int] = None
    bathrooms: Optional[int] = None
    area: Optional[float] = None
    price: float
    currency: str = "UGX"
    is_furnished: bool = False
    has_parking: bool = False
    has_security: bool = False
    has_water: bool = True
    has_electricity: bool = True

class PropertyCreate(PropertyBase):
    pass

class PropertyUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    property_type: Optional[PropertyType] = None
    status: Optional[PropertyStatus] = None
    address: Optional[str] = None
    city: Optional[str] = None
    district: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    bedrooms: Optional[int] = None
    bathrooms: Optional[int] = None
    area: Optional[float] = None
    price: Optional[float] = None
    currency: Optional[str] = None
    is_furnished: Optional[bool] = None
    has_parking: Optional[bool] = None
    has_security: Optional[bool] = None
    has_water: Optional[bool] = None
    has_electricity: Optional[bool] = None

class PropertyInDBBase(PropertyBase):
    id: int
    status: PropertyStatus
    owner_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class Property(PropertyInDBBase):
    owner: User

class PropertySearchParams(BaseModel):
    property_type: Optional[PropertyType] = None
    min_price: Optional[float] = None
    max_price: Optional[float] = None
    city: Optional[str] = None
    district: Optional[str] = None
    bedrooms: Optional[int] = None
    bathrooms: Optional[int] = None
    is_furnished: Optional[bool] = None
    has_parking: Optional[bool] = None
    has_security: Optional[bool] = None
    radius: Optional[float] = None  # in kilometers
    latitude: Optional[float] = None
    longitude: Optional[float] = None 