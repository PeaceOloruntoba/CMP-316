# Given list of integers
numbers = [1, 2, 3, 4, 5]

# Lambda function to square a number
square = lambda x: x ** 2

# Lambda function to cube a number
cube = lambda x: x ** 3

# Using map() to apply the lambda functions to each element in the list
squared_numbers = list(map(square, numbers))
cubed_numbers = list(map(cube, numbers))

# Display the results
print("Original List:", numbers)
print("Squared List:", squared_numbers)
print("Cubed List:", cubed_numbers)
