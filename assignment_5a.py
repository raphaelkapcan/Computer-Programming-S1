# Kaplan, Raphael
# Computer Programming, period 4
# Assignment: Homework 6
# 11 November 2026

#1
people = int(input("How many people are in your group? "))
if people > 8:
    print("You have to wait for a table.")
elif people < 8:
    print("Your table is ready.")
else:
    print("Your not coming in.")

#2
number = int(input("Enter a number: "))
if number % 10 == 0:
    print("The number is a multiple of 10.")
else:
    print("The number is not a multiple of 10.")

#3
pizza_toppings = input("Enter your pizza toppings: ")
while pizza_toppings != "quit":
    print(f"Adding {pizza_toppings} to your pizza.")
    pizza_toppings = input("Enter another topping (or 'quit' to finish): ")
print("Your pizza is ready!")

#4
#A
theater_cost = input("What is your age? (or 'quit' to finish): ")
while theater_cost.lower() != "quit":
    age = float(theater_cost)
    if age < 0:
        print("That age doesn't make sense. Please enter a valid age.")
    elif age < 3:
        print("Your ticket is free.")
    elif 3 <= age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")
    theater_cost = input("What is your age? (or 'quit' to finish): ")
# B
active = True
while active:
    theater_cost = input("What is your age? (or 'quit' to finish): ")
    if theater_cost.lower() == "quit":
        active = False
    else:
        age = float(theater_cost)
        if age < 0:
            print("That age doesn't make sense.")
        elif age < 3:
            print("Your ticket is free.")
        elif 3 <= age <= 12:
            print("Your ticket costs $10.")
        else:
            print("Your ticket costs $15.")
#C
while True:
    theater_cost = input("What is your age? (or 'quit' to finish): ")
    if theater_cost.lower() == "quit":
        break
    
    age = float(theater_cost)
    if age < 0:
        print("That age doesn't make sense. Please enter a valid age.")
    elif age < 3:
        print("Your ticket is free.")
    elif 3 <= age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")
#5
sandwich_orders = ["tuna", "ham", "cheese", "veggie"]
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Making your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)
print("All sandwiches are ready!")

#6
sandwich_orders = ["tuna", "pastrami", "ham", "pastrami", "cheese", "veggie", "pastrami"]
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
print("Sorry, we are out of pastrami.")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Making your {current_sandwich} sandwich.")
print("All sandwiches are ready!")
#7'
dream_vacation = input("What is your dream vacation destination? ")
print(f"Your dream vacation destination is {dream_vacation}.")
