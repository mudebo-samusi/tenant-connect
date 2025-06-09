from sqlalchemy import Boolean, Column, Integer, String, Float, ForeignKey, Enum, Text
from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.orm import relationship
import enum
from ..database import Base

class PropertyType(str, enum.Enum):
    APARTMENT = "apartment"
    HOUSE = "house"
    VILLA = "villa"
    COMMERCIAL = "commercial"
    LAND = "land"

class PropertyStatus(str, enum.Enum):
    AVAILABLE = "available"
    RENTED = "rented"
    PENDING = "pending"
    MAINTENANCE = "maintenance"

class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    property_type = Column(Enum(PropertyType), nullable=False)
    status = Column(Enum(PropertyStatus), default=PropertyStatus.AVAILABLE)
    
    # Location
    address = Column(String, nullable=False)
    city = Column(String, nullable=False)
    district = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    
    # Details
    bedrooms = Column(Integer)
    bathrooms = Column(Integer)
    area = Column(Float)  # in square meters
    price = Column(Float, nullable=False)  # in UGX
    currency = Column(String, default="UGX")
    
    # Features
    is_furnished = Column(Boolean, default=False)
    has_parking = Column(Boolean, default=False)
    has_security = Column(Boolean, default=False)
    has_water = Column(Boolean, default=True)
    has_electricity = Column(Boolean, default=True)
    
    # Relationships
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    owner = relationship("User", back_populates="properties")
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now()) 