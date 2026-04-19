from collections import Counter

with open("../datasets/counting_dna_nucleotides.txt") as f:
  data = f.read()

counts = Counter(data)
print(counts)
print(*(counts[k] for k in sorted(counts)))