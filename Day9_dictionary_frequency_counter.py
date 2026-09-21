words = ["cat", "dog", "cat"]
freq = {}

for y in words:
  freq[y] = freq.get(y, 0) + 1

print(y)  # Output: {'cat': 2, 'dog': 1}