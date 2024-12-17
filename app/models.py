from sqlalchemy import Column, Integer, String, Float
from app.database import Base

# Define the Book table model
class Book(Base):
    __tablename__ = "books"  # Table name in the database

    id = Column(Integer, primary_key=True, index=True)  # Auto-increment ID
    title = Column(String(255), nullable=False)  # Title of the book
    author = Column(String(255), nullable=False)  # Author of the book
    price = Column(Float, nullable=False)  # Price of the book
    description = Column(String(500), nullable=True)  # Description of the book