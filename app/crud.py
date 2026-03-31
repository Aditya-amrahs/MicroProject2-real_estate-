from sqlalchemy.orm import Session
from . import models
def create_favorite(db: Session, user_id: int, property_id: int):
    favorite = models.Favorite(
        user_id=user_id,
        property_id=property_id
    )

    db.add(favorite)
    db.commit()
    db.refresh(favorite)

    return favorite

def create_inquiry(db: Session, inquiry):
    new_inquiry = models.Inquiry(
        user_id=inquiry.user_id,
        property_id=inquiry.property_id,
        message=inquiry.message
    )

    db.add(new_inquiry)
    db.commit()
    db.refresh(new_inquiry)

    return new_inquiry