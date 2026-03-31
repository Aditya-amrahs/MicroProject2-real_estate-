from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, crud, models

router = APIRouter()

@router.post("/inquiries")
def send_inquiry(inquiry: schemas.InquiryCreate, db: Session = Depends(get_db)):

    property = db.query(models.Property).filter(
        models.Property.id == inquiry.property_id
    ).first()

    if not property:
        raise HTTPException(status_code=404, detail="Property not found")

    return crud.create_inquiry(db, inquiry)