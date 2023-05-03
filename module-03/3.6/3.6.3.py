# 3.6.3 Slices – negative indices

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[:]
print(new_list)

# More about the del instruction

my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)

my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)

# This causes error
# my_list = [10, 8, 6, 4, 2]
# del my_list
# print(my_list)