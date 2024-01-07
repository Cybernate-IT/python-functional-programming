# Understanding Closures in Python
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure_example = outer_function(10)
result = closure_example(5)  # Result will be 15


# How Closures Capture and Retain Outer Function Scope
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure_example = outer_function(10)
# Even though outer_function has finished, closure_example still retains access to 'x'
result = closure_example(5)  # Result will be 15


# Practical Example of Closures: Counter
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter_example = counter()
print(counter_example())  # 1
print(counter_example())  # 2


# Encapsulating State Within Closures
def adder(x):
    def inner_adder(y):
        return x + y
    return inner_adder

add_five = adder(5)
result = add_five(3)  # Result will be 8


# Solving Practical Programming Challenges with Closures: Memoization
def memoize(func):
    cache = {}

    def memoized_func(*args):
        if args not in cache:
            result = func(*args)
            cache[args] = result
        return cache[args]

    return memoized_func

# Applying closure to memoize a recursive Fibonacci function
@memoize
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

result = fibonacci(10)  # Result will be cached for subsequent calls
