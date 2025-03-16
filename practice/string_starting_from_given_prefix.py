s = [('ca',('cat','car','fear','center'))]
prefix = s[0][0]
print(prefix)
p = []
for i in s[0][1]:
    print(i)
    if prefix in str(i):
        p.append(i)
print(p)