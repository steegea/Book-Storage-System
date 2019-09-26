
import mysql.connector.errors
from .database_connection import DatabaseConnection
from typing import List, Dict, Union

#Defines book object
Book = Dict[str, Union[str, int]]

#Creates the "Books" table
def create_book_table() -> None:
    with DatabaseConnection() as db_connection:

        cursor = db_connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS Books(name VARCHAR(255) primary key, author VARCHAR(255), has_read INT)")


#Adds a book to the database
def add_book(name:str, author:str) -> None:
    with DatabaseConnection() as db_connection:
        
        cursor = db_connection.cursor(prepared=True)

        try:
            cursor.execute('INSERT INTO Books VALUES(?, ?, 0)', (name, author))

        except mysql.connector.InterfaceError:
            print("\nError: The book is already in the database.")

#Returns a list of all books in the database
def get_all_books() -> List[Book]:
    with DatabaseConnection() as db_connection:
        cursor = db_connection.cursor()
        cursor.execute('SELECT * From Books')
        books = [{"name": row[0], "author":row[1], "read": row[2]} for row in cursor.fetchall()]

    return books
    
#Marks a book as read (sets "has_read" to True)
def mark_book_as_read(name: str) -> None:
    with DatabaseConnection() as db_connection:
        cursor = db_connection.cursor(prepared=True)
        cursor.execute("UPDATE Books Set Has_Read = 1 where name = ?", (name,))


#Marks a book as not read/not finished (sets "has_read" to False)
def mark_book_as_not_read(name: str) -> None:

    with DatabaseConnection() as db_connection:
        cursor = db_connection.cursor(prepared=True)
        cursor.execute('UPDATE Books Set Has_Read = 0 where name = ?', (name,))


#Removes a book from the database
def delete_book(name: str) -> None:
    with DatabaseConnection() as db_connection:
        cursor = db_connection.cursor(prepared = True)
        cursor.execute("Delete From Books where name = ?", (name,))

