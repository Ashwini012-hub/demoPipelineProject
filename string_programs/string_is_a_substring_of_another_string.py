def find_substring(str1, str2):
    m = len(str1)
    n = len(str2)
    for i in range(m-n+1):
        j = 0
        while j<n and str1[i]==str2[j]:
            j = j + 1
    if j == n:
        return i
    else:
        return -1
print(find_substring('computer', 'put'))