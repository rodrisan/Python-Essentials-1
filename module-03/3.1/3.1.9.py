# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.

largest_number = max(number1, number2, number3)
print("The largest number is: ", largest_number)

minimal_number = min(number1, number2, number3)
print("The min number is: ", minimal_number)