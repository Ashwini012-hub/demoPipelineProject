def outer():
    def inner():
        x = 20
        return x
    return inner
inner = outer()
print(inner())
print(outer())