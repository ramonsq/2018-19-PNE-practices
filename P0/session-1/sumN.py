print("Program for adding the numbers from 1 to the integer you want.")
def sum(n):
    sum1 = 0
    for number in range(1, n+1):
        sum1 = sum1 + number
    return sum1

num = int(input("Enter the integer you want to make the sum of the numbers: "))
print("The total sum is:", sum(num))