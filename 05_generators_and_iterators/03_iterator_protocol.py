# Implementing the Iterable Protocol for Custom Objects
class CustomIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        # Returning an iterator object
        return CustomIterator(self.data)

# Iterator class for the iterable protocol
class CustomIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        result = self.data[self.index]
        self.index += 1
        return result

# Using the custom iterable object in a for loop
custom_data = [1, 2, 3, 4, 5]
custom_iterable = CustomIterable(custom_data)

for value in custom_iterable:
    print(value)


# Making Objects Compatible with the for Loop
class CustomIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return iter(self.data)

# Using the custom iterable object in a for loop
custom_data = [1, 2, 3, 4, 5]
custom_iterable = CustomIterable(custom_data)

for value in custom_iterable:
    print(value)


