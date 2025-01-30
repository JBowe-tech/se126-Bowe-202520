#Jayda Bowe
#Jan 23rd 2025
#W3D2 - List Review - 1 Dimensional Lists & Parallel Lists

#Prompt: We will continue to work with the class_grades.csv file, as used in the W3D2 demo. We will practice connecting to a file, storing the file data into parallel lists, and creating new data for each student record based on these lists. We will then build a sequential search program which will allow us to find students in the file, and write data regarding them to a newly created file in our repository.

 

#this file uses: class_grade.csv

#--IMPORTS--------------------------------------------------------------------------------------------------
import csv

#--FUNCTIONS--------------------------------------------------------------------------------------------------
def letter(num):
    if num >= 90:
        let = "A"
    elif num >= 80:
        let = "B"
    elif num >= 70:
        let = "C"
    elif num >= 60:
        let = "D"
    elif num < 60:
        let = "F"
    else:
        let = "***ERROR***"


    return let #the value stored to 'let' will literally replace the letter() call in main code


#--MAIN EXECUTING CODE--------------------------------------------------------------------------------------------------


#create some empty lists - one list for every potential list in the file

total_records = 0

#create an empty or populated list for every potential field
firstName = []
lastName = []
test1 = []
test2 = []
test3 = []



#connecting to the file----------------
with open("text_files/class_grades.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        
        total_records += 1

        #fname = rec[0] 

        #print(fname)

        #store data from current record to corresponding lists (each field is its own!)
        #.append() --> adds the data to the next available space in the list (end)

        #parallel lists --> data dispersed across lists, connected by the same index 
        firstName.append(rec[0])
        lastName.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))


#disconnected from the file ---------------------------------------------------------------------------------------------


#process the lists to create and store each student's numeric average as well as a letter grade average, then display all data to user


num_avg = []        #holds student's numeric avg: (test1 + test2 + test3 ) / 3
let_avg = []        #holds student's letter avg: letter(num_avg) return

for i in range(0,len(firstName)):
    a = (test1[i] + test2[i] + test3[i]) / 3
    num_avg.append(a)


    let_avg.append(letter(a))


#print field headers for display below
print(f"{'First':10} {'Last':10} {'T1':3} {'T2':3} {'T3':3} {'# AVG':6} {'L AVG'}")
print("-------------------------------------------------------------------------------------------------------------------------------------------")


#processing through lists for display
for i in range(0, len(firstName)):
    print(f"{firstName[i]:10} {lastName[i]:10} {test1[i]:3} {test2[i]:3} {test3[i]:3} {num_avg[i]:6.1f} {let_avg[i]}")

print("-------------------------------------------------------------------------------------------------------------------------------------------")
print(f"TOTAL STUDENTS IM FILE: {len(firstName)}") #You can use any list as they are all parallel and show the same total amount


#sequentail search - search for a student by their LAST name

#Step 1: Set-up and gain search query

found = -1
answer = "y"

while answer == "y":
    print(f"------MENU------\n1.Last Name \n2.First Name \n3.Letter Grade")
    search = input("Enter the menu option you wish to find: ") #name we are looking for 

    if search == "Last Name":
    #Step 2: Perform search algo (seq. search -> for loop w/ if statemnt)
        for i in range(0, len(lastName)):
        #for loop performs the SEQUENCE - from start through end of list items

            if search.lower() == lastName[i].lower(): 
            #if performs the SEARCH - is what we're looking for here in the list?
                found = i #stores found item's INDEX LOCATION

    
    #Step 2: Perform search algo (seq. search -> for loop w/ if statemnt)
    elif search == "First Name":
        for i in range(0, len(firstName)):
        #for loop performs the SEQUENCE - from start through end of list items

        if search.lower() == firstName[i].lower(): 
            #if performs the SEARCH - is what we're looking for here in the list?
            found = i #stores found item's INDEX LOCATION

    
    #Step 2: Perform search algo (seq. search -> for loop w/ if statemnt)
    for i in range(0, len(let_avg)):
        #for loop performs the SEQUENCE - from start through end of list items

        if search.lower() == let_avg[i].lower(): 
            #if performs the SEARCH - is what we're looking for here in the list?
            found = i #stores found item's INDEX LOCATION



    #Step 3: display results to user; make sure you give info: both for found or NOT found

    if found != -1:
        #last name FOUND!

        print(f"Your search for {search} was FOUND! Here is their data:")
        print(f"{firstName[found]:10} {lastName[found]:10} {test1[found]:3} {test2[found]:3} {test3[found]:3} {num_avg[found]:6.1f} {let_avg[found]}")
    else:
        #NOT FOUND
        print(f"Your search for {search} was NOT FOUND!")
        print("Check your cAsiNg and SpeLlINg and try again!")

        answer = input("Would you like to search something else? [y/n]").lower()
