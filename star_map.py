# Part 1
stars = {
    "Sun": {"x": 0, 
            "y": 0, 
            "z": 0, 
            "luminosity": 1.0, 
            "mass": 1.0},
    "Sirius": {"x": -1.6, 
               "y": 8.1, 
               "z": -2.5, 
               "luminosity": 25.4, 
               "mass": 2.06},
    "Vega": {"x": 7.2, 
             "y": -4.5,
            "z": 25.3, 
            "luminosity": 40.0, 
            "mass": 2.14},
    "Proxima Centauri": {"x": 1.6, 
                         "y": -3.8, 
                         "z": -1.2, 
                         "luminosity": 0.0017, 
                         "mass": 0.12},
    "Betelgeuse": {"x": 88.0,
                    "y": -120.0, 
                    "z": 45.0,
                    "luminosity": 100000.0, 
                    "mass": 16.5}
}

print(f"Number of stars: {len(stars)}")
print(f"Sirius mass: {stars['Sirius']['mass']}")
vega_x = stars["Vega"]["x"]
vega_y = stars["Vega"]["y"]
vega_z = stars["Vega"]["z"]
print(f"Vega is at ({vega_x}, {vega_y}, {vega_z})")
# Part 2
total_mass = 0
for name in stars:
    mass = stars[name]["mass"]
    luminosity = stars[name]["luminosity"]
    print(f"{name}: mass {mass}, luminosity {luminosity}")
    total_mass = total_mass + mass
average_mass = total_mass / len(stars)
print(f"Average mass: {average_mass}")
brightest_star = ""
highest_luminosity = 0
for name in stars:
    if stars[name]["luminosity"] > highest_luminosity:
        highest_luminosity = stars[name]["luminosity"]
        brightest_star = name

print(f"Brightest star: {brightest_star}")
# Part 3
user_star = input("Enter a star name to look up:").strip().title()

if user_star in stars:
    print(stars[user_star])
else:
    print("Star not found")

stars["Proxima Centauri"]["mass"] = 0.122

stars["Polaris"] = {"x": 0.0, 
                    "y": 433.0, "z": 0.0, 
                    "luminosity": 1260.0, 
                    "mass": 5.4}

del stars["Sun"]
print(f"Updated star count after deletion: {len(stars)}")

total_mass = 0
for name in stars:
    total_mass = total_mass + stars[name]["mass"]

new_average_mass = total_mass / len(stars)
print(f"New Average mass: {new_average_mass}")
# Part 4
observation_log = [
    {
        "star": "Sirius", 
        "night": 1, 
        "clear_sky": True
    },
    {
        "star": "Vega", 
        "night": 2, 
        "clear_sky": True
    },
    {
        "star": "Betelgeuse", 
        "night": 3, 
        "clear_sky": False
    }
]

for entry in observation_log:
    star_name = entry["star"]
    night_num = entry["night"]
    sky = entry["clear_sky"]
    star_mass = stars[star_name]["mass"]
    print(f"Night {night_num}: {star_name} (clear sky: {sky}) - Mass: {star_mass}")

new_obs_star = input("Enter observed star name to log: ").strip().title()

observation_log.append({"star": new_obs_star, "night": 4, "clear_sky": True})
print(f"Total observation log entries: {len(observation_log)}")