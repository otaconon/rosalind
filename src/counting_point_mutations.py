from collections import Counter

with open("input.txt") as f:
  data = [line.strip() for line in f.readlines()]

print(sum(a != b for a, b in zip(data[0], data[1])))