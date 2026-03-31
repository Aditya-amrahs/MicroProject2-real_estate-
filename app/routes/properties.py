from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app import schemas, crud
from app.database import get_db

router = APIRouter(prefix="/properties", tags=["Properties"])


# -------------------- CREATE --------------------
@router.post("/", response_model=schemas.PropertyOut)
def create_property(
    property_data: schemas.PropertyCreate, db: Session = Depends(get_db)
):
    return crud.create_property(db, property_data)


# -------------------- LIST (Task 8) --------------------
@router.get("/", response_model=List[schemas.PropertyOut])
def list_properties(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_properties(db, skip, limit)


# -------------------- DETAILS (Task 9) --------------------
@router.get("/{property_id}", response_model=schemas.PropertyDetail)
def get_property(property_id: int, db: Session = Depends(get_db)):
    prop = crud.get_property_by_id(db, property_id)

    if not prop:
        raise HTTPException(status_code=404, detail="Property not found")

    return prop


# -------------------- UPDATE --------------------
@router.put("/{property_id}", response_model=schemas.PropertyOut)
def update_property(
    property_id: int, updates: schemas.PropertyUpdate, db: Session = Depends(get_db)
):
    updated = crud.update_property(db, property_id, updates)

    if not updated:
        raise HTTPException(status_code=404, detail="Property not found")

    return updated


# -------------------- DELETE --------------------
@router.delete("/{property_id}")
def delete_property(property_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_property(db, property_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Property not found")

    return {"message": "Property deleted successfully"}


# -------------------- SEARCH (Task 10) --------------------
@router.get("/search/", response_model=List[schemas.PropertyOut])
def search_properties(
    city: Optional[str] = None,
    min_price: Optional[float] = Query(None),
    max_price: Optional[float] = Query(None),
    db: Session = Depends(get_db),
):
    return crud.search_properties(db, city, min_price, max_price)
