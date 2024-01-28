def even_odd():
  print("Please do not repeat an integer")
  my_list = input("Enter list integers separated by commas: ").split(",")
  my_list = [int(item) for item in my_list]
  print("Items at even positions:")
  for i in range(0, len(my_list), 2):
    print(my_list[i])
  print("\nItems at odd positions:")
  for i in range(1, len(my_list), 2):
    print(my_list[i])

even_odd()
