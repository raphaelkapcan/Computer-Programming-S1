# Kaplan, Raphael
# Comptuer Programming, Period 4
# Assignment: 2C
# September 18, 2026

flight_log = [1000, 2500, 4200, 6000, 7800, 9500, 11000, 12500]
print("Initial log:", flight_log)
flight_log.append(13800)
flight_log.append(15000)
print("After append:", flight_log)
removed_reading = flight_log.pop(0)
print(f"Removed noise reading ({removed_reading}). After pop:", flight_log)
flight_log.insert(3, 7000)
print("After insert:", flight_log)
print(f"Reading at index 3: {flight_log[3]}")