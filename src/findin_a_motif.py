def solve(dna: str, motif: str):
    pos = []
    for i in range(len(dna)):
        if dna[i:i+len(motif)] == motif:
            pos.append(i+1)
    return pos


if __name__ == "__main__":
    with open("input.txt") as f:
        dna, motif = f.readlines()
        #print(f.readlines())
    for x in solve(dna.strip(), motif.strip()):
        print(f"{x} ", end="")