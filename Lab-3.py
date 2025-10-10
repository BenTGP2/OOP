class Book:
    def __init__(self):
        self.title = ""
        self.author_id = ""
        self.publish_date = ""
        self.book_id = ""
        self.publisher = ""

    def add_book(self):
        self.title = input("Enter the title of the book: ")
        self.author_id = input("Enter the author ID: ")
        self.publish_date = input("Enter the publish date: ")
        self.book_id = input("Enter the book ID: ")
        self.publisher = input("Enter the publisher: ")

    def book_information(self):
        print("The title of the book is", self.title)
        print("The ID of the book is", self.book_id)
        print("The author of the book is", self.author_id)
        print("The publish date of the book is", self.publish_date)
        print("The publisher of the book is", self.publisher)

class Author:
    def __init__(self):
        self.author_id = ""
        self.name = ""
        self.affiliation = ""
        self.country = ""
        self.phone = ""
        self.email = ""

    def add_author(self):
        self.author_id = input("Enter the author ID: ")
        self.name = input("Enter the name of the author: ")
        self.affiliation = input("Enter affiliation: ")
        self.country = input("Enter country: ")
        self.phone = input("Enter phone: ")
        self.email = input("Enter email: ")

    def author_information(self):
        print("The name of the author is", self.name)
        print("The ID of the author is", self.author_id)
        print("The affiliation of the author is", self.affiliation)
        print("The country of the author is", self.country)
        print("The phone of the author is", self.phone)
        print("The email of the author is", self.email)

class User:
    def __init__(self):
        self.user_id = ""
        self.password = ""
        self.address = ""
        self.phone = ""
        self.email = ""
        self.books_borrowed = []

    def add_user(self):
        self.user_id = input("Enter the user ID: ")
        self.password = input("Enter password: ")
        self.address = input("Enter address: ")
        self.phone = input("Enter phone: ")
        self.email = input("Enter email: ")

    def user_information(self):
        print("The name of the user is", self.user_id)
        print("The password of the user is", self.password)
        print("The address of the user is", self.address)
        print("The phone of the user is", self.phone)
        print("The email of the user is", self.email)

    def checkout_book(self, book1):
        self.books_borrowed.append(book1)

while True:
    print("1. Display book information")
    print("2. Display author's information")
    print("3. Display user's information")
    print("4. Checkout a book")
    print("5. Register a book")
    print("6. Register an author")
    print("7. Register a user")
    print("8. Terminate program")

    book = Book()
    author = Author()
    user = User()

    Input = input("Enter your selection:")
    if Input == "1":
        book.book_information()
    elif Input == "2":
        author.author_information()
    elif Input == "3":
        user.user_information()
    elif Input == "4":
        user.checkout_book(book)
    elif Input == "5":
        book.add_book()
    elif Input == "6":
        author.add_author()
    elif Input == "7":
        user.add_user()
    elif Input == "8":
        print("Terminating program...")
        break
