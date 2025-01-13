#Jayda Bowe
#W1D2 Lab #1
#1-12-2025 [W1D2]

#PROGRAM PROMPT: You will be writing one Python file for this project - it is a program that determines whether a
#meeting room is in violation of fire regulations regarding the maximum room capacity. The
#program will accept the maximum room capacity and the number of people attending the
#meeting. If the number of people is less than or equal to the maximum room capacity, the
#program announces that it is legal to hold the meeting and tells how many additional people may
#legally attend. If the number of people exceeds the maximum room capacity, the program
#announces that the meeting cannot be held as planned due to the fire regulation and tells how
#many people must be excluded in order to meet the fire regulations. The user should be allowed
#to enter and check as many rooms as they would like without exiting the program. 

#VARIABLE DICTIONARY
#people - the amount of people attending the meeting
#max_cap - Max room capacity
#space_left - The space remaining in the room]
#space_needed - space needed for room to adhere to safety protocol
#difference - function used to calculate if the number of people adheres to fire safety
#response - if user wants to use the program again
#decision - function that shows if user has entered appropriate information
#name - name of meeting

#--------IMPORTS----------------------------------------------

#--------FUNCTIONS--------------------------------------------

#Calculates if the number of people adheres to fire safety
def difference(people, max_cap):
    space_left = people - max_cap
    space_needed = max_cap - people
    if space_left >= 0:
        print("Your meeting adheres to fire safety.")
        print(f"You can add {space_left} people to the meeting.")
    else:
        print("Your meeting does not adhere to fire safety, it is not legal.")   
        print(f"{space_needed} people need to removed to adhere to fire safety protocols.") 

#Shows if user has entered appropriate information
def decision(response): 
  
    #User error trap loop - ensures user provides valid value

    while response != "y" and response != "n":
        print("***INVALID ENTRY!***")
        response = input("\t\tWould you like to check another room? [y/n]: ").lower()
    
    return response #this value will replace the function call in the main code
  

#--------MAIN EXECUTING CODE----------------------------------

#Welcome Statement
print("Welcome to my fire regulation program!")

response = "y"

#Loop responsible for allowing users to input as many rooms as they want
while response == "y":
    name = input("Enter the meeting name :")

    max_cap = int(input("Enter the maximum room capacity: "))

    people = int(input("Enter the number of people attending the meeting: "))

    difference(max_cap, people)

    response = input("\t\tWould you like to check another room? [y/n]: ").lower()

    decision(response)

#End of program
print("Thank you for using my program. Goodbye!")    