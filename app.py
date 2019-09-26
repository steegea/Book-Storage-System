#File that represents the app's business logic

from utils import database

USER_CHOICE = """
Enter:
- "a" to add a new book
- "d" to delete a book
- "l" to view your list of books
- "r" to mark a book as read
- "nr" to mark a book as not read
- "q" to quit

Your choice: """

#Function representing the UI
#Specifies the actions taken if the user types certain letters
def menu():
    database.create_book_table()

    user_input = input(USER_CHOICE)
    while user_input != "q":

        if user_input == "a":
            prompt_add_book()

        elif user_input == "d":
            prompt_delete_book()

        elif user_input == "l":
            prompt_get_all_books()
        
        elif user_input == "r":
            prompt_mark_book_as_read()

        elif user_input == "nr":
            prompt_mark_book_as_not_read()

        else:
            print("Invalid input!")
            
        user_input = input(USER_CHOICE)
        
    else: 
        print("\nYou have logged out of your account.\n")


def prompt_add_book():
    book_name = input("Book Name: ")
    book_author = input("Book Author: ")

    database.add_book(book_name, book_author)

def prompt_get_all_books():
    books = database.get_all_books()

    if books == []:
        print("\nYour list is empty!")
    
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']}, read: {read}")


def prompt_mark_book_as_read():
    book_name = input("Please type the name of the book you have read: ")
    database.mark_book_as_read(book_name)

def prompt_mark_book_as_not_read():
    book_name = input("Please enter the name of the book you would like to update: ")
    database.mark_book_as_not_read(book_name)

def prompt_delete_book():
    book_name = input("Please enter the name of the book you would like to delete: ")
    database.delete_book(book_name)


#Calling the menu() function
menu()