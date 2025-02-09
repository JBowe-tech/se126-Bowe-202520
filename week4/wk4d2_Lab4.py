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

file = open("text_files/westeros.csv", "w")

for i in range(0, len(firstname)):
    file.write(f"{firstname[i]},{lastname[i]},{emails[i]},{departments[i]},{extensions[i]}\n")

file.close()