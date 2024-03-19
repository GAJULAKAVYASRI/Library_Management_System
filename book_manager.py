# book_manager.py

from typing import List, Optional
from storage import Storage
from book import Book
import logging

class BookManager:
    """
    Manages the collection of books in the library, offering operations such as
    adding, listing, updating, and deleting books.

    Attributes:
        storage (Storage): The storage handler for persistent data storage.
    """

    def __init__(self, storage: Storage):
        self.storage = storage
        self.books = self.load_books()

    def load_books(self) -> List[Book]:
        """
        Loads books from storage into the book manager.
        """
        book_data = self.storage.read().get("books", [])
        return [Book(**data) for data in book_data]

    def save_books(self):
        """
        Saves the current state of the book collection to storage.
        """
        book_data = [book.to_dict() for book in self.books]  # Ensure Book has a to_dict method
        self.storage.write({"books": book_data})
        logging.info("Books have been saved to storage.")

    def add_book(self, book: Book) -> bool:
        """
        Adds a new book to the collection, ensuring no duplicates by ISBN.

        Parameters:
            book (Book): The book to be added.

        Returns:
            bool: True if the book was added successfully, False otherwise.
        """
        if any(b.isbn == book.isbn for b in self.books):
            logging.warning(f"Duplicate book ISBN: {book.isbn}.")
            return False
        self.books.append(book)
        self.save_books()
        logging.info(f"Book added: {book.isbn}")
        return True

    def list_books(self) -> List[Book]:
    # def list_books(self) -> None:

        """
        Returns a list of all books in the collection.

        Returns:
            List[Book]: The list of books.
        """
        if not self.books:
            print("No books available.")
            return
        for book in self.books:
            # print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")
            print(book)# Utilizes the __str__ method of the Book class 

    def update_book(self, isbn: str, title: Optional[str] = None, author: Optional[str] = None) -> bool:
        """
        Updates the title and/or author of a book identified by its ISBN.

        Parameters:
            isbn (str): The ISBN of the book to update.
            title (Optional[str]): The new title of the book, if provided.
            author (Optional[str]): The new author of the book, if provided.

        Returns:
            bool: True if the book was updated successfully, False if the book was not found.
        """
        for book in self.books:
            if book.isbn == isbn:
                if title:
                    book.title = title
                if author:
                    book.author = author
                self.save_books()
                logging.info(f"Book updated: {isbn}")
                return True
        logging.warning(f"Book not found for update: {isbn}")
        return False

    def delete_book(self, isbn: str) -> bool:
        """
        Deletes a book from the collection by its ISBN.

        Parameters:
            isbn (str): The ISBN of the book to delete.

        Returns:
            bool: True if the book was deleted successfully, False if the book was not found.
        """
        for i, book in enumerate(self.books):
            if book.isbn == isbn:
                del self.books[i]
                self.save_books()
                logging.info(f"Book deleted: {isbn}")
                return True
        logging.warning(f"Book not found for deletion: {isbn}")
        return False

    def find_book_by_isbn(self, isbn: str) -> Optional[Book]:
        """
        Finds and returns a book by its ISBN.

        Parameters:
            isbn (str): The ISBN of the book to find.

        Returns:
            Optional[Book]: The found book, or None if no book matches the ISBN.
        """
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_books_by_author(self, author: str) -> List[Book]:
        """
        Finds books by a specific author.

        Parameters:
            author (str): The author to search for in book records.

        Returns:
            List[Book]: A list of books by the specified author.
        """
        return [book for book in self.books if author.lower() in book.author.lower()]


    def find_books_by_title(self, title: str) -> List[Book]:
        """
        Finds and returns books that contain the given title substring.

        Parameters:
            title (str): The title or substring to search for in book titles.

        Returns:
            List[Book]: A list of books that match the search criteria.
        """
        return [book for book in self.books if title.lower() in book.title.lower()]
    

    '''
    def to_dict(self):
     """Converts the book instance into a dictionary."""
     return {"title": self.title, "author": self.author, "isbn": self.isbn}
    '''



