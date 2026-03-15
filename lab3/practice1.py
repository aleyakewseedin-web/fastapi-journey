from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()

books = [
    {"id": 1, "title": "1984", "author": "George Orwell", "year": 1949},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925}
]


class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int

@app.get("/books/{books_id}", response_model=Book)
async def read_book(books_id: int):
     for book in books:
        if book["id"] == books_id:
            return book
     raise HTTPException(status_code=404, detail="Book not found")