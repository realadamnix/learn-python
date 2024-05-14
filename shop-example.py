"""
This program allows the user to select the number of milk cartons and bread loaves they would like to buy. The program then calculates the total price of the items, including a 5% tax.
copyright: Adam Nix (2024)
"""
tax = 0.05
price_of_milk = 2.50
price_of_bread = 1.20

print("please enter the number of milk cartons you want to buy:")
price_of_milk = int(input())

print("please enter the number of bread loaves you want to buy:")
price_of_bread = int(input())

total = (price_of_milk + price_of_bread) * (1 + tax)
print("The total price is:", total, "euros")
