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

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
            print(f"{book.title} is in the library.")

    def add_member(self, member):
        if member not in self.members:
            self.members.append(member)
            print(f"{member.name} is a member at the library.")

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def borrow_book(self, member_id, title):
        member = self.find_member(member_id)

        book = self.find_book(title)

        if member is None:
            print(f"{member_id} does not exists.")
            return

        if book is None:
            print(f"{title} does not exists.")
            return

        member.borrow_book(book)

    def return_book(self, member_id, title):
        member = self.find_member(member_id)

        book = self.find_book(title)

        if member is None:
            print(f"{member_id} does not exists.")
            return

        if book is None:
            print(f"{title} does not exists.")
            return

        member.return_book(book)





