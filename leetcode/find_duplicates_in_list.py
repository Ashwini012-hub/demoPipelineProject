a = [1,-1,3,2,-1,1]
d = {}
b = []
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i] = 1
for j in d:
    if d[j]>1:
        b.append(j)
print(b)
