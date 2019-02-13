f = open("DNA.txt")
sequence = f.read()

sequence = sequence.replace("\n", "")
print("Total length", len(sequence))
countA = 0
countC = 0
countG = 0
countT = 0
for letter in sequence.lower():
    if letter == "a":
        countA += 1
    elif letter == "c":
        countC += 1
    elif letter == "g":
        countG += 1
    elif letter =="t":
        countT += 1
print("A:", countA)
print("C:", countC)
print("G:", countG)
print("T:", countT)
f.close()