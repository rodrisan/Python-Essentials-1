# 2.4.9   LAB   Variables ‒ a simple converter

kilometers = 12.25
miles = 7.38
one_mile_to_km = 1.61

miles_to_kilometers = one_mile_to_km * miles
kilometers_to_miles = one_mile_to_km / kilometers

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")
