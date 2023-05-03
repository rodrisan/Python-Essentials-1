# 3.4.8 Adding elements to a list: append() and insert()

numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

#
numbers.insert(1, 333)
print(numbers)

print("\n\nCreating a list")

my_list = []  # Creating an empty list.

for i in range(5):
    my_list.append(i + 1)

print(my_list)


print("\n\nInverse order created list")

my_list = []  # Creating an empty list.

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)