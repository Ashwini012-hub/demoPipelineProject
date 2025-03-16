l = [5,3,1,4,3,7,6,9,2]
a = l[0]
b = l[1]
c = []
for i in range(0, len(l)):
    for j in range(i+1, len(l)):
        if l[i] * l[j] > a * b:
            a,b = l[i],l[j]
c.append(a)
c.append(b)
print(c)


