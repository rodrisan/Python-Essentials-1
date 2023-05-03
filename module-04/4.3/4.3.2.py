# 4.3.2 A few words about None

# print(None + 2)
# Causes error


value = None
if value is None:
    print("Sorry, you don't carry any value")

print("\n\n")

def strange_function(n):
    if(n % 2 == 0):
        return True

print(strange_function(2))
print(strange_function(1))