#Jayda Bowe
#Feb 16 2025
#W6D2 - SE126_Lab5-1

#Prompt - Build a personal library search system using the file book_list.csv. It is set up as follows:

#Store the file data into 1D parallel lists, then use the appropriate searching algorithms for the menu system options.
#Your program should give your user the following menu:
#Personal Library Menu
#1. Show All Titles – list all book data to the user alphabetically by title
#2. Search by Title – allow for an entire title or a title key word
#3. Search by Author – show all titles of the searched-for author
#4. Search by Genre - show all titles of the searched-for genre
#5. Search by Library Number – only allow for one specific library number item
#6. Show All Available – show all titles with status “available”
#7. Show All On Loan - show all titles with status “on loan”
#8. EXIT
#When your user runs any of the options 1 – 7, show all data associated with the search [Library Number, Title, Author,
#Genre, Page count, Status]. Do not allow the program to end unless the user chooses option 8 to exit. All searches
#should not be case sensitive.

#Variable Dictionary:



#this file uses: book_list.csv

#PROGRAM PROMPT: Build a repeatable, menu-driven program to access and search for data within the file

#--IMPORTS-------------------------------------------------------------------------------
import csv

# --FUNCTIONS-----------------------------------------------------------------------------

# -- FUNCTIONS -----------------------------------------------------------------------
def display(x, records):
    '''
    PARAMETERS:
        x   signifier for if we are printing a single record or multiple
            when x != "x" it is an integer index and we have one value, otherwise we have multiple
        records   the length of a list we are going to process through (# of loops/prints)
    '''
    print(f"{'Library #':20}  {'Title':40}  {'Author':20}  {'Genre':20} {'Page Count':20} {'Status'}")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------")
    if x != "x":
        # Printing one record
        print(f"{library_num[x]:20}  {title[x]:40}  {author[x]:20}  {genre[x]:20} {pg_count[x]:20} {status[x]}")
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------\n")

    elif found:
        # Printing multiples, based on length stored in 'foundList'
        for i in range(0, records):
            print(f"{library_num[found[i]]:20}  {title[found[i]]:40}  {author[found[i]]:20}  {genre[found[i]]:20} {pg_count[found[i]]:20} {status[found[i]]}") 
            print("-----------------------------------------------------------------------------------------------------------------------------------------------------\n")

    else:
        # Printing full data, based on length stored in 'records'
        for i in range(0, records):
            print(f"{library_num[i]:20}  {title[i]:40}  {author[i]:20}  {genre[i]:20} {pg_count[i]:20} {status[i]}")
            print("-----------------------------------------------------------------------------------------------------------------------------------------------------\n")

def seqSearch(search, listname):

    for i in range(0, len(listname)):
        if search.lower() in listname[i].lower():
            found.append(i)
    
    if not found:  # If found list is still empty
        print(f"Sorry, your search for '{search}' came up empty :[")
    else:
        # Call display() to show the values
        print(f"'{search}' was found!")
        display("x", len(found))

def swap(i, listName):
    temp = listName[i]
    listName[i] = listName[i + 1]
    listName[i + 1] = temp
# -- MAIN EXECUTING CODE -------------------------------------------------------------
library_num = []
title = [] 
author = []
genre = []
pg_count = []
status = []

found = []

# Read data from the CSV file
with open("text_files/book_list.csv", newline='', encoding='utf-8') as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        library_num.append(rec[0])
        title.append(rec[1])
        author.append(rec[2])
        genre.append(rec[3])
        pg_count.append(rec[4])
        status.append(rec[5])

# List storing the menu choices
menu_options = ["1", "2", "3", "4", "5", "6", "7", "8"]

ans = input("Would you like to enter the search program? [y/n]: ").lower()

# Validity and user error trap loop
while ans != "y" and ans != "n":
    print("***INVALID ENTRY!***")
    ans = input("Would you like to enter the search program? [y/n]: ").lower()

# Main searching loop
while ans == "y":
    found = []  # Resets found list so each new menu/search it is empty

    print("\tSEARCHING MENU")
    print("1. Search All Titles")
    print("2. Search by Title")
    print("3. Search by Author")
    print("4. Search by Genre")
    print("5. Search by Library Number")
    print("6. Search by All Available")
    print("7. Search by All On-Loan")
    print("8. EXIT")

    search_type = input("\nHow would you like to search today? [1-8]: ")

    # Using 'not in' for user validity checks
    if search_type not in menu_options:
        print("***INVALID ENTRY!***\nPlease try again")
    
    elif search_type == "1":
        print(f"\nYou have chosen to search for All Titles.")

        # Bubble Sort --> higher values 'bubble' to the bottom of the collection
        for i in range(0, len(library_num)-1):
            for j in range(0, len(library_num)-1):
                if library_num[j] > library_num[j + 1]:
                    # Swap
                    swap(j, title)
                    swap(j, author)
                    swap(j, genre)
                    swap(j, pg_count)
                    swap(j, status)

                    

        # Display the whole list data to user
        display("x", len(library_num)) 

    elif search_type == "2":
        print(f"\nYou have chosen to search by Title.")

        # Allow the user to search for a certain TITLE or keyword
        search_title = input("Enter Book Title or Keyword to search:\n").lower()
        
        found = []

        seqSearch(search_title, title)

    elif search_type == "3":
        print(f"\nYou have chosen to search for Author's Name.")

        search_author = input("Enter the Author's Name:\n").lower()
        seqSearch(search_author, author)  

    elif search_type == "4":
        print(f"\nYou have chosen to search by Genre.")

        search_genre = input("Enter the book Genre:\n").lower()
        seqSearch(search_genre, genre) 

    elif search_type == "5":
        print(f"\nYou have chosen to search by Library Number.")

        # Allow the user to search for ONE specific and unique name value (binary search)
        search = input("Enter the Library Number you are looking for: ")

        # Bubble Sort: Sort the library numbers for binary search
        for i in range(0, len(library_num)-1):
            for j in range(0, len(library_num)-1):
                if library_num[j] > library_num[j + 1]:
                    swap(j, title)
                    swap(j, author)
                    swap(j, genre)
                    swap(j, pg_count)
                    swap(j, status)
                    
                    

        # Binary Search for Library Number
        min = 0
        max = len(library_num) - 1
        mid = (min + max) // 2

        while min <= max:
            if library_num[mid] == search:
                print(f"Huzzah! We have found your search for Library Number {search}, see details below:")
                display(mid, len(library_num))
                break
            elif library_num[mid] < search:
                min = mid + 1
            else:
                max = mid - 1

            mid = (min + max) // 2

        if min > max:
            print(f"Sorry, we could not find your search for Library Number {search}. Please try again.")

    elif search_type == "6":
        print(f"\nYou have chosen to search by All Available Books.")
        
        found = []
        for i in range(0, len(status)):
            if status[i].lower() == "available":
                found.append(i)
        
        if found:
            display("x", len(found))
        else:
            print("No available books found.")

    elif search_type == "7":
        print(f"\nYou have chosen to search by All On-Loan Books.")
        
        found = []
        for i in range(0, len(status)):
            if status[i].lower() == "on loan":
                found.append(i)
        
        if found:
            display("x", len(found))
        else:
            print("No on-loan books found.")
    
    elif search_type == "8":
        print(f"\nYou have chosen to EXIT.")
        ans = "n"

    else:
        print("***INVALID INPUT***")

# Alert user that the program is about to end
print("Thank you for using my program, goodbye!\n")
