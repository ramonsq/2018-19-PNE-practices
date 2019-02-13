from Seq import Seq

s1 = Seq("AGTACACTGGT")
s2 = Seq("CGTAAC")
s3 = s1.complement()
s4 = s3.reverse()


sequences = (s1, s2, s3, s4)

for elem in sequences:
    print("Sequence:{}".numberofthesequence, elem.strbases)
    print("  Length:", elem.len())
    bases = ["A", "C", "G", "T"]

    for i in bases:
        print("Sequence:", )



print("Sequence {}".format(key))
print("  Length: {}".format(total_length))
print("  Bases count: {}".format())
print("  Percentage: {}".format(percentage))
