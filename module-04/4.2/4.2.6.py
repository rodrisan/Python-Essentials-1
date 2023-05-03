# 4.2.6 SECTION SUMMARY

# An example of a one-parameter function:

def hi(name):
    print("Hi,", name)

hi("Greg")

# An example of a two-parameter function:

def hi_all(name_1, name_2):
    print("Hi,", name_2)
    print("Hi,", name_1)

hi_all("Sebastian", "Konrad")

# An example of a three-parameter function:

def address(street, city, postal_code):
    print("Your address is:", street, "St.,", city, postal_code)

s = input("Street: ")
p_c = input("Postal Code: ")
c = input("City: ")
address(s, c, p_c)

# Ex. 1
print("\n")
def subtra(a, b):
    print(a - b)

subtra(5, 2) # outputs: 3
subtra(2, 5) # outputs: -3


# Ex. 2
print("\n")
def subtra(a, b):
    print(a - b)

subtra(a=5, b=2) # outputs: 3
subtra(b=2, a=5) # outputs: 3

# Ex. 3
print("\n")
def subtra(a, b):
    print(a - b)

subtra(5, b=2) # outputs: 3
subtra(5, 2) # outputs: 3

# position arguments

def subtra(a, b):
    print(a - b)

subtra(5, b=2) # outputs: 3
# subtra(a=5, 2) # Syntax Error

# 3. You can use the keyword argument-passing technique to pre-define a value for a given argument:

def name(first_name, last_name="Smith"):
    print(first_name, last_name)

name("Andy") # outputs: Andy Smith
name("Betty", "Johnson") # outputs: Betty Johnson (the keyword argument replaced by "Johnson")
