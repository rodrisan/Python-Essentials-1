# 3.4.3 Accessing list content

numbers = [10, 5, 7, 2, 1]
print(numbers[0]) # Accessing the list's first element.

print("")

numbers = [10, 5, 7, 2, 1]
print("Original list contents:", numbers)  # Printing original list contents.

numbers[0] = 111
print("\nPrevious list contents:", numbers)  # Printing previous list contents.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("Previous list contents:", numbers)  # Printing previous list contents.

print("\nList length:", len(numbers))  # Printing the list's length.