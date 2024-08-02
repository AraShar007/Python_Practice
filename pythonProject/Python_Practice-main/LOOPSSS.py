# colors= ["pink", "blue", "purple", "black", "yellow", "orange", "green"]
# for i in colors:
#     print(i)
# i=1
# while i<5:
#     print(i)
#     i += 1
#
# x=0
# while not( 1<=x<=100):
#     x=int(input("Enter a num b/w 1 and 100:"))c
# print("valid")
#
# for i in range(3):
#     x=int(input("enter the no"))
#     if (1<=x<=100):
#         print(x)
#         print("valid")
#     else:
#         print("invalid")

# i=-2
# while True:
#     print("I:", i)
#     i += 1
#     if i>0:
#         break
#     else:
#         print("number less than 0")
#
# # ------------------------------------------
#
# sales_data= [25,50, 75, 95, 200, 235, 100, 150, 125]
# sales= 0
# for s in sales_data:
#     sales += s
#     print(sales)
#
# # ------------------------------------------
#
# #user  input validation
# u_input = ''
# while not u_input.isdigit():
#     u_input = input("enter a no:")
# print(f"{u_input} is a valid digit")

# ------------------------------------------

# file  processing
with open("new_file.txt", "r") as file:
    for line in file:
        # print(line)
        print(line.rstrip())

# ------------------------------------------

# automating repetitive tasks:
email_list = ["gaurav@itt", "anshu@itt", "manish@itt", "aravi@gmail"]
for mail in email_list:
    print(f"Email sent to {mail}")

# ------------------------------------------

# for loop is used when we are certain about the no of iterations in advance
# while loop is used when the no of iterations are uncertain and the loop continues until a certain condition is met.

count = 0
while count< 5:
    print(f"{count+1}st Person")
    count += 1
else:
    print("End of line ")


for i in ["tanjiro", "GENYA", "nezuko", "zenitsu", "inosuke"]:
    print(i)
else:
    print("Murata san- the saviour")

#------------------------

# break

for i in ["tanjiro", "GENYA", "nezuko", "zenitsu", "inosuke"]:
    if(i=="zenitsu"):
        print("we are doomed --breaking--")
        break
    print(i)
else:
    print("Murata san- the saviour")

#------------------------

# continue

for i in ["tanjiro", "GENYA", "nezuko", "zenitsu", "inosuke"]:
    if(i=="zenitsu"):
        print("we are doomed --breaking--")
        continue
    print(i)
else:
    print("Murata san- the saviour")

# -----------------------------------

# comprehension
# list, set, dictionary, generator comprehension

#using for loop:

l1= [1,2,3,4,5]
l2=[]
for num in l1:
    l2.append(num+7)
print(l2)

# using L.C
l3=[x**2 for x in l1]
print (l3)

# newlist = [experssion for item in iterable]
l4= [x**2 if x%2 ==0 else x for x in l1]
print(l4)

#---------------------

# dictionary comprehension
d1 = {key: f"value {key}" for key in l1}
print(d1)

# using zip
list1 = [1, 4, 9, 16, 25]
list2 = ["one sq", "two sq" , "three sq", "four sq", "five sq"]
d2 = {i[0]: i[1] for i in zip(list1, list2)}
print(d2)

#-------------------------
#set comprehension
print(list1)
s1= {x**2 for x in list1}
print ("square", s1)
#output may be unordered

#-------------------------
#generator comp

g1= (x**3 for x in list1)
print(g1)
print(list(g1))