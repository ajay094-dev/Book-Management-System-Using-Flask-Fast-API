from pydantic import BaseModel, Field
from typing import Optional

# Request schema for creating a book
class BookCreate(BaseModel):
    title: str = Field(..., max_length=255, description="Title of the book")
    author: str = Field(..., max_length=255, description="Author of the book")
    price: float = Field(..., gt=0, description="Price of the book")
    description: Optional[str] = Field(None, max_length=500, description="Description of the book")

# Response schema for retrieving a book
class BookResponse(BookCreate):
    id: int  # Auto-increment ID of the book

    class Config:
        orm_mode = True  # Allows ORM objects to be converted to Pydantic models