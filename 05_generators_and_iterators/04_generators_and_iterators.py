# Efficiently Processing Large Datasets with Generators
def large_dataset_generator():
    for i in range(1, 1000001):
        yield i

# Using the generator in a for loop
for value in large_dataset_generator():
    # Process each value without loading the entire dataset into memory
    print(value)


# Iterating Over Complex Data Structures with Generators
def nested_data_structure_iterator(data):
    for sublist in data:
        for item in sublist:
            yield item

# Using the iterator for a nested list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for value in nested_data_structure_iterator(nested_list):
    print(value)


# Controlling the Iteration Process with Generators
def controlled_iteration_generator(start, end, step):
    current = start
    while current <= end:
        yield current
        current += step

# Using the generator with controlled iteration
for value in controlled_iteration_generator(1, 10, 2):
    # Process values with a specific step
    print(value)

