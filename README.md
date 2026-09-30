Library Book Search Management System

A Library Book Search Management System developed using Python and Streamlit as a Data Structures Assignment.

The project demonstrates the implementation of a List of Dictionaries data structure and the Linear Search algorithm for managing and searching library book records.

Features

- Add new books
- Display all books
- Search books by Title
- Search books by Author
- Search books by Genre
- Search books by Book ID
- Automatic Book ID generation
- Display total number of books
- Case-insensitive search for Title, Author, and Genre

Technologies Used

- Python
- Streamlit
- List of Dictionaries
- Linear Search

Data Structure

The application uses a List of Dictionaries to store book records.

Each book record contains the following fields:

{
    "id": int,
    "title": str,
    "author": str,
    "genre": str
}

The book records are maintained using Streamlit session state.

Search Algorithm

The application implements Linear Search to find books in the library.

The search can be performed using:

- Title
- Author
- Genre
- ID

Title, Author, and Genre searches are case-insensitive. The algorithm checks the book records sequentially and returns all matching records.

Complexity

- Time Complexity: O(n)
- Space Complexity: O(k)

Where:

- "n" represents the number of books.
- "k" represents the number of matching records returned by the search.

Project Structure

Library-Book-Search/
│
├── final_libary_search_algorithm.py
└── README.md

Installation

1. Clone the Repository

git clone <repository-url>

2. Navigate to the Project Directory

cd Library-Book-Search

3. Install Dependencies

Install Streamlit using pip:

pip install streamlit

Running the Application

Run the following command:

streamlit run final_libary_search_algorithm.py

The Streamlit application will start and can be accessed through the local URL provided in the terminal.

Application Modules

Add Book

Users can add a new book by providing:

- Book Title
- Author Name
- Genre

Title and Author are required fields. If no genre is provided, the application assigns "General" as the default genre. Each new book receives an automatically generated ID.

Display Books

The Display Books section presents all stored books in a table containing:

- ID
- Title
- Author
- Genre

The total number of records is also displayed.

Search Book

Users can select a search field, enter a search value, and perform a search. The application displays all matching book records.

Functions

Function| Description
"add_book()"| Adds a new book record to the library
"display_books()"| Returns the complete list of stored books
"search_book()"| Performs a linear search
"render_book_card()"| Displays individual book information

The application is organized into modular functions to separate book management, display, searching, and presentation logic.

Data Storage

The current implementation stores book records in Streamlit session state. The data is maintained in memory during the application session and is not stored in a permanent database or file.

Author
Monisha 

Project Type

Data Structures Assignment
