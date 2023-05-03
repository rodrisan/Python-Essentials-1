# 3.2.12 The while loop and the else branch

i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

print("\nModifying a bit\n")

i = 5
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)