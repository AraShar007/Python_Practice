# n = int(input("enter n: "))
# for i in range(n):
#     for j in range(i+1):
#         print(" ", end='')
#     for k in range(i,2*n-i-1):
#         print("*", end='')
#     for j in range(i+1):
#         print(" ", end='')
#     print()

#can be dome like
n = int(input("enter n: "))
for i in range(n):
    for j in range(i+1):
        print(" ", end='')
    for k in range(i, n-1):
        print("*", end='')
    for l in range(i,n):
        print("*", end='')
    print()