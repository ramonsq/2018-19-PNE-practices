def count_bases(seq):

    result = {"A": 0, "C": 0, "G": 0, "T": 0}
    for key in result:
        result[key] = seq.count(key)

    return result

#MAIN PROGRAM
s1 = input("Enter the sequence 1:")
s2 = input("Enter the sequence 2:")
seqs = s1, s2
for seq in seqs:
    na = count_bases(seq)
    total_length = len(seq)
    print("The sequence is {}".format(total_length), "bases in length")
    for key, element in na.items():
        percentage = round(100.0 * element / total_length, 1)

        print("Base {}".format(key))
        print("  Counter:", element)
        print("  Percentage:{}".format(percentage))
