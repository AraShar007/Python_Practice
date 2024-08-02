
class Parent:
    def __init__(self):
        self.a=5
        self._b=4
        self.__c=10
        # print(a)
    # print(a, _b, __c)
    def mul(self):
        print(f"Multiplication of {self.a}, {self._b}, {self.__c} is {self.a * self._b * self.__c}")

# obj=Parent()
# obj.mul()

class Child(Parent):
    def show(self):
        print(super().a)
        print(self._b)
        #print(self.__c)  # error as private member can not be inherited
# obj=Child()
# obj.show()

class other:
    """hbfjesfo"""
    def show(self):
        print(Parent()._b)
        # print(Parent()._b)
        # print(Parent.__c)
obj_other=other()
print(obj_other.__doc__)
obj_other.show()

