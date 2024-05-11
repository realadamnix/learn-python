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
    
    
print ("Thank you for using our car rental service!")