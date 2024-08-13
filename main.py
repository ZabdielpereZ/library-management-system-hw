from user_operations import UserOperations
from book_operations import BookOperations
from author_operations import AuthorOperations


def main_menu():
    user_ops = UserOperations()
    book_ops = BookOperations()
    author_ops = AuthorOperations()

    while True:
        print("\nMain Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Quit")
        choice = input("Select an option: ")

        if choice == '1':
            book_operations_menu(book_ops)
        elif choice == '2':
            user_operations_menu(user_ops)
        elif choice == '3':
            author_operations_menu(author_ops)
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

def book_operations_menu(book_ops):
    while True:
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Back to main menu")
        choice = input("Select an option: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            genre = input("Enter book genre: ")
            publication_date = input("Enter publication date: ")
            book_ops.add_new_book(title, author, genre, publication_date)
        elif choice == '2':
            title = input("Enter book title: ")
            book_ops.borrow_book(title)
        elif choice == '3':
            title = input("Enter book title: ")
            book_ops.return_book(title)
        elif choice == '4':
            title = input("Enter book title: ")
            book_ops.search_book(title)
        elif choice == '5':
            book_ops.display_all_books()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def user_operations_menu(user_ops):
    while True:
        print("\nUser Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")
        print("4. Back to main menu")
        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter user name: ")
            library_id = input("Enter library ID: ")
            user_ops.add_new_user(name, library_id)
        elif choice == '2':
            library_id = input("Enter library ID: ")
            user_ops.view_user_details(library_id)
        elif choice == '3':
            user_ops.display_all_users()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def author_operations_menu(author_ops):
    while True:
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")
        print("4. Back to main menu")
        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter author name: ")
            biography = input("Enter author biography: ")
            author_ops.add_new_author(name, biography)
        elif choice == '2':
            name = input("Enter author name: ")
            author_ops.view_author_details(name)
        elif choice == '3':
            author_ops.display_all_authors()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
