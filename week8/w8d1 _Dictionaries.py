#W8D1 - Introduction

#Dictionaries in Python are a collection set sumilar to associative arrays in JavaScript


#----Imports---------------------------------------------------------------


#----Main Executing Code---------------------------------------------------


#start creating a populated dictionary

myCar = {
    #'key' : value,
    "make" : "Ford",
    "model" : "Focus SE Hatchback",
    "year" : 2014,
    "name" : "Gwendoline",
    "color" : "black",

    #key names CANNOT be repeated / NO DUPLICATES of keys! It will skip the first definiton and print the second value
    "color" : "red"
}

#view the entire dictionary and all of its data
print(myCar)

#view specific value from the dictionary --> name[key] --> value
print(f"My car is a {myCar["make"]} {myCar["model"]}. It is {myCar["color"]}.")

yourCar = {
    #'key' : value,
    "make" : "Ford",
    "model" : "F-150",
    "year" : 2024,
    "name" : "Gandalf",
    "color" : "black",
    "friend" : ["Tyler", "Tony", "Steve"]
}

print(f"My car is a {yourCar["make"]} {yourCar["model"]}. It is {yourCar["color"]}.")

#add some data to a dictionary one created
yourCar["plate"] = "12345"

#or use the .update({key:value}) method
yourCar.update({"wheels" : "4"})

for key in yourCar:
    #for every key stored to the yourCar dicitionary
    print(f"{key.upper():10}\t {yourCar[key]}")
