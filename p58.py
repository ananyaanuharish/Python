class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f'"{book_name}" has been added to the library.')

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("Available books:")
            for book in self.books:
                print(f"- {book}")

    def borrow_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f'You have borrowed "{book_name}".')
        else:
            print(f'Sorry, "{book_name}" is not available.')

    def return_book(self, book_name):
        self.books.append(book_name)
        print(f'Thank you for returning "{book_name}".')


# Example usage:
library = Library()

library.add_book("Python Basics")
library.add_book("Data Science with Python")
library.display_books()

library.borrow_book("Python Basics")
library.display_books()

library.return_book("Python Basics")
library.display_books()
