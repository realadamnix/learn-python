"""
This program allows the user to select a car brand (Ford, Honda, or Toyota) and the number of
days they would like to rent the car for. The program then calculates the total cost of renting
the car based on the selected brand and number of days.
Copyright: Adam Nix (2024)
"""

from types import SimpleNamespace

ford = SimpleNamespace(id=1, name="Ford", cost=20)
honda = SimpleNamespace(id=2, name="Honda", cost=25)
toyota = SimpleNamespace(id=3, name="Toyota", cost=30)

cars = [ford, honda, toyota]


def choose_car():
    """
    This function displays a list of car brands and asks the user to select a car brand.
    The function then returns the selected car brand.
    Extended description of function.


    Returns:
        _type_: _description_
    """

    print("Welcome to our car rental service!")
    print("Please select a car brand:")
    for car in cars:
        print(f"{car.id}. {car.name}")

    while True:
        choice = int(input("Please enter your choice: "))
        if choice <= 0 or choice > 3:
            print("Invalid choice (please select 1, 2, or 3)")
        else:
            return cars[choice - 1]


def calculate_total_cost(days, car, tax=0.2):
    """Calculate the total cost of renting a car for a given number of days.

    Args:
        days (_type_): _description_
        car (_type_): _description_
        tax (float, optional): _description_. Defaults to 0.2.
    """
    print(f"The cost of renting a {car.name} is ${car.cost} per day")
    total = days * car.cost * (1 + tax)
    print(f"The total cost of renting a {car.name} for {days} days is ${total}")


def main():
    """Main function of the program."""
    car = choose_car()
    print(f"You have selected {car.name}")
    days = int(
        input(
            "Please enter the number of days you would like to rent the car for (20% tax): "
        )
    )
    calculate_total_cost(days, car)

    print("Thank you for using our car rental service!")


if __name__ == "__main__":
    main()
