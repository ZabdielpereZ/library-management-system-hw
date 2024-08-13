

class BookOperations:
    def __init__(self):
        self.books = []

    def add_new_book(self, title, author, genre, publication_date):
        new_book = Book(title, author, genre, publication_date)
        self.books.append(new_book)
        print(f"Book '{title}' added successfully.")

    def borrow_book(self, title):
        for book in self.books:
            if book.get_title() == title:
                if book.borrow():
                    print(f"Book '{title}' borrowed successfully.")
                else:
                    print(f"Book '{title}' is not available.")
                return
        print("Book not found.")

    def return_book(self, title):
        for book in self.books:
            if book.get_title() == title:
                book.return_book()
                print(f"Book '{title}' returned successfully.")
                return
        print("Book not found.")

    def search_book(self, title):
        for book in self.books:
            if book.get_title() == title:
                print(f"Title: {book.get_title()}")
                print(f"Author: {book.get_author()}")
                print(f"Genre: {book.get_genre()}")
                print(f"Publication Date: {book.get_publication_date()}")
                print(f"Availability: {'Available' if book.is_available() else 'Borrowed'}")
                return
        print("Book not found.")

    def display_all_books(self):
        if not self.books:
            print("No books found.")
            return
        for book in self.books:
            print(f"Title: {book.get_title()}, Author: {book.get_author()}, Genre: {book.get_genre()}, Publication Date: {book.get_publication_date()}, Availability: {'Available' if book.is_available() else 'Borrowed'}")

class Book:
    def __init__(self, title, author, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__is_available = True

    # Getters and Setters
    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def get_genre(self):
        return self.__genre

    def set_genre(self, genre):
        self.__genre = genre

    def get_publication_date(self):
        return self.__publication_date

    def set_publication_date(self, publication_date):
        self.__publication_date = publication_date

    def is_available(self):
        return self.__is_available

    def borrow(self):
        if self.__is_available:
            self.__is_available = False
            return True
        return False

    def return_book(self):
        self.__is_available = True
