def sort_words(text):
  words = text.split()
  words.sort()
  return " ".join(words)

text = input("Enter any string to sort: ")
sorted_text = sort_words(text)
print(f"Original text: {text}")
print(f"Sorted text: {sorted_text}")
