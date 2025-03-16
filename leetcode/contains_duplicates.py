a = [-1,1,-1,1,0,2]
d = {}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in d:
    if d[i]>1:
        print("contains duplicates")