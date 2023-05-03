# 2.6.11   LAB   Operators and expressions – 2

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# dura_hours = dura / 60
# dura_minutes = dura % 60

# dura += dura_hours
# mins += dura_minutes

mins += dura
hour += mins // 60
mins %= 60
hour %= 24

print()
print(hour, ":", mins, sep='')