# class demo:
#     def __init__(self):
#         print("Jaggu")
# obj1 = demo()
# class sum:
#     def __init__(self, a,b):
#         self._a = a
#         self._b = b
# class num(sum):
#     def add(self):
#         add = self._a + self._b
#         # print(type(self.a))
#         # print(type(self.b))
#         print(add)
#
# obj2 = num(2,7)
# obj2.add()

# Python Program to perform addition
# of two complex numbers using binary
# + operator overloading.

class complex:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	# adding two objects
	def __add__(self, other):
		return complex(self.a + other.a, self.b + other.b)
	def __str__(self):
		return f"({self.a}, {self.b})"
Ob1 = complex(1, 2)
Ob2 = complex(2, 3)
obj = complex(4,7)
Ob3 = Ob1 + Ob2 + obj
print(Ob3)
