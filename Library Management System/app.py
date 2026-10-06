class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"{self.title} has been borrowed.")
        else:
            print(f"{self.title} is not available")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} was not borrowed.")

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"{book.title} is not available")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned the book {book}")
        else:
            print(f"{self.name} does not have {book}")