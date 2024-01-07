# Stateless Function
def calculate_square(x):
    return x ** 2

result1 = calculate_square(3)
result2 = calculate_square(5)
# The function has no internal state; the result depends only on the input

# Stateless Function Enhancing Predictability
def calculate_total_price(unit_price, quantity):
    return unit_price * quantity

total_price1 = calculate_total_price(10, 5)
total_price2 = calculate_total_price(10, 5)
# The function is predictable, always producing the same result for the same input
assert total_price1 == total_price2


# Stateless Computation in Data Processing
def process_data(data, processing_function):
    return [processing_function(item) for item in data]

data = [1, 2, 3, 4]
processed_data = process_data(data, calculate_square)
# Stateless computation applied to process data in a predictable manner
