"""
    This program generates a random number.
    
    The user is asked to choose between three options:
    1. Generate a random number between 1 and 10
    2. Generate a random number between 1 and 100
    3. Generate a random number between 100 and 1000
    
    The program then generates a random number based on the user's choice.
    
    Copyright: Adam Nix (2024)
"""

import random

print("welcome to the random number generator.")
print("This program generates a random number between two numbers.")

print ("enter 1 to generate a random number between 1 and 10")
print ("enter 2 to generate a random number between 1 and 100")
print ("enter 3 to generate a random number between 100 and 1000")

choice = input ("Please enter your choice: ")
choice = int(choice)

if choice == 1:
    print(random.randint(1, 10))
elif choice == 2:
    print(random.randint(1, 100))
elif choice == 3:
    print(random.randint(100, 1000))
else:
    print("invalid choice")
