# Anonymous Function (Lambda Function) Example
multiply = lambda x, y: x * y
result = multiply(3, 5)


# Lambda Function Syntax
addition = lambda a, b: a + b
result = addition(2, 3)


# Use Case: Lambda Function with Map
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
