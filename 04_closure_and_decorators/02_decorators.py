# Introduction to Decorators
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# Calling the decorated function
say_hello()


# Syntax and Structure of Decorator Functions
def decorator_template(func):
    def wrapper(*args, **kwargs):
        # Additional functionality before the original function
        result = func(*args, **kwargs)
        # Additional functionality after the original function
        return result
    return wrapper

@decorator_template
def example_function():
    print("Original function behavior")

# Calling the decorated function
example_function()


# Applying Decorators to Modify Function Behavior
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_decorator
def greet(name):
    return f"Hello, {name}!"

# Calling the decorated function
result = greet("John")
print(result)  # Output: HELLO, JOHN!

# Implementation Examples

# Logging and Timing Functions with Decorators
import functools
import time

def log_and_time_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} executed in {end_time - start_time:.2f} seconds.")
        return result
    return wrapper

@log_and_time_decorator
def example_function():
    print("Executing the example function.")

# Calling the decorated function
example_function()

# Extending Functionality Without Modifying Original Code
def uppercase_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_decorator
def greet(name):
    return f"Hello, {name}!"

# Calling the decorated function
result = greet("John")
print(result)  # Output: HELLO, JOHN!


# Use Cases for Creating Reusable Decorators
def debug_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@debug_decorator
def add(a, b):
    return a + b

@debug_decorator
def multiply(x, y):
    return x * y

# Calling the decorated functions
result_add = add(3, 5)
result_multiply = multiply(4, 6)



