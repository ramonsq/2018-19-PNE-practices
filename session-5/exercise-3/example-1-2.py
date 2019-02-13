from Bases import count_bases

s = input("Enter the sequence:")
na = count_bases(s)
total_length = len(s)
print("The sequence is {}".format(total_length), "bases in length")
for key, element in na.items():
    percentage = round(100.0 * element / total_length, 1)

    print("Base {}".format(key))
    print("  Counter:", element)
    print("  Percentage:{}".format(percentage))
