list1 = [int(x) for x in input("Enter the element").split()]
print(list1)
def remove_even(list1):
    for x in list1:
        if (x%2==0):
            list1.remove(x)
    print(list1)
remove_even(list1)
