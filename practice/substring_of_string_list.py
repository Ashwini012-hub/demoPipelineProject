s = 'bye'
sub = []
for i in range(0, len(s)):
    for j in range(i+1, len(s)+1):
        sub.append(s[i:j])
print(sub)

a = [0,1,2,3,4,5,6,7]
b = []
for i in range(0, len(a)):
    for j in range(i+1, len(a)+1):
        b.append(a[i:j])
print(b)
