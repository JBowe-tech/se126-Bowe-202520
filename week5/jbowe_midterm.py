#Jayda Bowe
#Jan 30 2025
#MIDTERM - Using the file named above, read the data from the file and store to 1D parallel lists. Once the lists have
#been fully populated with file data, create a new list to hold an office number for each of the employees.
#Office numbers should start at 100 and not exceed 200. Assign each employee an office number and
#store to the newly created list, then process through the six lists to display all of the data to the user as
#well as the total number of records in the file.
#Once all of the data has been displayed, write all of the list data to a new file called
#‘midterm_choice1.csv’, where each employee’s information is found on one record in the file and their
#data is separated by a comma (additional empty line in resulting file is okay).
#Finally, create a sequential search program that allows a user to repeatedly search the employee
#information stored in the lists based on the following menu:
#Westeros Services Directory Search
#1. Search by EMAIL
#2. Search by DEPARTMENT
#3. EXIT
#For option 1: When a searched-for item is found, print all data* in the program on the specific employee
#from the lists. If they are not found, alert the user.
#For option 2: When a searched for item is found, print all data* in the program on all employees that
#match the criteria. If no one matches the searched-for criteria, alert the user.
#The user should not be able to quit the search program unless they choose option 3, to exit.
#*All Data to print per employee if found:
#first name, last name, email, department, phone extension, office number


#Variable Dictionary
#firstname - lists for storing first names from textfile
#lastname - lists for storing last names from textfile
#email - lists for storing emails from textfile
#department - lists for storing department names from textfile
#extention -lists for storing extensions from textfile
#office - lists for storing office numbers from textfile
#file - #allow the csv.reader() to access and read the file path; stores contents to 'file' [a 2D list/ matrix / table]
#found - #flag var, will be replaced with index position if name is found; we are using a -1 because it is not a valid index location
#search_email - used to find email
#serach - used to find department
#search_type - used to find out what user is searching for
#answer - used to find out if user is still using program or wants to use program


#--IMPORTS------------------------------------------------------------------------------------------------------------
import csv
import random

#--FUNCTIONS-----------------------------------------------------------------------------------------------------------

#--MAIN EXECUTING CODE--------------------------------------------------------------------------------------------------
#Lists
firstname = []
lastname = []
email = []
department = []
extension = []
office = []

with open("text_files\westeros.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        firstname.append(rec[0])
        lastname.append(rec[1])
        email.append(rec[2])
        department.append(rec[3])
        extension.append(rec[4])


#disconnected from the file--------------------------------
#print statements for header
print(f"{'FIRST':8}  {'LAST':10}  {'EMAIL':30}  {'DEPARTMENT':23}  {'EXT':7}  {'OFFICE#':6}")
print("-----------------------------------------------------------------------------------------------------")

for i in range(0,len(firstname)):
    
    office.append((random.randrange(100, 200))) 

    print(f"{firstname[i]:8}  {lastname[i]:10}  {email[i]:30}  {department[i]:23}  {extension[i]:6}  {office[i]:6}")

    
print("-----------------------------------------------------------------------------------------------------")
print(f"There are {len(firstname)} records in this file.")
print("-----------------------------------------------------------------------------------------------------")


#Creates new .csv file
file = open("text_files/miderm_choice1.csv", "w")

for i in range(0, len(firstname)):
    file.write(f"{firstname[i]},{lastname[i]},{email[i]},{department[i]},{extension[i]},{office[i]}\n")

file.close()


#Searching
print(f"~Westeros Services Directory Search~\n")

answer = input("Would you like to start your search [y/n]?: ").lower()

while answer == "y":
    #show user search menu
    print("\t~Search Menu~")
    print("1.Search by EMAIL")
    print("2.Search by Department")
    print("3.EXIT")

    search_type = input("What would you like to search for?[1-3]: ")

    if search_type == "1": #EMAIL
        

        print("\t~EMAIL SEARCH~")

        found = -1 
        search_email = input("Enter the email you wish to find: ") 

        
        for i in range(0, len(firstname)):
            

            if search_email.lower() == email[i].lower():
    
                found = i 

        if found != -1:
            
            print(f"Your search for {search_email} was FOUND! Here is their data: ")
            print(f"{'FIRST':8}  {'LAST':10}  {'EMAIL':30}  {'DEPARTMENT':23}  {'EXT':7}  {'OFFICE#':6}")
            print("-----------------------------------------------------------------------------------------------------")
            print(f"{firstname[found]:8}  {lastname[found]:10}  {email[found]:30}  {department[found]:23}  {extension[found]:6},{office[found]:6}\n")


        else:
            #Not found
            print(f"Your search for {search_email} was NOT FOUND!")
            print(f"Check your CasINg and spELLinG and try again!\n")
    
    elif search_type == "2": #DEPARTMENT
        print(f"\t~DEPARTMENT SEARCH~")

       
        found = []
        search = input("Enter the department you're looking for: ")

        for i in range(0, len(department)):
            if search.lower() in department[i].lower():
                found.append(i)

        print("Here is what the found list contains:")
        #for i in range(0, len(found)):
            
            
        if not found: #if the found list is empty
            print(f"Your search for {search} was not FOUND :[")
        else:
            print(f"Your search for {search} was FOUND! Here is their data:")
            print(f"{'FIRST':8}  {'LAST':10}  {'EMAIL':30}  {'DEPARTMENT':23}  {'EXT':7}  {'OFFICE#':6}")
            print("-----------------------------------------------------------------------------------------------------")
            for i in range (0, len(found)):
                print(f"{firstname[found[i]]:8} {lastname[found[i]]:10} {email[found[i]]:30} {department[found[i]]:23} {extension[found[i]]:6} {office[found[i]]:6}")


    elif search_type == "3": #exit

        print("\t~EXIT~")
        answer = "x"
    else:
        print(f"\t!INVALID ENTRY!\n")

    if search_type == "1" or search_type == "2":
        answer = input("Would you like to search again? [y/n]: ").lower()
    
#End of file
print("~ THANK YOU FOR USING MY PROGRAM! GOODBYE :D ~")