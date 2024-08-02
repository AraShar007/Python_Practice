list = [1, 2, 3,4,5]
# list[0], list[-1] = list[-1], list[0]
# print(list)

# temp = list[0]
# list[0] = list[-1]
# list[-1] = temp
# print(list)

# def swap_last_first(list):
#     start, *middle, end = list
#     list = [end, *middle, start]
#     print(list)
# swap_last_first(list)
n=len(list)
def swapping(list):
    a= list.pop(0)
    b= list.pop(-1)
    list.insert(n-1,a)
    list.insert(0,b)
    print(list)
swapping(list)
