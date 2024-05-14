"""
This program allows the user to select an operation (addition, subtraction, multiplication, or division) and two numbers. The program then performs the selected operation on the two numbers and displays the result.
copyright: Adam Nix (2024)
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
    
    while True:
        choice = int(input("Please enter your choice: "))
      
        if choice == 1:
            print("You have selected addition")
            break
        elif choice == 2:
            print("You have selected subtraction")
            break
        elif choice == 3:
            print("You have selected multiplication")
            break
        elif choice == 4:
            print("You have selected division")
            break
        else:
            print("Invalid choice (please select 1, 2, 3, or 4)")
        
    return choice

def addition(choice, num1, num2):
    
    if choice == 1:
        num1 = int(input("please enter the first number:"))
        num2 = int(input("please enter the second number:"))
        total = num1 + num2
        print("The result of adding", num1, "and", num2, "is", total)
    

def subtraction(choice, num1, num2):
    
    if choice == 2:
        num1 = int(input("please enter the first number:")) 
        num2 = int(input("please enter the second number:"))
        total = num1 - num2
        print("The result of subtracting", num1, "and", num2, "is", total)
