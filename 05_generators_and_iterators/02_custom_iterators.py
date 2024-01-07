# Introduction to Iterators and Iterable Objects
class SquaresIterable:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        result = self.current ** 2
        self.current += 1
        return result

# Using the iterator
squares_iterable = SquaresIterable(5)
for square in squares_iterable:
    print(square)


# Designing Classes with __iter__ and __next__ Methods
class CountDownIterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        result = self.current
        self.current -= 1
        return result

# Using the iterator
countdown_iter = CountDownIterator(3)
for count in countdown_iter:
    print(count)


# Stopping Iteration with the StopIteration Exception
class InfiniteCounter:
    def __init__(self):
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = self.current
        self.current += 1
        if result > 5:  # Stopping iteration after 5 iterations
            raise StopIteration
        return result

# Using the iterator
infinite_counter = InfiniteCounter()
for value in infinite_counter:
    print(value)

