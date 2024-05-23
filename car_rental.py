"""
This program allows the user to select a car brand (Ford, Honda, or Toyota) and the number of days they would like to rent the car for. The program then calculates the total cost of renting the car based on the selected brand and number of days.
copyright: Adam Nix (2024)
"""

ford = 1
ford_name = "Ford"
honda = 2
honda_name = "Honda"
toyota = 3
toyota_name = "Toyota"

def choose_car() -> int:
    
    print("Welcome to our car rental service!")
    print("Please select a car brand:")
    print(f"{ford}. {ford_name}")
    print(f"{honda}. {honda_name}")
    print(f"{toyota}. {toyota_name}")

    while True:
        choice = int(input("Please enter your choice: "))

        if choice == ford:
            print("You have selected Ford")
            return choice
        elif choice == honda:
            print("You have selected Honda")
            return choice
        elif choice == toyota:
            print("You have selected Toyota")
            return choice
        else:
            print("Invalid choice (please select 1, 2, or 3)")
        


def calculate_total_cost(days, choice, tax=0.2):
    
    
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


def main():
    choice = choose_car()
    days = int(input("Please enter the number of days you would like to rent the car for (20% tax): "))
    calculate_total_cost(days, choice)

    print("Thank you for using our car rental service!")    

if __name__ == "__main__":
    main()