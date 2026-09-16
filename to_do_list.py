file = open ("to_do.txt" , "a+" , encoding = 'utf-8')

while True:
    add_item = input("Do you want to add new To-Do item ? (answer 'y' for yes and 'n' for no) \n")
    if add_item == 'y':
        new_item = input("Type your new To-Do item : \n")
        file.write(new_item + '\n')
    elif add_item == 'n':
        list_items = input("Do you want to list your To-Do items ? (answer 'y' for yes and 'n' for no) \n")
        if list_items == 'y':
            file.seek(0)
            print(file.read())
        elif list_items == 'n':
            continue
    elif add_item == 'exit':
        print("Thank you for using the To-Do program, come back again soon ..")
        break

file.close()
