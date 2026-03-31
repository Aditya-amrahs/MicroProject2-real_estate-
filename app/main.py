from fastapi import FastAPI
from app.database import engine
from app import models
from app.routes import auth, properties
from app.routes import favorites
from app.routes import inquiries
import uvicorn

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Real Estate API",
    description="API for managing real estate properties, user authentication, favorites, and inquiries.",
    version="1.0.0",
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

# adding routes
app.include_router(auth.router)
app.include_router(favorites.router)
app.include_router(inquiries.router)
app.include_router(properties.router)


@app.get("/")
def home():
    return {"message": "Real Estate API Running"}
