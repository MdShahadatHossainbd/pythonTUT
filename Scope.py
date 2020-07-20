y = 20 # Global Scope

def fun():
    z = 10 # Local Scope

    def inner(): # Nested Scope
        n = 50
        print("n",n)

    inner()
    print("Z:",z)
"""
    global y
    y = y + 40 # Global Scope using in local function
    print(y)
"""

fun()
print("y: ",y)