# Treating Functions as Values
def square(x):
    return x ** 2

# Assigning a function to a variable
my_function = square

# Using the variable as a function
result = my_function(5)


# Passing Functions as Arguments
def apply_operation(func, x):
    return func(x)

# Passing a function as an argument
result = apply_operation(square, 3)


# Returning Functions from Other Functions
def get_operation(power):
    def custom_power(x):
        return x ** power
    return custom_power

# Returning a function
square_function = get_operation(2)
result = square_function(4)

