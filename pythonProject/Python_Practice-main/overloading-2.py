from multipledispatch import dispatch
class Test:
    @dispatch(int, int)
    def add(self, a,b):
        print(a+b)
    @dispatch(float, float)
    def add(self,a,b):
        print(a+b)
    @dispatch(int, float)
    def add(self,a,b):
        print(a+b)
    @dispatch(int,int,float)
    def add(self, a,b,c):
        print(a+b+c)
t = Test()
t.add(100,30)
t.add(100,90.6)
t.add(56, 78, 98.9)
t.add(78.9, 76.7)
