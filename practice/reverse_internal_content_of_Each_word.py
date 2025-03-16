s = 'python is easy'
#nohtyp si ysae
p = s.split(' ')
q = []
for i in p:
    q.append(i[::-1])
print(' '.join(q))