# 3.2.10   LAB   The continue statement – the Ugly Vowel Eater

user_word = input("Enter a word: ").upper()
user_word = user_word.upper()

for letter in user_word:
    if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
        continue
    print(letter)
