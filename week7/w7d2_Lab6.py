#Jayda Bowe
#Feb 24 2025
#W7D2 - SE126_Lab6

#Prompt - For Lab #6, you must use lists to create the airplane seating chart - either 1D or 2D lists. You may either create a file to read the data in for the seats, or you can hand-populate your own 1/2D lists. If you choose to create your own file, please upload along with your completed Lab #6 .py file. 


#-----Functions------------------------------------------------------------------------------------------------------
def display():
    for i in range(len(seatA)):
        print(f"{i + 1} {seatA[i]} {seatB[i]} {seatC[i]} {seatD[i]}")

def ans(response): 
  
    #User error trap loop - ensures user provides valid value

    while response != "y" and response != "n":
        print("***INVALID ENTRY!***")
        response = input("Would you like to check another seat? [y/n]: ").lower()
    
    return response #this value will replace the function call in the main code

#-----Main Code------------------------------------------------------------------------------------------------------
print(f"Welcome to my seat booking program :D!\n")

seatA = ["A", "A", "A", "A", "A", "A", "A"]
seatB = ["B", "B", "B", "B", "B", "B", "B"]
seatC = ["C", "C", "C", "C", "C", "C", "C"]
seatD = ["D", "D", "D", "D", "D", "D", "D"]

response = "y"

while response == "y":

    display()

    row = int(input("Enter row #[1-7]: "))
    seat = input("Enter seat type [A/B/C/D]: ").upper()

    if seat.upper() == "A":
        if seatA[row - 1] != "X":
            seatA[row - 1] = "X"
        else: 
            seatA[row -1] = "X"
            print(f"Sorry, seat {row} {seat.upper()} is taken.")

    elif seat.upper() == "B":
        if seatB[row - 1] != "X":
            seatB[row - 1] = "X"
        else: 
            seatB[row -1] = "X"
            print(f"Sorry, seat {row} {seat.upper()} is taken.")

    elif seat.upper() == "C":
        if seatC[row - 1] != "X":
            seatC[row - 1] = "X"
        else: 
            seatC[row -1] = "X"
            print(f"Sorry, seat {row} {seat.upper()} is taken.")

    elif seat.upper() == "D":
        if seatD[row - 1] != "X":
            seatD[row - 1] = "X"
        else: 
            seatD[row -1] = "X"
            print(f"Sorry, seat {row} {seat.upper} is taken.")

    else:
        print(f"Sorry, we could not find this seat.")

    response = input("Would you like to check another seat? [y/n]: ").lower()

    ans(response)

print("Thank you for using my program!")
