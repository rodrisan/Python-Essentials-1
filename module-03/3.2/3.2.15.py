# 3.2.15   LAB   Collatz's hypothesis

steps = 0
c0 = int(input("Enter a number: "))

while c0 != 1:
    if c0 % 2 == 0:
        c0 //= 2 # even
        steps +=1
        print(c0)
    elif c0 % 2 != 0:
        c0 = 3 * c0 + 1 # odd
        steps +=1
        print(c0)
    else:
        break
print("steps", steps)
