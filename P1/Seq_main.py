from Seq import Seq

s1 = Seq("AGTACACTGGT")
s2 = Seq("CGTAAC")
s3 = s1.complement()
s4 = s3.reverse()

sequences = [s1, s2, s3, s4]
counter = 1
for elem in sequences:
    print("Sequence {}:".format(counter), elem.strbases)
    print("  Length:", elem.len())
    bases = ["A", "T", "C", "G"]
    counter += 1
    for i in bases:
        print("  Bases count: {}, {}".format(i, elem.count(i)))
        print("  Bases {} percentage: {}".format(i, elem.perc(i)), "%")

#("%s : s%" % (i, elem.count(i)))