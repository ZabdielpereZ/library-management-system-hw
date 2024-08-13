

class UserOperations:
    def __init__(self):
        self.users = []

    def add_new_user(self, name, library_id):
        new_user = User(name, library_id)
        self.users.append(new_user)
        print(f"User {name} added successfully.")

    def view_user_details(self, library_id):
        for user in self.users:
            if user.get_library_id() == library_id:
                print(f"Name: {user.get_name()}")
                print(f"Library ID: {user.get_library_id()}")
                print(f"Borrowed Books: {', '.join(user.get_borrowed_books())}")
                return
        print("User not found.")

    def display_all_users(self):
        if not self.users:
            print("No users found.")
            return
        for user in self.users:
            print(f"Name: {user.get_name()}, Library ID: {user.get_library_id()}")

class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    # Getters and Setters
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_library_id(self):
        return self.__library_id

    def set_library_id(self, library_id):
        self.__library_id = library_id

    def get_borrowed_books(self):
        return self.__borrowed_books

    def borrow_book(self, book_title):
        self.__borrowed_books.append(book_title)

    def return_book(self, book_title):
        self.__borrowed_books.remove(book_title)
