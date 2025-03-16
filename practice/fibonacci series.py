def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        print(a, end=' ')
        a, b = b, a + b
        count += 1

num_terms = int(input("How many terms of the Fibonacci series would you like to generate? "))
fibonacci(num_terms)