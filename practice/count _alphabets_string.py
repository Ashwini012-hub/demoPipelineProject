# s = 'a,a,a,b,b,c,c,c'
# # {a:3, b:2, c:3}
# q = s.split(',')
# d = {}
# for i in q:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1
# print(d)

s = 'a,a,a,b,b,c,c,c'
d = {}
p = s.split(',')
for i in p:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
