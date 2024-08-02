n=int(input("enter n:"))
for i in range(n):
    for j in range(n):
        if(i==(n-1)/2 or j==(n-1)/2 ):
            print("*", end='')
        else:
            print(" ", end='')
    print()