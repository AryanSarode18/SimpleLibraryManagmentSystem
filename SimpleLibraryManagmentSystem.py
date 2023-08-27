class Library:
    def __init__(self):
        # Initialize the library with no books and an empty list to store books
        self.no_books = 0
        self.books = []

    def add_book(self, book):
        # Add a new book to the library's list of books
        self.books.append(book)
        # Update the number of books in the library
        self.no_books = len(self.books)

    def display(self):
        # Display the number of books in the library
        print(f"There are {self.no_books} books in the library. They are:")
        # Display the list of books in the library
        for book in self.books:
            print(book)


# Create an instance of the Library class
l = Library()

# Add books to the library
l.add_book("Harry Potter 1")
l.add_book("Harry Potter 2")
l.add_book("Harry Potter 3")
l.add_book("Harry Potter 4")
l.add_book("Harry Potter 5")
l.add_book("Harry Potter 6")
l.add_book("Harry Potter 7.1")
l.add_book("Harry Potter 7.2")

# Display the contents of the library
l.display()
