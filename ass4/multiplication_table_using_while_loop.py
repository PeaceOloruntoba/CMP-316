number = int(input("Enter the number for the multiplication table: "))

i = 1

while i <= 12:
    result = number * i
    print(f"{number} * {i} = {result}")
    i += 1
