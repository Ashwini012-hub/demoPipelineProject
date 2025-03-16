d = {'jay':['male', 32], 'raj':30, 'ram':['male', 30]}
count = 0
for i in d:
    if isinstance(d[i], list):
        count +=1
print(count)        
