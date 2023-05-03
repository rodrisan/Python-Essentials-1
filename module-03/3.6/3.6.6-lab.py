# 3.6.6   LAB   Operating with lists ‒ basics

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

clean_list = [my_list[0]]

for element in my_list[1:]:
    if element not in clean_list:
        clean_list.append(element)

my_list = clean_list[:]

print("The list with unique elements only:")
print(my_list)
