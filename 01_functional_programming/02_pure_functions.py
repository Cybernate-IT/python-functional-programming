# Pure Function: Deterministic
def add(x, y):
    return x + y

result1 = add(3, 5)
result2 = add(3, 5)
assert result1 == result2  # The result is always the same for the same input

# Pure Function: Immutability
def multiply_by_two(numbers):
    return [num * 2 for num in numbers]

original_list = [1, 2, 3]
modified_list = multiply_by_two(original_list)  # Creates a new list


# Impure Function with Side Effects
global_variable = 10

def impure_function(x):
    global global_variable
    global_variable += x
    return x + global_variable

result = impure_function(5)  # Has a side effect on the global state

# Pure Function without Side Effects
def pure_function(x, state):
    return x + state, state

result, new_state = pure_function(5, 10)  # No side effect on the global state


# Advantage: Code Simplicity
def pure_add(x, y):
    return x + y

result = pure_add(3, 5)  # Simplicity in function usage

# Advantage: Ease of Testing
def pure_multiply_by_two(numbers):
    return [num * 2 for num in numbers]

original_data = [1, 2, 3]
result = pure_multiply_by_two(original_data)  # Easy to test and predict

# Advantage: Maintainability
def calculate_total_price(unit_price, quantity):
    return pure_add(unit_price, quantity)

total_price = calculate_total_price(10, 5)  # Easier to maintain and reason about
