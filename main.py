# Integers
number_of_donuts = 12
print(number_of_donuts)

# Booleans
donuts_exist = False
print(donuts_exist)

# Strings
donut_name = "Chocolate Glaze"
print(donut_name)

print("\nThis will print on the next line")
print("\tThis is tabbed in")
print("\"This will put quotation marks in your sting\"")

greetings = "Hello World!"
intro = "I'm a computer."
print(greetings + " " + intro)

name = input("Enter the character's name: ")
age = input("Enter the character's age: ")
species = input("Enter the character's species: ")
world = input("Enter the world that the character lives in: ")
hobby = input("Enter the character's hobby: ")

print("Name: " + name)
print("Age: " + age + " years old")
print("Species: " + species)
print("World: " + world)
print("Hobby: " + hobby)

age = 16
if (age >= 5) and (age < 12):
    print("You must be in elementary school.")
elif (age >= 12) and (age < 15):
    print("You must be in middle school.")
else:
    print("You must be in high school!")

number_of_leaves = 14
for x in range(0, number_of_leaves):
    print("A leaf fell to the ground " + str(x) + " leaves have fallen.")
    print("All the leaves fell. For loop complete.")

guessed = False
while not guessed:
    password = input("Enter a password: ")
    if password == "PythonCoding":
        guessed = True
        print("Access Granted!")
    else:
        print("Access Denied! Try again!")

import random
print("Rolling the Dice!")
rand_num = random.randint(1, 6)
print(rand_num)

import random
def random_number(max_int):
    print("Rolling the Dice!")
    rand_num = random.randint(1, max_int)
    return rand_num

