# 3. Write a Python program to get the largest number from a list.
list = []
def largest(list):
    n = int(input("Enter the no of elements"))
    for i in range(0,n):
        element = int(input("Enter the element"))
        list.append(element)
    print(list)
    max = 0
    for i in list:
        if i > max:
            max = i
    print(max)
largest(list)