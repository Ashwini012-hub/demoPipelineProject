#using generator
# def fibonacci():
#     a,b = 0, 1
#     while True:
#         yield a
#         a,b = b, a+b
# f = fibonacci()
# for i in f:
#     if i>100:
#         break
#     print(i)

#usingnormal
def fibonacci(num):
    a,b = 0,1
    for i in range(1,num):
        print(a)
        a,b = b, a+b
fibonacci(10)        