# Definition and Characteristics of Generators
def simple_generator():
    yield 1
    yield 2
    yield 3

# Creating a generator object
gen = simple_generator()

# Iterating through the generator
for value in gen:
    print(value)


# Creating Generator Functions Using the `yield` Statement
def countdown_generator(n):
    while n > 0:
        yield n
        n -= 1

# Creating a generator object
countdown = countdown_generator(5)

# Iterating through the generator
for value in countdown:
    print(value)


# Advantages of Lazy Evaluation in Generators
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

# Creating a generator object
numbers = infinite_sequence()

# Lazily evaluating and printing values
for _ in range(5):
    print(next(numbers))
