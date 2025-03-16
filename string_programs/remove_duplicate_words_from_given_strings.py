str1 = 'cat bat mat cat rat sat bat'
q = str1.split(' ')
b = []
for i in q:
    if i not in b:
        b.append(i)
print(b)            
