from pydantic import BaseModel, Field
class FavoriteCreate(BaseModel):
    user_id: int
    property_id: int

class InquiryCreate(BaseModel):
    user_id: int
    property_id: int
    message: str = Field(..., min_length=5, max_length=500)