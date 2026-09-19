words = ["cat", "dog", "cat"]
freq = {}

for w in words:
  freq[w] = freq.get(w, 0) + 1

print(freq)  # Output: {'cat': 2, 'dog': 1}