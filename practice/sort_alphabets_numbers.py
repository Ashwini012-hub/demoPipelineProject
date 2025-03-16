s = 'A7B1R3'
#ABR137
a = []
n = []
for i in s:
    if i.isalpha():
        a.append(i)
    else:
        n.append(i)
print(''.join(sorted(a) + sorted(n)))
