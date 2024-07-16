#Lists are used to store multiple items in a single variable.
my_list= ["Demon Slayer", "Harry Potter", "The office", "Spy Family", "Modern Family", "Brooklyn 99"]
print(my_list)
print(my_list[4])
print(len(my_list))
print(type(my_list))
my_list1= list((1,2,3,4,5))
print(type(my_list),my_list1)
print(my_list[-1])
print(my_list[-6])
print(my_list[1:4])
print(my_list[:4])
print(my_list[2:])
print(my_list[-4:-1])
print(my_list[-5:-2])
my_list[4]="bridgerton"
print(my_list)
if "bridgerton" in my_list:
  print("Bridgerton added to my list")
else:
  print("bridgerton is not added")
my_list[2:3]=["The Office-US", "MODERN FAMILY"]
print(my_list)
print(len(my_list))
my_list.insert(0, "BTS")
print(my_list, "len:",len(my_list))
my_list.append("Kim's conveinance")
print(my_list, "len:",len(my_list))
my_list.extend(my_list1)
print(my_list, "len:",len(my_list))
my_list1.extend(my_list1)
print(my_list1, "len:",len(my_list1))
my_tup=("this", "is", "a", "sample", "tuple")
my_list.extend(my_tup)
print(my_list, "len:",len(my_list))
my_list.remove("sample")
print(my_list, "len:",len(my_list))
my_list.pop(12)
print(my_list, "len:",len(my_list))
my_list.pop()
print(my_list, "len:",len(my_list))
del my_list[14]
print(my_list, "len:",len(my_list))
my_list1.clear()
print(my_list1)
l1=["hi", "i", "am", "aravi"]
del l1
for x in my_list:
  print(x)
for item in range(len(my_list)):
  print(my_list[item])
print("--------------")
i=0
while i <len(my_list):
  print(my_list[i])
  i+=1
print("--------------")
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

fruits= ["apple", "guava", "mango", "litchi", "cherry", "berries", "grapes", "kiwi"]
# new_fruits=[]
# for item in fruits:
#   if "a" in item:
#     new_fruits.append(item)
# print(new_fruits)

#using list comprehension
new_fruits=[item for item in fruits if "a" in item]
print(new_fruits)
#syntax: newlist = [expression for item in iterable if condition == True]

new_fruits=[item for item in fruits if item != "litchi"]
print(new_fruits)

new_fruits=[item for item in fruits]
print(new_fruits)

newlist = [x for x in range(10)]
print(newlist)

newlist = [x for x in range(20) if x%2==0]
print(newlist)

new_fruits=[item.upper() for item in fruits]
print(new_fruits)

newlist = [ 'konichiwa' for x in newlist]
print(newlist)

new_fruits=[item if "a" in item else "without a" for item in fruits]
#new_fruits= [x if x != "apple" else "watermelon" for x in fruits]
print(new_fruits)
new_fruits.sort()
print(new_fruits)
thislist = [100, 77, 348, 65, 82, 23, 7]
thislist.sort()
print(thislist)

thislist.sort(reverse=True)
print(thislist)

Flist = ["orange", "mango", "kiwi", "pineapple", "banana"]
Flist.sort(reverse = True)
print(Flist)
def func1(n):
  return abs(n-50)
num_list=[34, 100, 77, 55, 60, 45, 49]
num_list.sort(key= func1)
print(num_list)

def func2(n):
  return n%2!=0
num_list=[34, 100, 77, 55, 60, 45, 49]
num_list.sort(key=func2)
print(num_list)

l2=["HI", "this","is", "A", "List" , "for", "sorting"]
l2.sort()
print(l2)

l2.sort(key= str.lower)
print(l2)