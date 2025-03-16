s = 'hello world'
p = s.split(' ')
print(p)
q = []
for i in p:
    q.append(i[0].upper() + i[1:-1] + i[-1].upper())
print(' '.join(q))