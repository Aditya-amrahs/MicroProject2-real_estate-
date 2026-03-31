from pydoc import text

from sqlalchemy import Column, Float, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)

    favorites = relationship("Favorite", back_populates="user")
    inquiries = relationship("Inquiry", back_populates="user")
    agent = relationship("Agent", back_populates="user", uselist=False)


class Agent(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    contact = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="agent")
    properties = relationship("Property", back_populates="agent")


class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    city = Column(String, index=True)
    price = Column(Float, nullable=False)
    agent_id = Column(Integer, ForeignKey("agents.id"))

    agent = relationship("Agent", back_populates="properties")
    images = relationship("PropertyImage", back_populates="property")
    favorites = relationship("Favorite", back_populates="property")
    inquiries = relationship("Inquiry", back_populates="property")


class PropertyImage(Base):
    __tablename__ = "property_images"

    id = Column(Integer, primary_key=True, index=True)
    property_id = Column(Integer, ForeignKey("properties.id"))
    image_url = Column(String, nullable=False)

    property = relationship("Property", back_populates="images")


class Favorite(Base):
    __tablename__ = "favorites"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    property_id = Column(Integer, ForeignKey("properties.id"))

    user = relationship("User", back_populates="favorites")
    property = relationship("Property", back_populates="favorites")


class Inquiry(Base):
    __tablename__ = "inquiries"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"))
    property_id = Column(Integer, ForeignKey("properties.id"))

    user = relationship("User", back_populates="inquiries")
    property = relationship("Property", back_populates="inquiries")
