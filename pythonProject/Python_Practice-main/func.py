# def my_function(x, y):
#   print(x)
#   print(y)
#
# my_function(3, y=4)

import array as arr
a = arr.array("i",[1,2,3,4])
for i in range(4):
    print(a[i], end=' ')
print(type(a))
print(a)
print(type(a[0]))