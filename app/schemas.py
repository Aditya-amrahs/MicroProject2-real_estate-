from pydantic import BaseModel, Field
from typing import Optional, List


class FavoriteCreate(BaseModel):
    user_id: int
    property_id: int


class InquiryCreate(BaseModel):
    user_id: int
    property_id: int
    message: str = Field(..., min_length=5, max_length=500)


# Auth
class UserLogin(BaseModel):
    email: str
    password: str


# Property schemas
class PropertyBase(BaseModel):
    title: str
    city: str
    price: float
    agent_id: int


class PropertyCreate(PropertyBase):
    pass


class PropertyUpdate(BaseModel):
    title: Optional[str] = None
    city: Optional[str] = None
    price: Optional[float] = None


class PropertyOut(PropertyBase):
    id: int

    class Config:
        from_attributes = True


# Property Image schemas
class PropertyImageOut(BaseModel):
    id: int
    image_url: str

    class Config:
        from_attributes = True


# Agent schemas
class AgentOut(BaseModel):
    id: int
    name: str
    contact: Optional[str]

    class Config:
        from_attributes = True


# Property Details schema
class PropertyDetail(PropertyOut):
    agent: Optional[AgentOut]
    images: List[PropertyImageOut] = []

    class Config:
        from_attributes = True
