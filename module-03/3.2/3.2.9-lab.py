# 3.2.9   LAB   The break statement – Stuck in a loop

msg = "Enter the correct hidden word: "
word = input(msg)

while word != "chupacabra":
    if word == "chupacabra":
        break
    word = input(msg)

print("You've successfully left the loop.")