#Jayda Bowe
#February 27th 2025
#SE126 - Python
#W8D2

#Prompt - Build a mini programming dictionary a user can search through and ad to using the ad to using the words.csv file:Access the words.csv file and store the data to a dictionary, where each word in the file is a key of the dictionary and the value stored to each key is the word’s corresponding definition. Then, create a repeatable program that allows a user to interact with the dictionary based on the following menu.

#Variable Dictionary:
#library - list holding the 'keys' and 'values'
#ans - 'y' is the response used to exit the while loop
#menu - list holding the menu options
#choice - the choice of user from the menu given
#search - the word user chooses to find
#found - #flag var, will be replaced with index position if name is found; we are using a -1 because it is not a valid index location
#word - user added word to the dictionary
#meaning - the meaning user inputs for the word they add

#----Imports---------------------------------------------------------------
import csv

#----Fuctions--------------------------------------------------------------    
def swap(index, listName):
    temp = listName[index]
    listName[index] = listName[index + 1]
    listName[index + 1] = temp

#----Main Executing Code---------------------------------------------------
library = {}

names = []
defs = []

with open("text_files/words.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        #for every record in the file, do the following 
        #file --> 2D list; rec --> 1 record's data, also a list!
        library.update({rec[0] : rec[1]})
        names.append(rec[0])
        defs.append(rec[1])
          
        #library_num --> rec[0], a string
        #title --> rec[1], also a string

#disconnected from file-----------------------------------------------------
ans = "y"
menu = ['1', '2', '3', '4', '5']#menu choices

while ans == "y": #Looping containing all options for program
    print("My Programming Dictionary Menu")
    print("1. Show all words")      #Show all words and their definitions stored to the dictionary
    print("2. Search for a word")   #Allows the user to enter a word and if it is in the dictionary,shows its   definition and tells the user if the word is not in the dictionary
    print("3. Add a word")          #Allow a user to add a word and its definition to the dictionary if it does not already exist
    print("4. Sort list alphabetically in ascending order (A -> Z") 
    print("5. Exit")                #Allowes user to exit program

    choice = input("What would you like to do [1-5]?: ") #User choice

    if choice not in menu:
        print("!INVALID ENTRY!\nPlease try again.\n")

    elif choice == "1":
        print("\n~Show all words~")

        print(f"{'WORD':25} : {'DEFINITION'}")
        print("-" * 180)


        for key in library:
        #for every key found in the library dictionary
            print(f"{key.upper():25} : {library[key]}")
            print("-" * 180)

    elif choice == "2":
        print("\n~Search for a Word~")

        search = input("Enter the word you would like to search for?: ").lower()

        found = 0

        for key in library:
            if search.lower() == key.lower():
                found = key

        if found != 0:
            print(f"\nWe found your search for {search}, here is the info:\n")
            print("-" * 180)
            print(f"{found.upper():4} : {library[found]}")
            print("-" * 180)
        else:
            print(f"\nWe could not find your search for {search}.\n")

    elif choice == "3":
        print("\n~Add a Word~")

        word = input("Enter the word you would like to add: ")
        meaning = input("Enter the definition of the word you wish to add: ")

        if word not in library:
            library.update({word : meaning})
            print("-" * 180)
            print(f"{'WORD':25} : {'DEFINITION'}")
            print("-" * 180)
        
            for key in library:
            #for every key found in the library dictionary
                print(f"{key.upper():25} : {library[key]}")
                print("-" * 180)

    elif choice == "4":
         #Bubbele Sort -- *always sort before BINARY SEARCH!*
        for i in range(len(names) -1):
            for j in range(len(names) -1):
                if names[j] > names [j + 1]:
                    #SWAP!
                    swap(j, defs)
        
        print(f"{names:25} : {defs}")
        print("-" * 180)
                    

    elif choice == "5":
        print(f"\n~EXIT~")
        ans = "n"
    
    else:
        print("***INVALID ENTRY***")

print("\n~Thank you for using my program goodbye :D~")
    


