n = int(input("enter n"))
# for i in range(1, n + 1):
#     for j in range(0, n-i):
#         print(" ", end='')
#     for k in range(1, i+1):
#         print("*", end="")
#     print()

for i in range(n):
    for j in range(i, n):
        print(" ", end='')
    for k in range(i+1):
        print("*", end='')
    print()
