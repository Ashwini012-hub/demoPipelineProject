import time

def exec_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        results = func(*args, **kwargs)
        end = time.time()
        print(f"execuction time of func {func.__name__} is {end-start}")
        return results
    return inner
@exec_time
def addition(a,b):
    time.sleep(2)
    sum = a+b
    return sum
print(addition(4,5))