# A decorator is function that takes other function as argument and modify tthat function and return it
def outer(value):
 def decor(func):
    def inner(a,b):
        result = func(a,b)
        result += value
        return result
    return inner
 return decor



@outer(3)
def addition(a,b):
    result = a + b
    return result
print(addition(2,3))
