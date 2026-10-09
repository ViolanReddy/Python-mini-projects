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

def show_menu():
    print("\n==== Library Management System ====")
    print("1. Add Book")
    print("2. Add Member")
    print("3. View Books")
    print("4. View Members")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. Exit")

    library = Library()

while True:
    show_menu()
    library = Library()

    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Enter Book Title: ")
        author = input("Enter Author: ")
        isbn = input("Enter ISBN: ")

        book = Book(title, author, isbn)

        library.add_book(book)

    elif choice == "2":
        name = input("Enter Member Name: ")
        member_id = input("Enter Member ID: ")

        member = Member(name, member_id)

        library.add_member(member)

    elif choice == "3":
        print("\n==== BOOKS ====")
        for book in library.books:
            print(f"Title: {book.title}")
            print(f"Author: {book.auhtor}")
            print(f"ISBN: {book.isbn}")
            print(f"Available: {book.is_available}")
            print()

    elif choice == "4":
        print("\n==== LIBRARY MEMBERS ====")

        if not library.members:
            print("No members registered.")
        else:
            for member in library.members:
                print(f"Member Name: {member.name}")
                print(f"Member ID: {member.member_id}")

            if member.borrowed_books:
                for book in member.borrowed_books:
                    print(f"Borrowed Books: {book.title}")
            else:
                print(f"Borrowed Books: None")

            print()

    elif choice == "5":
        member_id = input("Enter member ID: ")
        title = input("Enter Book Title: ")

        library.borrow_book(member_id, title)