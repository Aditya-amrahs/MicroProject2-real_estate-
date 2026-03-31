from fastapi import FastAPI
from app.database import engine
from app import models
from app.routes import auth
from app.routes import favorites
from app.routes import inquiries
import uvicorn

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

# adding routes
app.include_router(auth.router)
app.include_router(favorites.router)
app.include_router(inquiries.router)


@app.get("/")
def home():
    return {"message": "Real Estate API Running"}
