number = int(input("Enter the number for the multiplication table: "))

for i in range(1, 12):
    result = number * i
    print(f"{number} * {i} = {result}")
