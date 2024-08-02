def cmp(x, y):
   return (x > y) - (x < y)

list1 = ['123', 'abc']
list2 = ['234', 'bcd']
print (cmp(list1, list2))
print (cmp(list2, list1))
#checking for integers
# x>y
x=5
y=3
print("x and y:", cmp(x,y))
print("y and x:", cmp(y,x))   # y>x
a=10
b=10
print("a and b:", cmp(a,b))
