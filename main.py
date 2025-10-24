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


######################
# FUNCTIONS FOR MENU #
######################



##########################
# MAIN PROGRAM EXECUTION #
##########################

if __name__ == "__main__":
    
    while(True):

        # Main menu

        print("""Welcome to the Library Management System
          1. List all books
          2. List all available books
          3. Add a book
          4. Remove a book
          5. Reserve a book
          0. Exit""")
        
        option = int(input("Choose your option: "))
        
        match option:
            case 0:     # Exit program
                break
            case 1:     # List all books
                pass
            case 2:     # List all available books
                pass
            case 3:     # Add a book
                pass
            case 4:     # Remove a book
                pass
            case 5:     # Reserve a book
                pass
            case _:     # Invalid option
                print("Invalid option. Please try again.")




Book("yes i am", "me and myself", 149053143)
Library.listAllBooks()