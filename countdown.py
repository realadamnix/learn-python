"""
This program will take a time input from the user and count down to zero.
copyright: Adam Nix (2024)
"""

import time

# Set the countdown time

print("Welcome to the countdown timer.")
print("please enter your time in seconds")

# Get the time from the user
time_input = int(input())

if time_input < 0:
    print("Please enter a positive integer") 


# Start the countdown
print("You're timer has started")
while time_input > -1: # this will take the time and subtract 1 from it until it reaches 0.

    print(time_input)
    time.sleep(1) # this will make the program wait for 1 second before continuing the loop.
    time_input = time_input - 1 #this makes the program will count to 0.
print("timer is up")