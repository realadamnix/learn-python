"""
This program allows the user to select an operation (addition, subtraction, multiplication
or division) and two numbers. The program then performs the selected operation on the two 
numbers and displays the result.

Copyright: Adam Nix (2024)
"""


def menu_system():
    """
    Displays the menu system and returns the user's choice.
    """
    print("welcome to the simple calculator")
    print("1. addition")
    print("2. subtraction")
    print("3. multiplication")
    print("4. division")
    print("5. exit")

    while True:
        choice = int(input("Please enter your choice: "))

        if choice == 1:
            print("You have selected addition")
            return addition()
        elif choice == 2:
            print("You have selected subtraction")
            return subtraction(choice)
        elif choice == 3:
            print("You have selected multiplication")
            return multiplication(choice)
        elif choice == 4:
            print("You have selected division")
            return division(choice)
        else:
            print("Invalid choice (please select 1, 2, 3, or 4)")


def addition():
    """
    Performs addition on two numbers.
    """
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))
    total = num1 + num2
    print("The result of adding", num1, "and", num2, "is", total)


def subtraction(choice, num1=None, num2=None):
    """
    Performs subtraction on two numbers.
    """
    if choice == 2:
        num1 = int(input("Please enter the first number: "))
        num2 = int(input("Please enter the second number: "))
    total = num1 - num2
    print("The result of subtracting", num1, "and", num2, "is", total)


def multiplication(choice, num1=None, num2=None):
    """
    Performs multiplication on two numbers. (Add logic here)
    """
    if choice == 3:
        num1 = int(input("Please enter the first number: "))
        num2 = int(input("Please enter the second number: "))
    total = num1 * num2
    print("The result of multiplying", num1, "and", num2, "is", total)


def division(choice, num1=None, num2=None):
    """
    Performs division on two numbers.
    """
    if choice == 4:
        num1 = int(input("Please enter the first number: "))
        num2 = int(input("Please enter the second number: "))
        while num2 == 0:
            print("Error: Cannot divide by zero.")
            num2 = int(input("Please enter a non-zero second number: "))
    total = num1 / num2
    print("The result of dividing", num1, "and", num2, "is", total)


menu_system()
