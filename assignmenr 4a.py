# Kaplan, Raphael
# Computer Programming, period 4
# Assignment: Homework 4a
# 26 October 2026

# A
person1 = {
    "first_name": "Nathan",
    "last_name": "Kaplan",
    "city": "Frankfurt"
}

for k,v in person1.items():
    print(k,v)

# B
about_me = {
    "name": "James",
    "age": "16",
    "favFood": "grapes",
    "hairColor": "black",
    "favSubject": "math",
    "favSweet": "lolipop",
    "favHobbies": ["Riding his Bike", "Dancing", "Disco"],
    "likeCoding": "Yes",
}
print(about_me)

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

phonebook["Jake"] = 9383451924
del phonebook["Jill"]
print(phonebook)

#Part B
five_words = {
    "monotheism": "belief in one god",
    "polytheism": "belief in many gods",
    "Federalists": "people who believed in having a strong central governmnet",
    "George Washington": "The first president of the united states",
    "King George III": "The king of britain during the revolutionary war",
    "Bread": "It is made of yeast",
    "Sushi": "It has fish",
    "Steak": "It is made from cows",
    "Chicken": "It is made from chicken",
    "Fish": "It is made from Fish"
}

for k,v in five_words.items():
    print(k,v, "\n")

rivers = {
    "Nile": "Egypt",
    "Tigris": "Iraq",
    "Mississippi": "USA"
}

for k,v in rivers.items():
    print(f"The {k} runs through {v}")

person1 = {
    "firstName": "Alice",
    "lastName": "Smith",
    "favColor": "Blue",
    "birthMonth": "March",
}

person2 = {
    "firstName": "Bob",
    "lastName": "Jones",
    "favColor": "Red",
    "birthMonth": "April",
}

person3 = {
    "firstName": "Charlie",
    "lastName": "Brown",
    "favColor": "Green",
    "birthMonth": "December",
}

people = [person1, person2, person3]

for person in people:
    for k, v in person.items():
        print(k, v)

cities = {
    "Tokyo": {
        "country": "Japan",
        "population": "14 million",
        "fact": "It is the most populous metropolitan area in the world.",
    },
    "Paris": {
        "country": "France",
        "population": "2.1 million",
        "fact": "The Eiffel Tower was originally intended to be a temporary installation.",
    },
    "Cairo": {
        "country": "Egypt",
        "population": "10 million",
        "fact": "It is located near the Giza pyramid complex.",
    },
}

for city, info in cities.items():
    print(city)
    print(info)
    print()