# 3.1.12   LAB   Essentials of the if-elif-else statement

year = int(input("Enter a year: "))
common_type = "Common year"
leap_type = "Leap year"

if year < 1582:
	print("Not within the Gregorian calendar period")
else:
	if year % 4:
		print(common_type)
	elif year % 100:
		print(leap_type)
	elif year % 400:
		print(common_type)
	else:
		print(leap_type)
