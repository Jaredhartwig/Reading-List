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
            
    return reading_list

# Writes reading list information to a text file so it may be accessed later. Each item is written on a new line.
# Users can access this file to update their reading list or to view it.
def writeFile(reading_list):
    with open("reading_list.txt", "w") as file:
        for item in reading_list:
            file.write("".join(item) + ", ")

def readFile():
    reading_list = []
    with open("reading_list.txt", "r") as file:
        for line in file:
            item = line.strip().split(", ")
            reading_list.append(item)
            print(reading_list)
    return reading_list

# this function allows the user to print their current reading list to the console.
# Prints the contents of the text file that was created by the writeFile function.
def printList(reading_list):
    for i, item in enumerate(reading_list):
        print(f"{i + 1}. Title: {item}, Author: {item}, Notes: {item}, Status: {item}")

# This function allows the user to add a book to their reading list, update read/unread 
def updateList():
    reading_list = readFile()
    printList(reading_list)
    choice = input("Please enter the number of the book you would like to update: ")
    if choice.isdigit() and 1 <= int(choice) <= len(reading_list):
        index = int(choice) - 1
        new_status = input("Have you read this book? (y/n): ")
        reading_list[index][3] = new_status
        writeFile(reading_list)
        print("Reading list updated successfully!")
    else:
        print("Invalid input. Please enter a valid number.")

def getInput():
    state = True
    reading_list = []
    choice = 0

    while state is True:
        print ("\nWelcome to your reading list! Please select an option:")
        print("1. Create a new reading list")
        print("2. Print your current reading list")
        print("3. Update your reading list")
        print("4. Exit the program\n")
        choice = input("Please enter the number corresponding to your choice: ")
        if choice == "1":
            reading_list = createList()
            # writeFile(reading_list)
        elif choice == "2":
            # reading_list = readFile()
            printList(reading_list)
        elif choice == "3":
            updateList(reading_list)
        elif choice == "4":
            print("\nNow closing your reading list...\n")
            state = False
        else:
            print("\nInvalid input. Please enter a number between 1 and 4.")
