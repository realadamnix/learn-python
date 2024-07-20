print ("select a random BETWEEN 1 TO 10 for your teammate to guess")
number_chosen = input()

while True:
    if int(number_chosen) <= 0 or int(number_chosen) >= 10:
        print("invalid values entered")
        print("Please enter a valid value")
        number_chosen = input()
    else:
        break


print ("please enter your guess")
User_guess= input()

while True:
    if number_chosen == User_guess:
         print ("correct")
         break
    else:
        print("incorrect (Please try again)")
        User_guess = input()       