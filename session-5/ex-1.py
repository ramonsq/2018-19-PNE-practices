def count_a(seq):
    """Counting the number of As in the sequence"""

    result = 0
    for b in seq:
        if b == "A":
            result += 1

    #return the result
    return result


# Main program

s = input("Please enter the sequence:")
na = count_a(s)
print("The number of As is: {}".format(na))

#Calculate the total sequence
total_length = len(s)

#Calculate the percentage of As in the sequence
percentage = round(100.0 * na / total_length, 1)

print("The total length is: {}".format(total_length))
print("The percentage of As is {}%".format(percentage))