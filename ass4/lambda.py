# Lambda function to add 10 to a given number
add_10 = lambda x: x + 10

# Lambda function to multiply two arguments and print the result
multiply = lambda x, y: print(f"The result of {x} * {y} is: {x * y}")

number_input = float(input("Enter a number: "))
result_add_10 = add_10(number_input)
print(f"The result of adding 10 to {number_input} is: {result_add_10}")

number_x = float(input("Enter the first number (x) for multiplication: "))
number_y = float(input("Enter the second number (y) for multiplication: "))
multiply(number_x, number_y)
