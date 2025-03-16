a = ['cat', 'tea', 'tan', 'ate', 'nat', 'bat']
d = {}
for i in a:
    b = ' '.join(sorted(i))
    if b in d:
        d[b].append(i)
    else:
        d[b] = [i]
print(list(d.values()))        
