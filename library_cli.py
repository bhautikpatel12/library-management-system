
# library_cli.py
class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, name, author, qty):
        self.books[book_id] = {"name": name, "author": author, "qty": qty}

    def view_books(self):
        for bid, info in self.books.items():
            print(bid, info)

    def issue_book(self, book_id):
        if book_id in self.books and self.books[book_id]["qty"] > 0:
            self.books[book_id]["qty"] -= 1
            print("Book Issued")
        else:
            print("Book Not Available")

    def return_book(self, book_id):
        if book_id in self.books:
            self.books[book_id]["qty"] += 1
            print("Book Returned")

lib = Library()

while True:
    print("\n1.Add Book 2.View Books 3.Issue Book 4.Return Book 5.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        lib.add_book(
            input("Book ID: "),
            input("Book Name: "),
            input("Author: "),
            int(input("Quantity: "))
        )
    elif choice == "2":
        lib.view_books()
    elif choice == "3":
        lib.issue_book(input("Book ID: "))
    elif choice == "4":
        lib.return_book(input("Book ID: "))
    elif choice == "5":
        break
