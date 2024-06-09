from fastapi import FastAPI, HTTPException, Body
from typing import Optional
app = FastAPI()


BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]
'''
BOOKS = {
    'book_1':{'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    'book_2':{'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    'book_3':{'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    'book_4':{'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    'book_5':{'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    'book_6':{'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
}
'''

@app.get("/")
async def first_api():
    return {"message":"Hello Eric!"}

@app.get("/books")
async def read_all_books():
    return BOOKS

'''
@app.get("/books/{book_id}")
async def read_book_id(book_id: int):
    print('book_id: ', book_id)
    return {"id": book_id}
'''

@app.get("/books/{book_title}")
async def read_book(book_title: str):

    print(book_title)
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

    raise HTTPException(status_code=404, detail=f"Book with {book_title=} does not exist.") 



#Query Parameters
@app.get("/books/readAll")
async def read_all_books(skip_book: Optional[str]=None):

    if skip_book:
        new_books = BOOKS.copy()
        del new_books[skip_book]
        return new_books
    
    return BOOKS


#Query Parameters
@app.post("/books/newBook")
async def add_new_book():

    book_len = BOOKS.__len__()
    
    BOOKS['book_'+str(book_len+1)]={'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}

    return BOOKS


#PUT
@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book


#DELETE
@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break