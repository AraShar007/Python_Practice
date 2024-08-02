n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        if(i+j==n-1 or i==n-1 or j==n-1):
            print("*", end='')
        else:
            print(" ", end='')
    print()
