"""
In this project the primary focus is on the concept of file handling and functions.
User can delete, create and read notes from commeand line. 
"""

import os # To delete existing note in the working directory. Just one functionality of removing file is used.

# To create new note or edit existing
def create(file_name, file_format):

    new = open(file_name+file_format, 'a')

    file_text = input("Note is created. Now enter your desire text, Enter done to save and close note.\n")

    while file_text.lower != 'done':

        new.write(file_text + '\n')

        if file_text.lower() == 'done':
            new.close()
            break

        file_text = input()

    new.close()
    print("Note is saved.")

# To delete note
def delete(file_name):
    file_name = file_name + '.txt'
    os.remove(file_name) #remove text file
    print ('Deleted')

# To read text in existing note
def read_note(file_name):
    existing = file_name+'.txt'
    with open(existing, "r") as file: 
        data = file.readlines() 
        for line in data:  
            print (line, end='') 

# Instructions for input commands
welcome_note = """ Welcome to note taking app.
Important features: (Write following commands to get desired functionality)
open <file_name> - to create new note (.txt) or add stuff in existing note.
delete <file_name> - to delete existing code
read <file_name> - to read existing notes

Enter close exit program.
"""
print(welcome_note)

# Main program logic
while True:

    user_input = input().lower().split()

    if user_input[0] == 'open':
        create(user_input[1], '.txt')

    elif user_input[0] == 'delete':
        delete(user_input[1])

    elif user_input[0] == 'read':
        read_note(user_input[1])

    elif user_input[0] == 'close':
        exit

    else:
        print("Please enter valid input. Enter again")
        continue
