#Jayda Bowe
#Jan 30 2025
#W4D2 - This is a two-part program where you will work on creating and populating parallel lists based on file data, then create and write data to a file.

#Variable Dictionary


#--IMPORTS------------------------------------------------------------------------------------------------------------
import csv

import random

#--FUNCTIONS-----------------------------------------------------------------------------------------------------------


#--MAIN EXECUTING CODE--------------------------------------------------------------------------------------------------

firstname = []
lastname = []
age = []
screen_name = []
house = []
emails = []
extensions = []
departments = []

with open("text_files\got_emails.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:

        firstname.append(rec[0])
        lastname.append(rec[1])
        age.append(rec[2])
        screen_name.append(rec[3])
        house.append(rec[4])



#disconnected from the file------------------------------------------------------------------------------------------------

for i in range(0,len(firstname)):
    #Email Addresses
    address = (f"{screen_name[i]}@westeros.net")

    emails.append(address)

    #Phone Extensions
    
    if house[i] == "House Stark":
        extensions.append((random.randrange(100, 199))) 
    
    elif house[i] == "House Targaryen":
        extensions.append((random.randrange(200, 299))) 
    
    elif house[i] == "House Tully":
        extensions.append((random.randrange(300, 399))) 
    
    elif house[i] == "House Lannister":
        extensions.append((random.randrange(400, 499))) 
    
    elif house[i] == "House Baratheon":
        extensions.append((random.randrange(500, 599))) 
    
    elif house[i] == "The Night's Watch":
        extensions.append((random.randrange(600, 699))) 
    else:
        print("No extenstion found")
    
    #Departments

    if house[i] == "House Stark":
        departments.append("Research & Development") 
    
    elif house[i] == "House Targaryen":
        departments.append("Marketing") 
    
    elif house[i] == "House Tully":
        departments.append("Human Resources") 
    
    elif house[i] == "House Lannister":
        departments.append("Accounting") 
    
    elif house[i] == "House Baratheon":
        departments.append("Sales") 
    
    elif house[i] == "The Night's Watch":
        departments.append("Auditing") 
    else:
        print("Department not found")
    


print(f"{'FIRST':8}  {'LAST':10}  {'EMAIL':30}  {'DEPARTMENT':23}  {'EXT':3}")
print("-----------------------------------------------------------------------------------------------------")
for i in range(0, len(firstname)):

    print(f"{firstname[i]:8}  {lastname[i]:10}  {emails[i]:30}  {departments[i]:23}  {extensions[i]:3}")
print("-----------------------------------------------------------------------------------------------------")


#Searching
print(f"Westeros Services Directory Search")

answer = input("Would you like to start your search [y/n]?: ").lower()

while answer == "y":
    #show user search menu
    print("\t~Search Menu~")
    print("1. Search by First Name")         #one search value found
    print("2. Search by Phone Extension")      #multiple searcg values found
    print("3. Search by Last Name")
    print("4. Search by Department")
    print("5. Exit")

    #gain search type
    search_type = input("Enter your search type [1-5]: ")

    #filter search options based on type
    if search_type == "1": #First Name
        

        print("\t~First Name Search~")
        #step 1: set-up and gain search query

        found = -1 #flag var, will be replaced with index position if name is found; we are using a -1 because it is not a valid index location
        search_first = input("Enter the first name you wish to find: ") #namewe are look for

        #step 2: perform search algo (seq. search -> for loop w/ if statement)
        for i in range(0, len(firstname)):
            #for loop performs the SEQUENCE - fromm start through end of list items

            if search_first.lower() == firstname[i].lower():
                #if performs the SEARCH - is what we're looking for here in the list?
                
                found = i #stores found item's INDEX LOCATION


        #step 3: display results to user; make sure you give info: both for found or NOT found
        if found != -1:
            #last name FOUND!

            print(f"Your search for {search_first} was FOUND! Here is their data: ")
            print(f"{firstname[found]:8}  {lastname[found]:10}  {emails[found]:30}  {departments[found]:23}  {extensions[found]:3}")


        else:
            #NOT FOUND!
            print(f"Your search for {search_first} was NOT FOUND!")
            print("Check your CasINg and spELLinG and try again!")


    elif search_type == "2": #LETTER GRADE
        print("\t~PHONE EXTENSION SEARCH~")

        #sequential search - search for a collection of students based on their Letter Grade Average
        #this version of sequential search is looking for MULTIPLE items, based on a specific letter grade

        #step 1: set-up and gain search query
        found = []  #empty list, found locations (index) will be stored if/when found
        search_ex = input("Enter the LETTER GRADE you wish to find: ") #grade we are looking through all students for

        #step 2: perform search algo (seq. search -> for loop w/ if statement)
        for i in range(0, len(extensions)):
            #for loop performs the SEQUENCE - from start through end of list items

            if search_ex.upper() == extensions[i]: 
                #if performs the SEARCH - is what we're looking for here in the list?
                found.append(i)  #stores found item's INDEX LOCATION to the found list because we may have multiple students whose letter grade fits the searched for grade
                print(f"Found a {search_ex} grade in INDEX {i}")

        #step 3: display results to user; make sure you give info: both for found or NOT found
        if not found: #'if not found' means 'found' is an EMPTY LIST
            #NOT found
            print(f"Your search for {search_ex} was NOT FOUND!")
            print("Check your cAsInG and sPeLlInG and try again!")
        else: 
            #last name FOUND!
            print(f"Your search for {search_ex} was FOUND! Here is their data: ")

            #'found' is a list populated with index locations - we loop through this list, and use found[i] (which again, holds an INDEX from our other searched-through list) to be recalled and used below
            for i in range(0, len(found)):
                 print(f"{firstname[found]:8}  {lastname[found]:10}  {emails[found]:30}  {departments[found]:23}  {extensions[found]:3}")
    
    elif search_type == "3":
         #sequential search - search for a student by their First name

        print("\t~Last Name Search~")
        #step 1: set-up and gain search query

        found = -1 
        search_last = input("Enter the last name you wish to find: ") 

        #step 2: perform search algo 
        for i in range(0, len(lastname)):
            #for loop performs the SEQUENCE - from start through end of list items

            if search_last.lower() == lastname[i].lower():
        
                
                found = i #stores found item's INDEX LOCATION


        #step 3: display results to user; make sure you give info: both for found or NOT found
        if found != -1:
            #First name FOUND!

            print(f"Your search for {search_last} was FOUND! Here is their data: ")
            print(f"{firstname[found]:8}  {lastname[found]:10}  {emails[found]:30}  {departments[found]:23}  {extensions[found]:3}")

        else:
            #NOT FOUND!
            print(f"Your search for {search_last} was NOT FOUND!")
            print("Check your CasINg and spELLinG and try again!")

    elif search_type == "4":
        print("\t~Department Search~")
        #step 1: set-up and gain search query

        found = -1 
        search_dep = input("Enter the department you wish to find: ") 

        #step 2: perform search algo 
        for i in range(0, len(departments)):
            #for loop performs the SEQUENCE - from start through end of list items

            if search_dep.lower() == departments[i].lower():
        
                
                found = i #stores found item's INDEX LOCATION


        #step 3: display results to user; make sure you give info: both for found or NOT found
        if found != -1:
            #First name FOUND!

            print(f"Your search for {search_dep} was FOUND! Here is their data: ")
            print(f"{firstname[found]:8}  {lastname[found]:10}  {emails[found]:30}  {departments[found]:23}  {extensions[found]:3}")
        
        else:
            #NOT FOUND!
            print(f"Your search for {search_dep} was NOT FOUND!")
            print("Check your CasINg and spELLinG and try again!")


    elif search_type == "5": #exit

        print("\t~EXIT~")
        answer = "x"
    else:
        print("\t!INVALID ENTRY!")
    
    #build a way out of the loop - answer should be able to change value! 
    if search_type == "1" or search_type == "2":
        #when search_type == "3" the user has chosen to exit, and if they did not provide a 1, 2, or 3 to search_type then they will automatically be brought back through the loop to see the menu again
        answer = input("Would you like to search again? [y/n]: ").lower()


print("\nThanks for using the search program. Goodbye!\n")  

file = open("text_files/westeros.csv", "w")

for i in range(0, len(firstname)):
    file.write(f"{firstname[i]},{lastname[i]},{emails[i]},{departments[i]},{extensions[i]}\n")

file.close()