# Write a Python program to shuffle and print a specified list.
list1 = [x for x in input("enter list element").split()]
set1 = set(list1)
print(type(set1))
print(set1)
list_new = list(set1)
print(type(list_new))
print(list_new)