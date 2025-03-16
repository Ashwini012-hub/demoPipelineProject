def max_sum_sublist(a):
    b = []
    for i in range(0, len(a)):
        for j in range(i+1, len(a)+1):
             b.append(a[i:j])
    max = sum(b[0])
    for i in range(1, len(b)):
        #sub_list = str(i)
        if sum(b[i]) > max:
            max = sum(b[i])
            sub = b[i]
    return max, sub
print(max_sum_sublist([-2,1,-3,4,-1,2,1,-5,4]))
