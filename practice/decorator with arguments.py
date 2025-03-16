# Decorator with argument
def repeat_decorator(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator

# Applying the decorator with argument
@repeat_decorator(3)
def greet(name):
    print(f"Hello, {name}!")

# Calling the decorated function
greet("Alice")
