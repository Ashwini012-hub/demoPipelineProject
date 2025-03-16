s = 'a3b2c4'
#aaabbcccc
output = ''
for i in s:
    if i.isalpha():
        ch = i
    else:
        d = int(i)
        output = output + (d * ch)
print(output)