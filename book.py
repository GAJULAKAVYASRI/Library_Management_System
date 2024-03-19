# book.py

class Book():
    """
    Represents a book in the library, with relevant attributes.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str) : isbn number of the book

    """

    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self) -> str:
        """
        Provides a string representation of the book.
        """
        return f"{self.title} by {self.author}, ISBN: {self.isbn}"

    def to_dict(self):
        """
        Converts the book object to a dictionary for storage.
        """
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn
        }

