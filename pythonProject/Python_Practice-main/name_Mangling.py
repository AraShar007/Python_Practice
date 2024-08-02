# __method is replaced by python as _className__method
class Myclass():
    def __init__(self):
        self.__var = "Private"
        print(self.__my_func())
    def my_func(self):
        return "parent func"
    __my_func = my_func
class Childclass(Myclass):
    def my_func(self):
        return "child func"
    __my_func = my_func

obj = Myclass()
# print(obj.__var)
print(obj._Myclass__var) # we shouldnt do this
child_obj = Childclass()
child_obj.my_func()
