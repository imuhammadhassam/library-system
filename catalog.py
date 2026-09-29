# Library System Catalog

# This file contains library book information


books = [
    "Python Basics",
    "Data Science",
    "Clean Code"
]


def search_book(book_name):
    if book_name in books:
        return "Book Found"
    else:
        return "Book Not Found"


print(search_book("Python Basics"))