# 2. Write a Python program to multiply all the items in a list.
list = []
def mulof(list):
    mul = 1
    n = int(input("Enter the no of elements in the list"))
    for i in range(0,n):
        element = int(input("Enter the element"))
        list.append(element)
        mul = mul * element
    print(list)
    print(mul)
mulof(list)