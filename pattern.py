n= int(input("enter n"))
for i in range(1, n+1):
    for j in range(1, i+1):
        print("*",  end= ' ')
    print()

# second way to do this
#
# for i in range(1, n + 1):
#     for j in range( n-i,n):
#         print("*", end=' ')
#     print()