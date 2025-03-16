a = [1,2,[7,9,[15,[12,9,]],18,10]]


def flatten(a):
    b = []
    for i in a:
        if isinstance(i, list):
            b.extend(flatten(i))
        else:
            b.append(i)
    return b
print(flatten(a))

q = [[1,2],[3],[4,5,6]]
z = [item for sublist in q for item in sublist]
print(z)


from functools import reduce
r = list(reduce(lambda x, y : x+y, q))
print(r)