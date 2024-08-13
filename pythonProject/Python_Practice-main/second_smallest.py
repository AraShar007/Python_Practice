from array import *
values = array('i', [3, -5, 5])
print(values)
list1 = list(values)
min_val = list1[0]
for i in range(len(list1)):
    if min_val > list1[i]:
        list1[i-1], list1[i] = list1[i], list1[i-1]
print(list1)
print(list1[1])
