"""
This program allows the user to select a car brand (Ford, Honda, or Toyota) and the number of days they would like to rent the car for. The program then calculates the total cost of renting the car based on the selected brand and number of days.
copyright: Adam Nix (2024)
"""

ford = 1
honda = 2
toyota = 3

def choose_car():
    
    print("Welcome to our car rental service!")
    print("Please select a car brand:")
    print("1. Ford")
    print("2. Honda")
    print("3. Toyota")

    while True:
        choice = int(input("Please enter your choice: "))

        if choice == ford:
            print("You have selected Ford")
            break
        elif choice == honda:
            print("You have selected Honda")
            break
        elif choice == toyota:
            print("You have selected Toyota")
            break
        else:
            print("Invalid choice (please select 1, 2, or 3)")
        
    return choice

choice = choose_car()

def calculate_total_cost(choice, days, tax=0.2):
    
    
    if choice == ford:
        print("The cost of renting a Ford is $20 per day")
        total = days * 20 * (1 + tax) 
        print("The total cost of renting a Ford for", days, "days is $", total)
        
    elif choice == honda:
        print("The cost of renting a Honda is $25 per day")
        total = days * 25 * (1 + tax)
        print("The total cost of renting a Honda for", days, "days is $", total)
        
    elif choice == toyota:
        print("The cost of renting a Toyota is $30 per day")
        total = days * 30  * (1 + tax)
        print("The total cost of renting a Toyota for", days, "days is $", total)

days = int(input("Please enter the number of days you would like to rent the car for (20% tax): "))

calculate_total_cost(choice, days)

print("Thank you for using our car rental service!")
