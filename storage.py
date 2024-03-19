# storage.py

import json
from typing import Dict, List, Any
import os

class Storage:
    """
    Manages the storage of the library's data using a JSON file.
    Singleton pattern to ensure one instance manages the file access.

    Attributes:
        filename (str): The file path for the JSON storage file.
    """
    
    _instance = None

    def __new__(cls, filename='library_data.json'):
        if cls._instance is None:
            cls._instance = super(Storage, cls).__new__(cls)
            cls._instance.filename = filename
            cls._instance.init_storage()
        return cls._instance

    def init_storage(self):
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                json.dump({"books": [], "users": [], "checkouts": []}, f)
       

    def read(self) -> Dict[str, List[Any]]:
        """
        Reads data from the JSON file. If the file does not exist, initializes the data structure.

        Returns:
            A dictionary with keys for 'books', 'users', and 'checkouts', each mapping to a list of items.
        """
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {"books": [], "users": [], "checkouts": []}

    def write(self, data: Dict[str, List[Any]]) -> None:
        """
        Writes the given data to the JSON file.

        Parameters:
            data (Dict[str, List[Any]]): The data to be written to the file.
        """
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)

