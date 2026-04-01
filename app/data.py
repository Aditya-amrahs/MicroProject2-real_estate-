# app/data.py

from sqlalchemy.orm import Session
from app import models
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


def data(db: Session):

    # so that no duplicate data is created when the app restarts
    if db.query(models.User).first():
        db.close()
        return  # Data already exists, skip seeding the database

    # ---------- USERS ----------
    if db.query(models.User).count() == 0:
        users = [
            models.User(name="urvi", email="test@test.com", password="1234"),
            models.User(name="Adi", email="api@api.com", password="1234"),
        ]
        db.add_all(users)
        db.commit()

    # ---------- AGENTS ----------
    if db.query(models.Agent).count() == 0:
        agents = [
            models.Agent(name="Test Agent A", contact="9999999999", user_id=1),
            models.Agent(name="Test Agent B", contact="9888999999", user_id=2),
        ]
        db.add_all(agents)
        db.commit()

    # ---------- PROPERTIES ----------
    if db.query(models.Property).count() == 0:
        properties = [
            models.Property(
                title="Luxury Villa",
                price=750000,
                city="Delhi",
                agent_id=1,
            ),
            models.Property(
                title="Modern Apartment",
                price=450000,
                city="Mumbai",
                agent_id=2,
            ),
            models.Property(
                title="Beach House",
                price=950000,
                city="Goa",
                agent_id=2,
            ),
            models.Property(
                title="City Flat",
                price=350000,
                city="Bangalore",
                agent_id=1,
            ),
            models.Property(
                title="House",
                price=1200000,
                city="Noida",
                agent_id=2,
            ),
        ]
        db.add_all(properties)
        db.commit()

    # ---------- PROPERTY IMAGES ----------
    if db.query(models.PropertyImage).count() == 0:
        images = [
            models.PropertyImage(
                property_id=1,
                image_url="https://images.pexels.com/photos/28449020/pexels-photo-28449020.jpeg",
            ),
            models.PropertyImage(
                property_id=3,
                image_url="https://images.pexels.com/photos/14384535/pexels-photo-14384535.jpeg",
            ),
            models.PropertyImage(
                property_id=2,
                image_url="https://images.pexels.com/photos/14043284/pexels-photo-14043284.jpeg",
            ),
        ]
        db.add_all(images)
        db.commit()

    # ---------- FAVORITES ----------
    if db.query(models.Favorite).count() == 0:
        favorites = [
            models.Favorite(user_id=1, property_id=1),
            models.Favorite(user_id=2, property_id=2),
        ]
        db.add_all(favorites)
        db.commit()

    # ---------- INQUIRIES ----------
    if db.query(models.Inquiry).count() == 0:
        inquiries = [
            models.Inquiry(
                user_id=1, property_id=1, message="Interested in this property"
            ),
            models.Inquiry(user_id=2, property_id=3, message="Need more details"),
        ]
        db.add_all(inquiries)
        db.commit()
