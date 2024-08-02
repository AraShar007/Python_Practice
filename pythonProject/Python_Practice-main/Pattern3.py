n= int(input("enter n: "))
for i in range(1, n+1):
    for j in range(n-i+1,0,-1):
        print("*",  end= '')
    print()
