from abc  import ABC, abstractmethod
class Interface(ABC):
    @abstractmethod
    def abs_method(self):
        pass

    @abstractmethod
    def abs_method2(self):
        pass

class Interface2(ABC):
    @abstractmethod
    def int2_method(self):
        pass
class Child(Interface, Interface2):
    def abs_method(self):
        print("abstact method")
    def abs_method2(self):
        print("second abstact method")

    def int2_method(self):
        print("Interface 2 method")

    def normal_method(self):
        print("Normal method")


obj_child = Child()
obj_child.normal_method()
obj_child.abs_method()
obj_child.abs_method2()
obj_child.int2_method()
print(type(Interface))
