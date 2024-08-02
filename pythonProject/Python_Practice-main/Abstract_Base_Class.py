from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def func1(self):
        pass

    def func2(self):
        print("This is a normal function")

class MyABC2(ABC):
    @abstractmethod
    def area(self):
        pass

    def describe(self):
        print("This is a shape")


class NormalClass(AbstractClass, MyABC2):
    def func1(self):
        print("Implementation of func1")

    def area(self):
        print("Implementation of area")

class aravi:
    pass

obj = NormalClass()
obj.func1()
obj.func2()
obj.area()
obj.describe()
print("Type of normal class is",type(NormalClass))
print("Type of abstract class is",type(AbstractClass))
print(type(aravi))