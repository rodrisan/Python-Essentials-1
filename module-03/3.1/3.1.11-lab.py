# 3.1.11   LAB   Essentials of the if-else statement

income = float(input("Enter the annual income: "))

if income < 85528:
	tax = income * 0.18 - 556.02
elif income >= 85528:
    tax = 14_839.2 + 0.32 * (income - 85528)

if tax < 0:
    tax = 0.0

tax = round(tax, 0)

print("The tax is:", tax, "thalers")