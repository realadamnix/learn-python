"""
This program allows the user to select a car brand (Ford, Honda, or Toyota) and the number of days they would like to rent the car for. The program then calculates the total cost of renting the car based on the selected brand and number of days.
copyright: Adam Nix (2024)
"""

car_names = ["Ford", "Honda", "Toyota"]
car_costs = [20, 25, 30]


def choose_car() -> int:

    print("Welcome to our car rental service!")
    print("Please select a car brand:")
    for index, car in enumerate(car_names):
        print(f"{index+1}. {car}")

    while True:
        choice = int(input("Please enter your choice: "))
        if choice <= 0 or choice > 3:
            print("Invalid choice (please select 1, 2, or 3)")
        else:
            print(f"You have selected {car_names[choice-1]}")
            return choice


def calculate_total_cost(days, choice, tax=0.2):

    print(
        f"The cost of renting a {car_names[choice-1]} is ${car_costs[choice-1]} per day"
    )
    total = days * car_costs[choice - 1] * (1 + tax)
    print(
        f"The total cost of renting a {car_names[choice-1]} for {days} days is ${total}"
    )


def main():
    choice = choose_car()
    days = int(
        input(
            "Please enter the number of days you would like to rent the car for (20% tax): "
        )
    )
    calculate_total_cost(days, choice)

    print("Thank you for using our car rental service!")


if __name__ == "__main__":
    main()
           