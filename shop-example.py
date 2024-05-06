"""
This is a shop example program in python
Copyright Adam Nix
"""
tax = 0.06
price_of_milk = 2.50
price_of_bread = 1.20

print("please enter the number of milk cartons you want to buy:")
price_of_milk = int(input())

print("please enter the number of bread loaves you want to buy:")
price_of_bread = int(input())

total = (price_of_milk + price_of_bread) * (1 + tax)
print("The total price is:", total, "euros")
