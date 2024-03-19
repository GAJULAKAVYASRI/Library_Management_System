# main.py
import sys
#from datetime import datetime
from book import Book
from user import User
from book_manager import BookManager
from user_manager import UserManager
from checkout_manager import CheckoutManager
from storage import Storage
from log_config import setup_logging
import logging

# Initialize logging
setup_logging()

def main():
    # Initialize storage and manager classes
    storage = Storage("library_data.json")
    book_manager = BookManager(storage)
    user_manager = UserManager(storage)
    checkout_manager = CheckoutManager(storage)

    # Main application loop
    while True:
        print("\n--- Library Management System ---")
        print("1. Manage Books")
        print("2. Manage Users")
        print("3. Checkout or Checkin Books")
        print("4. List Overdue Books")
        print("5. Exit")
        choice = input("Please choose an option: ")

        if choice == '1':
            manage_books(book_manager)
        elif choice == '2':
            manage_users(user_manager)
        elif choice == '3':
            manage_checkouts(checkout_manager)
        elif choice == '4':
            list_overdue_books(checkout_manager)
        elif choice == '5':
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def manage_books(book_manager):
    # Book management submenu
    while True:
        print("\n--- Book Management ---")
        print("1. Add Book")
        print("2. List Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Return to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author's name: ")
            isbn = input("Enter book ISBN: ")
            '''
            isbn = input("Enter book ISBN (format XXX-X-XX-XXXXXX-X): ")
            if not re.match(r'\d{3}-\d-\d{2}-\d{6}-\d', isbn):
                print("Invalid ISBN format.")
                continue
            '''
            book = Book(title, author, isbn)  # Ensure the Book class has an appropriate constructor
            if book_manager.add_book(book):
                print("Book added successfully.")
            else:
                print("Failed to add book. It may already exist.")
        elif choice == '2':
            book_manager.list_books()
        elif choice == '3':
            isbn = input("Enter book ISBN to update: ")
            title = input("New title (press enter to skip): ")
            author = input("New author (press enter to skip): ")
            if book_manager.update_book(isbn, title, author):
                print("Book updated successfully.")
            else:
                print("Failed to update book. It may not exist.")
        elif choice == '4':
            isbn = input("Enter book ISBN to delete: ")
            if book_manager.delete_book(isbn):
                print("Book deleted successfully.")
            else:
                print("Failed to delete book. It may not exist.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_users(user_manager):
    # User management submenu
    while True:
        print("\n--- User Management ---")
        print("1. Add User")
        print("2. List Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Return to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            user = User(name, user_id)  # Ensure the User class has an appropriate constructor
            if user_manager.add_user(user):
                print("User added successfully.")
            else:
                print("Failed to add user. They may already exist.")
        elif choice == '2':
            user_manager.list_users()
        elif choice == '3':
            user_id = input("Enter user ID to update: ")
            name = input("New name (press enter to skip): ")
            if user_manager.update_user(user_id, name):
                print("User updated successfully.")
            else:
                print("Failed to update user. They may not exist.")
        elif choice == '4':
            user_id = input("Enter user ID to delete: ")
            if user_manager.delete_user(user_id):
                print("User deleted successfully.")
            else:
                print("Failed to delete user. They may not exist.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_checkouts(checkout_manager):
    while True:
        print("\n--- Checkout Management ---")
        print("1. Checkout Book")
        print("2. Checkin Book")
        print("3. List Checked Out Books")
        print("4. Return to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            isbn = input("Enter book ISBN to checkout: ")
            user_id = input("Enter user ID: ")
            if checkout_manager.checkout_book(user_id, isbn):
                print("Book checked out successfully.")
            else:
                print("Failed to checkout book. It may already be checked out or does not exist.")
        elif choice == '2':
            isbn = input("Enter book ISBN to checkin: ")
            if checkout_manager.checkin_book(isbn):
                print("Book checked in successfully.")
            else:
                print("Failed to checkin book. It may not have been checked out or does not exist.")
        elif choice == '3':
            checkout_manager.list_checked_out_books()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def list_overdue_books(checkout_manager):
    print("\n--- Overdue Books ---")
    checkout_manager.list_overdue_books()

if __name__ == "__main__":
    main()

