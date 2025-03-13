#Jayda Bowe
#March 12th 2025
#SE 126 - Intermediate Programming with Python
#Final Project
#This is an item shop rpg where you either enter as the shopkeeper or a cuustomer.


# Imports-----------------
from os import system, name
import csv
import random

# Function to clear the screen based on OS
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def wrong():
    # Error message for invalid input
    print("**I think you did something wrong...the shopkeeper is staring at you funny...")

# Function to display the welcome message
def welcome_message():
    print("Scenario: You've been traveling for some time now, your food's low, your clothes are torn and it's unlikely you'll survive another night out here without a weapon...")
    print("It's been so long since you've had a drink of...anything that you're starting to see things...it almost looks like there's a shop here in the middle of nowhere...wait...")
    print("There really is a shop here in the middle of nowhere...huh... well...\n")

#Bubble sort function
def swap(index, listName):
    temp = listName[index]
    listName[index] = listName[index + 1]
    listName[index + 1] = temp

#-------------------------------------------Main Code-------------------------------------------

clear()
names = []
cost = []
stock = []
found = []

# Gaining data from a text file 
with open("text_files/finals.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        names.append(rec[0])
        cost.append(int(rec[1]))
        stock.append(rec[2])

# Dictionary to store items and their costs
item_costs = {      # Dictionary to store items and their costs
    "1": 200,  # Cursed Fruit
    "2": 150,  # Eyes of the Undead
    "3": 300,  # Phantom's Cloak
    "4": 250,  # Banshee's Mask
    "5": 100,  # Vial of Witch's Breath
    "6": 180,  # Spider Silk Rope
    "7": 220,  # Fleshbound Tome
    "8": 170,  # Ectoplasm Potion
    "9": 90,   # Boneblade Dagger
    "10": 50,  # Mummified Hand Skewer
    "11": 350, # Green Liquid
    "12": 400, # Ghostly Steed Figurine
    "13": 75,  # Shadow Berries
    "14": 500, # Dragon's Blood Elixir
    "15": 130  # Witch's Eyeballs
}

#Dictionary to store the stock
inventory = {
    "Cursed Fruit" : 200,
    "Eyes of the Undead" : 150,
    "Phantom's Cloak": 300,
    "Banshee's Mask": 250,
    "Vial of Witch's Breath": 100,
    "Spider Silk Rope": 180,
    "Fleshbound Tome":220,
    "Ectoplasm Soda": 170,
    "Boneblade Dagger": 90,
    "Mummified Hand on a Skewer": 50,
    "Green Liquid": 350,
    "Ghostly Steed Figurine": 400,
    "Shadow Berries": 75,
    "Dragon's Blood Elixir": 500,
    "Witch's Eyeballs": 130

}

# Dictionary to store item names
item_names_dict = {
    "1": "Cursed Fruit",
    "2": "Eyes of the Undead",
    "3": "Phantom's Cloak",
    "4": "Banshee's Mask",
    "5": "Vial of Witch's Breath",
    "6": "Spider Silk Rope",
    "7": "Fleshbound Tome",
    "8": "Ectoplasm Soda",
    "9": "Boneblade Dagger",
    "10": "Mummified Hand on a Skewer",
    "11": "Green Liquid",
    "12": "Ghostly Steed Figurine",
    "13": "Shadow Berries",
    "14": "Dragon's Blood Elixir",
    "15": "Witch's Eyeballs"
}

total = 0
total_items = 0
#Defined Lists
item_names = []
item_prices = []
#Random money generator
money_ran = random.randrange(500, 1500)

#User choice to be customer or shopkeeper
user = input("Are you the customer or shopkeeper?[Customer/Shopkeeper]: ").lower()

#If statement for if they choose customer
if user == "customer":
    welcome_message()
    answer = input("**Will you enter?** [Y/N]: ").lower()

    while answer == "y":
        clear()       
        

        print("Shopkeeper: WELCOME TRAVELLER! Take a look around!")
        print(f"Don't forget you only have {money_ran} gold.")

        print(f"\nINDEX {'#':3} : {'Name':28}  {'Cost':3}   ")
        print("------------------------------------------------------------------------")
        for index in range(len(names)):
            print(f"Item# {index+1:2} : {names[index]:28}  {cost[index]:3}  ")
        print("--------------------------------------------------------------------------------\n")
        
        item_name = input("What item are you purchasing?[Enter item number 1-15]: ")

        if item_name in item_costs:
            cost_value = item_costs[item_name]
            total += cost_value
            total_items += 1
            item_names.append(item_names_dict[item_name])
            item_prices.append(cost_value)

    # If statements that display depending on which item is selected
            if item_name == "1":
                print("\nYou've chosen Cursed Fruit! This item costs 200 gold. It has an unsettling glow. \n**What can I even tell you at this point? You're going to be cursed if you eat that...you were already unlucky enough to end up here...please just throw it away...**")
            elif item_name == "2":
                print("\nYou've chosen Eyes of the Undead! This item costs 150 gold. These eyes are still alive...watching. \n**Why does this shop have so much severed eyes? Why are they still moving??? WHY ARE YOU STILL HERE???**")
            elif item_name == "3":
                print("\nYou've chosen Phantom's Cloak! This item costs 300 gold. It whispers in the darkness. \n**Great just what you needed more voices in your head.**")
            elif item_name == "4":
                print("\nYou've chosen Banshee's Mask! This item costs 250 gold. The mask seems to hum with the sound of distant wailing. So unsettling most creatures probably won't bother you while wearing it. \n**If you're willing to buy this mask then I'm sure you have no one around you to scare away anyway.**")
            elif item_name == "5":
                print("\nYou've chosen Vial of Witch's Breath! This item costs 100 gold. The vapors seem to claw at your lungs. \n**Why do you want someone's breathe...Creep.**")
            elif item_name == "6":
                print("\nYou've chosen Spider Silk Rope! This item costs 180 gold. It's unnervingly smooth, like a web. \n**It's comfortable. This is a good purchase.**")
            elif item_name == "7":
                print("\nYou've chosen Fleshbound Tome! This item costs 220 gold. The pages pulse with blood. \n**I can't express my disapointment in words.** ")
            elif item_name == "8":
                print("\nYou've chosen Ectoplasm Soda! This item costs 170 gold. It's a sickly, glowing blue liquid. \n**Don't be suprised if you turn into a ghost drinking this.**")
            elif item_name == "9":
                print("\nYou've chosen Boneblade Dagger! This item costs 90 gold. The hilt is made from a human femur. \n**I mean...a weapon's a weapon I guess. It's pretty cool if you don't ask questions.**")
            elif item_name == "10":
                print("\nYou've chosen Mummified Hand on a Skewer! This item costs 50 gold. It twitches as if it's still alive. \n**Is...this supposed to be food?**")
            elif item_name == "11":
                print("\nYou've chosen Green Liquid! This item costs 350 gold. The item isn't named it's just green liquid. \n**I guess your that desperate aren't you?**")
            elif item_name == "12":
                print("\nYou've chosen Ghostly Steed Figurine! This item costs 400 gold. The steed seems to shift and shimmer in the light. \n**You don't need this but, it's not a bad purchase...wait 400 gold? Can you even afford this?**")
            elif item_name == "13":
                print("\nYou've chosen Shadow Berries! This item costs 75 gold. These berries seem to dissolve into shadows. \n**If you eat them fast maybe...actually don't eat these...**")
            elif item_name == "14":
                print("\nYou've chosen Dragon's Blood Elixir! This item costs 500 gold. It burns with the heat of a dragon's breath. \n**What do you even need this for? Maybe it can keep you warm if you survive drinking it.**")
            elif item_name == "15":
                print("\nYou've chosen Witch's Eyeballs! This item costs 130 gold. They glow with an unnatural light. \n**Did you honestly buy this...Shameful?**")        
        else:
            wrong()
        
        answer = input("Do you want to look around more?[Y/N]: ").lower()

    #Bill Summary
    print("\nThank you for your purchase! Here's your bill summary:\n")
    print("------------------------------------------------------------")
    for i in range(total_items):
        print(f"{item_names[i]}: {item_prices[i]} gold")

    print(f"\nTotal items purchased: {total_items}")
    print(f"Subtotal: {total} gold")

    if money_ran < total:
            print("Did you forget you only had this much! Uh...the shopkeeper looks kinda angry...")
            print("You get kicked out for being to poor. Now you will die out in the wilderness alone. Good job.")
    elif money_ran == total:
        print("Great! Just enough now let's get out of here!")
        print("\n**What a strange place...**\n")
        print("Hey wait...where's your money pouch?")
    else:
        change_due = money_ran - total
        print(f"Change: {change_due:.0f} gold")
        print("\n**What a strange place...**\n")
        print("Hey wait...where's your money pouch?")
#Elif statement for if user choose shopkeeper
elif user == "shopkeeper":
    print("You enter your shop after securing more...eyes from God knows where.")
    print("There's a little frog on your desk wearing a wizards hat. It's your helpful familiar Flibbers.\n")
    answer = input("Flibbers: Welcome back Keeper! Do you want to manage the shop?[Y/N]:\n").lower()

    while answer == "y":
        #Menu
        print("~Menu~")
        print("1. Find Item")
        print("2. Check Stock")
        print("3. Add an Item")
        
        choice = input("Flibbers: What will you do?[1-3]: ")
        print("Flibbers: Alright let's go!")

        if choice == "1":
            #Bubbele Sort -- *always sort before BINARY SEARCH!*
            for i in range(len(names) -1):
                for j in range(len(names) -1):
                    if names[j] > names [j + 1]:
                        #SWAP!
                        swap(j, names)
                        swap(j, cost)
                        swap(j, stock)
        
            #Binary Search
            print(f"\nINDEX {'#':3} : {'Name':28}  {'Cost':3}  {'Stock':10} ")
            print("------------------------------------------------------------------------")
            for index in range(len(names)):
                print(f"Item# {index+1:2} : {names[index]:28}  {cost[index]:3} {stock[index]:10}  ")
            print("--------------------------------------------------------------------------------\n")
            
            search = input("Flibbers: You're looking for an item? Alright what item are you looking for?: ").lower()

            min = 0                         #FIRST INDEX
            max = len(names)-1              #LAST INDEX
            mid = int((min + max)/2)        #MIDDLE INDEX

            while min < max and search.lower() !=names[mid].lower():
                if search.lower() < names[mid].lower():
                    max = mid-1
                else:
                    #search.lower() > name[mid].lower()
                        min = mid + 1
                mid = int((min + max)/2)        
            if search.lower() == names[mid].lower():
                #FOUND IT!
                print(f"\nFlibbers: AH! I found {search}! Here's the information on this item: ")
                print(f"{'NAME':12} {'COST':3} {'STOCK':10}")
                print("--------------------------------------------------------------")
                print(f"{names[mid]:12} {cost[mid]:3} {stock[mid]:10}")
                print(f"--------------------------------------------------------------\n")
            else:
                print(f"\nFlibbers: Sorry shopkeeper we don't seem to have this item...have we even sold {search} here before?")
    

        elif choice == "2":
            search = input("Is it already time to get more items? Alright you should check what we need and what we don't. What do you want to check first?[Stocked/Out]:\n ").lower()
            found = []
        #Sequential Search 
            
            for i in range(0, len(names)):
                if search.lower() in stock[i].lower():
                    found.append(i)

            if not found: #if the found list is empty
                print(f"Flibbers: Sorry shopkeeper we don't seem to have this item...have we even sold {search} here before?\n")
            else:
                print("Flibbers: I found the list you were lookin for shopkeeper! Here ya go!")
                print(f"\n{'Name':28}  {'Cost':3} {'Stock'}  ")

                for i in range (0, len(found)):
                    print(f"{names[found[i]]:28}  {cost[found[i]]:3}  {stock[found[i]]:3}")

        elif choice == "3":
            print("Flibbers: Did you get something new? What is it?")
            item = input("Flibbers: What's it called?: ")
            cost = input("TFlibbers: hat sounds...interesting...how much are we charging for it?: ")

            if item not in inventory:
                inventory.update({item : cost})
                print("-" * 180)
                print(f"{'ITEM':25} : {'COST'}")
                print("-" * 180)
        
                for key in stock:
                #for every key found in the library dictionary
                    print(f"{key.upper():25} : {inventory[key]}")
                    print("-" * 180)
        else:
            wrong()
        #Breaks Loop
        answer = input("Do you want to do something else?[Y/N]: ").lower()



