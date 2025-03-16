#sort is a method of list class
#sorted is a built inmethod used for sorting iterablesnums = [2, 3, 1, 5, 6, 4, 0]

'''The primary difference between the two is that list.sort() will sort the list in-place, mutating its indexes and returning None, whereas sorted() will return a new sorted list leaving the original list unchanged. Another difference is that sorted() accepts any iterable while list.sort() is a method of the list class and can only be used with lists.'''
print(sorted(nums))   # [0, 1, 2, 3, 4, 5, 6]
print(nums)           # [2, 3, 1, 5, 6, 4, 0]

print(nums.sort())    # None
print(nums)           # [0, 1, 2, 3, 4, 5, 6]