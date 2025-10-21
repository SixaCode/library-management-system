from abc import ABC, abstractmethod

class Book:
    
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
        Library.books.append(self)

    def __str__(self):
        return f"""TITLE: {self.title}
AUTHOR: {self.author}
ISBN: {self.isbn}
AVAILABLE: {self.available}"""

class User(ABC):
    pass

class Library:
    
    books = []

    @classmethod
    def listAllBooks(self):
        print("ALL LIBRARY BOOKS")
        print("===================================")
        for book in self.books:
            print(book)
            print("===================================")

    def listAllAvailableBooks(self):
        print("ALL AVAILABLE BOOKS")
        print("===================================")
        for book in self.books:
            if book.available == True:
                print(book)
                print("===================================")

# Main program execution
if __name__ == "__main__":

    # Main menu

    option = -1
    print("""Welcome to the Library Management System
          1. List all books
          2. List all available books
          3. Add a book
          4. Remove a book
          5. """)
    
    while(True):
        match option:
            case 0:
                
                break




Book("yes i am", "me and myself", 149053143)
Library.listAllBooks()