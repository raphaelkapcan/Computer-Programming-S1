# Kaplan, Raphael
# Comptuer Programming, Period 4
# Assignment: 2A
# September 10, 2026

hobbies = ["Golf", "Walk", "Birdwatch", "Eat", "Think"]
print(hobbies)
print((len(hobbies)))
print(hobbies[2])
print(hobbies[0])
hello_list = ["Hello"] * 100
print(hello_list)
list_1 = ["Apple", "Banana", "Cherry"]
list_2 = ["Peach", "Mango", "Orange"]
list_3 = list_1 + list_2
print(list_3)
favfoods = ["Pizza", "Burger", "Bacon", "Wings", "Fries"]
print(len(favfoods))
print(favfoods[2])
print(favfoods[-5])
favfoods.append("Raphael")
favfoods.insert(2,16)
favfoods.remove("Fries")
print(favfoods)
for number in range(1, 21):
    print(number)
odd_numbers = list(range(1, 20, 2))
for number in odd_numbers:
    print(number)
animals = ["dog", "cat", "rabbit"]
for animal in animals:
    print(animal)
for animal in animals:
    print(f"A {animal} would make a great pet.")
print("Any of these animals would make a great pet!")
guests = ["Joseph Smith", "Michael Jordan", "Fredrick"]
for guest in guests:
    print(f"Dear {guest}, I would be honored to invite you to dinner!")
for guest in guests:
    print(f"Dear {guest}, I would be honored to invite you to dinner!")
cant_make_it = "Johnny York"
print(f"Unfortunately, {cant_make_it} can't make it to dinner.")
guests[2] = "Dante"
for guest in guests:
    print(f"Dear {guest}, I would be honored to invite you to dinner!")