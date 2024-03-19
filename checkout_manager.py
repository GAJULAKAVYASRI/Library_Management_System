# checkout_manager.py

from datetime import datetime, timedelta
from typing import Dict, List, Optional
from storage import Storage
import logging

class CheckoutManager:
    """
    Manages the checkout and check-in processes for books in the library.

    Attributes:
        storage (Storage): Storage handler for data persistence.
        checkouts (List[Dict]): A list of dictionaries, each representing a checkout.
    """

    def __init__(self, storage: Storage):
        self.storage = storage
        self.checkouts = self.load_checkouts()

    def load_checkouts(self) -> List[Dict[str, any]]:
        """
        Loads the checkouts from storage.
        """
        return self.storage.read().get("checkouts", [])

    def save_checkouts(self):
        """
        Saves the current checkouts back to storage.
        """
        self.storage.write({"checkouts": self.checkouts})
        logging.info("Checkouts have been successfully saved .")

    def checkout_book(self, user_id: str, isbn: str, due_date: Optional[datetime] = None) -> bool:
        """
        Checks out a book to a user, marking it as unavailable.

        Parameters:
            user_id (str): The ID of the user checking out the book.
            isbn (str): The ISBN of the book being checked out.
            due_date (Optional[datetime]): The due date for the book return. Defaults to 14 days from checkout.

        Returns:
            bool: True if the checkout was successful, False otherwise.
        """
        if due_date is None:
            due_date = datetime.now() + timedelta(days=14)
        
        if any(checkout['isbn'] == isbn for checkout in self.checkouts):
            logging.warning(f"Book already checked out: ISBN {isbn}")
            return False

        self.checkouts.append({"user_id": user_id, "isbn": isbn, "due_date": due_date.isoformat()})
        self.save_checkouts()
        logging.info(f"Book checked out: ISBN {isbn} by User ID {user_id}")
        return True

    def checkin_book(self, isbn: str) -> bool:
        """
        Checks in a book, making it available again.

        Parameters:
            isbn (str): The ISBN of the book being checked in.

        Returns:
            bool: True if the check-in was successful, False otherwise.
        """
        for i, checkout in enumerate(self.checkouts):
            if checkout['isbn'] == isbn:
                del self.checkouts[i]
                self.save_checkouts()
                logging.info(f"Book checked in: ISBN {isbn}")
                return True

        logging.warning(f"Attempt to check in a book not checked out: ISBN {isbn}")
        return False

    def list_checked_out_books(self) -> None:
        """
        Lists all currently checked out books.
        """
        if not self.checkouts:
            print("No books currently checked out.")
            return

        for checkout in self.checkouts:
            print(f"ISBN: {checkout['isbn']}, User ID: {checkout['user_id']}, Due Date: {checkout['due_date']}")


    def find_overdue_books(self) -> List[dict]:
        """
        Identifies books that are overdue for return.

        Returns:
            List[dict]: A list of checkouts that are overdue.
        """
        today = datetime.now()
        overdue_checkouts = [checkout for checkout in self.checkouts if datetime.fromisoformat(checkout['due_date']) < today]
        return overdue_checkouts

    def list_overdue_books(self) -> None:
        """
        Prints a list of all overdue books, including the user who has them and the overdue days.
        """
        overdue_checkouts = self.find_overdue_books()
        if not overdue_checkouts:
            print("No books are currently overdue.")
            return

        for checkout in overdue_checkouts:
            due_date = datetime.fromisoformat(checkout['due_date'])
            overdue_days = (datetime.now() - due_date).days
            print(f"ISBN: {checkout['isbn']}, User ID: {checkout['user_id']}, Overdue by: {overdue_days} days")

    def calculate_fine(self, isbn: str) -> Optional[float]:
        """
        Calculates the fine for an overdue book based on the number of days it is overdue.

        Parameters:
            isbn (str): The ISBN of the overdue book.

        Returns:
            Optional[float]: The fine amount or None if the book is not found or not overdue.
        """
        overdue_checkouts = self.find_overdue_books()
        for checkout in overdue_checkouts:
            if checkout['isbn'] == isbn:
                due_date = datetime.fromisoformat(checkout['due_date'])
                overdue_days = max((datetime.now() - due_date).days, 0)  # Ensure no negative days
                fine_per_day = 0.5  # Assuming a fine of $0.5 per day
                return overdue_days * fine_per_day

        logging.warning(f"Book with ISBN {isbn} is not overdue or not found.")
        return None


