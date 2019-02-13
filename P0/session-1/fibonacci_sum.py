def fibonacci(n):
    a, b = 0, 1
    count = 0
    for i in range(n+1):
        count += a
        a, b = b, (a+b)

        #print(a, end=',')
    print(count)
    return
fibonacci(int(input("Enter the number of terms you want to sum up to proceed:")))