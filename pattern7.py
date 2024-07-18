# n = int(input("enter n: "))
# for i in range(n):
#     for j in range(i, n):
#         print(" ", end='')
#     for k in range(0,2*i-1):
#         print("*", end='')
#     for j in range(1, n):
#         print(" ", end='')
#     print()

# #can also be done
n = int(input("enter n: "))
for i in range(n):
    for j in range(n-i-1):
        print(" ", end='')
    for k in range(2*i+1):
        print("*", end='')
    print()

