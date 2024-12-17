from sqlalchemy.orm import Session
from app import models, schemas

# Create a new book
def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(
        title=book.title,
        author=book.author,
        price=book.price,
        description=book.description
    )
    db.add(db_book)  # Add the new book to the session
    db.commit()  # Commit the transaction
    db.refresh(db_book)  # Refresh the book object to get the generated ID
    return db_book

# Get a book by ID
def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

# Get all books
def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Book).offset(skip).limit(limit).all()

# Update a book by ID
def update_book(db: Session, book_id: int, book: schemas.BookCreate):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not db_book:
        return None
    db_book.title = book.title
    db_book.author = book.author
    db_book.price = book.price
    db_book.description = book.description
    db.commit()
    db.refresh(db_book)
    return db_book

# Delete a book by ID
def delete_book(db: Session, book_id: int):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not db_book:
        return None
    db.delete(db_book)
    db.commit()
    return db_book