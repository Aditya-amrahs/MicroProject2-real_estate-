from fastapi import FastAPI
from .database import engine
from . import models
from .routes import auth
from app.routes import favorites
from app.routes import inquiries

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#adding routes
app.include_router(auth.router)
app.include_router(favorites.router)
app.include_router(inquiries.router)

@app.get("/")
def home():
    return {"message": "Real Estate API Running"}



