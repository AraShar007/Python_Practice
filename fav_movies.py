list = []
n = int(input("enter the no of movies you like"))
for i in range(n):
    i = input(f"Enter the {i+1}th favorite movie:")
    list.append(i)
print(list)