# 4.6.4 Dictionary methods and functions
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

print("\nIterate over keys")
for key in dictionary.keys():
    print(key, "->", dictionary[key])

    dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

print("\nIterate over Items")

for english, french in dictionary.items():
    print(english, "->", french)

print("\nUpdate value")
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
print(dictionary)
dictionary['cat'] = 'minou'
print(dictionary)


print("\nIterate over sorted Keys")
dictionary = {"dog": "chien", "horse": "cheval", "cat": "chat"}

for key in sorted(dictionary.keys()):
    print(key, "->", dictionary[key])

print("\nIterate over values")
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for french in dictionary.values():
    print(french)

# Adding a new key
print("\nAdding a new key")

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
dictionary['fish'] = 'poison'
print(dictionary)

# You can also insert an item to a dictionary by using the update() method, e.g.

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
dictionary.update({"duck": "canard"})
print(dictionary)

print("\nRemoving a key")
# Removing a key
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
del (dictionary['horse'])
print(dictionary)


print("\nRemoving the last item")
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary.popitem()
print(dictionary)  # outputs: {'cat': 'chat', 'dog': 'chien'}
