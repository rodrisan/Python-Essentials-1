# 3.4.9 Making use of lists

my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)

print("\n\nMore simple")

my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total)