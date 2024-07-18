# n=int(input("Enter rows:"))
# for i in range(n):
#     for j in range(i):
#         print(" ", end='')
#     for k in range(n-i):
#         print("* ", end='')
#     print()
# for i in range(1,n):
#     for j in range(n-i-1):
#         print(" ", end='')
#     for k in range(i+1):
#         print("* ", end='')
#     print()

n=int(input("Enter rows:"))
for i in range(n):
    for j in range(i):
        print(" ", end='')
    for k in range(2*(n-i)-1):
        print("*", end='')
    print()
for i in range(1,n):
    for j in range(n-i-1):
        print(" ", end='')
    for k in range(2*i+1):
        print("*", end='')
    print()
