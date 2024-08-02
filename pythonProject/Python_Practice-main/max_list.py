# list=[1,4,0,7,9]
#taking list input from user using for loops
# list= []
# n=int(input("Enter no of elements of list: "))
# for i in range(0, n):
#     element = int(input())
#     list.append(element)
# print(list)

#taking list input using split
list = [int(x) for x in input("Enter the elements separated by space: ").split()]
print(list)
n=len(list)

max_ind = 0
for i in range(n):
    if  list[max_ind] < list[i]:
        max_ind= i
print(list[max_ind])
list[0], list[max_ind] = list [max_ind], list[0]
print(list)
