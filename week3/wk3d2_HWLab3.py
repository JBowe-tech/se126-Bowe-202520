#Jayda Bowe
#Jan 26rd 2025
#W3D2 - HW Lab 3 Lab #3: 1D & Parallel Lists


#Prompt: his lab is a continuation of the Voter Registration Lab from SE116.  The original prompt is as follows:

#(Source: QBasic Fundamentals and Style, Quasney, Maniotes, Foremant; P. 190 #3)

#Construct a program that will analyze potential voters. The program should generate the following totals:

#Number of individuals not eligible to register.
#Number of individuals who are old enough to vote but have not registered.
#Number of individuals who are eligible to vote but did not vote.
#Number of individuals who did vote.
#Number of records processed.
 

#Variable - Dictionary:

#id - id number
#age - age of individual
#reg - if they're registered or not
#vote - if they voted or not
#young - count of those to young to vote
#n_reg - count of those not registered
#n_vote - count of those who did not vote
#y_vote - count of those who did vote

#--IMPORTS----------------------------------
import csv

#--MAIN EXECUTING CODE----------------------
# Create an empty list for every potential field
id = []
age = []
reg = []
vote = []

# Counters
young = 0              
n_reg = 0            
n_vote = 0            
y_vote = 0             
total_records = 0      

# Open the CSV file and read its contents
with open("text_files/voters_202040.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        # ID, Age, Registration, and Voting status
        id.append(int(rec[0]))
        age.append(int(rec[1]))
        reg.append(rec[2])  
        vote.append(rec[3])  

        # Count individuals under 18 
        if int(rec[1]) < 18:
            young += 1
        else:
            # Counts who are old enough but are not registered
            if rec[2] == 'N':
                n_reg += 1
            # Counts who are eligible but did not vote
            if rec[2] == 'Y' and rec[3] == 'N':
                n_vote += 1
            # Count individuals who did vote
            if rec[2] == 'Y' and rec[3] == 'Y':
                y_vote += 1

        total_records += 1

# Print the results
#disconnect from the file -- all file data is retained bc we are using lists
#Print Statements

print(f"\nINDEX {'#':10} : {'ID#':7}  {'AGE':4}  {'REG':5}  {'VOTE':6} ")
print("------------------------------------------------------------------------")
for index in range(0, len(id)): #len() --> length of collection, returns # of items
    print(f"INDEX {index:10} : {id[index]:5}  {age[index]:4}  {reg[index]:8}  {vote[index]}")
print("------------------------------------------------------------------------\n")

print(f"\nNo. of individuals not eligible to register: {young}")
print(f"No. of individuals who are old enough to vote but have not registered: {n_reg}")
print(f"No. of individuals who are eligible to vote but did not vote: {n_vote}")
print(f"No. of individuals who did vote: {y_vote}")
print(f"No. of records processed: {total_records}")








