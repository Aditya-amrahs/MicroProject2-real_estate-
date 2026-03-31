from sqlalchemy.orm import Session
from app import models


def create_favorite(db: Session, user_id: int, property_id: int):
    favorite = models.Favorite(user_id=user_id, property_id=property_id)

    db.add(favorite)
    db.commit()
    db.refresh(favorite)

    return favorite


def create_inquiry(db: Session, inquiry):
    new_inquiry = models.Inquiry(
        user_id=inquiry.user_id,
        property_id=inquiry.property_id,
        message=inquiry.message,
    )

    db.add(new_inquiry)
    db.commit()
    db.refresh(new_inquiry)

    return new_inquiry


# Auth
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def verify_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if user and user.password == password:
        return user
    return None


# Property CRUD
def create_property(db: Session, property_data):

    # validation to prevent creating property with zero or negative price
    if property_data.price <= 0:
        raise Exception("Price must be positive")

    # validation before creating property
    agent = (
        db.query(models.Agent).filter(models.Agent.id == property_data.agent_id).first()
    )
    if not agent:
        raise Exception("Invalid agent_id")
    #

    new_property = models.Property(**property_data.dict())
    db.add(new_property)
    db.commit()
    db.refresh(new_property)
    return new_property


def get_properties(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Property).offset(skip).limit(limit).all()


def get_property_by_id(db: Session, property_id: int):
    return db.query(models.Property).filter(models.Property.id == property_id).first()


def update_property(db: Session, property_id: int, updates):
    prop = get_property_by_id(db, property_id)
    if not prop:
        return None

    for key, value in updates.dict(exclude_unset=True).items():
        setattr(prop, key, value)

    db.commit()
    db.refresh(prop)
    return prop


def delete_property(db: Session, property_id: int):
    prop = get_property_by_id(db, property_id)
    if not prop:
        return None

    db.delete(prop)
    db.commit()
    return prop


# Search and filter properties
def search_properties(db: Session, city=None, min_price=None, max_price=None):
    query = db.query(models.Property)

    if city:
        query = query.filter(models.Property.city == city)

    if min_price is not None:
        query = query.filter(models.Property.price >= min_price)

    if max_price is not None:
        query = query.filter(models.Property.price <= max_price)

    return query.all()
