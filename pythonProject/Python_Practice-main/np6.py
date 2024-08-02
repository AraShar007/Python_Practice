n = 4
m = 7
for i in range(n):
    for j in range(m):
        if i==n-1 or i+j ==3 or j-i==3:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()
