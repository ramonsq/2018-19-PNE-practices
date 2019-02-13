f = open("CPLX2.txt")
dna_chain = f.read()
countA, countC, countG, countT = 0, 0, 0, 0
letter = 0

while letter < len(dna_chain):
    base = dna_chain[letter]

    if base == ">":
        letter += (dna_chain[letter:].find("\n"))
    elif base == "A":
        countA += 1
        letter += 1
    elif base == "C":
        countC += 1
        letter += 1
    elif base == "G":
        countG += 1
        letter += 1
    elif base == "T":
        countT += 1
        letter += 1
    else:
        letter += 1
print("A:", countA, "C:", countC, "G:", countG, "T:", countT)