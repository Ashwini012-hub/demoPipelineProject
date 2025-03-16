# import sys
# items = ["apple", "banana", "apple", "orange", "banana", "banana"]
#
# freq1 = {i:items.count(i) for i in items}
# print(freq1)
# print(sys.getsizeof(freq1))
#
# freq2 = {i:items.count(i) for i in set(items)}
# print(freq2)
# print(sys.getsizeof(freq2))

# d = {'a':1, 'b':2, 'c':3}
# l = [(i,v)for i,v in d.items()]
# # new_tuple = (l[1][0], 10)
# # l[0] = new_tuple
# print(l)
# new = (l[2][0], 4)
# l[2] = new
# print(l)
# news = ('q', l[1][1])
# l[1] = news
# print(l)


dict_items = {'apple': 10, 'banana': 3, 'orange': 7, 'grapes': 5}

asc = sorted(dict_items.items(), key=lambda x: x[0], reverse=True)
print(dict(asc))



list_of_tuples = [(1, 2), (3, 4), (5, 6)]


