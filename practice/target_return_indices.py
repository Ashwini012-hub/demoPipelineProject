nums = [2,7,11,15]
Target = 18
#[0,1]
l = []
for i in range(0, len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == Target:
            l.append(i)
            l.append(j)
print(l)            
