# 4.4.2 Functions and scopes: the global keyword

def my_function():
    global var
    var = 2
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)
