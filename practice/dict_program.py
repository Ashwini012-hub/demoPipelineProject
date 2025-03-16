d = {'orange':'fruit', 'potato':'vegetable', 'banana':'fruit'}
#{'fruit':['orange','banana'], 'vegetable':['potato']}
q = {}
for i in d:
    if d[i] not in q:
        q[d[i]]=[i]
    else:
        q[d[i]].append(i)
print(q)


p = {}
for i in d:
    if d[i] not in p:
        p[d[i]] = [i]
    else:
        p[d[i]].append(i)
print(p)