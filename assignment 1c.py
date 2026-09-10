# Raphael Kaplan
# Assignment 1C

# Part 1
name_of_object = input("Enter the name of the object:")
mass_kg = input("What is the mass of the object in kilograms:")
velocity = input("What is the velocity of the object in meters per second:")

name_of_object_clean = name_of_object.strip().title()
mass_kg_num = float(mass_kg)
velocity_num = float(velocity)

KE_jules = 1/2 * mass_kg_num * velocity_num ** 2
KE_calories = KE_jules / 4.184
KE_ergs = KE_jules * 10**7

#print("Kinetic Energy Report for: ", name_of_object_clean)
output_line_one = f"Kinetic Energy Report For: {name_of_object_clean}"
print(output_line_one)
print("--------------------------------")
output_line_three = f"Joules\t{KE_jules} J"
#print("Joules:\t", KE_jules, "J")
print(output_line_three)
output_line_four = f"Calories\t{KE_calories} cal"
#print("Calories:\t", KE_calories, "cal")
print(output_line_four)
output_line_five = f"Ergs\t{KE_ergs} ergs"
#print("Ergs:\t", KE_ergs, "ergs")
print(output_line_five)