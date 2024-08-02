count = 5
x = 7
def myfunc():
    global count
    count = count + 1
    print(count)
    def innerFunc():
        x = 8
        print("Inner function x is:", x)
    innerFunc()
myfunc()
print("outer function:", x)




