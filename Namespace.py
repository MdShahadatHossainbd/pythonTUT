"""
x = 10
def fun():
    x = 5
    print(x)

fun()
"""
print("initially: ", dir())
num = 230
def fun():
    n = 10
    print("inside: ", dir())

print("outside: ", dir())