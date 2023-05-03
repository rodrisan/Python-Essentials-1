# 3.2.14   LAB   Essentials of the while loop

blocks = int(input("Enter the number of blocks: "))
height = 0
block = 1

# for block in range(blocks):
#     if block + 1 == 1:
#         print("if ", block + 1)
#         height = 1
#     elif block + 1 <= height + 1:
#         print("elif", block + 1)
#         height += 1
#     else:
#         continue

while block <= blocks:
    height += 1
    blocks -= block
    block += 1

print("The height of the pyramid:", height)