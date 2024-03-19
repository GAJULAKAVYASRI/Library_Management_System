# README for Library Management System
Handles all programs related to library management system

## Introduction
This Library Management System is designed to efficiently manage library operations including managing books and users, checking out and checking in books, and tracking book availability. Utilizing Object-Oriented Programming (OOP) principles and file-based storage (JSON), this system ensures scalable, maintainable, and easy-to-use library management. It also incorporates logging for tracking operations and errors.

## Features
- **Manage Books**: Add, update, delete, list, and search books by title, author, or ISBN.
- **Manage Users**: Add, update, delete, list, and search users by name or user ID.
- **Book Check-Out and Check-In**: Handle the borrowing and returning of books, including availability tracking.
- **Logging**: Simple logging of operations and errors for maintenance and auditing.

## System Requirements
- Python 3.6 or later.
- No external libraries are required for the basic functionalities. For extended features, requirements will be specified.

## Installation
Clone the repository to your local machine:
```
git clone <repository-url>
```
Navigate to the system directory:
```
cd Library_Management_System
```

## Usage
To start the system, run the following command in your terminal:
```
python main.py
```
Follow the on-screen prompts to interact with the system through the Command Line Interface (CLI).

## Architecture
The system is built around the following key classes, aligning with OOP principles:

- **Book**: Represents a book with attributes like title, author, ISBN, and availability status.
- **User**: Represents a library user with attributes such as name and user ID.
- **Library**: The central class managing books and users, implementing functionalities to add, update, delete, list, and search for books and users.
- **Storage**: Handles data persistence using JSON file-based storage, ensuring data is saved and retrieved effectively.
- **Logger**: Manages logging of system operations and errors, aiding in debugging and system monitoring.

## File-Based Storage
This system uses JSON for persistent storage, enabling easy data manipulation and retrieval. Data is stored in a structured format, allowing for efficient data access and scalability.

## Error Handling and Validation
Comprehensive error handling and input validation are implemented throughout the system to ensure data integrity and system reliability. Users are prompted for correct inputs in case of errors.

## Extensibility
Designed for scalability, the system can be easily extended to include additional features such as handling new item types, incorporating due dates for books, calculating late fees, and more.

## Documentation
Each class and method includes detailed docstrings and comments explaining functionality, parameters, and return values, ensuring the codebase is understandable and maintainable.
