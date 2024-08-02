from array import *
values = array('i', [3, -5, 5])
print(values)
print(values.buffer_info())
print(values.typecode)
values.reverse()
print(values)
for i in range(3):
    print(values[i])
new_array = array(values.typecode, (a**3 for a in values))
print(new_array)