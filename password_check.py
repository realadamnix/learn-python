""" 
This program asks the user to enter a password.
If the password is correct, the program displays a message and ends.
If the password is incorrect, the program displays an error message and asks the user to try again.
The password is "12345" amd can be modified by changing the PASSWORD variable.

copyright: Adam Nix (2024)
"""

PASSWORD = "12345"

print("please enter your password")
user_input = input()

while True:

    if user_input == PASSWORD:

        print("password accepted")
        break
    else:
        print("incorrect password, please try again")
    user_input = input()
