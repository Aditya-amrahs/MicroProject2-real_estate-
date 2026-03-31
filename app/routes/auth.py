from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app import crud, schemas

router = APIRouter()


@router.post("/register")
def register(email: str, password: str, db: Session = Depends(get_db)):
    user = models.User(email=email, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = crud.verify_user(db, user.email, user.password)
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    return {
        "message": "Login successful",
        "user_id": db_user.id,
    }
