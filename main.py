#imports
from library import librarian
import json


file_name = "books.json"

#load data from file (json --> dictionary)
def load_books():
    try: 
       with open(file_name, "r", encoding="utf-8") as file:  #open file read
            return json.load(file) # read the data as json and convert it to python object (return it as dictionary)
    except FileNotFoundError:
        return{} # return empty dictionary

#saves data to the file (dictionary --> json)
def save_books(library): 
    with open(file_name, "w", encoding="utf-8") as file: #open write file
        json.dump(library, file, indent=4) #saves the dictionary inside the json file

def display_menu(): 
    print("\n===== Library Menu =====") 
    print("1. Add a book") 
    print("2. Display all books") 
    print("3. Search for a book") 
    print("4. Delete a book") 
    print("5. Borrow a book") 
    print("6. Return a book") 
    print("7. Exit")    

library = load_books()

while True: 
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1": 
        title = input("Enter book title: ") 
        author = input("Enter author: ") 
        isbn = input("Enter ISBN: ")

        librarian.add_book(library, title, author, isbn) 
        save_books(library)

    elif choice == "2": 
        librarian.display_books(library)

    elif choice == "3": 
        keyword = input("Enter title, author, or ISBN to search: ") 
        librarian.search_books(library, keyword)


    elif choice == "4": 
        isbn = input("Enter ISBN of the book to delete: ") 
        librarian.remove_book(library, isbn) 
        save_books(library)

    elif choice == "5": 
        isbn = input("Enter ISBN of the book to borrow: ") 
        librarian.check_out_book(library, isbn) 
        save_books(library)

    elif choice == "6": 
        isbn = input("Enter ISBN of the book to return: ") 
        librarian.return_book(library, isbn) 
        save_books(library)

    elif choice == "7": 
        print("Goodbye!")
        break

    else: 
        print("Invalid choice. Please try again.")