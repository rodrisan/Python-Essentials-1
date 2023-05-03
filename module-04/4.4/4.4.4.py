# 4.4.4 SECTION SUMMARY

# 1. A variable that exists outside a function has scope inside the function body (Example 1) unless the function defines a variable of the same name (Example 2, and Example 3), e.g.:

# Example 1:

var = 2


def mult_by_var(x):
    return x * var


print(mult_by_var(7))  # outputs: 14

print("\n\n")
# Example 2:


def mult(x):
    var = 5
    return x * var


print(mult(7))  # outputs: 35


print("\n\n")
# Example 3:


def mult(x):
    var = 7
    return x * var


var = 3
print(mult(7))  # outputs: 49


print("\n\n")
# 2. A variable that exists inside a function has scope inside the function body (Example 4), e.g.:

# Example 4:


def adding(x):
    var = 7
    return x + var


print(adding(4))  # outputs: 11
print(var)  # NameError


print("\n\n")

# 3. You can use the global keyword followed by a variable name to make the variable's scope global, e.g.:

var = 2
print(var)  # outputs: 2


def return_var():
    global var
    var = 5
    return var


print(return_var())  # outputs: 5
print(var)  # outputs: 5
