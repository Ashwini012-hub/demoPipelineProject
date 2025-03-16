# a = [1,2,3,['Ash','Anu'],45,[20,'NAitik'],43, 'stuti']
# b = [i for i in a if isinstance(i, list)]
# print(b)


# def reverse_string(s):
#     rev = ''
#     count = len(s)
#     while count>0:
#         rev = rev + s[count-1]
#         count-=1
#     return rev
# q = reverse_string('python')
# print(q)


def reverse_string(s):
    rev = ''
    for i in range(0, len(s)):
        rev = s[i] + rev
    return rev
print(reverse_string('python'))



#using recursion
def reverse_string(s):
    if len(s)==1:
        return s
    else:
        return reverse_string(s[1:]) + s[0]
s = 'python'
reversed_s = reverse_string(s)
print(reversed_s)

#using reduce
from functools import reduce
rev = reduce(lambda x, y : y + x, s)
print(rev)

#using list
l = list(s)
rev = ''
while l:
    rev = rev + l.pop()
print(rev)