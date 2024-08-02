
list1 = [x for x in input("Enter the strings").split()]
print(list1)
n = int(input("Enter the value of n: "))
list_new = []
for i in list1:
    if(len(i) > n):
        list_new.append(i)
print(list_new)
