import copy
#shallow copy
a = [1, 2, [3, 4]]
shallow_copy = copy.copy(a)

shallow_copy[2][0] = 99

print(a)
print(shallow_copy)

#deep copy
b = [1, 2, [3, 4]]
deep_copy = copy.deepcopy(b)
deep_copy[2][0] = 99

print(b)
print(deep_copy)

