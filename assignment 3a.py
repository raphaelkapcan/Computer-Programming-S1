# Kaplan, Raphael
# Computer Programming, period 4
# Assignment: Homework 3A
# 2 October 2026

alien_color = 'green'
if alien_color == 'green':
    print("5 Points")
else:
    print("10 Points")
alien_color2 = 'yellow'
if alien_color2 == 'yellow':
    print("5 Points")
else:
    print("10 Points")
#2
alien_color = "green"
if alien_color == "green":
    print("You earned 5 points!")
elif alien_color == "yellow":
    print("You earned 10 points!")
else:
    print("You earned 15 points!")

alien_color = "yellow"
if alien_color == "green":
    print("You earned 5 points!")
elif alien_color == "yellow":
    print("You earned 10 points!")
else:
    print("You earned 15 points!")

alien_color = "red"
if alien_color == "green":
    print("You earned 5 points!")
elif alien_color == "yellow":
    print("You earned 10 points!")
else:
    print("You earned 15 points!")
# 3
test_ages = [1, 3.9, 10, 13, 19, 20, 21, 65]
age = int(input("Enter an age:"))

if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")

# 4
usernames = ['admin', 'jaden', 'sarah', 'alex', 'mike']
User_input = input("Enter a your name:")
if not usernames:
    print("We need to find some users!")
else:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
# 5
new_users = ['SARAH', 'JOHN', 'Alex', 'ERIC', 'chris']
current_users_lower = [user.lower() for user in usernames] 

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, '{new_user}' is already taken. You will need to enter a new username.")
    else:
        print(f"Great, '{new_user}' is available!")
        numbers = list(range(1, 10))

# 6
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")
        