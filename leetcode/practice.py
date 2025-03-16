l =[4,1,5, 6, 7, 4, 3]
target = 9
p = []
for i in range(0, len(l)):
    for j in range(i+1, len(l)):
        if (l[i]+l[j]) == target:
            p.append([i, j])
print(p)

d = {}
for i, v in enumerate(l):
    temp = target - v
    if temp in d:
        print(d[temp], i)
    else:
        d[v] = i



