#Divide by Zero simpler version:


def decor_div(func):
    def inner(x, y):

        if y == 0:
            return "Number cannot be dived by zero. Give proper input."
        else:
            return func(x, y)

    return inner
@decor_div
def div(a, b):
    return a / b


d = decor_div(div)
print(d(8, 0))

