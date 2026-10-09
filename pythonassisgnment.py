library = []

def add_book(book):
    library.append(book)

def unique_categories():
    categories = {book["category"] for book in library}
    return categories

def find_by_title(title):
    return [book for book in library
            if book["title"].lower() == title.lower()]

def update_book(book_id, **updates):
    for book in library:
        if book["book_id"] == book_id:
            book.update(updates)
            return True
    return False

def count_available():
    return sum(book["available"] for book in library)

def find_by_author(author):
    return [book for book in library
            if book["author"].lower() == author.lower()]

def sort_books():
    return sorted(library, key=lambda book: book["title"].lower())

def delete_book(book_id):
    for book in library:
        if book["book_id"] == book_id:
            library.remove(book)
            return True
    return False

# Sample records
add_book({
    "book_id": "B1042",
    "title": "Python Programming",
    "author": "John Smith",
    "publisher": "Tech Books",
    "category": "Programming",
    "available": True,
    "price": 450,
    "shelf_number": "A12"
})

add_book({
    "book_id": "B1043",
    "title": "Data Structures",
    "author": "Jane Doe",
    "publisher": "Academic Press",
    "category": "Programming",
    "available": True,
    "price": 520,
    "shelf_number": "A13"
})

print("Books:", library)
print("Unique categories:", unique_categories())
print("Search result:", find_by_title("Python Programming"))
print("Available books:", count_available())
print("Author search:", find_by_author("John Smith"))
print("Sorted books:", sort_books())