text = input("Enter any given statement to check the vowel count")
vowel_counts = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
for char in text.lower():
  if char in vowel_counts:
    vowel_counts[char] += 1
print("Vowel counts:")
for vowel, count in vowel_counts.items():
  if count > 0:
    print(f"{vowel}: {count}")
total_vowels = sum(vowel_counts.values())
print(f"Total number of vowels: {total_vowels}")
