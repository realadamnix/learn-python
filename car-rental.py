"""
This is a car rental example program in python
Copyright Adam Nix 
"""

Ford = 1
Honda = 2
Toyota = 3

print("Welcome to our car rental service!")
print("Please select a car brand:")
print("1. Ford")
print("2. Honda")
print("3. Toyota")


while True:
    choice = int(input("Please enter your choice: "))

    if choice == Ford:
        print("You have selected Ford")
        break
    if choice == Honda:
        print("You have selected Honda")
        break
    if choice == Toyota:
        print("You have selected Toyota")
        break
    else:
        print("Invalid choice (please select 1, 2, or 3)")
    
        Cost = "days is $"


Cost = "days is $"

if choice == Ford:
    print("The cost of renting a Ford is $20 per day")

if choice == Honda:
    print("The cost of renting a Honda is $25 per day")

if choice == Toyota:
    print("The cost of renting a Toyota is $30 per day")

days = int(input("How many days would you like to rent the car for?: "))

if choice == Ford:
    total = days * 20
    print("The total cost of renting a Ford for", days, Cost, total)

if choice == Honda:
    total = days * 25
    print("The total cost of renting a Honda for", days, Cost, total)

if choice == Toyota:
    total = days * 30
    print("The total cost of renting a Toyota for", days, Cost, total)

print("Thank you for using our car rental service!")