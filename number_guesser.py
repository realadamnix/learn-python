"""
This is a number guessing game where a user selects a random number between 1 to 10
it works as follows:
1. The user selects a random number between 1 to 10
2. The other user has to guess the number
3. If the guess is correct, the program displays "correct"
4. If the guess is incorrect, the program displays "incorrect" and asks the user to try again
5. The program continues until the user guesses the correct number
copyright: Adam Nix (2024)
"""

print("select a random BETWEEN 1 TO 10 for your teammate to guess")
number_chosen = input()

while True:
    if int(number_chosen) <= 0 or int(number_chosen) >= 10:
        print("invalid values entered")
        print("Please enter a valid value")
        number_chosen = input()
    else:
        break


print("please enter your guess")
User_guess = input()

while True:
    if number_chosen == User_guess:
        print("correct")
        break
    else:
        print("incorrect (Please try again)")
        User_guess = input()