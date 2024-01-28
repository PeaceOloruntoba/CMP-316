def create_square_dict():
  print("For a dictionary with key 1 to n, the value of each key is it's square,")
  n = int(input("Enter the value of n: "))
  square_dict = {}
  for i in range(1, n + 1):
    square_dict[i] = i * i
  print("The dictionary is:", square_dict)
create_square_dict()
