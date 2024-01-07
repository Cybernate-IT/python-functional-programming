# Overview: Map, Filter, and Reduce Functions
numbers = [1, 2, 3, 4, 5]

# Map: Transforming data
squared_numbers = list(map(lambda x: x ** 2, numbers))

# Filter: Filtering data
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Reduce: Aggregating data
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)


# Applying Map for Data Transformation
names = ["Alice", "Bob", "Charlie"]
uppercase_names = list(map(lambda name: name.upper(), names))


# Using Filter for Data Filtering
ages = [18, 25, 30, 15, 22]
adults = list(filter(lambda age: age >= 18, ages))


# Utilizing Reduce for Aggregation
product = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])

