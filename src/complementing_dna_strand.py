def solve(dna: str) -> str:
    complement = {
        'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'
    }
    return "".join([complement[c] for c in reversed(dna.strip())])

with open("input.txt") as f:
    data = f.read()
  
print(solve(data))