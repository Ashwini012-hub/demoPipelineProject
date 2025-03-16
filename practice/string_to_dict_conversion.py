s = 'a=2&b=23&name=prakash'
p = s.split('&')
print(p)
q = []
for i in p:
    q.append(i.split('='))
print(dict(q))    
