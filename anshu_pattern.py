#  A-BAB-CBABC-DCBABCD
str1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = int(input("Enter number of rows: "))
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(i, 0, -1):
        print(str1[j], end=" ")
    for j in range(i + 1):
        print(str1[j], end=" ")
    print()  # Move to the next line for the next row