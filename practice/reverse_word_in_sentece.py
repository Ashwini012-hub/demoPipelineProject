s = "sky is blue"
p = s.split(' ')
q = []
for i in p[::-1]:
    q.append(i)
print(' '.join(q))    
