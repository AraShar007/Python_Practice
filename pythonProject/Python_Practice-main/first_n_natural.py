# Write a recursive function to calculate the sum of first n natural numbers.
n = int(input("Enter the no of numbers: "))

def natural(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    print(sum)
natural(n)

