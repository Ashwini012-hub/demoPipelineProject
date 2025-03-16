s = 'Python is good langugage'
d = {}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
freq_list = sorted(d, key=d.get, reverse=True)
print(freq_list[1])
