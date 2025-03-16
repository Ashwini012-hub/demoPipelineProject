# def twoSum(nums, target):
#     # Create a dictionary to store the complement of each element
#     d = {}
#     for i, v in enumerate(nums):
#         temp = target - v
#         if temp in d:
#             return [d[temp], i]
#         else:
#             d[v] = i
#
# print(twoSum([2,4,4,6,8,5], 10))


#
#
#
#
l = ['dog', 'god']
# m = []
# for i in l:
#     m.append(sorted(i))
# if m[0] == m[1]:
#     print("True")
# else:
#     print("False")


def anagrams(s1, s2):
     if len(s1) != len(s2):
         return False

     d = {}
     count = 0

     for i in s1:
         if i not in d:
             d[i] = 1
         else:
             d[i]+=1

     for i in s2:
         if i in d:
             d[i]-= 1
         else:
             return False

     for i in d:
         if d[i]!=0:
             return False
     return True

print(anagrams(l[0], l[1]))
