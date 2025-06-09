from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from geoalchemy2.shape import from_shape
from shapely.geometry import Point
from ..models.property import Property, PropertyType, PropertyStatus
from ..schemas.property import PropertyCreate, PropertyUpdate, PropertySearchParams

def create_property(db: Session, property_in: PropertyCreate, owner_id: int) -> Property:
    db_property = Property(
        **property_in.model_dump(),
        owner_id=owner_id,
        status=PropertyStatus.AVAILABLE
    )
    db.add(db_property)
    db.commit()
    db.refresh(db_property)
    return db_property

def get_property(db: Session, property_id: int) -> Optional[Property]:
    return db.query(Property).filter(Property.id == property_id).first()

def get_properties(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    search_params: Optional[PropertySearchParams] = None
) -> List[Property]:
    query = db.query(Property)
    
    if search_params:
        filters = []
        
        if search_params.property_type:
            filters.append(Property.property_type == search_params.property_type)
        
        if search_params.min_price is not None:
            filters.append(Property.price >= search_params.min_price)
        
        if search_params.max_price is not None:
            filters.append(Property.price <= search_params.max_price)
        
        if search_params.city:
            filters.append(Property.city.ilike(f"%{search_params.city}%"))
        
        if search_params.district:
            filters.append(Property.district.ilike(f"%{search_params.district}%"))
        
        if search_params.bedrooms is not None:
            filters.append(Property.bedrooms == search_params.bedrooms)
        
        if search_params.bathrooms is not None:
            filters.append(Property.bathrooms == search_params.bathrooms)
        
        if search_params.is_furnished is not None:
            filters.append(Property.is_furnished == search_params.is_furnished)
        
        if search_params.has_parking is not None:
            filters.append(Property.has_parking == search_params.has_parking)
        
        if search_params.has_security is not None:
            filters.append(Property.has_security == search_params.has_security)
        
        # Geospatial search
        if all([search_params.latitude, search_params.longitude, search_params.radius]):
            point = Point(search_params.longitude, search_params.latitude)
            filters.append(
                Property.geom.ST_DWithin(
                    from_shape(point, srid=4326),
                    search_params.radius * 1000  # Convert km to meters
                )
            )
        
        if filters:
            query = query.filter(and_(*filters))
    
    return query.offset(skip).limit(limit).all()

def update_property(
    db: Session,
    property_id: int,
    property_in: PropertyUpdate,
    owner_id: int
) -> Optional[Property]:
    db_property = db.query(Property).filter(
        Property.id == property_id,
        Property.owner_id == owner_id
    ).first()
    
    if not db_property:
        return None
    
    update_data = property_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_property, field, value)
    
    db.add(db_property)
    db.commit()
    db.refresh(db_property)
    return db_property

def delete_property(db: Session, property_id: int, owner_id: int) -> bool:
    db_property = db.query(Property).filter(
        Property.id == property_id,
        Property.owner_id == owner_id
    ).first()
    
    if not db_property:
        return False
    
    db.delete(db_property)
    db.commit()
    return True

def get_owner_properties(
    db: Session,
    owner_id: int,
    skip: int = 0,
    limit: int = 100
) -> List[Property]:
    return db.query(Property)\
        .filter(Property.owner_id == owner_id)\
        .offset(skip)\
        .limit(limit)\
        .all() 