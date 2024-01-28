def create_and_check_dict():
  my_dict = {}
  print("Please note that the program is case sensitive!!!")
  num_items = int(input("Enter the number of items in the dictionary: "))
  for i in range(num_items):
    key = input(f"Enter key {i+1}: ")
    value = input(f"Enter value for '{key}': ")
    my_dict[key] = value
  key_to_check = input("Enter a key to check: ")
  if key_to_check in my_dict:
    print(f"The key '{key_to_check}' exists in the dictionary.")
    print(f"Its value is: {my_dict[key_to_check]}")
  else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")

create_and_check_dict()
