s = 'abc'
b = []
for i in range(0, len(s)):
    for j in range(i+1, len(s)+1):
        b.append(s[i:j])
print(b)