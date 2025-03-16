numbers1 = [1, 2, 3, 4, 5]
numbers2 = [5, 6, 7, 8, 9]

squared_numbers = map(lambda x: x ** 2, numbers1, numbers2)
print(list(squared_numbers))