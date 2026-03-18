import os

clear = lambda: os.system('cls')

# This function gets/creates the users reading list and returns it as a list of strings
# The list consists of title, author, optional notes, and read/unread status
def createList():
    reading_list = []
    done = False

    clear()
    while done is False:
        title = input("Please enter the title of a book you want to add to your reading list: ")
        reading_list.append(title)
        author = input("Please enter the author of the book: ")
        reading_list.append(author)
        notes = input("Please enter any optional notes about the book (or press enter to skip): ")
        reading_list.append(notes)
        status = input("Have you read this book? (y/n): ")
        reading_list.append(status)

        cont = input("Would you like to add another book? (y/n): ")
        if cont.lower() == "n":
            done = True
    print(reading_list)
    return reading_list

# Writes reading list information to a text file so it may be accessed later. Each item is written on a new line.
# Users can access this file to update their reading list or to view it.
def writeFile(reading_list):
    with open("reading_list.txt", "w") as file:
        for item in reading_list:
            file.write(f"{item[0]}, {item[1]}, {item[2]}, {item[3]}\n")

# this function allows the user to print their current reading list to the console.
# Prints the contents of the text file that was created by the writeFile function.
def printList(reading_list):
    for i, item in enumerate(reading_list):
        print(f"{i + 1}. (Title: {item[0]}, Author: {item[1]}, Notes: {item[2]}, Status: {item[3]})")

# This function allows the user to add a book to their reading list, update read/unread 
def updateList():
    print("This is the updateList function")

def getInput():
    state = True
    reading_list = []
    choice = 0

    while state is True:
        print ("Welcome to your reading list! Please select an option:")
        print("1. Create a new reading list")
        print("2. Print your current reading list")
        print("3. Update your reading list")
        print("4. Exit the program\n")
        choice = input("Please enter the number corresponding to your choice: ")
        if choice == "1":
            reading_list = createList()
            writeFile(reading_list)
        elif choice == "2":
            printList(reading_list)
        elif choice == "3":
            updateList()
        elif choice == "4":
            print("Now closing your reading list...")
            state = False
        else:
            print("Invalid input. Please enter a number between 1 and 4.")