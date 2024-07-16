x = 7+4j

#display x:
print(x)

#display the data type of x:
print(type(x)) 

x = range(4)
print(x[0])
print(x[1])
print(x[2])
print(x[3])
# print(x[4])
print(type(x)) 
 # An immutable version of a Python set object is a frozen set.
f=frozenset({3,4,7,10,17})
print(f)
print(type(f))

# x = b"Hello"
x=bytes("Hello", 'utf-8')
print(x)
print(type(x)) 

# The bytes() function returns a bytes object.
Y=bytes(4)
print(Y)
# bytes(2,encoding=)

print(bytes())
# ignores the error
str1='GeeksfÖrGeeks'
print(str1)
print("Ignore Error: "+ str(bytes(str1, 'ascii', errors='ignore')))
# replaces error with ?
print("Replace Error: " + str(bytes(str1, 'ascii', errors='replace')))
# generates an UnicodeEncodeError
print("Strict error: "+ str(bytes(str1, 'utf-8', errors='strict')))
# print("Strict error: "+ str(bytes(str1, 'ascii', errors='strict')))
# The bytearray() function returns a bytearray object.
x = bytearray(5)
print(x)
print(type(x))
# diff between bytes() and bytearray() is that bytes() returns an object that cannot be modified, and bytearray() returns an object that can be modified

str = "Geeksforgeeks"

# encoding the string with unicode 8 and 16
array1 = bytearray(str, 'utf-8')
array2 = bytearray(str, 'utf-16')
print(array1)
print(array2)

size=4
array3 = bytearray(size)
print(array3)

arr1=bytearray(b"hiiii")
for char in arr1:
  print(char)
arr2= bytearray(b"aeiiiiooouu")
print("count of i in arr2: ", arr2.count(b"i"))
print("____")
arr3= bytearray(b"Konichiwa")
for value in arr3:
  print(value)

list1=[7,14,21,28,35,42,49,56,63,70]
array=bytearray(list1)
print(array)
print("count of bytes:", len(array))

array=bytearray()
print(array)

# The python memoryview() function returns a memoryview object of the given argument.
# The memoryview() function is used to view the memory of a particular object as a different type.
x = None
#display x:
print(x)
#display the data type of x:
print(type(x)) 

x = "hello"
y="konichiwa"
#if condition returns True, then nothing happens:
assert x == "hello"

#if condition returns False, AssertionError is raised:
assert x == "goodbye"
assert y != "hello", "y should be 'hello'"

def neha():
  pass

def aravi():
  print("F")

array_b=bytearray('XYZ', 'utf-8')
mv=memoryview(array_b)
print(mv)