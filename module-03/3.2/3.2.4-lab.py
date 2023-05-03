# 3.2.4   LAB   Guess the secret number

secret_number = 14

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

my_number = int(input("->"))
iterator = True

while iterator:
    if my_number == secret_number:
        iterator = False
        print("Well done, muggle! You are free now.")
    else:
        print("Ha ha! You're stuck in my loop!")
        my_number = int(input("Enter another number: "))
