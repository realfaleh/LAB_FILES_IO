# ----- choice.1 -----
def add_book(library, title, author, isbn):
    if isbn in library:
        print("A book with this ISBN already exists in the library")
        return
    
    library[isbn] = {
            "title" :  title ,
            "author" : author , 
            "isbn": isbn , 
            "available" : True
    }
    print("Book added successfuly.")

# ----- choice.2 -----
def display_books(library):
    if not library:
        print("No books in the library")
        return
    for book in library.values():
        status = "Available" if book["available"] else "Checked out"
        print(f"{book["title"]} by {book["author"]} (ISBN: {book["isbn"]}) - {status} \n")

# ----- choice.3 -----
def search_books(library, keyword):
    found = False # defult value
    for book in library.values(): 
        if (keyword.lower() in book["title"].lower() 
            or keyword.lower() in book["author"].lower() 
            or keyword in book["isbn"]): 

            status = "Available" if book["available"] else "Checked Out" 
            print( f'{book["title"]} by {book["author"]} ' f'(ISBN: {book["isbn"]}) - {status}' ) 
            found = True 
            if not found: 
                print("No books found")

# ----- choice.4 -----
def remove_book(library, isbn):
    if isbn in library:
        del library[isbn]
        print("Book removed successfuly")
    else: 
        print("Book not found")

# ----- choice.5 -----
def check_out_book(library, isbn):
    if isbn not in library:
        print("Book not found")
        return
    if not library[isbn]["available"]:
        print("Book is already checked out")
        return

    library[isbn]["available"] = "False"
    print("Book checked out successfuly")

# ----- choice.6 -----
def return_book(library, isbn):
    if isbn not in library:
            print("Book not found")
            return
    library[isbn]["available"] = True
    print("Book returned successfuly")

