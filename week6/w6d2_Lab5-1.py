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

#--FUNCTIONS-----------------------------------------------------------------------------
def display(x, records):
    '''
        PARAMETERS:
            x   signifier for if we are printing a single record or multiple
                when x != "x" it is an integere index and we have one value, otherwise we have multiple

            records   the length of a list we are going to process through (# of loops/prints)
    '''
    print(f"{'Libaray #':20}  {'Title':40}  {'Author':20}  {'Genre':20} {'Page Count':20} {'Status'}")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------")
    if x != "x":
        #printing one record
        print(f"{library_num[x]:50}  {title[x]:50}  {author[x]:50}  {genre[x]:50} {pg_count[x]:50} {status[x]}")

    elif found:
        #printing multiples, based on length stored in 'foundList'
        for i in range(0, records):
            print(f"{library_num[found[i]]:20}  {title[found[i]]:35}  {author[found[i]]:25}  {genre[found[i]]:20} {pg_count[found[i]]:20} {status[found[i]]}") 
    
    else:
        #printing full data, based on length stored in 'records'
        for i in range(0, records):
            print(f"{library_num[i]:20}  {title[i]:35}  {author[i]:25}  {genre[i]:20} {pg_count[i]:20} {status[i]}")

("-----------------------------------------------------------------------------------------------------------------------------------------------------\n")
def swap(i, listName):
    temp = listName[i]
    listName[i] = listName[i + 1]
    listName[i + 1] = temp


def seqSearch(search, listname):
    for i in range(0, len(listname)):
        if search.lower() in listname[i].lower():
            found.append(i)
        if not found: #If found list is still empty
                print(f"Sorry, your search for {search} came up empty :[")

        else:
            #call display() to show the values
            print(f"{search} was found!")
            display("x", len(found))

#--MAIN EXECUTING CODE-------------------------------------------------------------------

library_num = []
title = [] 
author = []
genre = []
pg_count = []
status = []


found = []

with open("text_files/book_list.csv") as csvfile: 
    file = csv.reader(csvfile)

    for rec in file:
        library_num.append(rec[0])
        title.append(rec[1])
        author.append(rec[2])
        genre.append(rec[3])
        pg_count.append(rec[4])
        status.append(rec[5])

#disconnected from file------------------------------------

#List storing the menu choices
menu_options = ["1", "2", "3", "4", "5", "6," "7", "8"]

ans = input("Would you like to enter the search program? [y/n]").lower()

#validity and user error trap loop
while ans != "y" and ans != "n":
    print("***INVALID ENTRY!***")
    ans = input("Would you like to enter the search program? [y/n]: ").lower()

#main searching loop
while ans == "y":
    found = [] #resets found list so each new menu/search it is empty

    print("\tSEARCHING MENU")
    print("1. Search All Titles") #Lists all book to user
    print("2. Search by Title") #Search book by title
    print("3. Search by Author") #Search book by author
    print("4. Search by Genre") #Search book by genre
    print("5. Search by Library Number") #Search book by library number
    print("6. Search by All Available") #Search book by all available books
    print("7. Search by All On-Loan") #Search book by all books on-loan
    print("8. EXIT")

    search_type = input("\nHow would you like to search today? [1-8]: ")

    #using 'not in' for user validity checks
    if search_type not in menu_options:
         print("***INVALID ENTRY!***\nPlease try again")
    
    elif search_type == "1":
        print(f"\nYou have chosen to search for All Titles.")
        
        #Bubble Sort --> higher values 'bubble' to the bottom of the collection
        
        for i in range(0,len(library_num)-1):
            for j in range(0, len(library_num)-1):
                if library_num[j] > library_num[j + 1]:
                    #they must swap places becuase the higher value must come afterwards
                    temp = library_num[j]
                    library_num[j] = library_num [j + 1]
                    library_num[j + 1] = temp

                    #use the function to cut down on coding and potential errors! 
                    swap(j, title)
                    swap(j, author)
                    swap(j, genre)
                    swap(j, pg_count)
                    swap(j, status)
     
        #display whole list data to user
        display("x",len(library_num)) #practice with function

    
    elif search_type == "2":
        print(f"\nYou have chosen to search by Title.")

        #allow the user to search for a certain TYPE and then display ALL records (multi) with that type
        search = input("Enter Book Title or Keyword to search:\n").lower()
            #Sequential Search for MULTIPLE search term
        

        for i in range(0,len(title)):
            if search.lower() == title[i].lower():
                found.append(i) #add current index (location) of found item to the 'found' list 

            #display results
            if not found: #If found list is still empty
                print(f"Sorry, your search for {search} came up empty :[")

            else:
                #call display() to show the values
                print(f"{search} was found!")
                display("x", len(found))

    elif search_type == "3":
        print(f"\nYou have chosen to search for Authors Name.")

        search = input("Enter the Author's Name:\n").lower()

        seqSearch(search,author)  

    elif search_type == "4":
        print(f"\nYou have chosen to search for Genres.")

        search = input("Enter the book Genre:\n").lower()

        seqSearch(search,genre) 

    elif search_type == "5":
        print(f"\nYou have chosen to search by Library Number.")


        #allow the user to search for ONE specific and unique name value (binary search!)
        search = input("Enter the Library Number you are looking for: ")
        #BINARY SEARCH: 
        #Bubble Sort --> higher values 'bubble' to the bottom of the collection
        for i in range(0,len(library_num)-1):
            for j in range(0, len(library_num)-1):
                if library_num[j] > library_num[j + 1]:
                    #they must swap places becuase the higher value must come afterwards
                    temp = library_num[j]
                    library_num[j] = library_num [j + 1]
                    library_num[j + 1] = temp

                    #use the function to cut down on coding and potential errors! 
                    swap(j, title)
                    swap(j, author)
                    swap(j, genre)
                    swap(j, pg_count)
                    swap(j, status)

        #check our bubble sort -- sorting in ascending order by name 
        display("x", len(library_num))

        #Binary Search: must be preformed on ordered or sorted lists
        #values - only find ONE item or value

        min = 0 #lowest possible index
        max = len(library_num) - 1 #highest index
        mid = int((min + max) / 2) #middle index in sorted list

        while min < max and search.lower() != library_num[mid].lower():
            #while above is true, list is not yet exhausted and we haven't found what we are lookinf for so, must go through another search iteration!
            if search.lower() < library_num[mid].lower():    
                max = mid + 1
            else:
                #search > name[mid]
                mid = mid + 1
        
            mid = int((min + max) / 2)
        
        if search.lower() == library_num[mid].lower():
            print(f"Huzzah! We have found your search for {search}, see details below:")
            display(mid, len(library_num))
        else:
            print(f"Sorry, we could not find your search for {search}. Please try again.")
        



        
    elif search_type == "6":
        print(f"\nYou have chosen to search by All-Available Books.")

        for i in range(0, len(status)):
            if status == "available":
                print
      
        
       

    elif search_type == "8":
        print(f"\nYou have chosen to EXIT")
        ans = "N"
    
    else:
        print("***INVALID INPUT***")

#alert user that program is about to end
print("Thank you for using my program, goodbye!\n")
