a = [1, 2, 2, 3, 3, 4, 5, 5, 5, 6, 6]
#[1,4]
d = {}
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
s = []
for i, v in d.items():
    if v == 1:
        s.append(i)
print(s)

l = [i for i in a if a.count(i)==1]
print(l)