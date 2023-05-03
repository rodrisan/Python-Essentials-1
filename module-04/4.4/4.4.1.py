# 4.4.1 Functions and scopes

def my_function():
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)

def my_function2():
    var = 2
    print("Do I know that variable?", var)

var = 1
my_function2()
print(var)
