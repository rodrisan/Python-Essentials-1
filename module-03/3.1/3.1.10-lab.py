# 3.1.10   LAB   Comparison operators and conditional execution

input = input("Give me your words: ")
message = ""

if input == "Spathiphyllum":
    message = "Yes - " + str(input) + "is the best plant ever!"
elif input == "spathiphyllum":
    message = "No, I want a big Spathiphyllum!"
else:
    message = "Spathiphyllum! Not " + str(input) + "!"

print(message)