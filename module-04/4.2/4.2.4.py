# 4.2.4 Mixing positional and keyword arguments

def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

adding(1, 2, 3)

adding(c = 1, a = 2, b = 3)

adding(3, c = 1, b = 2)