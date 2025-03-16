def anagram(str1, str2):
    if len(str1)!= len(str2):
        return False
    d = {}
    for i in str1:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1

    for i in str2:
        if i in d:
            d[i]-=1
        else:
            return False

    for i in d:
        if d[i]!=0:
            return False
        else:
            return True

print(anagram('Hi','ih'))    