import csv

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
                    library_num[j], library_num[j + 1] = library_num[j + 1], library_num[j]
                    title[j], title[j + 1] = title[j + 1], title[j]
                    author[j], author[j + 1] = author[j + 1], author[j]
                    genre[j], genre[j + 1] = genre[j + 1], genre[j]
                    pg_count[j], pg_count[j + 1] = pg_count[j + 1], pg_count[j]
                    status[j], status[j + 1] = status[j + 1], status[j]

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
                    library_num[j], library_num[j + 1] = library_num[j + 1], library_num[j]
                    
                    title[j], title[j + 1] = title[j + 1], title[j]
                    author[j], author[j + 1] = author[j + 1], author[j]
                    genre[j], genre[j + 1] = genre[j + 1], genre[j]
                    pg_count[j], pg_count[j + 1] = pg_count[j + 1], pg_count[j]
                    status[j], status[j + 1] = status[j + 1], status[j]

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
