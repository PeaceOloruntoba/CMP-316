def create_and_check_dict():
  """Creates a dictionary and checks for key existence."""

  # Create a dictionary
  my_dict = {"name": "Alice", "age": 30, "city": "New York"}

  # Get a key to check from the user
  key_to_check = input("Enter a key to check: ")

  # Check if the key exists in the dictionary
  if key_to_check in my_dict:
    print(f"The key '{key_to_check}' exists in the dictionary.")
    print(f"Its value is: {my_dict[key_to_check]}")
  else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")

create_and_check_dict()  # Call the function
