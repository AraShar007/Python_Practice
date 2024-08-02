for t in int, float, dict, list, tuple, str:
    print(type(t))

type(type)
class Parent:
    x = 10

Sample_Class = type('Sample_Class', (Parent,), {'print_x': lambda self: print(self.x)})

obj = Sample_Class()
obj.print_x()

class sample_meta_class(type):
    def __new__(cls, name, bases, dct):
        dct ={ 'key1' :"Value1"}
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=sample_meta_class):
    pass
obj = MyClass()
print(obj.key1)
print(type(sample_meta_class))
print(type(MyClass))







