s = 'python'
rev = ''
for i in s:
    rev = i + rev
print(rev)


output = ''
count = len(s)-1
while count>=0:
    output+= s[count]
    count-=1
print(output)
