# user_manager.py

from typing import List, Optional
from storage import Storage
from user import User
import logging

class UserManager:
    """
    Manages the collection of users in the library, handling operations such as
    adding, updating, deleting, and searching for users.

    Attributes:
        storage (Storage): Storage handler for data persistence.
    """

    def __init__(self, storage: Storage):
        self.storage = storage
        self.users = self.load_users()

    def load_users(self) -> List[User]:
        """
        Loads users from the storage.
        """
        user_data = self.storage.read().get("users", [])
        return [User(**data) for data in user_data]

    def save_users(self):
        """
        Saves the current list of users back to storage.
        """
        user_data = [user.to_dict() for user in self.users]
        self.storage.write({"users": user_data})
        logging.info("Users have been successfully saved to storage.")

    def add_user(self, user: User) -> bool:
        """
        Adds a new user to the library if there is no user with the same user ID already present.

        Parameters:
            user (User): The user to be added.

        Returns:
            bool: True if the user was added, False otherwise.
        """
        if any(u.user_id == user.user_id for u in self.users):
            logging.warning(f"Attempted to add a user with duplicate ID: {user.user_id}")
            return False
        self.users.append(user)
        self.save_users()
        logging.info(f"User added: {user.name}, ID: {user.user_id}")
        return True

    def update_user(self, user_id: str, name: Optional[str] = None) -> bool:
        """
        Updates the name of a user identified by their user ID.

        Parameters:
            user_id (str): The ID of the user to update.
            name (Optional[str]): The new name of the user, if updating.

        Returns:
            bool: True if the user was updated, False otherwise.
        """
        for user in self.users:
            if user.user_id == user_id:
                if name is not None:
                    user.name = name
                self.save_users()
                logging.info(f"User updated: ID: {user_id}")
                return True
        logging.warning(f"User not found for update: ID: {user_id}")
        return False

    def delete_user(self, user_id: str) -> bool:
        """
        Deletes a user from the library identified by their user ID.

        Parameters:
            user_id (str): The ID of the user to delete.

        Returns:
            bool: True if the user was deleted, False otherwise.
        """
        for i, user in enumerate(self.users):
            if user.user_id == user_id:
                del self.users[i]
                self.save_users()
                logging.info(f"User deleted: ID: {user_id}")
                return True
        logging.warning(f"User not found for deletion: ID: {user_id}")
        return False

    def find_user_by_id(self, user_id: str) -> Optional[User]:
        """
        Finds a user by their user ID.

        Parameters:
            user_id (str): The ID of the user to find.

        Returns:
            Optional[User]: The found user or None if not found.
        """
        return next((user for user in self.users if user.user_id == user_id), None)

    def find_users_by_name(self, name: str) -> List[User]:
        """
        Finds users whose names contain the given substring.

        Parameters:
            name (str): The name or substring to search for in user names.

        Returns:
            List[User]: A list of users that match the search criteria.
        """
        return [user for user in self.users if name.lower() in user.name.lower()]

    def list_users(self) -> None:
        """
        Prints a list of all users in the library.
        """
        if not self.users:
            print("No users available.")
            return
        for user in self.users:
            print(f"ID: {user.user_id}, Name: {user.name}")
'''

    def to_dict(self) -> dict:
        """
        Converts the user object to a dictionary for easier storage.

        Returns:
            dict: A dictionary representation of the user.
        """
        return {"name": self.name, "user_id": self.user_id}
'''



