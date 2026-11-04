car_brands = {
    "Toyota": "Japan",
    "Ford": "USA",
    "BMW": "Germany",
}


inventory = {"apples": 10, "oranges": 0, "bananas": 5, "grapes": 0}

# Safely loop through key-value pairs
for key, value in list(inventory.items()):
    if value == 0:
        del inventory[key]
