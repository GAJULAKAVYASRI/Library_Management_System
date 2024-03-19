# user.py

class User:
    """
    Represents a library user.

    Attributes:
        name (str): The name of the user.
        user_id (str): A unique identifier for the user.
    """
    
    def __init__(self, name: str, user_id: str):
        self.name = name
        self.user_id = user_id

    def __str__(self) -> str:
        """
        Provides a string representation of the user.
        """
        return f"User ID: {self.user_id}, Name: {self.name}"
    def to_dict(self):
        """
        Converts the user object to a dictionary for JSON storage.
        """
        return {
            "name": self.name,
            "user_id": self.user_id
        }

