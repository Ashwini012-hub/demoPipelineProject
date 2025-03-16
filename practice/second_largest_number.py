a = [78, 45, 76, 90, 23, 73, 84]
for i in range(0, len(a)):
    for j in range(i+1, len(a)):
        if a[i]>a[j]:
            a[i],a[j] = a[j],a[i]
print(a[-2])            