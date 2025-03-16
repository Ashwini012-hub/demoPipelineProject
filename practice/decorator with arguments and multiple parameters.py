# Decorator with multiple parameters
def log_args(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments were: {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

# Applying the decorator
@log_args
def process_data(name, age, city):
    print(f"Processing data for {name}, {age}, {city}")

# Calling the decorated function
process_data("Alice", 30, "New York")
