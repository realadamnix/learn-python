"""
Thos program converts temperature from Celsius to Fahrenheit and vice versa.
The user is presented with a menu system that allows them to select the conversion they would like to perform.
The program then prompts the user to enter the temperature they would like to convert and displays the result.
Copyright: Adam Nix (2024)
"""


def menu_system():
    """
    Displays the menu system and returns the user's choice.
    """

    print(
        "welcome to my temperature converter. Please enter an option for the following list "
    )
    print("select 1 for °C to °F")
    print("select 2 for °F to °C")

    while True:
        try:
            choice = int(input("Please enter your choice: "))
        except ValueError:
            print("Invalid choice (please select 1 or 2)")
            continue                                                            
        if choice == 1:
            print("You have selected °C to °F")
            return celsius_to_fahrenheit()
        elif choice == 2:
            print("You have selected °F to °C")
            return fahrenheit_to_celsius()
        else:
            print("Invalid choice (please select 1 or 2)")


def celsius_to_fahrenheit():
    """
    Converts temperature from Celsius to Fahrenheit.
    """
    celsius = float(input("Please enter the temperature in Celsius: "))
    fahrenheit = round((celsius * 9 / 5) + 32, 2)
    print("The temperature in Fahrenheit is", fahrenheit, "°F")


def fahrenheit_to_celsius():
    """
    Converts temperature from Fahrenheit to Celsius.
    """
    fahrenheit = float(input("Please enter the temperature in Fahrenheit: "))
    celsius = round((fahrenheit - 32) * 5 / 9, 2)
    print("The temperature in Celsius is", celsius, "°C")


if __name__ == "__main__":
    menu_system()
