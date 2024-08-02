class Test:
    def mt1(self, *a):
        print(a)


t = Test()
t.mt1()
t.mt1(10.8)
t.mt1(10, 20)
t.mt1(10, 20, 30)
t.mt1(999, 888, 777, 666, 555)

