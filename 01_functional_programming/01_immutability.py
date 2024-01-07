
# Immutability with Numbers
original_number = 5
modified_number = original_number + 2  # Creates a new variable

# Immutability with Strings
original_string = "Hello"
modified_string = original_string + ", World!"  # Creates a new string

# Immutability with Tuples
immutable_tuple = (1, 2, 3)
new_tuple = immutable_tuple + (4,)  # Creates a new tuple

# Immutability with Lists (using tuple conversion)
immutable_list = [1, 2, 3]
new_list = tuple(immutable_list)  # Creates a new tuple


# Benefits: Readability
mutable_list = [1, 2, 3]
immutable_tuple = tuple(mutable_list)  # Improved readability

# Benefits: Predictability
original_dict = {'a': 1, 'b': 2}
immutable_dict = frozenset(original_dict.items())  # Creates an immutable dictionary

# Benefits: Ease of Debugging
def process_data(data):
    # Some processing logic
    return frozenset(data)

original_data = [1, 2, 3]
processed_data = process_data(original_data)  # Debugging is easier with immutable data


# Avoiding Side Effects
def add_to_list(input_list, new_element):
    # Modifying the input list would have side effects
    return input_list + [new_element]

original_list = [1, 2, 3]
modified_list = add_to_list(original_list, 4)  # Creating a new list instead

# Predictability in Functions
def multiply_by_two(value):
    # The function is deterministic, always returning the same result for the same input
    return value * 2

result1 = multiply_by_two(3)
result2 = multiply_by_two(3)
assert result1 == result2  # The results are always the same
