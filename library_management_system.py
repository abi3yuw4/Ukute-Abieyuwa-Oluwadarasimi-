class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")

    def register_member(self, member):
        self.members.append(member)
        print("Member registered successfully.")

    def borrow_book(self, member_id, book_id):
        for member in self.members:
            if member.member_id == member_id:
                for book in self.books:
                    if book.book_id == book_id and book.is_available:
                        book.is_available = False
                        member.borrowed_books.append(book)
                        print("Book borrowed successfully.")
                        return
        print("Book not available or member not found.")

    def return_book(self, member_id, book_id):
        for member in self.members:
            if member.member_id == member_id:
                for book in member.borrowed_books:
                    if book.book_id == book_id:
                        book.is_available = True
                        member.borrowed_books.remove(book)
                        print("Book returned successfully.")
                        return
        print("Invalid return operation.")

    def display_books(self):
        for book in self.books:
            status = "Available" if book.is_available else "Borrowed"
            print(book.book_id, book.title, book.author, status)


# Main Program
library = Library()

library.add_book(Book(1, "Python Basics", "John Doe"))
library.add_book(Book(2, "Software Engineering", "Ian Sommerville"))

library.register_member(Member(101, "Alice"))
library.register_member(Member(102, "Bob"))

library.display_books()
library.borrow_book(101, 1)
library.display_books()
library.return_book(101, 1)
library.display_books()
