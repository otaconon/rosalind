def solve(dna: str) -> str:
  return "".join([c if c != 'T' else 'U' for c in dna])

with open("input.txt") as f:
  data = f.read()
  
print(solve(data))