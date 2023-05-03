# 3.2.6 More about the for loop and the range() function with three arguments

for i in range(2, 8, 3):
    print("The value of i is currently", i)

print("Not works, needs the second paramenter to be greater")
for i in range(1, 1):
    print("The value of i is currently", i)

print("Not works, needs the second paramenter to be greater")
for i in range(2, 1):
    print("The value of i is currently", i)

print()
power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2