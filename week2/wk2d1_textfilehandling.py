#Jayda Bowe
#W2D1 - Text File Handling Intro Demo
#1-13-2025 [W2D1]

#Step 1: Import the csv (comma seperated value )libray

import csv

total_records = 0 #holds total num of recs in file

#Step 2: connect to file
#--connected to file----------------------------------------------------------------------
#include relative file path in open()
#male sure \ switches to /
with open("text_files/simple.csv") as csvfile:
    #make sure to indent inside of code block


    #allow the csv.reader() to access and read the file path; stores contents to 'file' [a 2D list/ matrix / table]
    file = csv.reader(csvfile)

    #print for headers
    print(f"{'NAME':10}  {'NUM':6} {'COLOR'}")
    


    #Step 3: process through every record (row) in the file
    for record in file:
        #add +1 to total_records to keep accurate count of recs
        total_records += 1

        #print(record) #entire record/ row data as a list

        name = record[0]    #name field
        number = record[1]  #number field
        color = record[2]   #color field

        print(f"{name:10}  {number:6}  {color.title()}")



#--disconnected from file----------------------------------------------------------------------
print(f"\nTOTAL RECORDS: {total_records}\n")