#Jayda Bowe
#W2D2 - Text File Handling Review
#1-16-2025 [W2D2]

#Program Prompt:The csv file classLab2.csv contains a list of rooms, the maximum number of people that the room
#can accommodate, and the number of people currently registered for the event. Write a program that
#displays all rooms that are over the maximum limit of people and the number of people that have to
#be notified that they will have to be put on the wait list. After the file is completely processed the
#program should display the number of records processed and the number of rooms that are over the
#limit.



#Variable Dictionary:

#difference - function that subtracts the people from the max amount of people
#diff - returned value from the difference function
#total_rec - total rooms in the file
#rooms_over - the rooms that go over room capacity
#file -  #allow the csv.reader() to access and read the file path; stores contents to 'file' [a 2D list/ matrix / table]
#name - name of room
#max - max amount of people
#ppl - the amount of people
#remaining - the remaining amount of people that can be in the room 




#--------IMPORTS-----------------------------------------------------
import csv

#--------FUNCTIONS----------------------------------------------------

def difference(people, max_cap):
    '''This function is passed two values and returns the difference between them.'''
    
    diff = max_cap - people

    return diff #this value will replace the difference() call in the main code


#--------MAIN EXECUTING CODE--------------------------------------------

#initialize needed counting vars

total_rec = 0

rooms_over = 0

#-----------connected to file-------------------------------------------
with open("text_files/classLab2-1.csv") as csvfile: 
    #we must indent one level while connected to the file

    file = csv.reader(csvfile)

    print(f"\n\n{'NAME':20}     {'MAX':5}     {'PPL':5}    {'OVER':5}")
    print("-------------------------------------------------------------")

    for rec in file:
        #below code occurs for very record (row)in the file (text file -> 2D list!)


        #assign each field data value to a friendly var name
        name = rec[0]
        max = int(rec[1])    #all text data read as a 
        ppl = int(rec[2])

        #call the difference() to find people over/under capacity
        remaining = difference(ppl,max)


        
        #count and display the rooms that are over capacity (remaining is negative)
        if remaining < 0:
            rooms_over += 1
            
            
            print(f"{name:20}    {max:5}    {ppl:5}    {abs(remaining):5}") #or multiply remaining * -1 to change the neg # to positives

        #count ALL rooms!
        total_rec += 1    





#disconnected from file--------------------------------------------------
#displays final data (counting vars)

print(f"\nRooms currently OVER capacity: {rooms_over}")

print(f"Total rooms in the file: {total_rec}")


