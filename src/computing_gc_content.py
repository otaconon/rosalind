class DNA:
    id:str
    bps:str

    def __init__(self, id:str, bps:str):
        self.id = id
        self.bps = bps

    def __str__(self):
        return f"{self.id}\n{self.get_gc_content()}\n"

    def get_gc_content(self) -> float:
        return sum(bp in ['G', 'C'] for bp in self.bps) / len(self.bps) * 100
    
with open("input.txt") as f:
    dna_data = f.read()

dnas = []

for dna_part in dna_data.split('>')[1:]:
    dna_part.strip()
    id = dna_part[:13]
    bps = ''.join(dna_part[13:].split())

    dnas.append(DNA(id, bps))

print(max((dna for dna in dnas), key=lambda dna: dna.get_gc_content()))