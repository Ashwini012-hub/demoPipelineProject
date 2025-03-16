def remove_common(str1, str2):
    b = []
    p = str1.split(' ')
    q = str2.split(' ')
    for i in p:
        if i not in q:
            b.append(i)
    return b
print(remove_common('Good Morning', 'Morning Good'))            