s = 'aaaabbbccd'
#4a3b2c1d
output = ''
temp = s[0]
count = 0
for i in s:
    if i == temp:
        count += 1
    else:
        output = output + str(count) + i
        temp = i
        count = 1
print(output)
