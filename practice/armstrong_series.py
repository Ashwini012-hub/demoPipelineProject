# # armstrong number get length and power it and it should be equal to same number
# num = 1634
# l = len(str(num))
# n = str(num)
# result = 0
# for j in n:
#     result += int(j) ** l
# if int(result) == num:
#     print("Number is armstrong")
# else:
#     print("not")

#
#
#
#
#
num = int(input("Enter a number"))
s = str(num)
q = len(s)
sum = 0
for i in s:
    sum+= int(i) ** q
if sum == num:
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")



