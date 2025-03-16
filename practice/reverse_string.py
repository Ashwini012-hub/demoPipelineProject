#using while loop
s = 'python'
rev = ''
count = len(s)-1
while count>=0:
    rev = rev + s[count]
    count = count-1
print(rev)


#using for loop
m = ''
for i in s:
    m = i + m
print(m)


def reverse_string(s):
    if len(s)==0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

s = "Python"
print(reverse_string(s))



print(s[::-1])


numbers = [1, 2, 3, 4, 5, 6]
squares = [i**2 for i in numbers]
print(squares)

map_squares = list(map(lambda x: x**2, numbers))
print(map_squares)