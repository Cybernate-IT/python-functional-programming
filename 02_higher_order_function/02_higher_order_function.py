# Characteristic: Accepting a Function as a Parameter
def apply_operation(func, x):
    return func(x)

# Characteristic: Returning a Function
def get_operation(power):
    def custom_power(x):
        return x ** power
    return custom_power


# Function Operating on Another Function
def square(x):
    return x ** 2

def double(func, x):
    return func(x) * 2

result = double(square, 3)


# Functional Composition with Higher-Order Function
def compose(func1, func2):
    return lambda x: func1(func2(x))

# Combining two functions using composition
result = compose(square, get_operation(3))(2)
