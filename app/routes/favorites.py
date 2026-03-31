from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, crud, models

router = APIRouter()

@router.post("/favorites")
def add_favorite(favorite: schemas.FavoriteCreate, db: Session = Depends(get_db)):

    # check property exists
    property = db.query(models.Property).filter(
        models.Property.id == favorite.property_id
    ).first()

    if not property:
        raise HTTPException(status_code=404, detail="Property not found")


    #check if already in favorites
    existing = db.query(models.Favorite).filter(
        models.Favorite.user_id == favorite.user_id,
        models.Favorite.property_id == favorite.property_id
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Already in favorites")


    # create favorite
    return crud.create_favorite(
        db,
        favorite.user_id,
        favorite.property_id
    )